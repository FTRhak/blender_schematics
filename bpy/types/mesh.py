from id import ID
from anim_data import AnimData
from key import Key
from mathutils import Vector, Matrix

# https://docs.blender.org/api/current/bpy.types.Mesh.html

class Mesh(ID):
    animation_data: AnimData
    attributes: any
    auto_smooth_angle: float
    auto_texspace: bool
    color_attributes: any
    corner_normals: any
    cycles: any
    edge_creases: any
    edges: any
    face_maps: any
    has_bevel_weight_edge: bool
    has_bevel_weight_vertex: bool
    has_crease_edge: bool
    has_crease_vertex: bool
    has_custom_normals: bool
    is_editmode: bool
    loop_triangle_polygons: any
    loop_triangles: any
    loops: any
    materials: any
    polygon_layers_float: any
    polygon_layers_int: any
    polygon_layers_string: any
    polygon_normals: any
    polygons: any
    remesh_mode: any
    remesh_voxel_adaptivity: float
    remesh_voxel_size: float
    sculpt_vertex_colors: any
    shape_keys: Key
    skin_vertices: any
    texco_mesh: any
    texspace_location: Vector
    texspace_size: Vector
    texture_mesh: any
    total_edge_sel: int
    total_face_sel: int
    total_vert_sel: int
    use_auto_smooth: bool
    use_auto_texspace: bool
    use_mirror_topology: bool
    use_mirror_vertex_groups: bool
    use_mirror_x: bool
    use_mirror_y: bool
    use_mirror_z: bool
    use_paint_mask: bool
    use_paint_mask_vertex: bool
    use_remesh_fix_poles: bool
    use_remesh_preserve_paint_mask: bool
    use_remesh_preserve_sculpt_face_sets: bool
    use_remesh_preserve_vertex_colors: bool
    use_remesh_preserve_volume: bool
    uv_layer_clone: any
    uv_layer_clone_index: int
    uv_layer_stencil: any
    uv_layer_stencil_index: int
    uv_layers: any
    vertex_colors: any
    vertex_creases: any
    vertex_layers_float: any
    vertex_layers_int: any
    vertex_layers_string: any
    vertex_normals: any
    vertex_paint_masks: any
    vertices: any
    edge_keys: any

    def transform(self, matrix: Matrix, shape_keys=False):
        pass

    def flip_normals(self):
        pass

    def calc_normals(self):
        """Deprecated. Has no effect. Normals are calculated upon retrieval
        """
        pass

    def create_normals_split(self):
        pass

    def calc_normals_split(self):
        pass

    def free_normals_split(self):
        pass

    def split_faces(free_loop_normals=True):
        pass

    def calc_tangents(self, uvmap: str=''):
        pass

    def free_tangents(self):
        pass

    def calc_loop_triangles(self):
        pass

    def calc_smooth_groups(self, use_bitflags=False) -> any:
        pass

    def normals_split_custom_set(self, normals: list[float]):
        """_summary_

        Args:
            normals (list[float]): float multi-dimensional array of 1 * 3 items in [-1, 1]
        """
        pass

    def normals_split_custom_set_from_vertices(self, normals: list[float]):
        """_summary_

        Args:
            normals (list[float]): float multi-dimensional array of 1 * 3 items in [-1, 1]
        """
        pass

    def update(self, calc_edges=False, calc_edges_loose=False):
        pass

    def update_gpu_tag(self):
        pass

    def unit_test_compare(self, mesh=None, threshold=7.1526e-06) -> str:
        pass

    def clear_geometry(self):
        pass

    def validate(self, verbose=False, clean_customdata=True) -> bool:
        pass

    def validate_material_indices(self) -> bool:
        pass

    def count_selected_items(self) -> list[int]:
        """_summary_

        Returns:
            list[int]: int array of 3 items in [0, inf]
        """
        pass

    def from_pydata(self, vertices, edges, faces, shade_flat=True):
        pass

    def shade_flat(self):
        pass

    def shade_smooth(self):
        pass
