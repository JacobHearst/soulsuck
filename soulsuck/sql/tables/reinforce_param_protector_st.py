from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import REINFORCE_PARAM_PROTECTOR_ST


class ReinforceParamProtectorST(Base):
    __tablename__ = "reinforce_param_protector_st"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    physical_defense_multiplier: Mapped[float]
    magic_defense_multiplier: Mapped[float]
    fire_defense_multiplier: Mapped[float]
    lightning_defense_multiplier: Mapped[float]
    slash_defense_multiplier: Mapped[float]
    strike_defense_multiplier: Mapped[float]
    thrust_defense_multiplier: Mapped[float]
    poison_resistance_multiplier: Mapped[float]
    toxic_resistance_multiplier: Mapped[float]
    bleed_resistance_multiplier: Mapped[float]
    curse_resistance_multiplier: Mapped[float]
    wearer_special_effect1: Mapped[int]
    wearer_special_effect2: Mapped[int]
    wearer_special_effect3: Mapped[int]
    upgrade_material_id: Mapped[int]
    
    def __init__(self, id: int, source: REINFORCE_PARAM_PROTECTOR_ST):
        self.id = id
        self.physical_defense_multiplier = source.PhysicalDefenseMultiplier
        self.magic_defense_multiplier = source.MagicDefenseMultiplier
        self.fire_defense_multiplier = source.FireDefenseMultiplier
        self.lightning_defense_multiplier = source.LightningDefenseMultiplier
        self.slash_defense_multiplier = source.SlashDefenseMultiplier
        self.strike_defense_multiplier = source.StrikeDefenseMultiplier
        self.thrust_defense_multiplier = source.ThrustDefenseMultiplier
        self.poison_resistance_multiplier = source.PoisonResistanceMultiplier
        self.toxic_resistance_multiplier = source.ToxicResistanceMultiplier
        self.bleed_resistance_multiplier = source.BleedResistanceMultiplier
        self.curse_resistance_multiplier = source.CurseResistanceMultiplier
        self.wearer_special_effect1 = source.WearerSpecialEffect1
        self.wearer_special_effect2 = source.WearerSpecialEffect2
        self.wearer_special_effect3 = source.WearerSpecialEffect3
        self.upgrade_material_id = source.UpgradeMaterialID