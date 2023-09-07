from bpy.types.bpy_struct import bpy_struct
from object import Object

# https://docs.blender.org/api/current/bpy.types.BlendDataObjects.html

class BlendDataObjects(bpy_struct):

    def new(self, name, object_data) -> Object:
        pass

    def remove(self, object: Object, do_unlink=True, do_id_user=True, do_ui_user=True):
        pass

    def tag(value: bool):
        pass