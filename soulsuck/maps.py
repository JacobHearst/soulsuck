from os import path
from pathlib import Path
from soulstruct.darksouls1ptde.maps.map_studio_directory import MapStudioDirectory
from soulstruct.darksouls1ptde.maps.msb import MSB

GAME_AREA_NAMES = [
    "Common",
    "Depths",
    "UndeadBurg",
    "FirelinkShrine",
    "PaintedWorld",
    "DarkrootGarden",
    "Oolacile",
    "Catacombs",
    "TombOfTheGiants",
    "AshLake",
    "Blighttown",
    "LostIzalith",
    "SensFortress",
    "AnorLondo",
    "NewLondoRuins",
    "DukesArchives",
    "KilnOfTheFirstFlame",
    "UndeadAsylum",
]

def loadMapStudioDir(dataDir: str) -> MapStudioDirectory:
    mapStudioPath = path.join(dataDir, f"map/MapStudio")
    return MapStudioDirectory(mapStudioPath)

def loadMSB(dataDir: str, id: str) -> MSB:    
    msbPath = path.join(dataDir, f"map/MapStudio/{id}.msb")
    msb = MSB(Path(msbPath))
    print(msb.get_field_names())