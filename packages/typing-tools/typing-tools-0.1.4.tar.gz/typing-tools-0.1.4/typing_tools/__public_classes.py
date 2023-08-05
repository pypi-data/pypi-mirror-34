from typing import Dict, Any
from typing_tools.__common import _getter, debug_msg, _PUBLIC_CLASSES, _DEFAULT_OBJECT


def _public_class_metaclass__generator():
    def _public_class_metaclass(future_class_name, future_class_parents, future_class_attributes):
        def __init__(self, *args, __owner__=_DEFAULT_OBJECT, **kwargs):
            debug_msg(f"Constructing a new {self.__class__} object, owner={__owner__} ...")
            if (__owner__ is not _DEFAULT_OBJECT):
                debug_msg(f"Constructing a super-class, owner={__owner__}...")
                super(self.__class__, self).__init__(*args, **kwargs)
            
            self.__owner__ = __owner__
        def __getitem__(self, key):
            debug_msg(f"__getitem__ called with key={key}")
            value = (super(self.__class__, self) if (self.__owner__ is None) else self.__owner__).__getitem__(key)
            
            if (hasattr(self, '__annotations__') and key in self.__annotations__):
                return _getter(self.__annotations__[key], value)
            return value
        def __setitem__(self, *args, **kwargs):
            return (super(self.__class__, self) if (self.__owner__ is None) else self.__owner__).__setitem__(*args, **kwargs)
        
        annotations = dict()
        for _parent in reversed(future_class_parents):
            if (hasattr(_parent, '__annotations__')):
                annotations.update(_parent.__annotations__)
        if ('__annotations__' in future_class_attributes):
            annotations.update(future_class_attributes['__annotations__'])
        
        # future_class_attributes['__init__'] = __init__
        # future_class_attributes['__getitem__'] = __getitem__
        # future_class_attributes['__setitem__'] = __setitem__
        future_class_attributes['__owner__'] = None
        future_class_attributes['__annotations__'] = annotations
        _class = type(future_class_name, future_class_parents, future_class_attributes)
        _PUBLIC_CLASSES.append(_class)
        return _class
    return _public_class_metaclass

class DictStruct(Dict[str, Any], metaclass=_public_class_metaclass__generator()):
    def __getitem__(self, key):
        debug_msg(f"__getitem__ called with key={key}")
        value = (super() if (self.__owner__ is None) else self.__owner__).__getitem__(key)
        
        if (hasattr(self, '__annotations__') and key in self.__annotations__):
            return _getter(self.__annotations__[key], value)
        return value
    def __setitem__(self, *args, **kwargs):
        if (self.__owner__ is not None):
            self.__owner__.__setitem__(*args, **kwargs)
        return super().__setitem__(*args, **kwargs)
    def __init__(self, *args, __owner__ = None, **kwargs):
        super().__init__(*args, **kwargs)
        self.__owner__ = __owner__
        
        _annotations = self.__annotations__
        _cls = self.__class__
        _dict = _cls.__dict__
        _self_dict = self.__dict__
        
        for _key, _value in _dict.items():
            if (not (_key.startswith('__') and _key.endswith('__')) and _key in _annotations):
                if (_key not in self):
                    _cls.__setattr__(self, _key, _value)
                else:
                    _self_dict[_key] = self[_key]
    
    def __setattr__(self, key, value):
        debug_msg(f"__setattr__ called with key={key}, value={value}")
        super().__setattr__(key, value)
        
        if (not (key.startswith('__') and key.endswith('__'))):
            self[key] = value
            if (self.__owner__):
                self.__owner__[key] = value
    def __getattr__(self, key):
        debug_msg(f"__getattribute__ called with key={key}")
        if (key.startswith('__') and key.endswith('__')):
            return super().__getattr__(key)
        else:
            return self[key]
    def __iter__(self):
        raise TypeError(f"Cannot iterate over {type(self)}")
    
    def get(self, key, *args, **kwargs):
        debug_msg(f"__getitem__ called with key={key}")
        value = (super() if (self.__owner__ is None) else self.__owner__).get(key, *args, **kwargs)

        if (hasattr(self, '__annotations__') and key in self.__annotations__):
            return _getter(self.__annotations__[key], value)
        return value
