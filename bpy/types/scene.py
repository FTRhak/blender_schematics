from typing import Type
from id import ID
from anim_data import AnimData
from object import Object
from collection import Collection
from node_tree import NodeTree
from view_layer import ViewLayer
from mathutils import Vector

# https://docs.blender.org/api/current/bpy.types.Scene.html

class Scene(ID):
    active_clip: any
    animation_data: AnimData
    audio_distance_model: any
    audio_doppler_factor: float
    audio_doppler_speed: float
    audio_volume: float
    background_set: Type['Scene']
    camera: Object
    collection: Collection
    cursor: any
    cycles: any
    cycles_curves: any
    display: any
    display_settings: any
    eevee: any
    frame_current: any
    frame_current_final: float
    frame_end: int
    frame_float: float
    frame_preview_end: int
    frame_preview_start: int
    frame_start: int
    frame_step: int
    frame_subframe: int
    gravity: Vector
    grease_pencil: any
    grease_pencil_settings: any
    is_nla_tweakmode: bool
    keying_sets: any
    keying_sets_all: any
    lock_frame_selection_to_range: bool
    node_tree: NodeTree
    objects: any
    render: any
    rigidbody_world: any
    safe_areas: any
    sequence_editor: any
    sequencer_colorspace_settings: any
    show_keys_from_selected_only: bool
    show_subframe: bool
    sync_mode: any
    timeline_markers: any
    tool_settings: any
    transform_orientation_slots: any
    unit_settings: any
    use_audio: bool
    use_audio_scrub: bool
    use_gravity: bool
    use_nodes: bool
    use_preview_range: bool
    use_stamp_note: str
    view_layers: any
    view_settings: any
    world: any

    @classmethod
    def update_render_engine():
        pass

    def statistics(self, view_layer: ViewLayer) -> str:
        pass

    def frame_set(self, frame: int, subframe: float=0.0):
        pass

    def uvedit_aspect(self, object: Object) -> Vector:
        pass

    def ray_cast(self, depsgraph: any, origin, direction, distance=1.70141e+38) -> any:
        pass

    def sequence_editor_create(self) -> any:
        pass

    def sequence_editor_clear(self):
        pass

    def alembic_export(self, filepath, frame_start=1, frame_end=1, xform_samples=1, geom_samples=1, shutter_open=0.0, shutter_close=1.0, selected_only=False, uvs=True, normals=True, vcolors=False, apply_subdiv=True, flatten=False, visible_objects_only=False, face_sets=False, subdiv_schema=False, export_hair=True, export_particles=True, packuv=False, scale=1.0, triangulate=False, quad_method='BEAUTY', ngon_method='BEAUTY'):
        pass

