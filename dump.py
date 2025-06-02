import argparse
import json
from os.path import join as joinPaths
import os
from soulsuck.maps import loadMSB, loadMapStudioDir
from soulsuck.params import loadParamRows
import sys

def parseArgs():
    if len(sys.argv) == 1:
        parser.print_help()
        exit(1)

    parser = argparse.ArgumentParser()
    parser.add_argument("--gameParam", type=str, help="GameParamBND property to dump")
    parser.add_argument("--msb", type=str, help="The id of the map to dump")
    parser.add_argument("--mapStudio", action="store_true")
    parser.add_argument("--outputDir", default="./ptde-params")
    parser.add_argument("--dataDir", type=str, help="Path to an unpacked ptde DATA folder", default="C:/Program Files (x86)/Steam/steamapps/common/Dark Souls Prepare to Die Edition/DATA")
    return parser.parse_args()

def write(dict: dict, path: str):
    jsonStr = json.dumps(dict, indent=4)
    with open(path, "w") as file:
        file.write(jsonStr)

if __name__ == "__main__":
    args = parseArgs()
    os.makedirs(args.outputDir, exist_ok=True)

    if args.gameParam:
        paramRows = loadParamRows(args.dataDir, args.gameParam)
        write(paramRows, f"{args.outputDir}/{args.gameParam}.json")

    if args.msb:
        msb = loadMSB(args.dataDir, args.msb)
        print(msb.get_field_names())

    if args.mapStudio:
        mapStudioDir = loadMapStudioDir(args.dataDir)
        mapStudioDir.write_json_directory(args.outputDir)
        