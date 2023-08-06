"""
Works with Python3.5+

JSON (de)serialization (jsons) from and to dicts and plain old Python objects.

Works with dataclasses (Python3.7+).


**Example:**

    >>> from dataclasses import dataclass
    >>> @dataclass
    ... class Car:
    ...     color: str
    >>> @dataclass
    ... class Person:
    ...     car: Car
    ...     name: str
    >>> c = Car('Red')
    >>> p = Person(c, 'John')
    >>> dumped = dump(p)
    >>> dumped['name']
    'John'
    >>> dumped['car']['color']
    'Red'
    >>> p_reloaded = load(dumped, Person)
    >>> p_reloaded.name
    'John'
    >>> p_reloaded.car.color
    'Red'


Deserialization will work with older Python classes (Python3.5+) given that
type hints are present for custom types (i.e. any type that is not set at
the bottom of this module). Serialization will work with no type hints at
all.


**Example**

    >>> class Car:
    ...     def __init__(self, color):
    ...         self.color = color
    >>> class Person:
    ...     def __init__(self, car: Car, name):
    ...         self.car = car
    ...         self.name = name
    >>> c = Car('Red')
    >>> p = Person(c, 'John')
    >>> dumped = dump(p)
    >>> dumped['name']
    'John'
    >>> dumped['car']['color']
    'Red'
    >>> p_reloaded = load(dumped, Person)
    >>> p_reloaded.name
    'John'
    >>> p_reloaded.car.color
    'Red'


Alternatively, you can make use of the `JsonSerializable` class.


**Example**

    >>> class Car(JsonSerializable):
    ...     def __init__(self, color):
    ...         self.color = color
    >>> class Person(JsonSerializable):
    ...     def __init__(self, car: Car, name):
    ...         self.car = car
    ...         self.name = name
    >>> c = Car('Red')
    >>> p = Person(c, 'John')
    >>> dumped = p.json
    >>> dumped['name']
    'John'
    >>> dumped['car']['color']
    'Red'
    >>> p_reloaded = Person.from_json(dumped)
    >>> p_reloaded.name
    'John'
    >>> p_reloaded.car.color
    'Red'

"""
import json
from datetime import datetime
from enum import Enum
from jsons._common_impl import dump_impl, load_impl, CLASSES_SERIALIZERS, \
    CLASSES_DESERIALIZERS, SERIALIZERS, DESERIALIZERS
from jsons.deserializers import default_list_deserializer, \
    default_enum_deserializer, default_datetime_deserializer, \
    default_string_deserializer, default_primitive_deserializer, \
    default_object_deserializer, default_dict_deserializer, \
    default_tuple_deserializer
from jsons.serializers import default_list_serializer, \
    default_enum_serializer, default_datetime_serializer, \
    default_primitive_serializer, default_object_serializer, \
    KEY_TRANSFORMER_SNAKECASE, KEY_TRANSFORMER_CAMELCASE, \
    KEY_TRANSFORMER_PASCALCASE, KEY_TRANSFORMER_LISPCASE, \
    default_dict_serializer, default_tuple_serializer

dump = dump_impl
load = load_impl


def dumps(obj: object, *args, **kwargs) -> str:
    """
    Extend ``json.dumps``, allowing any Python instance to be dumped to a
    string. Any extra (keyword) arguments are passed on to ``json.dumps``.

    :param obj: the object that is to be dumped to a string.
    :param args: extra arguments for ``json.dumps``.
    :param kwargs: extra keyword arguments for ``json.dumps``. They are also
    passed on to the serializer function.
    :return: ``obj`` as a ``str``.
    """
    return json.dumps(dump(obj, **kwargs), *args, **kwargs)


def loads(str_: str, cls: type = None, *args, **kwargs) -> object:
    """
    Extend ``json.loads``, allowing a string to be loaded into a dict or a
    Python instance of type ``cls``. Any extra (keyword) arguments are passed
    on to ``json.loads``.

    :param str_: the string that is to be loaded.
    :param cls: a matching class of which an instance should be returned.
    :param args: extra arguments for ``json.dumps``.
    :param kwargs: extra keyword arguments for ``json.dumps``. They are also
    passed on to the deserializer function.
    :return: an instance of type ``cls`` or a dict if no ``cls`` is given.
    """
    obj = json.loads(str_, *args, **kwargs)
    return load(obj, cls, **kwargs) if cls else obj


def set_serializer(func: callable, cls: type, high_prio: bool = True) -> None:
    """
    Set a serializer function for the given type. You may override the default
    behavior of ``jsons.load`` by setting a custom serializer.

    The ``func`` argument must take one argument (i.e. the object that is to be
    serialized) and also a ``kwargs`` parameter. For example:

    >>> def func(obj, **kwargs):
    ...    return dict()

    You may ask additional arguments between ``cls`` and ``kwargs``.

    :param func: the serializer function.
    :param cls: the type this serializer can handle.
    :param high_prio: determines the order in which is looked for the callable.
    :return: None.
    """
    if cls:
        index = 0 if high_prio else len(CLASSES_SERIALIZERS)
        CLASSES_SERIALIZERS.insert(index, cls)
        SERIALIZERS[cls.__name__.lower()] = func
    else:
        SERIALIZERS['nonetype'] = func


