from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import FACE_PARAM_ST


class FaceParamST(Base):
    __tablename__ = "face_param_st"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    geometry_data_00: Mapped[int]
    geometry_data_01: Mapped[int]
    geometry_data_02: Mapped[int]
    geometry_data_03: Mapped[int]
    geometry_data_04: Mapped[int]
    geometry_data_05: Mapped[int]
    geometry_data_06: Mapped[int]
    geometry_data_07: Mapped[int]
    geometry_data_08: Mapped[int]
    geometry_data_09: Mapped[int]
    geometry_data_10: Mapped[int]
    geometry_data_11: Mapped[int]
    geometry_data_12: Mapped[int]
    geometry_data_13: Mapped[int]
    geometry_data_14: Mapped[int]
    geometry_data_15: Mapped[int]
    geometry_data_16: Mapped[int]
    geometry_data_17: Mapped[int]
    geometry_data_18: Mapped[int]
    geometry_data_19: Mapped[int]
    geometry_data_20: Mapped[int]
    geometry_data_21: Mapped[int]
    geometry_data_22: Mapped[int]
    geometry_data_23: Mapped[int]
    geometry_data_24: Mapped[int]
    geometry_data_25: Mapped[int]
    geometry_data_26: Mapped[int]
    geometry_data_27: Mapped[int]
    geometry_data_28: Mapped[int]
    geometry_data_29: Mapped[int]
    geometry_data_30: Mapped[int]
    geometry_data_31: Mapped[int]
    geometry_data_32: Mapped[int]
    geometry_data_33: Mapped[int]
    geometry_data_34: Mapped[int]
    geometry_data_35: Mapped[int]
    geometry_data_36: Mapped[int]
    geometry_data_37: Mapped[int]
    geometry_data_38: Mapped[int]
    geometry_data_39: Mapped[int]
    geometry_data_40: Mapped[int]
    geometry_data_41: Mapped[int]
    geometry_data_42: Mapped[int]
    geometry_data_43: Mapped[int]
    geometry_data_44: Mapped[int]
    geometry_data_45: Mapped[int]
    geometry_data_46: Mapped[int]
    geometry_data_47: Mapped[int]
    geometry_data_48: Mapped[int]
    geometry_data_49: Mapped[int]
    texture_data_00: Mapped[int]
    texture_data_01: Mapped[int]
    texture_data_02: Mapped[int]
    texture_data_03: Mapped[int]
    texture_data_04: Mapped[int]
    texture_data_05: Mapped[int]
    texture_data_06: Mapped[int]
    texture_data_07: Mapped[int]
    texture_data_08: Mapped[int]
    texture_data_09: Mapped[int]
    texture_data_10: Mapped[int]
    texture_data_11: Mapped[int]
    texture_data_12: Mapped[int]
    texture_data_13: Mapped[int]
    texture_data_14: Mapped[int]
    texture_data_15: Mapped[int]
    texture_data_16: Mapped[int]
    texture_data_17: Mapped[int]
    texture_data_18: Mapped[int]
    texture_data_19: Mapped[int]
    texture_data_20: Mapped[int]
    texture_data_21: Mapped[int]
    texture_data_22: Mapped[int]
    texture_data_23: Mapped[int]
    texture_data_24: Mapped[int]
    texture_data_25: Mapped[int]
    texture_data_26: Mapped[int]
    texture_data_27: Mapped[int]
    texture_data_28: Mapped[int]
    texture_data_29: Mapped[int]
    texture_data_30: Mapped[int]
    texture_data_31: Mapped[int]
    texture_data_32: Mapped[int]
    texture_data_33: Mapped[int]
    texture_data_34: Mapped[int]
    texture_data_35: Mapped[int]
    texture_data_36: Mapped[int]
    texture_data_37: Mapped[int]
    texture_data_38: Mapped[int]
    texture_data_39: Mapped[int]
    texture_data_40: Mapped[int]
    texture_data_41: Mapped[int]
    texture_data_42: Mapped[int]
    texture_data_43: Mapped[int]
    texture_data_44: Mapped[int]
    texture_data_45: Mapped[int]
    texture_data_46: Mapped[int]
    texture_data_47: Mapped[int]
    texture_data_48: Mapped[int]
    texture_data_49: Mapped[int]
    hair_style: Mapped[int]
    base_hair_color: Mapped[int]
    hair_color_red: Mapped[int]
    hair_color_green: Mapped[int]
    hair_color_blue: Mapped[int]
    eye_color_red: Mapped[int]
    eye_color_green: Mapped[int]
    eye_color_blue: Mapped[int]
    
    def __init__(self, id: int, param: FACE_PARAM_ST):
        self.id = id
        self.geometry_data_00 = param.GeometryData00
        self.geometry_data_01 = param.GeometryData01
        self.geometry_data_02 = param.GeometryData02
        self.geometry_data_03 = param.GeometryData03
        self.geometry_data_04 = param.GeometryData04
        self.geometry_data_05 = param.GeometryData05
        self.geometry_data_06 = param.GeometryData06
        self.geometry_data_07 = param.GeometryData07
        self.geometry_data_08 = param.GeometryData08
        self.geometry_data_09 = param.GeometryData09
        self.geometry_data_10 = param.GeometryData10
        self.geometry_data_11 = param.GeometryData11
        self.geometry_data_12 = param.GeometryData12
        self.geometry_data_13 = param.GeometryData13
        self.geometry_data_14 = param.GeometryData14
        self.geometry_data_15 = param.GeometryData15
        self.geometry_data_16 = param.GeometryData16
        self.geometry_data_17 = param.GeometryData17
        self.geometry_data_18 = param.GeometryData18
        self.geometry_data_19 = param.GeometryData19
        self.geometry_data_20 = param.GeometryData20
        self.geometry_data_21 = param.GeometryData21
        self.geometry_data_22 = param.GeometryData22
        self.geometry_data_23 = param.GeometryData23
        self.geometry_data_24 = param.GeometryData24
        self.geometry_data_25 = param.GeometryData25
        self.geometry_data_26 = param.GeometryData26
        self.geometry_data_27 = param.GeometryData27
        self.geometry_data_28 = param.GeometryData28
        self.geometry_data_29 = param.GeometryData29
        self.geometry_data_30 = param.GeometryData30
        self.geometry_data_31 = param.GeometryData31
        self.geometry_data_32 = param.GeometryData32
        self.geometry_data_33 = param.GeometryData33
        self.geometry_data_34 = param.GeometryData34
        self.geometry_data_35 = param.GeometryData35
        self.geometry_data_36 = param.GeometryData36
        self.geometry_data_37 = param.GeometryData37
        self.geometry_data_38 = param.GeometryData38
        self.geometry_data_39 = param.GeometryData39
        self.geometry_data_40 = param.GeometryData40
        self.geometry_data_41 = param.GeometryData41
        self.geometry_data_42 = param.GeometryData42
        self.geometry_data_43 = param.GeometryData43
        self.geometry_data_44 = param.GeometryData44
        self.geometry_data_45 = param.GeometryData45
        self.geometry_data_46 = param.GeometryData46
        self.geometry_data_47 = param.GeometryData47
        self.geometry_data_48 = param.GeometryData48
        self.geometry_data_49 = param.GeometryData49
        self.texture_data_00 = param.TextureData00
        self.texture_data_01 = param.TextureData01
        self.texture_data_02 = param.TextureData02
        self.texture_data_03 = param.TextureData03
        self.texture_data_04 = param.TextureData04
        self.texture_data_05 = param.TextureData05
        self.texture_data_06 = param.TextureData06
        self.texture_data_07 = param.TextureData07
        self.texture_data_08 = param.TextureData08
        self.texture_data_09 = param.TextureData09
        self.texture_data_10 = param.TextureData10
        self.texture_data_11 = param.TextureData11
        self.texture_data_12 = param.TextureData12
        self.texture_data_13 = param.TextureData13
        self.texture_data_14 = param.TextureData14
        self.texture_data_15 = param.TextureData15
        self.texture_data_16 = param.TextureData16
        self.texture_data_17 = param.TextureData17
        self.texture_data_18 = param.TextureData18
        self.texture_data_19 = param.TextureData19
        self.texture_data_20 = param.TextureData20
        self.texture_data_21 = param.TextureData21
        self.texture_data_22 = param.TextureData22
        self.texture_data_23 = param.TextureData23
        self.texture_data_24 = param.TextureData24
        self.texture_data_25 = param.TextureData25
        self.texture_data_26 = param.TextureData26
        self.texture_data_27 = param.TextureData27
        self.texture_data_28 = param.TextureData28
        self.texture_data_29 = param.TextureData29
        self.texture_data_30 = param.TextureData30
        self.texture_data_31 = param.TextureData31
        self.texture_data_32 = param.TextureData32
        self.texture_data_33 = param.TextureData33
        self.texture_data_34 = param.TextureData34
        self.texture_data_35 = param.TextureData35
        self.texture_data_36 = param.TextureData36
        self.texture_data_37 = param.TextureData37
        self.texture_data_38 = param.TextureData38
        self.texture_data_39 = param.TextureData39
        self.texture_data_40 = param.TextureData40
        self.texture_data_41 = param.TextureData41
        self.texture_data_42 = param.TextureData42
        self.texture_data_43 = param.TextureData43
        self.texture_data_44 = param.TextureData44
        self.texture_data_45 = param.TextureData45
        self.texture_data_46 = param.TextureData46
        self.texture_data_47 = param.TextureData47
        self.texture_data_48 = param.TextureData48
        self.texture_data_49 = param.TextureData49
        self.hair_style = param.HairStyle
        self.base_hair_color = param.BaseHairColor
        self.hair_color_red = param.HairColorRed
        self.hair_color_green = param.HairColorGreen
        self.hair_color_blue = param.HairColorBlue
        self.eye_color_red = param.EyeColorRed
        self.eye_color_green = param.EyeColorGreen
        self.eye_color_blue = param.EyeColorBlue
