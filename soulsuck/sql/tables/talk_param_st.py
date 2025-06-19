from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from soulstruct.darksouls1ptde.params.paramdef import TALK_PARAM_ST


class TalkParamST(Base):
    __tablename__ = "talk_param_st"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    subtitle_text: Mapped[int]
    voice_sound: Mapped[int]
    talking_animation: Mapped[int]
    return_conversation: Mapped[int]
    reaction_conversation: Mapped[int]
    event_flag: Mapped[int]
    is_motion_loop: Mapped[int]
    
    def __init__(self, id: int, source: TALK_PARAM_ST):
        self.id = id
        self.subtitle_text = source.SubtitleText
        self.voice_sound = source.VoiceSound
        self.talking_animation = source.TalkingAnimation
        self.return_conversation = source.ReturnConversation
        self.reaction_conversation = source.ReactionConversation
        self.event_flag = source.EventFlag
        self.is_motion_loop = source.IsMotionLoop