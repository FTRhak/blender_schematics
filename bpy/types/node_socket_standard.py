from node_socket import NodeSocket
from ui_layout import UILayout
from node import Node

# https://docs.blender.org/api/current/bpy.types.NodeSocketStandard.html

class NodeSocketStandard(NodeSocket):
    links: any

    def draw(self, context, layout: UILayout, node: Node, text: str):
        pass

    def draw_color(self, context, node: Node) -> list[float]:
        pass

    @classmethod
    def bl_rna_get_subclass(id: str, default=None):
        pass

    @classmethod
    def bl_rna_get_subclass_py(id: str, default=None):
        pass