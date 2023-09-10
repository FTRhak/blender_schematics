from bpy.types.bpy_struct import bpy_struct
from node import Node
from node_socket import NodeSocket

#  https://docs.blender.org/api/current/bpy.types.NodeLink.html

class NodeLink(bpy_struct):
    from_node: Node
    from_socket: NodeSocket
    is_hidden: bool
    is_muted: bool
    is_valid: bool
    to_node: Node
    to_socket: NodeSocket