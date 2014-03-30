_imported_modules_ = {}


def add_module_to_imported_modules(src, mod):
    _imported_modules_[src] = mod


def get_module(src):
    if src in _imported_modules_.keys():
        return _imported_modules_[src]
    return None


def get_serializer(ser, f):
    root = f.__module__.split('.')[0]
    package_name = ser.rsplit('.', 1)[0]
    serializer_class_name = ser.rsplit('.', 1)[1]
    src = '.'.join([root, package_name, 'serializers'])
    try:
        mod = get_module(src)
        if not mod:
            mod = __import__(src, fromlist=[serializer_class_name])
            add_module_to_imported_modules(src, mod)
        klass = getattr(mod, serializer_class_name)
        return klass
    except:
        pass