registry = {}

class OverloadObj(object):
    def __init__(self, name):
        self.name = name
        self.typemap = {}
    def __call__(self, *args):
        types = tuple(arg.__class__ for arg in args)
        function = self.typemap.get(types)
        if function is None:
            raise TypeError("params not match")
        return function(*args)
    def register(self, types, function):
        if types in self.typemap:
            raise TypeError("duplicate registration")
        self.typemap[types] = function

def overload(*types):
    def register(function):
        name = function.__name__
        ol = registry.get(name)
        if ol is None:
            ol = registry[name] = OverloadObj(name)
        ol.register(types, function)
        return ol
    return register