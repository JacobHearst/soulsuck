from os.path import join as joinPaths
from soulstruct.base.params.param import Param
from soulstruct.darksouls1ptde.params.gameparambnd import GameParamBND
from pathlib import Path

PARAM_NAMES = [
    "Armor",
    "ArmorUpgrades",
    "Bosses",
    "Bullets",
    "Cameras",
    "Characters",
    "DefaultAIStandardInfo",
    "DefaultEnemyBehaviors",
    "Dialogue",
    "FaceGenerators",
    "Goods",
    "GrowthCurves",
    "ItemLots",
    "Knockbacks",
    "MenuColors",
    "Movement",
    "NonPlayerAttacks",
    "NonPlayerBehaviors",
    "ObjectActivations",
    "Objects",
    "PlayerAttacks",
    "PlayerBehaviors",
    "Players",
    "Ragdolls",
    "Rings",
    "Shops",
    "Skeletons",
    "SpecialEffectVisuals",
    "SpecialEffects",
    "Spells",
    "Terrains",
    "Throws",
    "UpgradeMaterials",
    "WeaponUpgrades",
    "Weapons",
]

def loadGameParams(dataDir: str) -> GameParamBND:
    gameParamBNDPath = joinPaths(dataDir, "param/GameParam/GameParam.parambnd")
    return GameParamBND(Path(gameParamBNDPath))


def loadParamRows(dataDir: str, name: str) -> dict:
    param: Param = getattr(loadGameParams(dataDir), name)
    return param.to_dict()["rows"]