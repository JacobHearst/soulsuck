from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session
from soulstruct.base.params.param import Param
from soulstruct.darksouls1ptde.params.gameparambnd import GameParamBND
from soulstruct.darksouls1ptde.params.paramdef import *
from .tables import *
from ..params import PARAM_NAMES

__all__ = [ "create_database", "populate_database" ]

def create_database(connection_url: str, echo: bool=False):
    engine = create_engine(connection_url, echo=echo)
    Base.metadata.create_all(engine)
    return engine

def populate_database(engine: Engine, params: GameParamBND):
    for name in PARAM_NAMES:
        print(f"Populating from {name}")
        param = getattr(params, name)
        if not issubclass(type(param), Param):
            print(f"Not a param: {type(param).__name__}")
            continue

        populate_table(engine, param)


def populate_table(engine: Engine, param: Param):
    row_type = type(list(param.rows.values())[0])
    SQLAlchemyType = sqlalchemy_typemap[row_type]

    if row_type in [ATK_PARAM_ST, BEHAVIOR_PARAM_ST]:
        # TODO: Figure out if this attack or behavior is for pcs or npcs
        print("Need to figure out if this is pc or npc")
        return
    
    if SQLAlchemyType is None:
        print(f"No SQL representation for: {row_type}")
        return
    
    print(f"Populating {SQLAlchemyType.__tablename__} with {type(param).__qualname__}")

    sql_rows = [SQLAlchemyType(id, row) for id, row in param.rows.items()]
    with Session(engine) as session:
        session.add_all(sql_rows)
        session.commit()

sqlalchemy_typemap = {
    SP_EFFECT_VFX_PARAM_ST: SpEffectVfxParamSt,
    TALK_PARAM_ST: TalkParamST,
    THROW_INFO_BANK: ThrowInfoBank,
    TONE_CORRECT_BANK: ToneCorrectBank,
    TONE_MAP_BANK: ToneMapBank,
    AI_STANDARD_INFO_BANK: AIStandardInfoBank,
    BEHAVIOR_PARAM_ST: BehaviorParamST,
    ATK_PARAM_ST: AtkParamST,
    BULLET_PARAM_ST: BulletParamST,
    CACL_CORRECT_GRAPH_ST: CaclCorrectGraphST,
    CHARACTER_INIT_PARAM: CharacterInitParam,
    DOF_BANK: DofBank,
    ENEMY_STANDARD_INFO_BANK: EnemyStandardInfoBank,
    ENV_LIGHT_TEX_BANK: EnvLightTexBank,
    EQUIP_MTRL_SET_PARAM_ST: EquipMtrlSetParamST,
    EQUIP_PARAM_ACCESSORY_ST: EquipParamAccessoryST,
    EQUIP_PARAM_GOODS_ST: EquipParamGoodsST,
    EQUIP_PARAM_PROTECTOR_ST: EquipParamProtectorST,
    EQUIP_PARAM_WEAPON_ST: EquipParamWeaponST,
    FACE_PARAM_ST: FaceParamST,
    FOG_BANK: FogBank,
    GAME_AREA_PARAM_ST: GameAreaParamST,
    HIT_MTRL_PARAM_ST: HitMtrlParamST,
    ITEMLOT_PARAM_ST: ItemlotParamST,
    KNOCKBACK_PARAM_ST: KnockbackParamST,
    LENS_FLARE_BANK: LensFlareBank,
    LENS_FLARE_EX_BANK: LensFlareExBank,
    LIGHT_BANK: LightBank,
    LIGHT_SCATTERING_BANK: LightScatteringBank,
    LOCK_CAM_PARAM_ST: LockCamParamST,
    LOD_BANK: LodBank,
    MAGIC_PARAM_ST: MagicParamST,
    MENU_PARAM_COLOR_TABLE_ST: MenuParamColorTableST,
    MOVE_PARAM_ST: MoveParamST,
    NPC_PARAM_ST: NPCParamST,
    NPC_THINK_PARAM_ST: NpcThinkParamST,
    OBJ_ACT_PARAM_ST: ObjActParamST,
    OBJECT_PARAM_ST: ObjectParamST,
    POINT_LIGHT_BANK: PointLightBank,
    QWC_CHANGE_PARAM_ST: QwcChangeParamST,
    QWC_JUDGE_PARAM_ST: QwcJudgeParamST,
    RAGDOLL_PARAM_ST: RagdollParamST,
    REINFORCE_PARAM_PROTECTOR_ST: ReinforceParamProtectorST,
    REINFORCE_PARAM_WEAPON_ST: ReinforceParamWeaponST,
    SHADOW_BANK: ShadowBank,
    SHOP_LINEUP_PARAM: ShopLineupParam,
    SKELETON_PARAM_ST: SkeletonParamSt,
    SP_EFFECT_PARAM_ST: SPEffectParamST,
}