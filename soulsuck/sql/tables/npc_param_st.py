from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import NPC_PARAM_ST


class NPCParamST(Base):
    __tablename__ = "npc_param_st"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    behavior_variation_id: Mapped[int]
    default_ai: Mapped[int]
    name_id: Mapped[int]
    turn_velocity: Mapped[float]
    hit_height: Mapped[float]
    hit_radius: Mapped[float]
    weight: Mapped[int]
    hit_y_offset: Mapped[float]
    maximum_hp: Mapped[int]
    maximum_mp: Mapped[int]
    soul_reward: Mapped[int]
    item_lot_id1: Mapped[int]
    item_lot_id2: Mapped[int]
    item_lot_id3: Mapped[int]
    item_lot_id4: Mapped[int]
    item_lot_id5: Mapped[int]
    item_lot_id6: Mapped[int]
    humanity_lot_id: Mapped[int]
    special_effect_id0: Mapped[int]
    special_effect_id1: Mapped[int]
    special_effect_id2: Mapped[int]
    special_effect_id3: Mapped[int]
    special_effect_id4: Mapped[int]
    special_effect_id5: Mapped[int]
    special_effect_id6: Mapped[int]
    special_effect_id7: Mapped[int]
    new_game_plus_special_effect: Mapped[int]
    physical_guard_cut_rate: Mapped[float]
    magic_guard_cut_rate: Mapped[float]
    fire_guard_cut_rate: Mapped[float]
    lightning_guard_cut_rate: Mapped[float]
    animation_id_offset: Mapped[int]
    move_animation_id: Mapped[int]
    special_move_animation_id1: Mapped[int]
    special_move_animation_id2: Mapped[int]
    network_warp_distance: Mapped[float]
    debug_behavior_r1: Mapped[int]
    debug_behavior_l1: Mapped[int]
    debug_behavior_r2: Mapped[int]
    debug_behavior_l2: Mapped[int]
    debug_behavior_rl: Mapped[int]
    debug_behavior_rr: Mapped[int]
    debug_behavior_rd: Mapped[int]
    debug_behavior_ru: Mapped[int]
    debug_behavior_ll: Mapped[int]
    debug_behavior_lr: Mapped[int]
    debug_behavior_ld: Mapped[int]
    debug_behavior_lu: Mapped[int]
    animation_id_offset2: Mapped[int]
    part1_damage_multiplier: Mapped[float]
    part2_damage_multiplier: Mapped[float]
    part3_damage_multiplier: Mapped[float]
    part4_damage_multiplier: Mapped[float]
    part5_damage_multiplier: Mapped[float]
    part6_damage_multiplier: Mapped[float]
    part7_damage_multiplier: Mapped[float]
    part8_damage_multiplier: Mapped[float]
    weak_parts_damage_multiplier: Mapped[float]
    poise_recovery_correction: Mapped[float]
    stagger_knockback_distance: Mapped[float]
    max_stamina: Mapped[int]
    stamina_recovery_base_speed: Mapped[int]
    physical_defense: Mapped[int]
    slash_defense: Mapped[int]
    strike_defense: Mapped[int]
    thrust_defense: Mapped[int]
    magic_defense: Mapped[int]
    fire_defense: Mapped[int]
    lightning_defense: Mapped[int]
    defense_repel_power: Mapped[int]
    poison_resistance: Mapped[int]
    toxic_resistance: Mapped[int]
    bleed_resistance: Mapped[int]
    curse_resistance: Mapped[int]
    ghost_model_id: Mapped[int]
    normal_change_resource_id: Mapped[int]
    guard_angle: Mapped[int]
    slash_damage_reduction_when_guarding: Mapped[int]
    strike_damage_reduction_when_guarding: Mapped[int]
    thrust_damage_reduction_when_guarding: Mapped[int]
    max_poise: Mapped[int]
    normal_change_texture_chr_id: Mapped[int]
    item_drop_appearance: Mapped[int]
    knockback_rate: Mapped[int]
    knockback_id: Mapped[int]
    fall_damage_reduction: Mapped[int]
    stamina_guard_defense: Mapped[int]
    pc_attr_b: Mapped[int]
    pc_attr_w: Mapped[int]
    pc_attr_l: Mapped[int]
    pc_attr_r: Mapped[int]
    area_attr_b: Mapped[int]
    area_attr_w: Mapped[int]
    area_attr_l: Mapped[int]
    area_attr_r: Mapped[int]
    mp_recovery_base_speed: Mapped[int]
    repel_damage_cut_rate: Mapped[int]
    default_lighting_param_id: Mapped[int]
    draw_type: Mapped[int]
    character_type: Mapped[int]
    team_type: Mapped[int]
    move_type: Mapped[int]
    lock_on_distance: Mapped[int]
    material: Mapped[int]
    material_sfx: Mapped[int]
    material_weak: Mapped[int]
    material_weak_sfx: Mapped[int]
    parts_damage_type: Mapped[int]
    max_unduration_angle: Mapped[int]
    guard_level: Mapped[int]
    burn_sfx_type: Mapped[int]
    poison_guard_resistance: Mapped[int]
    toxic_guard_resistance: Mapped[int]
    bleed_guard_resistance: Mapped[int]
    curse_guard_resistance: Mapped[int]
    parry_attack: Mapped[int]
    parry_defense: Mapped[int]
    sfx_size: Mapped[int]
    push_out_camera_region_radius: Mapped[int]
    hit_stop_type: Mapped[int]
    ladder_end_check_offset_top: Mapped[int]
    ladder_end_check_offset_bottom: Mapped[int]
    use_ragdoll_camera_hit: Mapped[bool]
    disable_cloth_rigid_hit: Mapped[bool]
    use_ragdoll: Mapped[bool]
    is_demon: Mapped[bool]
    is_ghost: Mapped[bool]
    is_no_damage_motion: Mapped[bool]
    is_unduration: Mapped[bool]
    is_change_wander_ghost: Mapped[bool]
    model_display_mask0: Mapped[bool]
    model_display_mask1: Mapped[bool]
    model_display_mask2: Mapped[bool]
    model_display_mask3: Mapped[bool]
    model_display_mask4: Mapped[bool]
    model_display_mask5: Mapped[bool]
    model_display_mask6: Mapped[bool]
    model_display_mask7: Mapped[bool]
    model_display_mask8: Mapped[bool]
    model_display_mask9: Mapped[bool]
    model_display_mask10: Mapped[bool]
    model_display_mask11: Mapped[bool]
    model_display_mask12: Mapped[bool]
    model_display_mask13: Mapped[bool]
    model_display_mask14: Mapped[bool]
    model_display_mask15: Mapped[bool]
    enable_neck_turn: Mapped[bool]
    disable_respawn_on_rest: Mapped[bool]
    is_move_animation_wait: Mapped[bool]
    is_crowd: Mapped[bool]
    is_weak_to_divine: Mapped[bool]
    is_weak_to_occult: Mapped[bool]
    is_abyssal: Mapped[bool]
    _bit_pad0: Mapped[int]
    vow_type: Mapped[int]
    disable_initialize_dead: Mapped[bool]
    _bit_pad1: Mapped[int]
    _pad0: Mapped[bytes]
    
    def __init__(self, id: int, source: NPC_PARAM_ST):
        self.id = id
        self.behavior_variation_id = source.BehaviorVariationID
        self.default_ai = source.DefaultAI
        self.name_id = source.NameID
        self.turn_velocity = source.TurnVelocity
        self.hit_height = source.HitHeight
        self.hit_radius = source.HitRadius
        self.weight = source.Weight
        self.hit_y_offset = source.HitYOffset
        self.maximum_hp = source.MaximumHP
        self.maximum_mp = source.MaximumMP
        self.soul_reward = source.SoulReward
        self.item_lot_id1 = source.ItemLotID1
        self.item_lot_id2 = source.ItemLotID2
        self.item_lot_id3 = source.ItemLotID3
        self.item_lot_id4 = source.ItemLotID4
        self.item_lot_id5 = source.ItemLotID5
        self.item_lot_id6 = source.ItemLotID6
        self.humanity_lot_id = source.HumanityLotID
        self.special_effect_id0 = source.SpecialEffectID0
        self.special_effect_id1 = source.SpecialEffectID1
        self.special_effect_id2 = source.SpecialEffectID2
        self.special_effect_id3 = source.SpecialEffectID3
        self.special_effect_id4 = source.SpecialEffectID4
        self.special_effect_id5 = source.SpecialEffectID5
        self.special_effect_id6 = source.SpecialEffectID6
        self.special_effect_id7 = source.SpecialEffectID7
        self.new_game_plus_special_effect = source.NewGamePlusSpecialEffect
        self.physical_guard_cut_rate = source.PhysicalGuardCutRate
        self.magic_guard_cut_rate = source.MagicGuardCutRate
        self.fire_guard_cut_rate = source.FireGuardCutRate
        self.lightning_guard_cut_rate = source.LightningGuardCutRate
        self.animation_id_offset = source.AnimationIDOffset
        self.move_animation_id = source.MoveAnimationID
        self.special_move_animation_id1 = source.SpecialMoveAnimationID1
        self.special_move_animation_id2 = source.SpecialMoveAnimationID2
        self.network_warp_distance = source.NetworkWarpDistance
        self.debug_behavior_r1 = source.DebugBehaviorR1
        self.debug_behavior_l1 = source.DebugBehaviorL1
        self.debug_behavior_r2 = source.DebugBehaviorR2
        self.debug_behavior_l2 = source.DebugBehaviorL2
        self.debug_behavior_rl = source.DebugBehaviorRL
        self.debug_behavior_rr = source.DebugBehaviorRR
        self.debug_behavior_rd = source.DebugBehaviorRD
        self.debug_behavior_ru = source.DebugBehaviorRU
        self.debug_behavior_ll = source.DebugBehaviorLL
        self.debug_behavior_lr = source.DebugBehaviorLR
        self.debug_behavior_ld = source.DebugBehaviorLD
        self.debug_behavior_lu = source.DebugBehaviorLU
        self.animation_id_offset2 = source.AnimationIDOffset2
        self.part1_damage_multiplier = source.Part1DamageMultiplier
        self.part2_damage_multiplier = source.Part2DamageMultiplier
        self.part3_damage_multiplier = source.Part3DamageMultiplier
        self.part4_damage_multiplier = source.Part4DamageMultiplier
        self.part5_damage_multiplier = source.Part5DamageMultiplier
        self.part6_damage_multiplier = source.Part6DamageMultiplier
        self.part7_damage_multiplier = source.Part7DamageMultiplier
        self.part8_damage_multiplier = source.Part8DamageMultiplier
        self.weak_parts_damage_multiplier = source.WeakPartsDamageMultiplier
        self.poise_recovery_correction = source.PoiseRecoveryCorrection
        self.stagger_knockback_distance = source.StaggerKnockbackDistance
        self.max_stamina = source.MaxStamina
        self.stamina_recovery_base_speed = source.StaminaRecoveryBaseSpeed
        self.physical_defense = source.PhysicalDefense
        self.slash_defense = source.SlashDefense
        self.strike_defense = source.StrikeDefense
        self.thrust_defense = source.ThrustDefense
        self.magic_defense = source.MagicDefense
        self.fire_defense = source.FireDefense
        self.lightning_defense = source.LightningDefense
        self.defense_repel_power = source.DefenseRepelPower
        self.poison_resistance = source.PoisonResistance
        self.toxic_resistance = source.ToxicResistance
        self.bleed_resistance = source.BleedResistance
        self.curse_resistance = source.CurseResistance
        self.ghost_model_id = source.GhostModelID
        self.normal_change_resource_id = source.NormalChangeResourceID
        self.guard_angle = source.GuardAngle
        self.slash_damage_reduction_when_guarding = source.SlashDamageReductionWhenGuarding
        self.strike_damage_reduction_when_guarding = source.StrikeDamageReductionWhenGuarding
        self.thrust_damage_reduction_when_guarding = source.ThrustDamageReductionWhenGuarding
        self.max_poise = source.MaxPoise
        self.normal_change_texture_chr_id = source.NormalChangeTextureChrID
        self.item_drop_appearance = source.ItemDropAppearance
        self.knockback_rate = source.KnockbackRate
        self.knockback_id = source.KnockbackID
        self.fall_damage_reduction = source.FallDamageReduction
        self.stamina_guard_defense = source.StaminaGuardDefense
        self.pc_attr_b = source.PCAttrB
        self.pc_attr_w = source.PCAttrW
        self.pc_attr_l = source.PCAttrL
        self.pc_attr_r = source.PCAttrR
        self.area_attr_b = source.AreaAttrB
        self.area_attr_w = source.AreaAttrW
        self.area_attr_l = source.AreaAttrL
        self.area_attr_r = source.AreaAttrR
        self.mp_recovery_base_speed = source.MPRecoveryBaseSpeed
        self.repel_damage_cut_rate = source.RepelDamageCutRate
        self.default_lighting_param_id = source.DefaultLightingParamID
        self.draw_type = source.DrawType
        self.character_type = source.CharacterType
        self.team_type = source.TeamType
        self.move_type = source.MoveType
        self.lock_on_distance = source.LockOnDistance
        self.material = source.Material
        self.material_sfx = source.MaterialSFX
        self.material_weak = source.MaterialWeak
        self.material_weak_sfx = source.MaterialWeakSFX
        self.parts_damage_type = source.PartsDamageType
        self.max_unduration_angle = source.MaxUndurationAngle
        self.guard_level = source.GuardLevel
        self.burn_sfx_type = source.BurnSFXType
        self.poison_guard_resistance = source.PoisonGuardResistance
        self.toxic_guard_resistance = source.ToxicGuardResistance
        self.bleed_guard_resistance = source.BleedGuardResistance
        self.curse_guard_resistance = source.CurseGuardResistance
        self.parry_attack = source.ParryAttack
        self.parry_defense = source.ParryDefense
        self.sfx_size = source.SFXSize
        self.push_out_camera_region_radius = source.PushOutCameraRegionRadius
        self.hit_stop_type = source.HitStopType
        self.ladder_end_check_offset_top = source.LadderEndCheckOffsetTop
        self.ladder_end_check_offset_bottom = source.LadderEndCheckOffsetBottom
        self.use_ragdoll_camera_hit = source.UseRagdollCameraHit
        self.disable_cloth_rigid_hit = source.DisableClothRigidHit
        self.use_ragdoll = source.UseRagdoll
        self.is_demon = source.IsDemon
        self.is_ghost = source.IsGhost
        self.is_no_damage_motion = source.IsNoDamageMotion
        self.is_unduration = source.IsUnduration
        self.is_change_wander_ghost = source.IsChangeWanderGhost
        self.model_display_mask0 = source.ModelDisplayMask0
        self.model_display_mask1 = source.ModelDisplayMask1
        self.model_display_mask2 = source.ModelDisplayMask2
        self.model_display_mask3 = source.ModelDisplayMask3
        self.model_display_mask4 = source.ModelDisplayMask4
        self.model_display_mask5 = source.ModelDisplayMask5
        self.model_display_mask6 = source.ModelDisplayMask6
        self.model_display_mask7 = source.ModelDisplayMask7
        self.model_display_mask8 = source.ModelDisplayMask8
        self.model_display_mask9 = source.ModelDisplayMask9
        self.model_display_mask10 = source.ModelDisplayMask10
        self.model_display_mask11 = source.ModelDisplayMask11
        self.model_display_mask12 = source.ModelDisplayMask12
        self.model_display_mask13 = source.ModelDisplayMask13
        self.model_display_mask14 = source.ModelDisplayMask14
        self.model_display_mask15 = source.ModelDisplayMask15
        self.enable_neck_turn = source.EnableNeckTurn
        self.disable_respawn_on_rest = source.DisableRespawnOnRest
        self.is_move_animation_wait = source.IsMoveAnimationWait
        self.is_crowd = source.IsCrowd
        self.is_weak_to_divine = source.IsWeakToDivine
        self.is_weak_to_occult = source.IsWeakToOccult
        self.is_abyssal = source.IsAbyssal
        self._bit_pad0 = source._BitPad0
        self.vow_type = source.VowType
        self.disable_initialize_dead = source.DisableInitializeDead
        self._bit_pad1 = source._BitPad1
        self._pad0 = source._Pad0