from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import TONE_CORRECT_BANK


class ToneCorrectBank(Base):
    __tablename__ = "tone_correct_bank"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    brightness_red: Mapped[float]
    brightness_green: Mapped[float]
    brightness_blue: Mapped[float]
    contrast_red: Mapped[float]
    contrast_green: Mapped[float]
    contrast_blue: Mapped[float]
    saturation_correction: Mapped[float]
    hue_correction: Mapped[float]
    
    def __init__(self, id: int, tone_correct_bank: TONE_CORRECT_BANK):
        self.id = id
        self.brightness_red = tone_correct_bank.BrightnessRed
        self.brightness_green = tone_correct_bank.BrightnessGreen
        self.brightness_blue = tone_correct_bank.BrightnessBlue
        self.contrast_red = tone_correct_bank.ContrastRed
        self.contrast_green = tone_correct_bank.ContrastGreen
        self.contrast_blue = tone_correct_bank.ContrastBlue
        self.saturation_correction = tone_correct_bank.SaturationCorrection
        self.hue_correction = tone_correct_bank.HueCorrection