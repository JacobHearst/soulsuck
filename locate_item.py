from soulstruct.config import PTDE_PATH
from soulstruct.darksouls1ptde.maps.events import MSBTreasureEvent
from soulstruct.darksouls1ptde.maps.msb import MSB
from soulsuck.maps import loadMapStudioDir, GAME_AREA_NAMES
from soulsuck.params import loadGameParams, loadParamRows
import sys

if len(sys.argv) != 2:
    print("Invalid number of args")
    exit(1)

# The id of the item in EquipParamGoods
goodID = sys.argv[1]
mapStudioDir = loadMapStudioDir(PTDE_PATH)
gameParams = loadGameParams(PTDE_PATH)


def objectsWithItemLot(itemLotID: str):
    treasures = treasuresWithItemLot(itemLotID)
    for treasure in treasures:
        pass


def treasuresWithItemLot(itemLotID: str) -> list[MSBTreasureEvent]:
    result = []
    for areaName in GAME_AREA_NAMES:
        area: MSB = getattr(mapStudioDir, areaName)
        for treasure in area.treasures:
            if itemLotID in [treasure.item_lot_1, treasure.item_lot_2, treasure.item_lot_3, treasure.item_lot_4, treasure.item_lot_5]:
                result.append(treasure)

    return result

def findItemLots(itemID: int):
    result = {}
    for lotID, lot in gameParams.ItemLots.items():
        if itemID in [lot.Item1ID, lot.Item2ID, lot.Item3ID, lot.Item4ID, lot.Item5ID, lot.Item6ID, lot.Item7ID, lot.Item8ID]:
            result[lotID] = lot

    return result

lots = findItemLots(int(goodID))
print(f"Found {len(lots)} item lots containing the good")

treasureCount = 0
for lotID, lot in lots.items():
    treasures = treasuresWithItemLot(808)
    treasureCount += len(treasures)

print(f"Found {treasureCount} treasures containing those item lots")