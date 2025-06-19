from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import LOCK_CAM_PARAM_ST


class LockCamParamST(Base):
    __tablename__ = "lock_cam_param_st"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    camera_distance_from_target: Mapped[float]
    min_rotation_elevation: Mapped[float]
    lock_elevation_shift_ratio: Mapped[float]
    character_vertical_offset: Mapped[float]
    max_distance_from_character: Mapped[float]
    vertical_field_of_view: Mapped[float]
    
    def __init__(self, id: int, param: LOCK_CAM_PARAM_ST):
        self.id = id
        self.camera_distance_from_target = param.CameraDistanceFromTarget
        self.min_rotation_elevation = param.MinRotationElevation
        self.lock_elevation_shift_ratio = param.LockElevationShiftRatio
        self.character_vertical_offset = param.CharacterVerticalOffset
        self.max_distance_from_character = param.MaxDistanceFromCharacter
        self.vertical_field_of_view = param.VerticalFieldOfView
