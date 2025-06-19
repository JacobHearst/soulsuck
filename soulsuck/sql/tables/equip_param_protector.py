from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import EQUIP_PARAM_PROTECTOR_ST


class EquipParamProtectorST(Base):
    __tablename__ = "equip_param_protector_st"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    sort_index: Mapped[int]
    ghost_armor_replacement: Mapped[int]
    vagrant_item_lot: Mapped[int]
    vagrant_bonus_enemy_drop_item_lot: Mapped[int]
    vagrant_item_enemy_drop_item_lot: Mapped[int]
    repair_cost: Mapped[int]
    basic_cost: Mapped[int]
    frampt_sell_value: Mapped[int]
    weight: Mapped[float]
    wearer_special_effect1: Mapped[int]
    wearer_special_effect2: Mapped[int]
    wearer_special_effect3: Mapped[int]
    upgrade_material_id: Mapped[int]
    site_damage_multiplier: Mapped[float]
    poise_recovery_time_modifier: Mapped[float]
    upgrade_origin0: Mapped[int]
    upgrade_origin1: Mapped[int]
    upgrade_origin2: Mapped[int]
    upgrade_origin3: Mapped[int]
    upgrade_origin4: Mapped[int]
    upgrade_origin5: Mapped[int]
    upgrade_origin6: Mapped[int]
    upgrade_origin7: Mapped[int]
    upgrade_origin8: Mapped[int]
    upgrade_origin9: Mapped[int]
    upgrade_origin10: Mapped[int]
    upgrade_origin11: Mapped[int]
    upgrade_origin12: Mapped[int]
    upgrade_origin13: Mapped[int]
    upgrade_origin14: Mapped[int]
    upgrade_origin15: Mapped[int]
    male_face_scale_x: Mapped[float]
    male_face_scale_z: Mapped[float]
    male_face_max_scale_x: Mapped[float]
    male_face_max_scale_z: Mapped[float]
    female_face_scale_x: Mapped[float]
    female_face_scale_z: Mapped[float]
    female_face_max_scale_x: Mapped[float]
    female_face_max_scale_z: Mapped[float]
    qwcid: Mapped[int]
    equipment_model: Mapped[int]
    male_icon: Mapped[int]
    female_icon: Mapped[int]
    knockback_percentage_reduction: Mapped[int]
    knockback_bounce_percentage: Mapped[int]
    initial_durability: Mapped[int]
    max_durability: Mapped[int]
    poise: Mapped[int]
    repel_defense: Mapped[int]
    physical_defense: Mapped[int]
    magic_defense: Mapped[int]
    fire_defense: Mapped[int]
    lightning_defense: Mapped[int]
    slash_defense: Mapped[int]
    strike_defense: Mapped[int]
    thrust_defense: Mapped[int]
    poison_resistance: Mapped[int]
    toxic_resistance: Mapped[int]
    bleed_resistance: Mapped[int]
    curse_resistance: Mapped[int]
    armor_upgrade_id: Mapped[int]
    achievement_contribution_id: Mapped[int]
    shop_level: Mapped[int]
    knockback_id: Mapped[int]
    repel_damage_percentage_reduction: Mapped[int]
    equipment_model_category: Mapped[int]
    equipment_model_gender: Mapped[int]
    armor_type: Mapped[int]
    sound_effect_on_hit: Mapped[int]
    visual_effect_on_hit: Mapped[int]
    parts_damage_type: Mapped[int]
    sound_effect_on_weak_spot_hit: Mapped[int]
    visual_effect_on_weak_spot_hit: Mapped[int]
    can_be_stored: Mapped[bool]
    equipped_to_head: Mapped[bool]
    equipped_to_body: Mapped[bool]
    equipped_to_hands: Mapped[bool]
    equipped_to_legs: Mapped[bool]
    use_face_scale: Mapped[bool]
    hide_flag0: Mapped[bool]
    hide_flag1_hair_fringe: Mapped[bool]
    hide_flag2_sideburns: Mapped[bool]
    hide_flag3_top_of_head: Mapped[bool]
    hide_flag4_top_of_head: Mapped[bool]
    hide_flag5_back_hair: Mapped[bool]
    hide_flag6_back_hair_tip: Mapped[bool]
    hide_flag7: Mapped[bool]
    hide_flag8: Mapped[bool]
    hide_flag9: Mapped[bool]
    hide_flag10_collar: Mapped[bool]
    hide_flag11_around_collar: Mapped[bool]
    hide_flag12: Mapped[bool]
    hide_flag13: Mapped[bool]
    hide_flag14: Mapped[bool]
    hide_flag15_hood_hem: Mapped[bool]
    hide_flag16: Mapped[bool]
    hide_flag17: Mapped[bool]
    hide_flag18: Mapped[bool]
    hide_flag19: Mapped[bool]
    hide_flag20_sleeve_a: Mapped[bool]
    hide_flag21_sleeve_b: Mapped[bool]
    hide_flag22: Mapped[bool]
    hide_flag23: Mapped[bool]
    hide_flag24: Mapped[bool]
    hide_flag25_arm: Mapped[bool]
    hide_flag26: Mapped[bool]
    hide_flag27: Mapped[bool]
    hide_flag28: Mapped[bool]
    hide_flag29: Mapped[bool]
    hide_flag30_belt: Mapped[bool]
    hide_flag31: Mapped[bool]
    hide_flag32: Mapped[bool]
    hide_flag33: Mapped[bool]
    hide_flag34: Mapped[bool]
    hide_flag35: Mapped[bool]
    hide_flag36: Mapped[bool]
    hide_flag37: Mapped[bool]
    hide_flag38: Mapped[bool]
    hide_flag39: Mapped[bool]
    hide_flag40: Mapped[bool]
    hide_flag41: Mapped[bool]
    hide_flag42: Mapped[bool]
    hide_flag43: Mapped[bool]
    hide_flag44: Mapped[bool]
    hide_flag45: Mapped[bool]
    hide_flag46: Mapped[bool]
    hide_flag47: Mapped[bool]
    disable_multiplayer_share: Mapped[bool]
    simple_dlc_model_exists: Mapped[bool]
    old_sort_index: Mapped[int]
    
    def __init__(self, id: int, source: EQUIP_PARAM_PROTECTOR_ST):
        self.id = id
        self.sort_index = source.SortIndex
        self.ghost_armor_replacement = source.GhostArmorReplacement
        self.vagrant_item_lot = source.VagrantItemLot
        self.vagrant_bonus_enemy_drop_item_lot = source.VagrantBonusEnemyDropItemLot
        self.vagrant_item_enemy_drop_item_lot = source.VagrantItemEnemyDropItemLot
        self.repair_cost = source.RepairCost
        self.basic_cost = source.BasicCost
        self.frampt_sell_value = source.FramptSellValue
        self.weight = source.Weight
        self.wearer_special_effect1 = source.WearerSpecialEffect1
        self.wearer_special_effect2 = source.WearerSpecialEffect2
        self.wearer_special_effect3 = source.WearerSpecialEffect3
        self.upgrade_material_id = source.UpgradeMaterialID
        self.site_damage_multiplier = source.SiteDamageMultiplier
        self.poise_recovery_time_modifier = source.PoiseRecoveryTimeModifier
        self.upgrade_origin0 = source.UpgradeOrigin0
        self.upgrade_origin1 = source.UpgradeOrigin1
        self.upgrade_origin2 = source.UpgradeOrigin2
        self.upgrade_origin3 = source.UpgradeOrigin3
        self.upgrade_origin4 = source.UpgradeOrigin4
        self.upgrade_origin5 = source.UpgradeOrigin5
        self.upgrade_origin6 = source.UpgradeOrigin6
        self.upgrade_origin7 = source.UpgradeOrigin7
        self.upgrade_origin8 = source.UpgradeOrigin8
        self.upgrade_origin9 = source.UpgradeOrigin9
        self.upgrade_origin10 = source.UpgradeOrigin10
        self.upgrade_origin11 = source.UpgradeOrigin11
        self.upgrade_origin12 = source.UpgradeOrigin12
        self.upgrade_origin13 = source.UpgradeOrigin13
        self.upgrade_origin14 = source.UpgradeOrigin14
        self.upgrade_origin15 = source.UpgradeOrigin15
        self.male_face_scale_x = source.MaleFaceScaleX
        self.male_face_scale_z = source.MaleFaceScaleZ
        self.male_face_max_scale_x = source.MaleFaceMaxScaleX
        self.male_face_max_scale_z = source.MaleFaceMaxScaleZ
        self.female_face_scale_x = source.FemaleFaceScaleX
        self.female_face_scale_z = source.FemaleFaceScaleZ
        self.female_face_max_scale_x = source.FemaleFaceMaxScaleX
        self.female_face_max_scale_z = source.FemaleFaceMaxScaleZ
        self.qwcid = source.QWCID
        self.equipment_model = source.EquipmentModel
        self.male_icon = source.MaleIcon
        self.female_icon = source.FemaleIcon
        self.knockback_percentage_reduction = source.KnockbackPercentageReduction
        self.knockback_bounce_percentage = source.KnockbackBouncePercentage
        self.initial_durability = source.InitialDurability
        self.max_durability = source.MaxDurability
        self.poise = source.Poise
        self.repel_defense = source.RepelDefense
        self.physical_defense = source.PhysicalDefense
        self.magic_defense = source.MagicDefense
        self.fire_defense = source.FireDefense
        self.lightning_defense = source.LightningDefense
        self.slash_defense = source.SlashDefense
        self.strike_defense = source.StrikeDefense
        self.thrust_defense = source.ThrustDefense
        self.poison_resistance = source.PoisonResistance
        self.toxic_resistance = source.ToxicResistance
        self.bleed_resistance = source.BleedResistance
        self.curse_resistance = source.CurseResistance
        self.armor_upgrade_id = source.ArmorUpgradeID
        self.achievement_contribution_id = source.AchievementContributionID
        self.shop_level = source.ShopLevel
        self.knockback_id = source.KnockbackID
        self.repel_damage_percentage_reduction = source.RepelDamagePercentageReduction
        self.equipment_model_category = source.EquipmentModelCategory
        self.equipment_model_gender = source.EquipmentModelGender
        self.armor_type = source.ArmorType
        self.sound_effect_on_hit = source.SoundEffectOnHit
        self.visual_effect_on_hit = source.VisualEffectOnHit
        self.parts_damage_type = source.PartsDamageType
        self.sound_effect_on_weak_spot_hit = source.SoundEffectOnWeakSpotHit
        self.visual_effect_on_weak_spot_hit = source.VisualEffectOnWeakSpotHit
        self.can_be_stored = source.CanBeStored
        self.equipped_to_head = source.EquippedToHead
        self.equipped_to_body = source.EquippedToBody
        self.equipped_to_hands = source.EquippedToHands
        self.equipped_to_legs = source.EquippedToLegs
        self.use_face_scale = source.UseFaceScale
        self.hide_flag0 = source.HideFlag0
        self.hide_flag1_hair_fringe = source.HideFlag1HairFringe
        self.hide_flag2_sideburns = source.HideFlag2Sideburns
        self.hide_flag3_top_of_head = source.HideFlag3TopOfHead
        self.hide_flag4_top_of_head = source.HideFlag4TopOfHead
        self.hide_flag5_back_hair = source.HideFlag5BackHair
        self.hide_flag6_back_hair_tip = source.HideFlag6BackHairTip
        self.hide_flag7 = source.HideFlag7
        self.hide_flag8 = source.HideFlag8
        self.hide_flag9 = source.HideFlag9
        self.hide_flag10_collar = source.HideFlag10Collar
        self.hide_flag11_around_collar = source.HideFlag11AroundCollar
        self.hide_flag12 = source.HideFlag12
        self.hide_flag13 = source.HideFlag13
        self.hide_flag14 = source.HideFlag14
        self.hide_flag15_hood_hem = source.HideFlag15HoodHem
        self.hide_flag16 = source.HideFlag16
        self.hide_flag17 = source.HideFlag17
        self.hide_flag18 = source.HideFlag18
        self.hide_flag19 = source.HideFlag19
        self.hide_flag20_sleeve_a = source.HideFlag20SleeveA
        self.hide_flag21_sleeve_b = source.HideFlag21SleeveB
        self.hide_flag22 = source.HideFlag22
        self.hide_flag23 = source.HideFlag23
        self.hide_flag24 = source.HideFlag24
        self.hide_flag25_arm = source.HideFlag25Arm
        self.hide_flag26 = source.HideFlag26
        self.hide_flag27 = source.HideFlag27
        self.hide_flag28 = source.HideFlag28
        self.hide_flag29 = source.HideFlag29
        self.hide_flag30_belt = source.HideFlag30Belt
        self.hide_flag31 = source.HideFlag31
        self.hide_flag32 = source.HideFlag32
        self.hide_flag33 = source.HideFlag33
        self.hide_flag34 = source.HideFlag34
        self.hide_flag35 = source.HideFlag35
        self.hide_flag36 = source.HideFlag36
        self.hide_flag37 = source.HideFlag37
        self.hide_flag38 = source.HideFlag38
        self.hide_flag39 = source.HideFlag39
        self.hide_flag40 = source.HideFlag40
        self.hide_flag41 = source.HideFlag41
        self.hide_flag42 = source.HideFlag42
        self.hide_flag43 = source.HideFlag43
        self.hide_flag44 = source.HideFlag44
        self.hide_flag45 = source.HideFlag45
        self.hide_flag46 = source.HideFlag46
        self.hide_flag47 = source.HideFlag47
        self.disable_multiplayer_share = source.DisableMultiplayerShare
        self.simple_dlc_model_exists = source.SimpleDLCModelExists
        self.old_sort_index = source.OldSortIndex