class NodeOperators:
    def add_collection(self, name='', session_uuid=0):
        pass

    def add_file(self, filepath='', hide_props_region=True, check_existing=False, filter_blender=False, filter_backup=False, filter_image=True, filter_movie=True, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='', name='', session_uuid=0):
        pass

    def add_group(self, name='', session_uuid=0):
        pass

    def add_group_asset(self):
        pass

    def add_mask(self, name='', session_uuid=0):
        pass

    def add_node(self, use_transform=False, settings=None, type=''):
        pass

    def add_object(self, name='', session_uuid=0):
        pass

    def add_reroute(self, path=None, cursor=8):
        pass

    def add_search(self, use_transform=True):
        pass

    def add_simulation_zone(self, use_transform=False, settings=None, offset=(150.0, 0.0)):
        pass

    def attach(self):
        pass

    def backimage_fit(self):
        pass

    def backimage_move(self):
        pass

    def backimage_sample(self):
        pass

    def backimage_zoom(self, factor=1.2):
        pass

    def clear_viewer_border(self):
        pass

    def clipboard_copy(self):
        pass

    def clipboard_paste(self, offset=(0.0, 0.0)):
        pass

    def collapse_hide_unused_toggle(self):
        pass

    def cryptomatte_layer_add(self):
        pass

    def cryptomatte_layer_remove(self):
        pass

    def deactivate_viewer(self):
        pass

    def delete(self):
        pass

    def delete_reconnect(self):
        pass

    def detach(self):
        pass

    def detach_translate_attach(self, NODE_OT_detach=None, TRANSFORM_OT_translate=None, NODE_OT_attach=None):
        pass

    def duplicate(self, keep_inputs=False, linked=True):
        pass

    def duplicate_move(self, NODE_OT_duplicate=None, NODE_OT_translate_attach=None):
        pass

    def duplicate_move_keep_inputs(self, NODE_OT_duplicate=None, NODE_OT_translate_attach=None):
        pass

    def duplicate_move_linked(self, NODE_OT_duplicate=None, NODE_OT_translate_attach=None):
        pass

    def find_node(self):
        pass

    def gltf_settings_node_operator(self):
        pass

    def group_edit(self, exit=False):
        pass

    def group_insert(self):
        pass

    def group_make(self):
        pass

    def group_separate(self, type='COPY'):
        pass

    def group_ungroup(self):
        pass

    def hide_socket_toggle(self):
        pass

    def hide_toggle(self):
        pass

    def insert_offset(self):
        pass

    def join(self):
        pass

    def link(self, detach=False, drag_start=(0.0, 0.0), inside_padding=2.0, outside_padding=0.0, speed_ramp=1.0, max_speed=26.0, delay=0.5, zoom_influence=0.5):
        pass

    def link_make(self, replace=False):
        pass

    def link_viewer(self):
        pass

    def links_cut(self, path=None, cursor=12):
        pass

    def links_detach(self):
        pass

    def links_mute(self, path=None, cursor=35):
        pass

    def move_detach_links(self, NODE_OT_links_detach=None, TRANSFORM_OT_translate=None):
        pass

    def move_detach_links_release(self, NODE_OT_links_detach=None, NODE_OT_translate_attach=None):
        pass

    def mute_toggle(self):
        pass

    def new_geometry_node_group_assign(self):
        pass

    def new_geometry_nodes_modifier(self):
        pass

    def new_node_tree(self, type='', name='NodeTree'):
        pass

    def node_color_preset_add(self, name='', remove_name=False, remove_active=False):
        pass

    def node_copy_color(self):
        pass

    def options_toggle(self):
        pass

    def output_file_add_socket(self, file_path='Image'):
        pass

    def output_file_move_active_socket(self, direction='DOWN'):
        pass

    def output_file_remove_active_socket(self):
        pass

    def parent_set(self):
        pass

    def preview_toggle(self):
        pass

    def read_viewlayers(self):
        pass

    def render_changed(self):
        pass

    def resize(self):
        pass

    def select(self, extend=False, deselect=False, toggle=False, deselect_all=False, select_passthrough=False, location=(0, 0), socket_select=False, clear_viewer=False):
        pass

    def select_all(self, action='TOGGLE'):
        pass

    def select_box(self, tweak=False, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, mode='SET'):
        pass

    def select_circle(self, x=0, y=0, radius=25, wait_for_input=True, mode='SET'):
        pass

    def select_grouped(self, extend=False, type='TYPE'):
        pass

    def select_lasso(self, tweak=False, path=None, mode='SET'):
        pass

    def select_link_viewer(self, NODE_OT_select=None, NODE_OT_link_viewer=None):
        pass

    def select_linked_from(self):
        pass

    def select_linked_to(self):
        pass

    def select_same_type_step(self, prev=False):
        pass

    def shader_script_update(self):
        pass

    def simulation_zone_item_add(self):
        pass

    def simulation_zone_item_move(self, direction='UP'):
        pass

    def simulation_zone_item_remove(self):
        pass

    def switch_view_update(self):
        pass

    def translate_attach(self, TRANSFORM_OT_translate=None, NODE_OT_attach=None):
        pass

    def translate_attach_remove_on_cancel(self, TRANSFORM_OT_translate=None, NODE_OT_attach=None):
        pass

    def tree_path_parent(self):
        pass

    def tree_socket_add(self, in_out='IN'):
        pass

    def tree_socket_change_subtype(self, socket_subtype='DEFAULT'):
        pass

    def tree_socket_change_type(self, in_out='IN', socket_type='DEFAULT'):
        pass

    def tree_socket_move(self, direction='UP', in_out='IN'):
        pass

    def tree_socket_remove(self, in_out='IN'):
        pass

    def view_all(self):
        pass

    def view_selected(self):
        pass

    def viewer_border(self, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True):
        pass