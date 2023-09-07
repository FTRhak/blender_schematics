class ActionOperator():

    def clean(self, threshold: float=0.001, channels: bool=False):
        pass

    def clickselect(self, wait_to_deselect_others=False, mouse_x=0, mouse_y=0, extend=False, deselect_all=False, column=False, channel=False):
        pass

    def copy(self):
        pass

    def delete(self, confirm=True):
        pass

    def duplicate(self):
        pass

    def duplicate_move(self, ACTION_OT_duplicate=None, TRANSFORM_OT_transform=None):
        pass

    def easing_type(self, type='AUTO'):
        pass

    def extrapolation_type(self, type='CONSTANT'):
        pass

    def frame_jump(self):
        pass

    def handle_type(self, type='FREE'):
        pass

    def interpolation_type(self, type='CONSTANT'):
        pass

    def keyframe_insert(self, type='ALL'):
        pass

    def keyframe_type(self, type='KEYFRAME'):
        pass

    def layer_next(self):
        pass

    def layer_prev(self):
        pass

    def markers_make_local(self):
        pass

    def mirror(self, type='CFRA'):
        pass

    def new(self):
        pass

    def paste(self, offset='START', merge='MIX', flipped=False):
        pass

    def previewrange_set(self):
        pass

    def push_down(self):
        pass

    def sample(self):
        pass

    def select_all(self, action='TOGGLE'):
        pass

    def select_box(self, axis_range=False, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, mode='SET', tweak=False):
        pass

    def select_circle(self, x=0, y=0, radius=25, wait_for_input=True, mode='SET'):
        pass

    def select_column(self, mode='KEYS'):
        pass

    def select_lasso(self, path=None, mode='SET'):
        pass

    def select_leftright(self, mode='CHECK', extend=False):
        pass

    def select_less(self):
        pass

    def select_linked(self):
        pass

    def select_more(self):
        pass

    def snap(self, type='CFRA'):
        pass

    def stash(self, create_new=True):
        pass

    def stash_and_create(self):
        pass

    def unlink(self, force_delete=False):
        pass

    def view_all(self):
        pass

    def view_frame(self):
        pass

    def view_selected(self):
        pass

