from action_operator import ActionOperator
from anim_operators import AnimOperators
from armature_operators import ArmatureOperators
from asset_operators import AssetOperators
from boid_operators import BoidOperators
from brush_operators import BrushOperators
from buttons_operators import ButtonsOperators
from cachefile_operators import CachefileOperators
from camera_operators import CameraOperators
from clip_operators import ClipOperators
from cloth_operators import ClothOperators
from collection_operators import CollectionOperators
from console_operators import ConsoleOperators
from constraint_operators import ConstraintOperators
from curve_operators import CurveOperators
from curves_operators import CurvesOperators
from cycles_operators import CyclesOperators
from dpaint_operators import DpaintOperators
from ed_operators import EdOperators
from node_operators import NodeOperators

from .object import *  # noqa: F403,F401

# https://docs.blender.org/api/current/bpy.ops.html
action: ActionOperator
anim: AnimOperators
archimesh: any
armature: ArmatureOperators
asset: AssetOperators
boid: BoidOperators
brush: BrushOperators
buttons: ButtonsOperators
cachefile: CachefileOperators
camera: CameraOperators
clip: ClipOperators
cloth: ClothOperators
collection: CollectionOperators
console: ConsoleOperators
constraint: ConstraintOperators
curve: CurveOperators
curve_extras: any
curves: CurvesOperators
curvetools: any
cycles: CyclesOperators
dpaint: DpaintOperators
ed: EdOperators
export_anim: any
export_gcode_format: any
export_mesh: any
export_scene: any
export_svg_format: any
file: any
fluid: any
font: any
geometry: any
gizmogroup: any
gpencil: any
graph: any
image: any
import_anim: any
import_curve: any
import_mesh: any
import_scene: any
info: any
io_export: any
io_import: any
lattice: any
marker: any
mask: any
material: any
mball: any
mesh: any
nla: any
node: NodeOperators
#object: any
outliner: any
paint: any
paintcurve: any
palette: any
particle: any
pose: any
poselib: any
preferences: any
ptcache: any
render: any
rigidbody: any
sapling: any
scene: any
screen: any
script: any
sculpt: any
sculpt_curves: any
sequencer: any
sound: any
spreadsheet: any
surface: any
text: any
texture: any
transform: any
ui: any
uilist: any
uv: any
view2d: any
view3d: any
wm: any
workspace: any
world: any
