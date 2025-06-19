from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import ENV_LIGHT_TEX_BANK


class EnvLightTexBank(Base):
    __tablename__ = "env_light_tex_bank"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    is_use: Mapped[int]
    auto_update: Mapped[int]
    inv_mul_col: Mapped[int]
    res_name_id_dif0: Mapped[int]
    inv_mul_col_dif0: Mapped[int]
    sepc_pow_dif0: Mapped[float]
    res_name_id_spc0: Mapped[int]
    inv_mul_col_spc0: Mapped[int]
    sepc_pow_spc0: Mapped[float]
    res_name_id_spc1: Mapped[int]
    inv_mul_col_spc1: Mapped[int]
    sepc_pow_spc1: Mapped[float]
    res_name_id_spc2: Mapped[int]
    inv_mul_col_spc2: Mapped[int]
    sepc_pow_spc2: Mapped[float]
    res_name_id_spc3: Mapped[int]
    inv_mul_col_spc3: Mapped[int]
    sepc_pow_spc3: Mapped[float]
    deg_rot_x_00: Mapped[int]
    deg_rot_y_00: Mapped[int]
    col_r_00: Mapped[int]
    col_g_00: Mapped[int]
    col_b_00: Mapped[int]
    col_a_00: Mapped[int]
    deg_rot_x_01: Mapped[int]
    deg_rot_y_01: Mapped[int]
    col_r_01: Mapped[int]
    col_g_01: Mapped[int]
    col_b_01: Mapped[int]
    col_a_01: Mapped[int]
    deg_rot_x_02: Mapped[int]
    deg_rot_y_02: Mapped[int]
    col_r_02: Mapped[int]
    col_g_02: Mapped[int]
    col_b_02: Mapped[int]
    col_a_02: Mapped[int]
    deg_rot_x_03: Mapped[int]
    deg_rot_y_03: Mapped[int]
    col_r_03: Mapped[int]
    col_g_03: Mapped[int]
    col_b_03: Mapped[int]
    col_a_03: Mapped[int]
    deg_rot_x_04: Mapped[int]
    deg_rot_y_04: Mapped[int]
    col_r_04: Mapped[int]
    col_g_04: Mapped[int]
    col_b_04: Mapped[int]
    col_a_04: Mapped[int]
    deg_rot_x_05: Mapped[int]
    deg_rot_y_05: Mapped[int]
    col_r_05: Mapped[int]
    col_g_05: Mapped[int]
    col_b_05: Mapped[int]
    col_a_05: Mapped[int]
    deg_rot_x_06: Mapped[int]
    deg_rot_y_06: Mapped[int]
    col_r_06: Mapped[int]
    col_g_06: Mapped[int]
    col_b_06: Mapped[int]
    col_a_06: Mapped[int]
    deg_rot_x_07: Mapped[int]
    deg_rot_y_07: Mapped[int]
    col_r_07: Mapped[int]
    col_g_07: Mapped[int]
    col_b_07: Mapped[int]
    col_a_07: Mapped[int]
    deg_rot_x_08: Mapped[int]
    deg_rot_y_08: Mapped[int]
    col_r_08: Mapped[int]
    col_g_08: Mapped[int]
    col_b_08: Mapped[int]
    col_a_08: Mapped[int]
    deg_rot_x_09: Mapped[int]
    deg_rot_y_09: Mapped[int]
    col_r_09: Mapped[int]
    col_g_09: Mapped[int]
    col_b_09: Mapped[int]
    col_a_09: Mapped[int]
    
    def __init__(self, id: int, env_light_tex_bank: ENV_LIGHT_TEX_BANK):
        self.id = id
        self.is_use = env_light_tex_bank.isUse
        self.auto_update = env_light_tex_bank.autoUpdate
        self.inv_mul_col = env_light_tex_bank.invMulCol
        self.res_name_id_dif0 = env_light_tex_bank.resNameId_Dif0
        self.inv_mul_col_dif0 = env_light_tex_bank.invMulCol_Dif0
        self.sepc_pow_dif0 = env_light_tex_bank.sepcPow_Dif0
        self.res_name_id_spc0 = env_light_tex_bank.resNameId_Spc0
        self.inv_mul_col_spc0 = env_light_tex_bank.invMulCol_Spc0
        self.sepc_pow_spc0 = env_light_tex_bank.sepcPow_Spc0
        self.res_name_id_spc1 = env_light_tex_bank.resNameId_Spc1
        self.inv_mul_col_spc1 = env_light_tex_bank.invMulCol_Spc1
        self.sepc_pow_spc1 = env_light_tex_bank.sepcPow_Spc1
        self.res_name_id_spc2 = env_light_tex_bank.resNameId_Spc2
        self.inv_mul_col_spc2 = env_light_tex_bank.invMulCol_Spc2
        self.sepc_pow_spc2 = env_light_tex_bank.sepcPow_Spc2
        self.res_name_id_spc3 = env_light_tex_bank.resNameId_Spc3
        self.inv_mul_col_spc3 = env_light_tex_bank.invMulCol_Spc3
        self.sepc_pow_spc3 = env_light_tex_bank.sepcPow_Spc3
        self.deg_rot_x_00 = env_light_tex_bank.degRotX_00
        self.deg_rot_y_00 = env_light_tex_bank.degRotY_00
        self.col_r_00 = env_light_tex_bank.colR_00
        self.col_g_00 = env_light_tex_bank.colG_00
        self.col_b_00 = env_light_tex_bank.colB_00
        self.col_a_00 = env_light_tex_bank.colA_00
        self.deg_rot_x_01 = env_light_tex_bank.degRotX_01
        self.deg_rot_y_01 = env_light_tex_bank.degRotY_01
        self.col_r_01 = env_light_tex_bank.colR_01
        self.col_g_01 = env_light_tex_bank.colG_01
        self.col_b_01 = env_light_tex_bank.colB_01
        self.col_a_01 = env_light_tex_bank.colA_01
        self.deg_rot_x_02 = env_light_tex_bank.degRotX_02
        self.deg_rot_y_02 = env_light_tex_bank.degRotY_02
        self.col_r_02 = env_light_tex_bank.colR_02
        self.col_g_02 = env_light_tex_bank.colG_02
        self.col_b_02 = env_light_tex_bank.colB_02
        self.col_a_02 = env_light_tex_bank.colA_02
        self.deg_rot_x_03 = env_light_tex_bank.degRotX_03
        self.deg_rot_y_03 = env_light_tex_bank.degRotY_03
        self.col_r_03 = env_light_tex_bank.colR_03
        self.col_g_03 = env_light_tex_bank.colG_03
        self.col_b_03 = env_light_tex_bank.colB_03
        self.col_a_03 = env_light_tex_bank.colA_03
        self.deg_rot_x_04 = env_light_tex_bank.degRotX_04
        self.deg_rot_y_04 = env_light_tex_bank.degRotY_04
        self.col_r_04 = env_light_tex_bank.colR_04
        self.col_g_04 = env_light_tex_bank.colG_04
        self.col_b_04 = env_light_tex_bank.colB_04
        self.col_a_04 = env_light_tex_bank.colA_04
        self.deg_rot_x_05 = env_light_tex_bank.degRotX_05
        self.deg_rot_y_05 = env_light_tex_bank.degRotY_05
        self.col_r_05 = env_light_tex_bank.colR_05
        self.col_g_05 = env_light_tex_bank.colG_05
        self.col_b_05 = env_light_tex_bank.colB_05
        self.col_a_05 = env_light_tex_bank.colA_05
        self.deg_rot_x_06 = env_light_tex_bank.degRotX_06
        self.deg_rot_y_06 = env_light_tex_bank.degRotY_06
        self.col_r_06 = env_light_tex_bank.colR_06
        self.col_g_06 = env_light_tex_bank.colG_06
        self.col_b_06 = env_light_tex_bank.colB_06
        self.col_a_06 = env_light_tex_bank.colA_06
        self.deg_rot_x_07 = env_light_tex_bank.degRotX_07
        self.deg_rot_y_07 = env_light_tex_bank.degRotY_07
        self.col_r_07 = env_light_tex_bank.colR_07
        self.col_g_07 = env_light_tex_bank.colG_07
        self.col_b_07 = env_light_tex_bank.colB_07
        self.col_a_07 = env_light_tex_bank.colA_07
        self.deg_rot_x_08 = env_light_tex_bank.degRotX_08
        self.deg_rot_y_08 = env_light_tex_bank.degRotY_08
        self.col_r_08 = env_light_tex_bank.colR_08
        self.col_g_08 = env_light_tex_bank.colG_08
        self.col_b_08 = env_light_tex_bank.colB_08
        self.col_a_08 = env_light_tex_bank.colA_08
        self.deg_rot_x_09 = env_light_tex_bank.degRotX_09
        self.deg_rot_y_09 = env_light_tex_bank.degRotY_09
        self.col_r_09 = env_light_tex_bank.colR_09
        self.col_g_09 = env_light_tex_bank.colG_09
        self.col_b_09 = env_light_tex_bank.colB_09
        self.col_a_09 = env_light_tex_bank.colA_09