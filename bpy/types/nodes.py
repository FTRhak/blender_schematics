from bpy.types.bpy_struct import bpy_struct
from node import Node

# https://docs.blender.org/api/current/bpy.types.Nodes.html

class Nodes(bpy_struct):
    active: Node

    def new(self, type: str) -> Node:
        pass

    def remove(self, node: Node):
        pass

    def clear(self):
        pass

    @classmethod
    def bl_rna_get_subclass(id: str, default=None):
        pass

    @classmethod
    def bl_rna_get_subclass_py(id: str, default=None):
        pass