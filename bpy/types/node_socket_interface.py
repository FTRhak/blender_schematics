from bpy.types.bpy_struct import bpy_struct
from node import Node
from node_socket import NodeSocket

# https://docs.blender.org/api/current/bpy.types.NodeSocketInterface.html

class NodeSocketInterface(bpy_struct):
    attribute_domain: any
    bl_label: str
    bl_socket_idname: str
    bl_subtype_label: str
    default_attribute_name: str
    description: str
    hide_in_modifier: bool
    hide_value: bool
    identifier: str
    is_output: bool
    name: str

    def draw(self, context, layout):
        pass

    def draw_color(self, context) -> list[float]:
        pass

    def init_socket(self, node: Node, socket: NodeSocket, data_path: str):
        pass

    def from_socket(self, node: Node, socket: NodeSocket):
        pass

    @classmethod
    def bl_rna_get_subclass(id: str, default=None):
        pass

    @classmethod
    def bl_rna_get_subclass_py(id: str, default=None):
        pass
