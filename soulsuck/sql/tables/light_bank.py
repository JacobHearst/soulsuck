from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import LIGHT_BANK


class LightBank(Base):
    __tablename__ = "light_bank"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    baked_light_0_rotation_x: Mapped[int]
    baked_light_0_rotation_y: Mapped[int]
    baked_light_0_red: Mapped[int]
    baked_light_0_green: Mapped[int]
    baked_light_0_blue: Mapped[int]
    baked_light_0_alpha: Mapped[int]
    baked_light_1_rotation_x: Mapped[int]
    baked_light_1_rotation_y: Mapped[int]
    baked_light_1_red: Mapped[int]
    baked_light_1_green: Mapped[int]
    baked_light_1_blue: Mapped[int]
    baked_light_1_alpha: Mapped[int]
    baked_light_2_rotation_x: Mapped[int]
    baked_light_2_rotation_y: Mapped[int]
    baked_light_2_red: Mapped[int]
    baked_light_2_green: Mapped[int]
    baked_light_2_blue: Mapped[int]
    baked_light_2_alpha: Mapped[int]
    top_down_light_red: Mapped[int]
    top_down_light_green: Mapped[int]
    top_down_light_blue: Mapped[int]
    top_down_light_alpha: Mapped[int]
    bottom_up_light_red: Mapped[int]
    bottom_up_light_green: Mapped[int]
    bottom_up_light_blue: Mapped[int]
    bottom_up_light_alpha: Mapped[int]
    specular_baked_light_rotation_x: Mapped[int]
    specular_baked_light_rotation_y: Mapped[int]
    specular_baked_light_red: Mapped[int]
    specular_baked_light_green: Mapped[int]
    specular_baked_light_blue: Mapped[int]
    specular_baked_light_alpha: Mapped[int]
    diffuse_light_red: Mapped[int]
    diffuse_light_green: Mapped[int]
    diffuse_light_blue: Mapped[int]
    diffuse_light_alpha: Mapped[int]
    specular_light_red: Mapped[int]
    specular_light_green: Mapped[int]
    specular_light_blue: Mapped[int]
    specular_light_alpha: Mapped[int]
    diffuse_light_texture_id: Mapped[int]
    specular_light_texture_id_0: Mapped[int]
    specular_light_texture_id_1: Mapped[int]
    specular_light_texture_id_2: Mapped[int]
    specular_light_texture_id_3: Mapped[int]
    
    def __init__(self, id: int, param: LIGHT_BANK):
        self.id = id
        self.baked_light_0_rotation_x = param.BakedLight0RotationX
        self.baked_light_0_rotation_y = param.BakedLight0RotationY
        self.baked_light_0_red = param.BakedLight0Red
        self.baked_light_0_green = param.BakedLight0Green
        self.baked_light_0_blue = param.BakedLight0Blue
        self.baked_light_0_alpha = param.BakedLight0Alpha
        self.baked_light_1_rotation_x = param.BakedLight1RotationX
        self.baked_light_1_rotation_y = param.BakedLight1RotationY
        self.baked_light_1_red = param.BakedLight1Red
        self.baked_light_1_green = param.BakedLight1Green
        self.baked_light_1_blue = param.BakedLight1Blue
        self.baked_light_1_alpha = param.BakedLight1Alpha
        self.baked_light_2_rotation_x = param.BakedLight2RotationX
        self.baked_light_2_rotation_y = param.BakedLight2RotationY
        self.baked_light_2_red = param.BakedLight2Red
        self.baked_light_2_green = param.BakedLight2Green
        self.baked_light_2_blue = param.BakedLight2Blue
        self.baked_light_2_alpha = param.BakedLight2Alpha
        self.top_down_light_red = param.TopDownLightRed
        self.top_down_light_green = param.TopDownLightGreen
        self.top_down_light_blue = param.TopDownLightBlue
        self.top_down_light_alpha = param.TopDownLightAlpha
        self.bottom_up_light_red = param.BottomUpLightRed
        self.bottom_up_light_green = param.BottomUpLightGreen
        self.bottom_up_light_blue = param.BottomUpLightBlue
        self.bottom_up_light_alpha = param.BottomUpLightAlpha
        self.specular_baked_light_rotation_x = param.SpecularBakedLightRotationX
        self.specular_baked_light_rotation_y = param.SpecularBakedLightRotationY
        self.specular_baked_light_red = param.SpecularBakedLightRed
        self.specular_baked_light_green = param.SpecularBakedLightGreen
        self.specular_baked_light_blue = param.SpecularBakedLightBlue
        self.specular_baked_light_alpha = param.SpecularBakedLightAlpha
        self.diffuse_light_red = param.DiffuseLightRed
        self.diffuse_light_green = param.DiffuseLightGreen
        self.diffuse_light_blue = param.DiffuseLightBlue
        self.diffuse_light_alpha = param.DiffuseLightAlpha
        self.specular_light_red = param.SpecularLightRed
        self.specular_light_green = param.SpecularLightGreen
        self.specular_light_blue = param.SpecularLightBlue
        self.specular_light_alpha = param.SpecularLightAlpha
        self.diffuse_light_texture_id = param.DiffuseLightTextureID
        self.specular_light_texture_id_0 = param.SpecularLightTextureID0
        self.specular_light_texture_id_1 = param.SpecularLightTextureID1
        self.specular_light_texture_id_2 = param.SpecularLightTextureID2
        self.specular_light_texture_id_3 = param.SpecularLightTextureID3
