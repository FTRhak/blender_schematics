class CurveOperators:
    def cyclic_toggle(self, direction='CYCLIC_U'):
        pass

    def de_select_first(self):
        pass

    def de_select_last(self):
        pass

    def decimate(self, ratio=1.0):
        pass

    def delete(self, type='VERT'):
        pass

    def dissolve_verts(self):
        pass

    def draw(self, error_threshold=0.0, fit_method='REFIT', corner_angle=1.22173, use_cyclic=True, stroke=None, wait_for_input=True):
        pass

    def duplicate(self):
        pass

    def duplicate_move(self, CURVE_OT_duplicate=None, TRANSFORM_OT_translate=None):
        pass

    def extrude(self, mode='TRANSLATION'):
        pass

    def extrude_move(self, CURVE_OT_extrude=None, TRANSFORM_OT_translate=None):
        pass

    def handle_type_set(self, type='AUTOMATIC'):
        pass

    def hide(self, unselected=False):
        pass

    def make_segment(self):
        pass

    def match_texture_space(self):
        pass

    def normals_make_consistent(self, calc_length=False):
        pass

    def pen(self, extend=False, deselect=False, toggle=False, deselect_all=False, select_passthrough=False, extrude_point=False, extrude_handle='VECTOR', delete_point=False, insert_point=False, move_segment=False, select_point=False, move_point=False, close_spline=True, close_spline_method='OFF', toggle_vector=False, cycle_handle_type=False):
        pass

    def primitive_bezier_circle_add(self, radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0)):
        pass

    def primitive_bezier_curve_add(self, radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0)):
        pass

    def primitive_nurbs_circle_add(self, radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0)):
        pass

    def primitive_nurbs_curve_add(self, radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0)):
        pass

    def primitive_nurbs_path_add(self, radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0)):
        pass

    def radius_set(self, radius=1.0):
        pass

    def reveal(self, select=True):
        pass

    def select_all(self, action='TOGGLE'):
        pass

    def select_less(self):
        pass

    def select_linked(self):
        pass

    def select_linked_pick(self, deselect=False):
        pass

    def select_more(self):
        pass

    def select_next(self):
        pass

    def select_nth(self, skip=1, nth=1, offset=0):
        pass

    def select_previous(self):
        pass

    def select_random(self, ratio=0.5, seed=0, action='SELECT'):
        pass

    def select_row(self):
        pass

    def select_similar(self, type='WEIGHT', compare='EQUAL', threshold=0.1):
        pass

    def separate(self, confirm=True):
        pass

    def shade_flat(self):
        pass

    def shade_smooth(self):
        pass

    def shortest_path_pick(self):
        pass

    def smooth(self):
        pass

    def smooth_radius(self):
        pass

    def smooth_tilt(self):
        pass

    def smooth_weight(self):
        pass

    def spin(self, center=(0.0, 0.0, 0.0), axis=(0.0, 0.0, 0.0)):
        pass

    def spline_type_set(self, type='POLY', use_handles=False):
        pass

    def spline_weight_set(self, weight=1.0):
        pass

    def split(self):
        pass

    def subdivide(self, number_cuts=1):
        pass

    def switch_direction(self):
        pass

    def tilt_clear(self):
        pass

    def vertex_add(self, location=(0.0, 0.0, 0.0)):
        pass