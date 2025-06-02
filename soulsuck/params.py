from os.path import join as joinPaths
from soulstruct.base.params.param import Param
from soulstruct.darksouls1ptde.params.gameparambnd import GameParamBND
from pathlib import Path

def loadGameParams(dataDir: str) -> GameParamBND:
    gameParamBNDPath = joinPaths(dataDir, "param/GameParam/GameParam.parambnd")
    return GameParamBND(Path(gameParamBNDPath))

def loadParamRows(dataDir: str, name: str) -> dict:
    param: Param = getattr(loadGameParams(dataDir), name)
    return param.to_dict()["rows"]