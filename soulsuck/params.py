from os.path import join as joinPaths
from soulstruct.base.params.param import Param
from soulstruct.darksouls1ptde.params.gameparambnd import GameParamBND
from pathlib import Path

def loadGameParams(dataDir: str) -> GameParamBND:
    gameParamBNDPath = joinPaths(dataDir, "param/GameParam/GameParam.parambnd")
    return GameParamBND(Path(gameParamBNDPath))

def loadParamRows(dataDir: str, name: str) -> dict:
    params = loadGameParams(dataDir)
    members = dir(params)
    if name not in members:
        print(f"Unknown param name: {name}")
        print(f"Found members: {members}")
        exit(1)

    param: Param = getattr(params, name)
    return param.to_dict()["rows"]