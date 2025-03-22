from typing import Optional, Union

import mesop as me

from frontend.app_classes import Message
from frontend.state import State
from reverse_o_matic.reverse_o_matic import reverse_everything

# Mesop Settings
def on_load(e: me.LoadEvent):
    me.set_theme_mode("light")

# Chat handler
def on_input(e: me.InputEvent):
    state = me.state(State)
    state.prompt = e.value

# Send prompt function, update upload and response based on which API is used
def send_prompt(e: Optional[Union[me.ClickEvent, me.TextareaShortcutEvent]] = None):
    state = me.state(State)

    input = state.prompt
    state.prompt = ""
    yield

    state.prompt_value=""
    yield

    output = state.messages
    if output is None:
        output = []

    output.append(Message(role="user", content=input))

    assistant_message = Message(role="model", content="")
    output.append(assistant_message)
    state.messages = output
    assistant_message.content += reverse_everything(input)
    yield