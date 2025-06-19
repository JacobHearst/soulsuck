from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import TONE_MAP_BANK


class ToneMapBank(Base):
    __tablename__ = "tone_map_bank"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    near_bloom_threshold: Mapped[int]
    near_bloom_multiplier: Mapped[int]
    far_bloom_threshold: Mapped[int]
    far_bloom_multiplier: Mapped[int]
    near_bloom_end_distance: Mapped[float]
    far_bloom_start_distance: Mapped[float]
    overall_brightness: Mapped[float]
    minimum_adaptation_brightness: Mapped[float]
    maximum_adaptation_brightness: Mapped[float]
    adaptation_speed: Mapped[float]
    light_shaft_threshold: Mapped[int]
    light_shaft_magnitude: Mapped[float]
    light_shaft_attenuation_rate: Mapped[float]
    
    def __init__(self, id: int, tone_map_bank: TONE_MAP_BANK):
        self.id = id
        self.near_bloom_threshold = tone_map_bank.NearBloomThreshold
        self.near_bloom_multiplier = tone_map_bank.NearBloomMultiplier
        self.far_bloom_threshold = tone_map_bank.FarBloomThreshold
        self.far_bloom_multiplier = tone_map_bank.FarBloomMultiplier
        self.near_bloom_end_distance = tone_map_bank.NearBloomEndDistance
        self.far_bloom_start_distance = tone_map_bank.FarBloomStartDistance
        self.overall_brightness = tone_map_bank.OverallBrightness
        self.minimum_adaptation_brightness = tone_map_bank.MinimumAdaptationBrightness
        self.maximum_adaptation_brightness = tone_map_bank.MaximumAdaptationBrightness
        self.adaptation_speed = tone_map_bank.AdaptationSpeed
        self.light_shaft_threshold = tone_map_bank.LightShaftThreshold
        self.light_shaft_magnitude = tone_map_bank.LightShaftMagnitude
        self.light_shaft_attenuation_rate = tone_map_bank.LightShaftAttenuationRate