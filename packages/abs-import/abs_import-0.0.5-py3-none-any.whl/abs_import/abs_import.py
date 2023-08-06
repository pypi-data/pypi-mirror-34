import importlib.util
import sys
import os

def abs_import(path: str):
    spec = importlib.util.spec_from_file_location('module name', path)
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
