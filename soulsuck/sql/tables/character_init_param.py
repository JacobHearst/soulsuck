from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import CHARACTER_INIT_PARAM


class CharacterInitParam(Base):
    __tablename__ = "character_init_param"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    base_rec_mp: Mapped[float]
    base_rec_sp: Mapped[float]
    red_fall_damage: Mapped[float]
    soul_count: Mapped[int]
    right_hand_weapon1: Mapped[int]
    right_hand_weapon2: Mapped[int]
    left_hand_weapon1: Mapped[int]
    left_hand_weapon2: Mapped[int]
    head_armor: Mapped[int]
    body_armor: Mapped[int]
    hands_armor: Mapped[int]
    legs_armor: Mapped[int]
    arrow_slot1: Mapped[int]
    bolt_slot1: Mapped[int]
    arrow_slot2: Mapped[int]
    bolt_slot2: Mapped[int]
    ring_slot1: Mapped[int]
    ring_slot2: Mapped[int]
    ring_slot3: Mapped[int]
    ring_slot4: Mapped[int]
    ring_slot5: Mapped[int]
    skill_slot1: Mapped[int]
    skill_slot2: Mapped[int]
    skill_slot3: Mapped[int]
    spell_slot1: Mapped[int]
    spell_slot2: Mapped[int]
    spell_slot3: Mapped[int]
    spell_slot4: Mapped[int]
    spell_slot5: Mapped[int]
    spell_slot6: Mapped[int]
    spell_slot7: Mapped[int]
    good_slot1: Mapped[int]
    good_slot2: Mapped[int]
    good_slot3: Mapped[int]
    good_slot4: Mapped[int]
    good_slot5: Mapped[int]
    good_slot6: Mapped[int]
    good_slot7: Mapped[int]
    good_slot8: Mapped[int]
    good_slot9: Mapped[int]
    good_slot10: Mapped[int]
    face_id: Mapped[int]
    default_ai: Mapped[int]
    base_max_hp: Mapped[int]
    base_max_mp: Mapped[int]
    base_max_stamina: Mapped[int]
    arrow_slot1_count: Mapped[int]
    bolt_slot1_count: Mapped[int]
    arrow_slot2_count: Mapped[int]
    bolt_slot2_count: Mapped[int]
    qwc_sb: Mapped[int]
    qwc_mw: Mapped[int]
    qwc_cd: Mapped[int]
    level: Mapped[int]
    vitality: Mapped[int]
    attunement: Mapped[int]
    endurance: Mapped[int]
    strength: Mapped[int]
    dexterity: Mapped[int]
    intelligence: Mapped[int]
    faith: Mapped[int]
    luck: Mapped[int]
    humanity: Mapped[int]
    resistance: Mapped[int]
    good_slot1_count: Mapped[int]
    good_slot2_count: Mapped[int]
    good_slot3_count: Mapped[int]
    good_slot4_count: Mapped[int]
    good_slot5_count: Mapped[int]
    good_slot6_count: Mapped[int]
    good_slot7_count: Mapped[int]
    good_slot8_count: Mapped[int]
    good_slot9_count: Mapped[int]
    good_slot10_count: Mapped[int]
    head_scale: Mapped[int]
    chest_scale: Mapped[int]
    abdomen_scale: Mapped[int]
    arm_scale: Mapped[int]
    leg_scale: Mapped[int]
    gesture1: Mapped[int]
    gesture2: Mapped[int]
    gesture3: Mapped[int]
    gesture4: Mapped[int]
    gesture5: Mapped[int]
    gesture6: Mapped[int]
    gesture7: Mapped[int]
    character_type: Mapped[int]
    draw_type: Mapped[int]
    gender: Mapped[int]
    covenant: Mapped[int]
    _bit_pad0: Mapped[int]
    _pad0: Mapped[bytes]
    
    def __init__(self, id: int, source: CHARACTER_INIT_PARAM):
        self.id = id
        self.base_rec_mp = source.BaseRecMP
        self.base_rec_sp = source.BaseRecSP
        self.red_fall_damage = source.RedFallDamage
        self.soul_count = source.SoulCount
        self.right_hand_weapon1 = source.RightHandWeapon1
        self.right_hand_weapon2 = source.RightHandWeapon2
        self.left_hand_weapon1 = source.LeftHandWeapon1
        self.left_hand_weapon2 = source.LeftHandWeapon2
        self.head_armor = source.HeadArmor
        self.body_armor = source.BodyArmor
        self.hands_armor = source.HandsArmor
        self.legs_armor = source.LegsArmor
        self.arrow_slot1 = source.ArrowSlot1
        self.bolt_slot1 = source.BoltSlot1
        self.arrow_slot2 = source.ArrowSlot2
        self.bolt_slot2 = source.BoltSlot2
        self.ring_slot1 = source.RingSlot1
        self.ring_slot2 = source.RingSlot2
        self.ring_slot3 = source.RingSlot3
        self.ring_slot4 = source.RingSlot4
        self.ring_slot5 = source.RingSlot5
        self.skill_slot1 = source.SkillSlot1
        self.skill_slot2 = source.SkillSlot2
        self.skill_slot3 = source.SkillSlot3
        self.spell_slot1 = source.SpellSlot1
        self.spell_slot2 = source.SpellSlot2
        self.spell_slot3 = source.SpellSlot3
        self.spell_slot4 = source.SpellSlot4
        self.spell_slot5 = source.SpellSlot5
        self.spell_slot6 = source.SpellSlot6
        self.spell_slot7 = source.SpellSlot7
        self.good_slot1 = source.GoodSlot1
        self.good_slot2 = source.GoodSlot2
        self.good_slot3 = source.GoodSlot3
        self.good_slot4 = source.GoodSlot4
        self.good_slot5 = source.GoodSlot5
        self.good_slot6 = source.GoodSlot6
        self.good_slot7 = source.GoodSlot7
        self.good_slot8 = source.GoodSlot8
        self.good_slot9 = source.GoodSlot9
        self.good_slot10 = source.GoodSlot10
        self.face_id = source.FaceID
        self.default_ai = source.DefaultAI
        self.base_max_hp = source.BaseMaxHP
        self.base_max_mp = source.BaseMaxMP
        self.base_max_stamina = source.BaseMaxStamina
        self.arrow_slot1_count = source.ArrowSlot1Count
        self.bolt_slot1_count = source.BoltSlot1Count
        self.arrow_slot2_count = source.ArrowSlot2Count
        self.bolt_slot2_count = source.BoltSlot2Count
        self.qwc_sb = source.QWC_SB
        self.qwc_mw = source.QWC_MW
        self.qwc_cd = source.QWC_CD
        self.level = source.Level
        self.vitality = source.Vitality
        self.attunement = source.Attunement
        self.endurance = source.Endurance
        self.strength = source.Strength
        self.dexterity = source.Dexterity
        self.intelligence = source.Intelligence
        self.faith = source.Faith
        self.luck = source.Luck
        self.humanity = source.Humanity
        self.resistance = source.Resistance
        self.good_slot1_count = source.GoodSlot1Count
        self.good_slot2_count = source.GoodSlot2Count
        self.good_slot3_count = source.GoodSlot3Count
        self.good_slot4_count = source.GoodSlot4Count
        self.good_slot5_count = source.GoodSlot5Count
        self.good_slot6_count = source.GoodSlot6Count
        self.good_slot7_count = source.GoodSlot7Count
        self.good_slot8_count = source.GoodSlot8Count
        self.good_slot9_count = source.GoodSlot9Count
        self.good_slot10_count = source.GoodSlot10Count
        self.head_scale = source.HeadScale
        self.chest_scale = source.ChestScale
        self.abdomen_scale = source.AbdomenScale
        self.arm_scale = source.ArmScale
        self.leg_scale = source.LegScale
        self.gesture1 = source.Gesture1
        self.gesture2 = source.Gesture2
        self.gesture3 = source.Gesture3
        self.gesture4 = source.Gesture4
        self.gesture5 = source.Gesture5
        self.gesture6 = source.Gesture6
        self.gesture7 = source.Gesture7
        self.character_type = source.CharacterType
        self.draw_type = source.DrawType
        self.gender = source.Gender
        self.covenant = source.Covenant
        self._bit_pad0 = source._BitPad0
        self._pad0 = source._Pad0