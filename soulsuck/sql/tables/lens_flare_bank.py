from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import LENS_FLARE_BANK


class LensFlareBank(Base):
    __tablename__ = "lens_flare_bank"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    lens_flare_texture_id: Mapped[int]
    is_lens_flare: Mapped[int]
    enable_rotation: Mapped[int]
    enable_scaling: Mapped[int]
    position_ratio: Mapped[float]
    texture_scale: Mapped[float]
    texture_red: Mapped[int]
    texture_green: Mapped[int]
    texture_blue: Mapped[int]
    texture_alpha: Mapped[int]
    
    def __init__(self, id: int, param: LENS_FLARE_BANK):
        self.id = id
        self.lens_flare_texture_id = param.LensFlareTextureID
        self.is_lens_flare = param.IsLensFlare
        self.enable_rotation = param.EnableRotation
        self.enable_scaling = param.EnableScaling
        self.position_ratio = param.PositionRatio
        self.texture_scale = param.TextureScale
        self.texture_red = param.TextureRed
        self.texture_green = param.TextureGreen
        self.texture_blue = param.TextureBlue
        self.texture_alpha = param.TextureAlpha