def set_deserializer(func: callable, cls: type, high_prio: bool = True) -> None:
    """
    Set a deserializer function for the given type. You may override the
    default behavior of ``jsons.dump`` by setting a custom deserializer.

    The ``func`` argument must take two arguments (i.e. the dict containing the
    serialized values and the type that the values should be deserialized into)
    and also a ``kwargs`` parameter. For example:

    >>> def func(dict_, cls, **kwargs):
    ...    return cls()

    You may ask additional arguments between ``cls`` and ``kwargs``.

    :param func: the deserializer function.
    :param cls: the type this serializer can handle.
    :param high_prio: determines the order in which is looked for the callable.
    :return: None.
    """
    if cls:
        index = 0 if high_prio else len(CLASSES_DESERIALIZERS)
        CLASSES_DESERIALIZERS.insert(index, cls)
        DESERIALIZERS[cls.__name__.lower()] = func
    else:
        DESERIALIZERS['nonetype'] = func


class JsonSerializable:
    """
    This class offers an alternative to using the ``jsons.load`` and
    ``jsons.dump`` methods. An instance of a class that inherits from
    ``JsonSerializable`` has the ``json`` property, which value is equivalent
    to calling ``jsons.dump`` on that instance. Furthermore, you can call
    ``from_json`` on that class, which is equivalent to calling ``json.load``
    with that class as an argument.
    """
    @classmethod
    def with_dump(cls, **kwargs) -> type:
        """
        Return a class (``type``) that is based on JsonSerializable with the
        ``dump`` method being automatically provided the given ``kwargs``.

        **Example:**

        >>> custom_serializable = JsonSerializable\
                .with_dump(key_transformer=KEY_TRANSFORMER_CAMELCASE)
        >>> class Person(custom_serializable):
        ...     def __init__(self, my_name):
        ...         self.my_name = my_name
        >>> p = Person('John')
        >>> p.json
        {'myName': 'John'}

        :param kwargs: the keyword args that are automatically provided to the
        ``dump`` method.
        :return: a class with customized behavior.
        """
        def _wrapper(inst, **kwargs_):
            return dump(inst, **{**kwargs_, **kwargs})

        type_ = type(JsonSerializable.__name__, (cls,), {})
        type_.dump = _wrapper
        return type_

    @classmethod
    def with_load(cls, **kwargs) -> type:
        """
        Return a class (``type``) that is based on JsonSerializable with the
        ``load`` method being automatically provided the given ``kwargs``.

        **Example:**

        >>> custom_serializable = JsonSerializable\
                .with_load(key_transformer=KEY_TRANSFORMER_SNAKECASE)
        >>> class Person(custom_serializable):
        ...     def __init__(self, my_name):
        ...         self.my_name = my_name
        >>> p_json = {'myName': 'John'}
        >>> p = Person.from_json(p_json)
        >>> p.my_name
        'John'

        :param kwargs: the keyword args that are automatically provided to the
        ``load`` method.
        :return: a class with customized behavior.
        """
        @classmethod
        def _wrapper(cls_, inst, **kwargs_):
            return load(inst, cls_, **{**kwargs_, **kwargs})
        type_ = type(JsonSerializable.__name__, (cls,), {})
        type_.load = _wrapper
        return type_

    @property
    def json(self) -> dict:
        """
        See ``jsons.dump``.
        :return: this instance in a JSON representation (dict).
        """
        return self.dump()

    @classmethod
    def from_json(cls: type, json_obj: dict, **kwargs) -> object:
        """
        See ``jsons.load``.
        :param json_obj: a JSON representation of an instance of the inheriting
        class
        :param kwargs: the keyword args are passed on to the deserializer
        function.
        :return: an instance of the inheriting class.
        """
        return cls.load(json_obj, **kwargs)

    def dump(self, **kwargs) -> dict:
        """
        See ``jsons.dump``.
        :param kwargs: the keyword args are passed on to the serializer
        function.
        :return: this instance in a JSON representation (dict).
        """
        return dump(self, **kwargs)

    @classmethod
    def load(cls: type, json_obj: dict, **kwargs) -> object:
        """
        See ``jsons.load``.
        :param kwargs: the keyword args are passed on to the serializer
        function.
        :return: this instance in a JSON representation (dict).
        """
        return load(json_obj, cls, **kwargs)


set_serializer(default_list_serializer, list)
set_serializer(default_tuple_serializer, tuple)
set_serializer(default_dict_serializer, dict)
set_serializer(default_enum_serializer, Enum)
set_serializer(default_datetime_serializer, datetime)
set_serializer(default_primitive_serializer, str)
set_serializer(default_primitive_serializer, int)
set_serializer(default_primitive_serializer, float)
set_serializer(default_primitive_serializer, bool)
set_serializer(default_primitive_serializer, None)
set_serializer(default_object_serializer, object, False)
set_deserializer(default_list_deserializer, list)
set_deserializer(default_tuple_deserializer, tuple)
set_deserializer(default_dict_deserializer, dict)
set_deserializer(default_enum_deserializer, Enum)
set_deserializer(default_datetime_deserializer, datetime)
set_deserializer(default_string_deserializer, str)
set_deserializer(default_primitive_deserializer, int)
set_deserializer(default_primitive_deserializer, float)
set_deserializer(default_primitive_deserializer, bool)
set_deserializer(default_primitive_deserializer, None)
set_deserializer(default_object_deserializer, object, False)
