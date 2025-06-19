from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import SP_EFFECT_PARAM_ST


class SPEffectParamST(Base):
    __tablename__ = "sp_effect_param_st"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    status_icon: Mapped[int]
    max_hp_percentage_for_effect: Mapped[float]
    effect_duration: Mapped[float]
    update_interval: Mapped[float]
    max_hp_multiplier: Mapped[float]
    max_mp_multiplier: Mapped[float]
    max_stamina_multiplier: Mapped[float]
    incoming_slash_damage_multiplier: Mapped[float]
    incoming_strike_damage_multiplier: Mapped[float]
    incoming_thrust_damage_multiplier: Mapped[float]
    incoming_neutral_damage_multiplier: Mapped[float]
    incoming_magic_damage_multiplier: Mapped[float]
    incoming_fire_damage_multiplier: Mapped[float]
    incoming_lightning_damage_multiplier: Mapped[float]
    outgoing_physical_damage_multiplier: Mapped[float]
    outgoing_magic_damage_multiplier: Mapped[float]
    outgoing_fire_damage_multiplier: Mapped[float]
    outgoing_lightning_damage_multiplier: Mapped[float]
    physical_attack_power_multiplier: Mapped[float]
    magic_attack_power_multiplier: Mapped[float]
    fire_attack_power_multiplier: Mapped[float]
    lightning_attack_power_multiplier: Mapped[float]
    physical_attack_power_addition: Mapped[int]
    magic_attack_power_addition: Mapped[int]
    fire_attack_power_addition: Mapped[int]
    lightning_attack_power_addition: Mapped[int]
    physical_defense_multiplier: Mapped[float]
    magic_defense_multiplier: Mapped[float]
    fire_defense_multiplier: Mapped[float]
    lightning_defense_multiplier: Mapped[float]
    physical_defense_addition: Mapped[int]
    magic_defense_addition: Mapped[int]
    fire_defense_addition: Mapped[int]
    lightning_defense_addition: Mapped[int]
    no_guard_incoming_damage_multiplier: Mapped[float]
    critical_hit_incoming_damage_multiplier: Mapped[float]
    non_critical_hit_incoming_damage_multiplier: Mapped[float]
    max_hp_change_ratio: Mapped[float]
    behavior_to_trigger: Mapped[int]
    hp_reduction_percentage: Mapped[float]
    hp_points_lost: Mapped[int]
    mp_reduction_percentage: Mapped[float]
    mp_points_lost: Mapped[int]
    mp_recovery_speed_change: Mapped[int]
    stamina_reduction_percentage: Mapped[float]
    stamina_points_lost: Mapped[int]
    stamina_recovery_speed_change: Mapped[int]
    magic_effect_time_change: Mapped[float]
    current_durability_addition: Mapped[int]
    max_durability_addition: Mapped[int]
    outgoing_stamina_damage_multiplier: Mapped[float]
    poison_damage: Mapped[int]
    toxic_damage: Mapped[int]
    bleed_damage: Mapped[int]
    curse_damage: Mapped[int]
    fall_damage_multiplier: Mapped[float]
    souls_from_kills_multiplier: Mapped[float]
    max_equip_load_multiplier: Mapped[float]
    max_item_load_multiplier: Mapped[float]
    soul_amount_change: Mapped[int]
    animation_id_offset: Mapped[int]
    soul_reward_multiplier: Mapped[float]
    target_priority_change: Mapped[float]
    enemy_sight_percentage_reduction: Mapped[int]
    enemy_hearing_percentage_reduction: Mapped[int]
    animation_speed_multiplier: Mapped[float]
    poison_resistance_multiplier: Mapped[float]
    toxic_resistance_multiplier: Mapped[float]
    bleed_resistance_multiplier: Mapped[float]
    curse_resistance_multiplier: Mapped[float]
    soul_steal_multiplier: Mapped[float]
    effect_duration_multiplier: Mapped[float]
    hp_recovery_rate: Mapped[float]
    next_special_effect: Mapped[int]
    special_effect_per_update: Mapped[int]
    special_effect_on_attack: Mapped[int]
    guard_defense_flick_power_rate: Mapped[float]
    guard_stamina_multiplier: Mapped[float]
    ray_cast_passing_time: Mapped[int]
    poise_addition: Mapped[int]
    bow_range_percentage_change: Mapped[int]
    special_effect_category: Mapped[int]
    special_effect_priority: Mapped[int]
    save_category: Mapped[int]
    attunement_slot_count_change: Mapped[int]
    attunement_miracle_slot_count_change: Mapped[int]
    humanity_damage: Mapped[int]
    riposte_defense_addition: Mapped[int]
    flick_damage_multiplier: Mapped[int]
    incoming_bleed_damage_percentage: Mapped[int]
    replace_no_impact_level: Mapped[int]
    replace_small_impact_level: Mapped[int]
    replace_medium_impact_level: Mapped[int]
    replace_large_impact_level: Mapped[int]
    replace_blowoff_impact_level: Mapped[int]
    replace_push_impact_level: Mapped[int]
    replace_strike_impact_level: Mapped[int]
    replace_small_blow_impact_level: Mapped[int]
    replace_minimal_impact_level: Mapped[int]
    replace_launch_impact_level: Mapped[int]
    replace_blow_backward_impact_level: Mapped[int]
    replace_breath_burn_impact_level: Mapped[int]
    attack_attribute: Mapped[int]
    element_attribute: Mapped[int]
    special_state: Mapped[int]
    affected_weapon_type: Mapped[int]
    movement_type: Mapped[int]
    effect_duration_multiplier_type: Mapped[int]
    throw_condition: Mapped[int]
    add_behavior_judge_id_condition: Mapped[int]
    add_behavior_judge_id_add: Mapped[int]
    can_affect_self: Mapped[bool]
    can_affect_ally: Mapped[bool]
    can_affect_enemy: Mapped[bool]
    can_affect_player: Mapped[bool]
    can_affect_ai: Mapped[bool]
    can_affect_players: Mapped[bool]
    can_affect_phantoms: Mapped[bool]
    can_affect_white_phantoms: Mapped[bool]
    can_affect_black_phantoms: Mapped[bool]
    can_affect_attacker: Mapped[bool]
    display_icon_when_inactive: Mapped[bool]
    use_visual_effect: Mapped[bool]
    use_intelligence_scaling: Mapped[bool]
    use_faith_scaling: Mapped[bool]
    for_new_game_plus: Mapped[bool]
    affects_magic: Mapped[bool]
    affects_miracles: Mapped[bool]
    clear_soul: Mapped[bool]
    request_white_phantom_summon: Mapped[bool]
    request_black_phantom_summon: Mapped[bool]
    request_invasion: Mapped[bool]
    request_kick: Mapped[bool]
    request_return_to_own_world: Mapped[bool]
    request_npc_invasion: Mapped[bool]
    immortal: Mapped[bool]
    current_hp_ignores_max_hp_change: Mapped[bool]
    ignore_corrosion: Mapped[bool]
    ignore_sight_reduction: Mapped[bool]
    ignore_hearing_reduction: Mapped[bool]
    ignore_magic_disabling: Mapped[bool]
    ignore_fake_targets: Mapped[bool]
    ignore_undead_fake_targets: Mapped[bool]
    ignore_beast_fake_targets: Mapped[bool]
    ignore_gravity: Mapped[bool]
    poison_immunity: Mapped[bool]
    toxic_immunity: Mapped[bool]
    bleed_immunity: Mapped[bool]
    curse_immunity: Mapped[bool]
    enable_charming: Mapped[bool]
    enable_life_time: Mapped[bool]
    has_target: Mapped[bool]
    fire_immunity: Mapped[bool]
    affected_by_effect_extension: Mapped[bool]
    request_coliseum_exit: Mapped[bool]
    _bit_pad0: Mapped[int]
    affects_characters_with_no_covenant: Mapped[bool]
    affects_way_of_white: Mapped[bool]
    affects_princess_guard: Mapped[bool]
    affects_warrior_of_sunlight: Mapped[bool]
    affects_darkwraith: Mapped[bool]
    affects_path_of_the_dragon: Mapped[bool]
    affects_gravelord_servant: Mapped[bool]
    affects_forest_hunter: Mapped[bool]
    affects_darkmoon_blade: Mapped[bool]
    affects_chaos_servant: Mapped[bool]
    affects_covenant10: Mapped[bool]
    affects_covenant11: Mapped[bool]
    affects_covenant12: Mapped[bool]
    affects_covenant13: Mapped[bool]
    affects_covenant14: Mapped[bool]
    affects_covenant15: Mapped[bool]
    _pad0: Mapped[bytes]
    
    def __init__(self, id: int, source: SP_EFFECT_PARAM_ST):
        self.id = id
        self.status_icon = source.StatusIcon
        self.max_hp_percentage_for_effect = source.MaxHPPercentageForEffect
        self.effect_duration = source.EffectDuration
        self.update_interval = source.UpdateInterval
        self.max_hp_multiplier = source.MaxHPMultiplier
        self.max_mp_multiplier = source.MaxMPMultiplier
        self.max_stamina_multiplier = source.MaxStaminaMultiplier
        self.incoming_slash_damage_multiplier = source.IncomingSlashDamageMultiplier
        self.incoming_strike_damage_multiplier = source.IncomingStrikeDamageMultiplier
        self.incoming_thrust_damage_multiplier = source.IncomingThrustDamageMultiplier
        self.incoming_neutral_damage_multiplier = source.IncomingNeutralDamageMultiplier
        self.incoming_magic_damage_multiplier = source.IncomingMagicDamageMultiplier
        self.incoming_fire_damage_multiplier = source.IncomingFireDamageMultiplier
        self.incoming_lightning_damage_multiplier = source.IncomingLightningDamageMultiplier
        self.outgoing_physical_damage_multiplier = source.OutgoingPhysicalDamageMultiplier
        self.outgoing_magic_damage_multiplier = source.OutgoingMagicDamageMultiplier
        self.outgoing_fire_damage_multiplier = source.OutgoingFireDamageMultiplier
        self.outgoing_lightning_damage_multiplier = source.OutgoingLightningDamageMultiplier
        self.physical_attack_power_multiplier = source.PhysicalAttackPowerMultiplier
        self.magic_attack_power_multiplier = source.MagicAttackPowerMultiplier
        self.fire_attack_power_multiplier = source.FireAttackPowerMultiplier
        self.lightning_attack_power_multiplier = source.LightningAttackPowerMultiplier
        self.physical_attack_power_addition = source.PhysicalAttackPowerAddition
        self.magic_attack_power_addition = source.MagicAttackPowerAddition
        self.fire_attack_power_addition = source.FireAttackPowerAddition
        self.lightning_attack_power_addition = source.LightningAttackPowerAddition
        self.physical_defense_multiplier = source.PhysicalDefenseMultiplier
        self.magic_defense_multiplier = source.MagicDefenseMultiplier
        self.fire_defense_multiplier = source.FireDefenseMultiplier
        self.lightning_defense_multiplier = source.LightningDefenseMultiplier
        self.physical_defense_addition = source.PhysicalDefenseAddition
        self.magic_defense_addition = source.MagicDefenseAddition
        self.fire_defense_addition = source.FireDefenseAddition
        self.lightning_defense_addition = source.LightningDefenseAddition
        self.no_guard_incoming_damage_multiplier = source.NoGuardIncomingDamageMultiplier
        self.critical_hit_incoming_damage_multiplier = source.CriticalHitIncomingDamageMultiplier
        self.non_critical_hit_incoming_damage_multiplier = source.NonCriticalHitIncomingDamageMultiplier
        self.max_hp_change_ratio = source.MaxHPChangeRatio
        self.behavior_to_trigger = source.BehaviorToTrigger
        self.hp_reduction_percentage = source.HPReductionPercentage
        self.hp_points_lost = source.HPPointsLost
        self.mp_reduction_percentage = source.MPReductionPercentage
        self.mp_points_lost = source.MPPointsLost
        self.mp_recovery_speed_change = source.MPRecoverySpeedChange
        self.stamina_reduction_percentage = source.StaminaReductionPercentage
        self.stamina_points_lost = source.StaminaPointsLost
        self.stamina_recovery_speed_change = source.StaminaRecoverySpeedChange
        self.magic_effect_time_change = source.MagicEffectTimeChange
        self.current_durability_addition = source.CurrentDurabilityAddition
        self.max_durability_addition = source.MaxDurabilityAddition
        self.outgoing_stamina_damage_multiplier = source.OutgoingStaminaDamageMultiplier
        self.poison_damage = source.PoisonDamage
        self.toxic_damage = source.ToxicDamage
        self.bleed_damage = source.BleedDamage
        self.curse_damage = source.CurseDamage
        self.fall_damage_multiplier = source.FallDamageMultiplier
        self.souls_from_kills_multiplier = source.SoulsFromKillsMultiplier
        self.max_equip_load_multiplier = source.MaxEquipLoadMultiplier
        self.max_item_load_multiplier = source.MaxItemLoadMultiplier
        self.soul_amount_change = source.SoulAmountChange
        self.animation_id_offset = source.AnimationIDOffset
        self.soul_reward_multiplier = source.SoulRewardMultiplier
        self.target_priority_change = source.TargetPriorityChange
        self.enemy_sight_percentage_reduction = source.EnemySightPercentageReduction
        self.enemy_hearing_percentage_reduction = source.EnemyHearingPercentageReduction
        self.animation_speed_multiplier = source.AnimationSpeedMultiplier
        self.poison_resistance_multiplier = source.PoisonResistanceMultiplier
        self.toxic_resistance_multiplier = source.ToxicResistanceMultiplier
        self.bleed_resistance_multiplier = source.BleedResistanceMultiplier
        self.curse_resistance_multiplier = source.CurseResistanceMultiplier
        self.soul_steal_multiplier = source.SoulStealMultiplier
        self.effect_duration_multiplier = source.EffectDurationMultiplier
        self.hp_recovery_rate = source.HPRecoveryRate
        self.next_special_effect = source.NextSpecialEffect
        self.special_effect_per_update = source.SpecialEffectPerUpdate
        self.special_effect_on_attack = source.SpecialEffectOnAttack
        self.guard_defense_flick_power_rate = source.GuardDefenseFlickPowerRate
        self.guard_stamina_multiplier = source.GuardStaminaMultiplier
        self.ray_cast_passing_time = source.RayCastPassingTime
        self.poise_addition = source.PoiseAddition
        self.bow_range_percentage_change = source.BowRangePercentageChange
        self.special_effect_category = source.SpecialEffectCategory
        self.special_effect_priority = source.SpecialEffectPriority
        self.save_category = source.SaveCategory
        self.attunement_slot_count_change = source.AttunementSlotCountChange
        self.attunement_miracle_slot_count_change = source.AttunementMiracleSlotCountChange
        self.humanity_damage = source.HumanityDamage
        self.riposte_defense_addition = source.RiposteDefenseAddition
        self.flick_damage_multiplier = source.FlickDamageMultiplier
        self.incoming_bleed_damage_percentage = source.IncomingBleedDamagePercentage
        self.replace_no_impact_level = source.ReplaceNoImpactLevel
        self.replace_small_impact_level = source.ReplaceSmallImpactLevel
        self.replace_medium_impact_level = source.ReplaceMediumImpactLevel
        self.replace_large_impact_level = source.ReplaceLargeImpactLevel
        self.replace_blowoff_impact_level = source.ReplaceBlowoffImpactLevel
        self.replace_push_impact_level = source.ReplacePushImpactLevel
        self.replace_strike_impact_level = source.ReplaceStrikeImpactLevel
        self.replace_small_blow_impact_level = source.ReplaceSmallBlowImpactLevel
        self.replace_minimal_impact_level = source.ReplaceMinimalImpactLevel
        self.replace_launch_impact_level = source.ReplaceLaunchImpactLevel
        self.replace_blow_backward_impact_level = source.ReplaceBlowBackwardImpactLevel
        self.replace_breath_burn_impact_level = source.ReplaceBreathBurnImpactLevel
        self.attack_attribute = source.AttackAttribute
        self.element_attribute = source.ElementAttribute
        self.special_state = source.SpecialState
        self.affected_weapon_type = source.AffectedWeaponType
        self.movement_type = source.MovementType
        self.effect_duration_multiplier_type = source.EffectDurationMultiplierType
        self.throw_condition = source.ThrowCondition
        self.add_behavior_judge_id_condition = source.AddBehaviorJudgeIDCondition
        self.add_behavior_judge_id_add = source.AddBehaviorJudgeIDAdd
        self.can_affect_self = source.CanAffectSelf
        self.can_affect_ally = source.CanAffectAlly
        self.can_affect_enemy = source.CanAffectEnemy
        self.can_affect_player = source.CanAffectPlayer
        self.can_affect_ai = source.CanAffectAI
        self.can_affect_players = source.CanAffectPlayers
        self.can_affect_phantoms = source.CanAffectPhantoms
        self.can_affect_white_phantoms = source.CanAffectWhitePhantoms
        self.can_affect_black_phantoms = source.CanAffectBlackPhantoms
        self.can_affect_attacker = source.CanAffectAttacker
        self.display_icon_when_inactive = source.DisplayIconWhenInactive
        self.use_visual_effect = source.UseVisualEffect
        self.use_intelligence_scaling = source.UseIntelligenceScaling
        self.use_faith_scaling = source.UseFaithScaling
        self.for_new_game_plus = source.ForNewGamePlus
        self.affects_magic = source.AffectsMagic
        self.affects_miracles = source.AffectsMiracles
        self.clear_soul = source.ClearSoul
        self.request_white_phantom_summon = source.RequestWhitePhantomSummon
        self.request_black_phantom_summon = source.RequestBlackPhantomSummon
        self.request_invasion = source.RequestInvasion
        self.request_kick = source.RequestKick
        self.request_return_to_own_world = source.RequestReturnToOwnWorld
        self.request_npc_invasion = source.RequestNPCInvasion
        self.immortal = source.Immortal
        self.current_hp_ignores_max_hp_change = source.CurrentHPIgnoresMaxHPChange
        self.ignore_corrosion = source.IgnoreCorrosion
        self.ignore_sight_reduction = source.IgnoreSightReduction
        self.ignore_hearing_reduction = source.IgnoreHearingReduction
        self.ignore_magic_disabling = source.IgnoreMagicDisabling
        self.ignore_fake_targets = source.IgnoreFakeTargets
        self.ignore_undead_fake_targets = source.IgnoreUndeadFakeTargets
        self.ignore_beast_fake_targets = source.IgnoreBeastFakeTargets
        self.ignore_gravity = source.IgnoreGravity
        self.poison_immunity = source.PoisonImmunity
        self.toxic_immunity = source.ToxicImmunity
        self.bleed_immunity = source.BleedImmunity
        self.curse_immunity = source.CurseImmunity
        self.enable_charming = source.EnableCharming
        self.enable_life_time = source.EnableLifeTime
        self.has_target = source.HasTarget
        self.fire_immunity = source.FireImmunity
        self.affected_by_effect_extension = source.AffectedByEffectExtension
        self.request_coliseum_exit = source.RequestColiseumExit
        self._bit_pad0 = source._BitPad0
        self.affects_characters_with_no_covenant = source.AffectsCharactersWithNoCovenant
        self.affects_way_of_white = source.AffectsWayOfWhite
        self.affects_princess_guard = source.AffectsPrincessGuard
        self.affects_warrior_of_sunlight = source.AffectsWarriorOfSunlight
        self.affects_darkwraith = source.AffectsDarkwraith
        self.affects_path_of_the_dragon = source.AffectsPathOfTheDragon
        self.affects_gravelord_servant = source.AffectsGravelordServant
        self.affects_forest_hunter = source.AffectsForestHunter
        self.affects_darkmoon_blade = source.AffectsDarkmoonBlade
        self.affects_chaos_servant = source.AffectsChaosServant
        self.affects_covenant10 = source.AffectsCovenant10
        self.affects_covenant11 = source.AffectsCovenant11
        self.affects_covenant12 = source.AffectsCovenant12
        self.affects_covenant13 = source.AffectsCovenant13
        self.affects_covenant14 = source.AffectsCovenant14
        self.affects_covenant15 = source.AffectsCovenant15
        self._pad0 = source._Pad0