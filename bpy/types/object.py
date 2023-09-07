from id import ID
from anim_data import AnimData
from mathutils import Vector, Euler, Quaternion, Matrix
from collection import Collection
from object import Object
from curve import Curve

# https://docs.blender.org/api/current/bpy.types.Object.html

class Object(ID):
    """
import bpy

view_layer = bpy.context.view_layer

# Create new light datablock.
light_data = bpy.data.lights.new(name="New Light", type='POINT')

# Create new object with our light datablock.
light_object = bpy.data.objects.new(name="New Light", object_data=light_data)

# Link light object to the active collection of current view layer,
# so that it'll appear in the current scene.
view_layer.active_layer_collection.collection.objects.link(light_object)

# Place light to a specified location.
light_object.location = (5.0, 5.0, 5.0)

# And finally select it and make it active.
light_object.select_set(True)
view_layer.objects.active = light_object
    """

    active_material: any
    active_material_index: int
    active_shape_key: any
    active_shape_key_index: int
    add_rest_position_attribute: bool
    animation_data: AnimData
    animation_visualization: any
    bound_box: any
    collision: any
    color: any
    constraints: any
    cycles: any
    data: ID
    delta_location: Vector
    delta_rotation_euler: Euler
    delta_rotation_quaternion: Quaternion
    delta_scale: Vector
    dimensions: Vector
    display: any
    display_bounds_type: any
    display_type: any
    empty_display_size: float
    empty_display_type: any
    empty_image_depth: any
    empty_image_offset: float
    empty_image_side: any
    face_maps: any
    field: any
    grease_pencil_modifiers: any
    hide_render: bool
    hide_select: bool
    hide_viewport: bool
    image_user: any
    instance_collection: Collection
    instance_faces_scale: float
    instance_type: any
    is_from_instancer: bool
    is_from_set: bool
    is_holdout: bool
    is_instancer: bool
    is_shadow_catcher: bool
    lightgroup: str
    lineart: any
    location: Vector
    lock_location: bool
    lock_rotation: bool
    lock_rotation_w: bool
    lock_rotations_4d: bool
    lock_scale: bool
    material_slots: any
    matrix_basis: Matrix
    matrix_local: Matrix
    matrix_parent_inverse: Matrix
    matrix_world: Matrix
    mode: any
    modifiers: any
    motion_path: any
    parent: Object
    parent_bone: str
    parent_type: any
    parent_vertices: int
    particle_systems: any
    pass_index: int
    pose: any
    rigid_body: any
    rigid_body_constraint: any
    rotation_axis_angle: float
    rotation_euler: Euler
    rotation_mode: any
    rotation_quaternion: Quaternion
    scale: Vector
    shader_effects: any
    show_all_edges: bool
    show_axis: bool
    show_bounds: bool
    show_empty_image_only_axis_aligned: bool
    show_empty_image_orthographic: bool
    show_empty_image_perspective: bool
    show_in_front: bool
    show_instancer_for_render: bool
    show_instancer_for_viewport: bool
    show_name: bool
    show_only_shape_key: bool
    show_texture_space: bool
    show_transparent: bool
    show_wire: bool
    soft_body: any
    track_axis: any
    type: any
    up_axis: any
    use_camera_lock_parent: bool
    use_dynamic_topology_sculpting: bool
    use_empty_image_alpha: bool
    use_grease_pencil_lights: bool
    use_instance_faces_scale: bool
    use_instance_vertices_rotation: bool
    use_mesh_mirror_x: bool
    use_mesh_mirror_y: bool
    use_mesh_mirror_z: bool
    use_shape_key_edit_mode: bool
    use_simulation_cache: bool
    vertex_groups: any
    visible_camera: bool
    visible_diffuse: bool
    visible_glossy: bool
    visible_shadow: bool
    visible_transmission: bool
    visible_volume_scatter: bool
    children: tuple
    children_recursive: tuple
    users_collection: tuple
    users_scene: tuple

    def select_get(self, view_layer=None) -> bool:
        pass

    def select_set(self, state: bool, view_layer=None):
        pass

    def hide_get(self, view_layer=None) -> bool:
        pass

    def hide_set(self, state: bool, view_layer=None):
        pass

    def visible_get(self, view_layer=None, viewport=None) -> bool:
        pass

    def holdout_get(self, view_layer=None) -> bool:
        pass

    def indirect_only_get(self, view_layer=None) -> bool:
        pass

    def local_view_get(self, viewport) -> bool:
        pass

    def local_view_set(self, viewport, state: bool):
        pass

    def visible_in_viewport_get(self, viewport) -> bool:
        pass

    def convert_space(self, pose_bone=None, matrix=((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)), from_space='WORLD', to_space='WORLD') -> Matrix:
        pass

    def calc_matrix_camera(self, depsgraph, x=1, y=1, scale_x=1.0, scale_y=1.0) -> Matrix:
        pass

    def camera_fit_coords(self, depsgraph: any, coordinates: list[float]) -> any:
        pass

    def crazyspace_eval(self, depsgraph, scene):
        pass

    def crazyspace_displacement_to_deformed(self, vertex_index=0, displacement=(0.0, 0.0, 0.0)) -> Vector:
        pass

    def crazyspace_displacement_to_original(self, vertex_index=0, displacement=(0.0, 0.0, 0.0)) -> Vector:
        pass

    def crazyspace_eval_clear(self):
        pass

    def to_mesh(self, preserve_all_data_layers=False, depsgraph=None) -> any:
        pass

    def to_mesh_clear(self):
        pass

    def to_curve(self, depsgraph, apply_modifiers=False) -> Curve:
        pass

    def to_curve_clear(self):
        pass

    def find_armature(self) -> any:
        pass

    def shape_key_add(self, name: str='Key', from_mix=True) -> any:
        pass

    def shape_key_remove(self, key: any) -> any:
        pass

    def shape_key_clear(self):
        """Remove all Shape Keys from this object
        """
        pass

    def ray_cast(self, origin: Vector, direction: Vector, distance: float=1.70141e+38, depsgraph: any=None) -> any:
        pass

    def closest_point_on_mesh(self, origin: Vector, distance: float=1.84467e+19, depsgraph=None) -> any:
        pass

    def is_modified(self, scene: any, settings: any) -> bool:
        pass

    def is_deform_modified(self, scene, settings) -> bool:
        pass

    def update_from_editmode(self) -> bool:
        pass

    def cache_release(self):
        pass

    def generate_gpencil_strokes(self, grease_pencil_object, use_collections=True, scale_thickness=1.0, sample=0.0) -> bool:
        pass