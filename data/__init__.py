import bpy
from . import materials


classes = (
)
reg_classes, unreg_classes = bpy.utils.register_classes_factory(classes)


def register():
    materials.register()
    reg_classes()

def unregister():
    unreg_classes()
    materials.unregister()