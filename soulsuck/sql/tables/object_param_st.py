from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import OBJECT_PARAM_ST


class ObjectParamST(Base):
    __tablename__ = "object_param_st"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    object_hp: Mapped[int]
    min_attack_for_damage: Mapped[int]
    external_texture_id: Mapped[int]
    material_id: Mapped[int]
    max_destruction_animation_id: Mapped[int]
    collides_with_camera: Mapped[bool]
    broken_by_player_collision: Mapped[bool]
    has_destruction_animation: Mapped[bool]
    hit_by_piercing_bullets: Mapped[bool]
    character_collision: Mapped[bool]
    deflects_attacks: Mapped[bool]
    cannot_spawn_broken: Mapped[bool]
    is_ladder: Mapped[bool]
    stop_animation_during_cutscenes: Mapped[bool]
    prevent_all_damage: Mapped[bool]
    is_moving_object: Mapped[bool]
    _bit_pad0: Mapped[int]
    default_lod: Mapped[int]
    destruction_sound_effect: Mapped[int]
    
    def __init__(self, id: int, source: OBJECT_PARAM_ST):
        self.id = id
        self.object_hp = source.ObjectHP
        self.min_attack_for_damage = source.MinAttackForDamage
        self.external_texture_id = source.ExternalTextureID
        self.material_id = source.MaterialID
        self.max_destruction_animation_id = source.MaxDestructionAnimationID
        self.collides_with_camera = source.CollidesWithCamera
        self.broken_by_player_collision = source.BrokenByPlayerCollision
        self.has_destruction_animation = source.HasDestructionAnimation
        self.hit_by_piercing_bullets = source.HitByPiercingBullets
        self.character_collision = source.CharacterCollision
        self.deflects_attacks = source.DeflectsAttacks
        self.cannot_spawn_broken = source.CannotSpawnBroken
        self.is_ladder = source.IsLadder
        self.stop_animation_during_cutscenes = source.StopAnimationDuringCutscenes
        self.prevent_all_damage = source.PreventAllDamage
        self.is_moving_object = source.IsMovingObject
        self._bit_pad0 = source._BitPad0
        self.default_lod = source.DefaultLOD
        self.destruction_sound_effect = source.DestructionSoundEffect