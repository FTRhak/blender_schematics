from id import ID
from mathutils import Vector
from bpy.types.bpy_prop_collection import bpy_prop_collection

# https://docs.blender.org/api/current/bpy.types.Collection.html

class Collection(ID):
    all_objects: bpy_prop_collection[any]
    children: bpy_prop_collection[any]
    color_tag: any
    hide_render: bool
    hide_select:  bool
    hide_viewport: bool
    instance_offset: Vector
    lineart_intersection_mask: list[bool]
    lineart_intersection_priority: int
    lineart_usage: any
    lineart_use_intersection_mask: bool
    objects: bpy_prop_collection[any]
    use_lineart_intersection_priority: bool
    children_recursive: any
    users_dupli_group: any

    @classmethod
    def bl_rna_get_subclass(id: str, default=None):
        pass

    @classmethod
    def bl_rna_get_subclass_py(id: str, default=None):
        pass