class ClipOperators:
    def add_marker(self, location=(0.0, 0.0)):
        pass

    def add_marker_at_click(self):
        pass

    def add_marker_move(self, CLIP_OT_add_marker=None, TRANSFORM_OT_translate=None):
        pass

    def add_marker_slide(self, CLIP_OT_add_marker=None, TRANSFORM_OT_translate=None):
        pass

    def apply_solution_scale(self, distance=0.0):
        pass

    def average_tracks(self, keep_original=True):
        pass

    def bundles_to_mesh(self):
        pass

    def camera_preset_add(self, name='', remove_name=False, remove_active=False, use_focal_length=True):
        pass

    def change_frame(self, frame=0):
        pass

    def clean_tracks(self, frames=0, error=0.0, action='SELECT'):
        pass

    def clear_solution(self):
        pass

    def clear_track_path(self, action='REMAINED', clear_active=False):
        pass

    def constraint_to_fcurve(self):
        pass

    def copy_tracks(self):
        pass

    def create_plane_track(self):
        pass

    def cursor_set(self, location=(0.0, 0.0)):
        pass

    def delete_marker(self, confirm=True):
        pass

    def delete_proxy(self):
        pass

    def delete_track(self, confirm=True):
        pass

    def detect_features(self, placement='FRAME', margin=16, threshold=0.5, min_distance=120):
        pass

    def disable_markers(self, action='DISABLE'):
        pass

    def dopesheet_select_channel(self, location=(0.0, 0.0), extend=False):
        pass

    def dopesheet_view_all(self):
        pass

    def filter_tracks(self, track_threshold=5.0):
        pass

    def frame_jump(self, position='PATHSTART'):
        pass

    def graph_center_current_frame(self):
        pass

    def graph_delete_curve(self, confirm=True):
        pass

    def graph_delete_knot(self):
        pass

    def graph_disable_markers(self, action='DISABLE'):
        pass

    def graph_select(self, location=(0.0, 0.0), extend=False):
        pass

    def graph_select_all_markers(self, action='TOGGLE'):
        pass

    def graph_select_box(self, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, deselect=False, extend=True):
        pass

    def graph_view_all(self):
        pass

    def hide_tracks(self, unselected=False):
        pass

    def hide_tracks_clear(self):
        pass

    def join_tracks(self):
        pass

    def keyframe_delete(self):
        pass

    def keyframe_insert(self):
        pass

    def lock_selection_toggle(self):
        pass

    def lock_tracks(self, action='LOCK'):
        pass

    def mode_set(self, mode='TRACKING'):
        pass

    def new_image_from_plane_marker(self):
        pass

    def open(self, directory='', files=None, hide_props_region=True, check_existing=False, filter_blender=False, filter_backup=False, filter_image=True, filter_movie=True, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method=''):
        pass

    def paste_tracks(self):
        pass

    def prefetch(self):
        pass

    def rebuild_proxy(self):
        pass

    def refine_markers(self, backwards=False):
        pass

    def reload(self):
        pass

    def select(self, extend=False, deselect_all=False, location=(0.0, 0.0)):
        pass

    def select_all(self, action='TOGGLE'):
        pass

    def select_box(self, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, mode='SET'):
        pass

    def select_circle(self, x=0, y=0, radius=25, wait_for_input=True, mode='SET'):
        pass

    def select_grouped(self, group='ESTIMATED'):
        pass

    def select_lasso(self, path=None, mode='SET'):
        pass

    def set_active_clip(self):
        pass

    def set_axis(self, axis='X'):
        pass

    def set_origin(self, use_median=False):
        pass

    def set_plane(self, plane='FLOOR'):
        pass

    def set_scale(self, distance=0.0):
        pass

    def set_scene_frames(self):
        pass

    def set_solution_scale(self, distance=0.0):
        pass

    def set_solver_keyframe(self, keyframe='KEYFRAME_A'):
        pass

    def set_viewport_background(self):
        pass

    def setup_tracking_scene(self):
        pass

    def slide_marker(self, offset=(0.0, 0.0)):
        pass

    def slide_plane_marker(self):
        pass

    def solve_camera(self):
        pass

    def stabilize_2d_add(self):
        pass

    def stabilize_2d_remove(self):
        pass

    def stabilize_2d_rotation_add(self):
        pass

    def stabilize_2d_rotation_remove(self):
        pass

    def stabilize_2d_rotation_select(self):
        pass

    def stabilize_2d_select(self):
        pass

    def track_color_preset_add(self, name='', remove_name=False, remove_active=False):
        pass

    def track_copy_color(self):
        pass

    def track_markers(self, backwards=False, sequence=False):
        pass

    def track_settings_as_default(self):
        pass

    def track_settings_to_track(self):
        pass

    def track_to_empty(self):
        pass

    def tracking_object_new(self):
        pass

    def tracking_object_remove(self):
        pass

    def tracking_settings_preset_add(self, name='', remove_name=False, remove_active=False):
        pass

    def update_image_from_plane_marker(self):
        pass

    def view_all(self, fit_view=False):
        pass

    def view_center_cursor(self):
        pass

    def view_ndof(self):
        pass

    def view_pan(self, offset=(0.0, 0.0)):
        pass

    def view_selected(self):
        pass

    def view_zoom(self, factor=0.0, use_cursor_init=True):
        pass

    def view_zoom_in(self, location=(0.0, 0.0)):
        pass

    def view_zoom_out(self, location=(0.0, 0.0)):
        pass

    def view_zoom_ratio(self, ratio=0.0):
        pass