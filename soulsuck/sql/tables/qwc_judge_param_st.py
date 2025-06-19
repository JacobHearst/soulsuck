from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import QWC_JUDGE_PARAM_ST


class QwcJudgeParamST(Base):
    __tablename__ = "qwc_judge_param_st"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    pc_judge_under_wb: Mapped[int]
    pc_judge_top_wb: Mapped[int]
    pc_judge_under_lr: Mapped[int]
    pc_judge_top_lr: Mapped[int]
    area_judge_under_wb: Mapped[int]
    area_judge_top_wb: Mapped[int]
    area_judge_under_lr: Mapped[int]
    area_judge_top_lr: Mapped[int]
    
    def __init__(self, id: int, param: QWC_JUDGE_PARAM_ST):
        self.id = id
        self.pc_judge_under_wb = param.PcJudgeUnderWB
        self.pc_judge_top_wb = param.PcJudgeTopWB
        self.pc_judge_under_lr = param.PcJudgeUnderLR
        self.pc_judge_top_lr = param.PcJudgeTopLR
        self.area_judge_under_wb = param.AreaJudgeUnderWB
        self.area_judge_top_wb = param.AreaJudgeTopWB
        self.area_judge_under_lr = param.AreaJudgeUnderLR
        self.area_judge_top_lr = param.AreaJudgeTopLR
