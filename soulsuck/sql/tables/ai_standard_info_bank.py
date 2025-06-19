from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import AI_STANDARD_INFO_BANK


class AIStandardInfoBank(Base):
    __tablename__ = "ai_standard_info_bank"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    radar_range: Mapped[int]
    radar_angle_x: Mapped[int]
    radar_angle_y: Mapped[int]
    territory_size: Mapped[int]
    threat_before_attack_rate: Mapped[int]
    force_threat_on_first_locked: Mapped[int]
    _pad0: Mapped[bytes]
    attack1_distance: Mapped[int]
    attack1_margin: Mapped[int]
    attack1_rate: Mapped[int]
    attack1_action_id: Mapped[int]
    attack1_delay_min: Mapped[int]
    attack1_delay_max: Mapped[int]
    attack1_cone_angle: Mapped[int]
    _pad1: Mapped[bytes]
    attack2_distance: Mapped[int]
    attack2_margin: Mapped[int]
    attack2_rate: Mapped[int]
    attack2_action_id: Mapped[int]
    attack2_delay_min: Mapped[int]
    attack2_delay_max: Mapped[int]
    attack2_cone_angle: Mapped[int]
    _pad2: Mapped[bytes]
    attack3_distance: Mapped[int]
    attack3_margin: Mapped[int]
    attack3_rate: Mapped[int]
    attack3_action_id: Mapped[int]
    attack3_delay_min: Mapped[int]
    attack3_delay_max: Mapped[int]
    attack3_cone_angle: Mapped[int]
    _pad3: Mapped[bytes]
    attack4_distance: Mapped[int]
    attack4_margin: Mapped[int]
    attack4_rate: Mapped[int]
    attack4_action_id: Mapped[int]
    attack4_delay_min: Mapped[int]
    attack4_delay_max: Mapped[int]
    attack4_cone_angle: Mapped[int]
    _pad4: Mapped[bytes]
    _pad5: Mapped[bytes]
    
    def __init__(self, id: int, source: AI_STANDARD_INFO_BANK):
        self.id = id
        self.radar_range = source.RadarRange
        self.radar_angle_x = source.RadarAngleX
        self.radar_angle_y = source.RadarAngleY
        self.territory_size = source.TerritorySize
        self.threat_before_attack_rate = source.ThreatBeforeAttackRate
        self.force_threat_on_first_locked = source.ForceThreatOnFirstLocked
        self._pad0 = source._Pad0
        self.attack1_distance = source.Attack1Distance
        self.attack1_margin = source.Attack1Margin
        self.attack1_rate = source.Attack1Rate
        self.attack1_action_id = source.Attack1ActionID
        self.attack1_delay_min = source.Attack1DelayMin
        self.attack1_delay_max = source.Attack1DelayMax
        self.attack1_cone_angle = source.Attack1ConeAngle
        self._pad1 = source._Pad1
        self.attack2_distance = source.Attack2Distance
        self.attack2_margin = source.Attack2Margin
        self.attack2_rate = source.Attack2Rate
        self.attack2_action_id = source.Attack2ActionID
        self.attack2_delay_min = source.Attack2DelayMin
        self.attack2_delay_max = source.Attack2DelayMax
        self.attack2_cone_angle = source.Attack2ConeAngle
        self._pad2 = source._Pad2
        self.attack3_distance = source.Attack3Distance
        self.attack3_margin = source.Attack3Margin
        self.attack3_rate = source.Attack3Rate
        self.attack3_action_id = source.Attack3ActionID
        self.attack3_delay_min = source.Attack3DelayMin
        self.attack3_delay_max = source.Attack3DelayMax
        self.attack3_cone_angle = source.Attack3ConeAngle
        self._pad3 = source._Pad3
        self.attack4_distance = source.Attack4Distance
        self.attack4_margin = source.Attack4Margin
        self.attack4_rate = source.Attack4Rate
        self.attack4_action_id = source.Attack4ActionID
        self.attack4_delay_min = source.Attack4DelayMin
        self.attack4_delay_max = source.Attack4DelayMax
        self.attack4_cone_angle = source.Attack4ConeAngle
        self._pad4 = source._Pad4
        self._pad5 = source._Pad5