from bpy.types.bpy_struct import bpy_struct
from node_socket import NodeSocket

class NodeOutputs(bpy_struct):
    
    def new(self, type: str, name: str, identifier: str='') -> NodeSocket:
        pass

    def remove(self, socket: NodeSocket):
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