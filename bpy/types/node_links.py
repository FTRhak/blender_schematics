from bpy.types.bpy_struct import bpy_struct
from node_link import NodeLink
from node_socket import NodeSocket

# https://docs.blender.org/api/current/bpy.types.NodeLinks.html

class NodeLinks(bpy_struct):
    def new(self, input: NodeSocket, output: NodeSocket, verify_limits=True) -> NodeLink:
        pass

    def remove(self, link: NodeLink):
        pass

    def clear(self):
        pass
