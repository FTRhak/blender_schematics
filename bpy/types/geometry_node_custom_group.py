from bpy.types.geometry_node import GeometryNode
from node_tree import NodeTree

class GeometryNodeCustomGroup(GeometryNode):
    node_tree: NodeTree
    
    @classmethod
    def bl_rna_get_subclass(id, default=None):
        pass

    @classmethod
    def bl_rna_get_subclass_py(id, default=None):
        pass
