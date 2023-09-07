from bpy.types.bpy_struct import bpy_struct
from node_socket_interface import NodeSocketInterface

# https://docs.blender.org/api/current/bpy.types.NodeTreeOutputs.html

class NodeTreeOutputs(bpy_struct):
    def new(self, type: str, name: str, identifier: str='') -> NodeSocketInterface:
        pass

    def remove(self, socket: NodeSocketInterface):
        pass

    def clear(self):
        pass

    def move(self, from_index: int, to_index: int):
        pass

    @classmethod
    def bl_rna_get_subclass(id, default=None):
        pass

    @classmethod
    def bl_rna_get_subclass_py(id, default=None):
        pass