import argparse
import json
import os
from soulstruct.config import PTDE_PATH
from soulsuck.maps import loadMSB, loadMapStudioDir
from soulsuck.params import loadGameParams, PARAM_NAMES
from soulsuck.translate import LANGS

def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("--GameParam", help="Param to dump", choices=PARAM_NAMES + ["All"])
    parser.add_argument("--msb", help="Id of the map to dump")
    parser.add_argument("--mapStudio", action="store_true")
    parser.add_argument("--lang", type=str, default="ENGLISH", choices=LANGS)
    parser.add_argument("--outputDir", default="./ptde-params")
    parser.add_argument("--dataDir", help="Path to an unpacked ptde DATA folder", default=PTDE_PATH)
    return parser.parse_args()

def write(dict: dict, path: str):
    jsonStr = json.dumps(dict, indent=4)
    with open(path, "w") as file:
        file.write(jsonStr)

if __name__ == "__main__":
    args = parseArgs()
    os.makedirs(args.outputDir, exist_ok=True)

    if args.GameParam:
        GameParams = loadGameParams(args.dataDir)
        if args.GameParam == "All":
            for name in PARAM_NAMES:
                paramRows = getattr(GameParams, name).to_dict()["rows"]
                write(paramRows, f"{args.outputDir}/{name}.json")
        else:
            write(getattr(GameParams, args.GameParam).to_dict()["rows"], f"{args.outputDir}/{args.GameParam}.json")
            

    if args.msb:
        msb = loadMSB(args.dataDir, args.msb)
        print(msb.get_field_names())

    if args.mapStudio:
        mapStudioDir = loadMapStudioDir(args.dataDir)
        mapStudioDir.write_json_directory(args.outputDir)
        