from node_tree import NodeTree

# https://docs.blender.org/api/current/bpy.types.GeometryNodeTree.html

class GeometryNodeTree(NodeTree):

    @classmethod
    def bl_rna_get_subclass(id: str, default=None):
        pass

    @classmethod
    def bl_rna_get_subclass_py(id: str, default=None):
        pass