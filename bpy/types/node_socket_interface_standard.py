from node_socket_interface import NodeSocketInterface
from ui_layout import UILayout

class NodeSocketInterfaceStandard(NodeSocketInterface):
    type: any

    def draw(self, context, layout: UILayout):
        pass

    def draw_color(context) -> list[float]:
        pass

    @classmethod
    def bl_rna_get_subclass(id: str, default=None):
        pass

    @classmethod
    def bl_rna_get_subclass_py(id: str, default=None):
        pass