from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import THROW_INFO_BANK


class ThrowInfoBank(Base):
    __tablename__ = "throw_info_bank"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    attacking_character_model: Mapped[int]
    defending_character_model: Mapped[int]
    max_distance: Mapped[float]
    min_difference_in_facing_angle: Mapped[float]
    max_difference_in_facing_angle: Mapped[float]
    max_distance_above: Mapped[float]
    max_distance_below: Mapped[float]
    max_angle_to_defender: Mapped[float]
    throw_id: Mapped[int]
    attacker_animation: Mapped[int]
    defender_animation: Mapped[int]
    min_hp_percentage_for_escape: Mapped[int]
    escape_cycle_time: Mapped[int]
    sphere_cast_upper_radius_ratio: Mapped[int]
    sphere_cast_lower_radius_ratio: Mapped[int]
    button_mash_type: Mapped[int]
    attack_enabled: Mapped[int]
    snap_to_attacker_model_point: Mapped[int]
    snap_to_defender_model_point: Mapped[int]
    throw_type: Mapped[int]
    escape_cycle_count: Mapped[int]
    model_point_character_direction_type: Mapped[int]
    attacker_turns: Mapped[bool]
    skip_attacker_weapon_category_check: Mapped[bool]
    skip_sphere_cast: Mapped[bool]
    _bit_pad0: Mapped[int]
    _pad0: Mapped[bytes]
    
    def __init__(self, id: int, source: THROW_INFO_BANK):
        self.id = id
        self.attacking_character_model = source.AttackingCharacterModel
        self.defending_character_model = source.DefendingCharacterModel
        self.max_distance = source.MaxDistance
        self.min_difference_in_facing_angle = source.MinDifferenceInFacingAngle
        self.max_difference_in_facing_angle = source.MaxDifferenceInFacingAngle
        self.max_distance_above = source.MaxDistanceAbove
        self.max_distance_below = source.MaxDistanceBelow
        self.max_angle_to_defender = source.MaxAngleToDefender
        self.throw_id = source.ThrowID
        self.attacker_animation = source.AttackerAnimation
        self.defender_animation = source.DefenderAnimation
        self.min_hp_percentage_for_escape = source.MinHPPercentageForEscape
        self.escape_cycle_time = source.EscapeCycleTime
        self.sphere_cast_upper_radius_ratio = source.SphereCastUpperRadiusRatio
        self.sphere_cast_lower_radius_ratio = source.SphereCastLowerRadiusRatio
        self.button_mash_type = source.ButtonMashType
        self.attack_enabled = source.AttackEnabled
        self.snap_to_attacker_model_point = source.SnapToAttackerModelPoint
        self.snap_to_defender_model_point = source.SnapToDefenderModelPoint
        self.throw_type = source.ThrowType
        self.escape_cycle_count = source.EscapeCycleCount
        self.model_point_character_direction_type = source.ModelPointCharacterDirectionType
        self.attacker_turns = source.AttackerTurns
        self.skip_attacker_weapon_category_check = source.SkipAttackerWeaponCategoryCheck
        self.skip_sphere_cast = source.SkipSphereCast
        self._bit_pad0 = source._BitPad0
        self._pad0 = source._Pad0