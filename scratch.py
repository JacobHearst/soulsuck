from sqlalchemy import select
from soulstruct.config import PTDE_PATH
from soulstruct.darksouls1ptde.text.msg_directory import MSGDirectory
from soulsuck.sql.tables import EquipParamProtectorST, AtkParamST
from soulsuck.translate import englishWeaponName
from soulsuck.params import loadGameParams
from soulsuck.sql.database import create_database, populate_database, populate_table
from sqlalchemy.orm import Session

gameParams = loadGameParams(PTDE_PATH)

# Convert dict_keys to list first to make it subscriptable
# firstWeap = list(gameParams.Weapons.keys())[100]
# print(englishWeaponName(firstWeap))

# For next time, connect to postgres, have Claude convert more models
engine = create_database("sqlite+pysqlite:///:memory:")
populate_database(engine, gameParams)

with Session(engine) as session:
    print(session.query(EquipParamProtectorST).count())

print(len(gameParams.Armor.rows))