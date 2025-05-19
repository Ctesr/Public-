import os
import sys
import importlib
import pkgutil


def export_classes(package_name):
    sys.path.append(f'{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}')
    package = importlib.import_module(package_name)
    classes = []
    for importer, module_name, _ in pkgutil.iter_modules(package.__path__):
        module = importlib.import_module(f"{package_name}.{module_name}")
        for item_name in dir(module):
            item = getattr(module, item_name)
            if isinstance(item, type):
                classes.append(item)
    return classes


package = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
print(package)
# 导出包内所有类
all_classes = export_classes(package)
# 拿指定的类
get_classes = []
for cls in all_classes:
    if 'Action' in cls.__name__ and cls.__name__ != 'BasePageAction':
        get_classes.append(cls)


def get_tag_cls(cls_name):
    for cls in get_classes:
        if cls_name == cls.__name__:
            return cls

if __name__ == "__main__" :
    pass