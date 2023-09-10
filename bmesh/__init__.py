from bpy.types.b_mesh import BMesh
from bpy.types.mesh import Mesh

# https://docs.blender.org/api/current/bmesh.html

def new(use_operators=True) -> BMesh:
    pass

def from_edit_mesh(mesh: Mesh) -> BMesh:
    pass

def update_edit_mesh(mesh: Mesh, loop_triangles=True, destructive=True):
    pass