from id import ID
from anim_data import AnimData

class Key(ID):
    animation_data: AnimData
    eval_time: float
    key_blocks: any
    reference_key: any
    use_relative: bool
    user: ID
