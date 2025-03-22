from typing import List

import mesop as me

from frontend.app_classes import Message

@me.stateclass
class State:
    prompt: str
    prompt_value: str
    messages: List[Message]
    prompt_key: int
