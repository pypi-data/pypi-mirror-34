import importlib.util
import sys
import os

def abs_import(path: str):
    assert isinstance(path, str)
    if path == '/':
        raise ValueError('root path / cannot be a abs package path')
    if os.path.isdir(path):
        if path[-1] == '/':
            path = path[0:-1]
        module_name = os.path.basename(path)
    else:
        basename = os.path.basename(path)
        if basename == '__init__.py':
            dirname = os.path.dirname(path)
            module_name = os.path.basename(dirname)
        else:
            module_name = basename
    spec = importlib.util.spec_from_file_location(module_name, path)
    modu = importlib.util.module_from_spec(spec)
    sys.path.append(resolve_path(path))
    spec.loader.exec_module(modu)
    return modu

def resolve_path(path: str):
    path = os.path.dirname(path)
    while os.path.isfile(os.path.join(path, '__init__.py')):
        path = os.path.join(path, '..')
        path = os.path.abspath(path)
    return path

# An example of abs_import:
# from abs_import import abs_import
# cctr = abs_import('/.../tensorflow/models/research/object_detection/dataset_tools/create_coco_tf_record.py')
