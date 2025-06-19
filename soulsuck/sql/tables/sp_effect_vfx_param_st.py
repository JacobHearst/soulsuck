from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import SP_EFFECT_VFX_PARAM_ST


class SpEffectVfxParamSt(Base):
    __tablename__ = "sp_effect_vfx_param_st"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    ongoing_visual_effect: Mapped[int]
    ongoing_sound_effect: Mapped[int]
    initial_visual_effect: Mapped[int]
    initial_sound_effect: Mapped[int]
    finish_visual_effect: Mapped[int]
    finish_sound_effect: Mapped[int]
    hide_start_distance: Mapped[float]
    hide_end_distance: Mapped[float]
    transformation_armor_id: Mapped[int]
    ongoing_model_point: Mapped[int]
    initial_model_point: Mapped[int]
    finish_model_point: Mapped[int]
    effect_type: Mapped[int]
    weapon_enchantment_soul_param: Mapped[int]
    playback_category: Mapped[int]
    playback_priority: Mapped[int]
    large_effect_exists: Mapped[bool]
    soul_effect_exists: Mapped[bool]
    invisible_when_hidden: Mapped[bool]
    hiding_active: Mapped[bool]
    invisible_when_friend_hidden: Mapped[bool]
    add_map_area_block_offset: Mapped[bool]
    half_hidden_only: Mapped[bool]
    armor_transformation_is_full_body: Mapped[bool]
    hide_weapon: Mapped[bool]
    is_silent: Mapped[bool]
    
    def __init__(self, id: int, sp_effect_vfx: SP_EFFECT_VFX_PARAM_ST):
        self.id = id
        self.ongoing_visual_effect = sp_effect_vfx.OngoingVisualEffect
        self.ongoing_sound_effect = sp_effect_vfx.OngoingSoundEffect
        self.initial_visual_effect = sp_effect_vfx.InitialVisualEffect
        self.initial_sound_effect = sp_effect_vfx.InitialSoundEffect
        self.finish_visual_effect = sp_effect_vfx.FinishVisualEffect
        self.finish_sound_effect = sp_effect_vfx.FinishSoundEffect
        self.hide_start_distance = sp_effect_vfx.HideStartDistance
        self.hide_end_distance = sp_effect_vfx.HideEndDistance
        self.transformation_armor_id = sp_effect_vfx.TransformationArmorID
        self.ongoing_model_point = sp_effect_vfx.OngoingModelPoint
        self.initial_model_point = sp_effect_vfx.InitialModelPoint
        self.finish_model_point = sp_effect_vfx.FinishModelPoint
        self.effect_type = sp_effect_vfx.EffectType
        self.weapon_enchantment_soul_param = sp_effect_vfx.WeaponEnchantmentSoulParam
        self.playback_category = sp_effect_vfx.PlaybackCategory
        self.playback_priority = sp_effect_vfx.PlaybackPriority
        self.large_effect_exists = sp_effect_vfx.LargeEffectExists
        self.soul_effect_exists = sp_effect_vfx.SoulEffectExists
        self.invisible_when_hidden = sp_effect_vfx.InvisibleWhenHidden
        self.hiding_active = sp_effect_vfx.HidingActive
        self.invisible_when_friend_hidden = sp_effect_vfx.InvisibleWhenFriendHidden
        self.add_map_area_block_offset = sp_effect_vfx.AddMapAreaBlockOffset
        self.half_hidden_only = sp_effect_vfx.HalfHiddenOnly
        self.armor_transformation_is_full_body = sp_effect_vfx.ArmorTransformationIsFullBody
        self.hide_weapon = sp_effect_vfx.HideWeapon
        self.is_silent = sp_effect_vfx.IsSilent