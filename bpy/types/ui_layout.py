from bpy.types.bpy_struct import bpy_struct
from bpy.types.operator_properties import OperatorProperties

# https://docs.blender.org/api/current/bpy.types.UILayout.html
class UILayout(bpy_struct):
    activate_init: bool
    active: bool
    active_default: bool
    alert: bool
    alignment: any
    direction: any
    emboss: any
    enabled: bool
    operator_context: any
    scale_x: float
    scale_y: float
    ui_units_x: float
    ui_units_y: float
    use_property_decorate: bool
    use_property_split: bool

    def row(self, align=False, heading='', heading_ctxt='', translate=True):
        pass

    def column(self, align=False, heading='', heading_ctxt='', translate=True):
        pass

    def column_flow(self, columns=0, align=False):
        pass

    def grid_flow(self, row_major=False, columns=0, even_columns=False, even_rows=False, align=False):
        pass

    def box(self):
        pass

    def split(self, factor=0.0, align=False):
        pass

    def menu_pie(self):
        pass

    @classmethod
    def icon(data):
        pass

    @classmethod
    def enum_item_name(data, property, identifier):
        pass

    @classmethod
    def enum_item_description(data, property, identifier):
        pass

    @classmethod
    def enum_item_icon(data, property, identifier):
        pass

    def prop(self, data, property, text='', text_ctxt='', translate=True, icon='NONE', expand=False, slider=False, toggle=-1, icon_only=False, event=False, full_event=False, emboss=True, index=-1, icon_value=0, invert_checkbox=False):
        pass

    def props_enum(self, data, property):
        pass

    def prop_menu_enum(self, data, property, text='', text_ctxt='', translate=True, icon='NONE'):
        pass

    def prop_with_popover(self, data, property, text="", text_ctxt="", translate=True, icon='NONE', icon_only=False, panel: str = ''):
        pass

    def prop_with_menu(self, data, property, text="", text_ctxt="", translate=True, icon='NONE', icon_only=False, menu: str = ''):
        pass

    def prop_tabs_enum(self, data, property, data_highlight=None, property_highlight='', icon_only=False):
        pass

    def prop_enum(self, data, property, value, text='', text_ctxt='', translate=True, icon='NONE'):
        pass

    def prop_search(self, data, property, search_data, search_property, text='', text_ctxt='', translate=True, icon='NONE', results_are_suggestions=False):
        pass

    def prop_decorator(self, data, property, index=-1):
        pass

    def operator(self, operator: str, text: str='', text_ctxt: str='', translate: bool=True, icon: any='NONE', emboss=True, depress=False, icon_value: int=0) -> OperatorProperties:
        pass

    def operator_menu_hold(self, operator: str, text="", text_ctxt="", translate=True, icon='NONE', emboss=True, depress=False, icon_value=0, menu: str = '') -> OperatorProperties:
        pass

    def operator_enum(self, operator: str, property: str, icon_only=False) -> None:
        pass

    def operator_menu_enum(self, operator: str, property: str, text='', text_ctxt='', translate=True, icon='NONE') -> OperatorProperties:
        pass

    def label(self, text='', text_ctxt='', translate=True, icon='NONE', icon_value=0):
        pass

    def menu(self, menu: str, text='', text_ctxt='', translate=True, icon='NONE', icon_value=0):
        pass

    def menu_contents(self, menu: str):
        pass

    def popover(self, panel: str, text='', text_ctxt='', translate=True, icon='NONE', icon_value=0):
        pass

    def popover_group(self, space_type: any, region_type: any, context: str, category: str):
        pass

    def separator(self, factor: float=1.0):
        pass

    def separator_spacer(self):
        pass

    def context_pointer_set(self, name: str, data: any):
        pass

    def template_header(self):
        pass

    def template_ID(self, data: any, property: str, new='', open='', unlink='', filter='ALL', live_icon=False, text='', text_ctxt='', translate=True):
        pass

    def template_ID_preview(self, data: any, property: str, new='', open='', unlink='', rows=0, cols=0, filter='ALL', hide_buttons=False):
        pass

    def template_any_ID(self, data: any, property: str, type_property, text='', text_ctxt='', translate=True):
        pass

    def template_ID_tabs(self, data, property, new='', menu='', filter='ALL'):
        pass

    def template_search(self, data, property, search_data, search_property, new='', unlink=''):
        pass

    def template_search_preview(self, data, property, search_data, search_property, new='', unlink='', rows=0, cols=0):
        pass

    def template_path_builder(self, data, property, root, text='', text_ctxt='', translate=True):
        pass

    def template_modifiers(self):
        pass

    def template_constraints(self, use_bone_constraints=True):
        pass

    def template_grease_pencil_modifiers(self):
        pass

    def template_shaderfx(self):
        pass

    def template_greasepencil_color(self, data, property, rows=0, cols=0, scale=1.0, filter='ALL'):
        pass

    def template_constraint_header(self, data):
        pass

    def template_preview(self, id, show_buttons=True, parent=None, slot=None, preview_id=''):
        pass

    def template_curve_mapping(self, data, property, type='NONE', levels=False, brush=False, use_negative_slope=False, show_tone=False):
        pass

    def template_curveprofile(self, data, property):
        pass

    def template_color_ramp(self, data, property, expand=False):
        pass

    def template_icon(self, icon_value: int, scale=1.0):
        pass

    def template_icon_view(self, data, property, show_labels=False, scale=6.0, scale_popup=5.0):
        pass

    def template_histogram(self, data, property):
        pass

    def template_waveform(self, data, property):
        pass

    def template_vectorscope(self, data, property):
        pass

    def template_layers(self, data, property, used_layers_data, used_layers_property, active_layer):
        pass

    def template_color_picker(self, data, property, value_slider=False, lock=False, lock_luminosity=False, cubic=False):
        pass

    def template_palette(self, data, property, color=False):
        pass

    def template_image_layers(self, image, image_user):
        pass

    def template_image(self, data, property, image_user, compact=False, multiview=False):
        pass

    def template_image_settings(self, image_settings, color_management=False, show_z_buffer=True):
        pass

    def template_image_stereo_3d(self, stereo_3d_format):
        pass

    def template_image_views(self, image_settings):
        pass

    def template_movieclip(self, data, property, compact=False):
        pass

    def template_track(self, data, property):
        pass

    def template_marker(self, data, property, clip_user, track, compact=False):
        pass

    def template_movieclip_information(self, data, property, clip_user):
        pass

    def template_list(self, listtype_name, list_id, dataptr, propname, active_dataptr, active_propname, item_dyntip_propname='', rows=5, maxrows=5, type='DEFAULT', columns=9, sort_reverse=False, sort_lock=False):
        pass

    def template_running_jobs(self):
        pass

    def template_operator_search(self):
        pass

    def template_menu_search(self):
        pass

    def template_header_3D_mode(self):
        pass

    def template_edit_mode_selection(self):
        pass

    def template_reports_banner(self):
        pass

    def template_input_status(self):
        pass

    def template_status_info(self):
        pass

    def template_node_link(self, ntree, node, socket):
        pass

    def template_node_view(self, ntree, node, socket):
        pass

    def template_node_asset_menu_items(self, catalog_path=''):
        pass

    def template_texture_user(self):
        pass

    def template_keymap_item_properties(self, item):
        pass

    def template_component_menu(self, data, property, name=''):
        pass

    def template_colorspace_settings(self, data, property):
        pass

    def template_colormanaged_view_settings(self, data, property):
        pass

    def template_node_socket(self, color=(0.0, 0.0, 0.0, 1.0)):
        pass

    def template_cache_file(self, data, property):
        pass

    def template_cache_file_velocity(self, data, property):
        pass

    def template_cache_file_procedural(self, data, property):
        pass

    def template_cache_file_time_settings(self, data, property):
        pass

    def template_cache_file_layers(self, data, property):
        pass

    def template_recent_files(self, rows=5):
        pass

    def template_file_select_path(self, params):
        pass

    def template_event_from_keymap_item(self, item, text='', text_ctxt='', translate=True):
        pass

    def template_asset_view(self, list_id: str, asset_library_dataptr: any, asset_library_propname: str, assets_dataptr, assets_propname, active_dataptr, active_propname, filter_id_types={}, display_options={}, activate_operator='', drag_operator=''):
        pass


    @classmethod
    def bl_rna_get_subclass(id, default=None):
        pass

    @classmethod
    def bl_rna_get_subclass_py(id, default=None):
        pass