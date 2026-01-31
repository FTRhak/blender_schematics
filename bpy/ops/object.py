# https://docs.blender.org/api/current/bpy.ops.object.html

def add(radius=1.0, type='EMPTY', enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0)):
    pass

def add_modifier_menu():
    pass

def add_named(linked=False, name='', session_uid=0, matrix=((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)), drop_x=0, drop_y=0):
    pass

def align(bb_quality=True, align_mode='OPT_2', relative_to='OPT_4', align_axis={}):
    pass

def anim_transforms_to_deltas():
    pass

def armature_add(radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0)):
    pass

def assign_property_defaults(process_data=True, process_bones=True):
    pass

def bake(type='COMBINED', pass_filter={}, filepath='', width=512, height=512, margin=16, margin_type='EXTEND', use_selected_to_active=False, max_ray_distance=0.0, cage_extrusion=0.0, cage_object='', normal_space='TANGENT', normal_r='POS_X', normal_g='POS_Y', normal_b='POS_Z', target='IMAGE_TEXTURES', save_mode='INTERNAL', use_clear=False, use_cage=False, use_split_materials=False, use_automatic_name=False, uv_layer=''):
    pass

def bake_image():
    pass

def camera_add(enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0)):
    pass

def camera_custom_update():
    pass

def clear_override_library():
    pass

def collection_add():
    pass

def collection_external_asset_drop(session_uid=0, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0), use_instance=True, drop_x=0, drop_y=0, collection=''):
    pass

def collection_instance_add(name='Collection', collection='', align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0), session_uid=0, drop_x=0, drop_y=0):
    pass

def collection_link(collection=''):
    pass

def collection_objects_select():
    pass

def collection_remove():
    pass

def collection_unlink():
    pass

def constraint_add(type=''):
    pass

def constraint_add_with_targets(type=''):
    pass

def constraints_clear():
    pass

def constraints_copy():
    pass

def convert(target='MESH', keep_original=False, merge_customdata=True, thickness=5, faces=True, offset=0.01):
    pass

def copy_global_transform():
    pass

def copy_relative_transform():
    pass

def correctivesmooth_bind(modifier=''):
    pass

def curves_empty_hair_add(align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0)):
    pass

def curves_random_add(align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0)):
    pass

def data_instance_add(name='', session_uid=0, type='ACTION', align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0), drop_x=0, drop_y=0):
    pass

def data_transfer(use_reverse_transfer=False, use_freeze=False, data_type='', use_create=True, vert_mapping='NEAREST', edge_mapping='NEAREST', loop_mapping='NEAREST_POLYNOR', poly_mapping='NEAREST', use_auto_transform=False, use_object_transform=True, use_max_distance=False, max_distance=1.0, ray_radius=0.0, islands_precision=0.1, layers_select_src='ACTIVE', layers_select_dst='ACTIVE', mix_mode='REPLACE', mix_factor=1.0):
    pass

def datalayout_transfer(modifier='', data_type='', use_delete=False, layers_select_src='ACTIVE', layers_select_dst='ACTIVE'):
    pass

def delete(use_global=False, confirm=True):
    pass

def delete_fix_to_camera_keys():
    pass

def drop_geometry_nodes(session_uid=0, show_datablock_in_modifier=True):
    pass

def drop_named_material(name='', session_uid=0):
    pass

def duplicate(linked=False, mode='TRANSLATION'):
    pass

def duplicate_move(OBJECT_OT_duplicate=None, TRANSFORM_OT_translate=None):
    pass

def duplicate_move_linked(OBJECT_OT_duplicate=None, TRANSFORM_OT_translate=None):
    pass

def duplicates_make_real(use_base_parent=False, use_hierarchy=False):
    pass

def editmode_toggle():
    pass

def effector_add(type='FORCE', radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0)):
    pass

def empty_add(type='PLAIN_AXES', radius=1.0, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0)):
    pass

def empty_image_add(filepath='', hide_props_region=True, check_existing=False, filter_blender=False, filter_backup=False, filter_image=True, filter_movie=True, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='', name='', session_uid=0, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0), background=False):
    pass

def explode_refresh(modifier=''):
    pass

def fix_to_camera(use_location=True, use_rotation=True, use_scale=True):
    pass

def forcefield_toggle():
    pass

def geometry_node_bake_delete_single(session_uid=0, modifier_name='', bake_id=0):
    pass

def geometry_node_bake_pack_single(session_uid=0, modifier_name='', bake_id=0):
    pass

def geometry_node_bake_single(session_uid=0, modifier_name='', bake_id=0):
    pass

def geometry_node_bake_unpack_single(session_uid=0, modifier_name='', bake_id=0, method='USE_LOCAL'):
    pass

def geometry_node_tree_copy_assign():
    pass

def geometry_nodes_input_attribute_toggle(input_name='', modifier_name=''):
    pass

def geometry_nodes_move_to_nodes(use_selected_objects=False):
    pass

def grease_pencil_add(type='EMPTY', use_in_front=True, stroke_depth_offset=0.05, use_lights=True, stroke_depth_order='3D', radius=1.0, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0)):
    pass

def grease_pencil_dash_modifier_segment_add(modifier=''):
    pass

# TODO add more operators here


def mode_set(mode='OBJECT', toggle=False):
    """
    Docstring for mode_set
    
    :param mode: Enum in ['OBJECT', 'EDIT', 'POSE', 'SCULPT', 'VERTEX_PAINT', 'WEIGHT_PAINT', 'TEXTURE_PAINT', 'PARTICLE_EDIT', 'EDIT_GPENCIL', 'SCULPT_GREASE_PENCIL', 'PAINT_GREASE_PENCIL', 'WEIGHT_GREASE_PENCIL', 'VERTEX_GREASE_PENCIL', 'SCULPT_CURVES']
    :param toggle: Description
    """
    pass







