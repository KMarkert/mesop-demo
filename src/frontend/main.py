import mesop as me

from frontend import handlers
from frontend.state import State
from frontend.app_classes import Message

# Main page definition
@me.page(
    title="Geospatial Reasoning",
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;700",
    ],
    security_policy=me.SecurityPolicy(
        allowed_script_srcs=[
            "https://cdn.jsdelivr.net",  # For Lit
        ],
        dangerously_disable_trusted_types=True,
    ),
    on_load=handlers.on_load,
)
def main():
    state = me.state(State)
    with me.box(
        style=me.Style(
            display="flex",
            flex_direction="column",
            font_family="Google Sans",
            background="#fff" if me.theme_brightness() == "light" else "#121212",
            height="100%",
            width="100%",
            margin=me.Margin.all(10),
            align_items="center",
            flex_grow=1,
        )
    ):

        with me.box(
            style=me.Style(
                width="80%",
                height="100%",
                margin=me.Margin(left="auto", right="auto"),
                overflow_y="scroll",
            )
        ):
            chat_content()

            with me.box(
                style=me.Style(
                    position="sticky",
                    margin=me.Margin(left="auto", right="auto"),
                    bottom=0,
                    width="80%",
                    z_index=1,
                )
            ):
                chat_input()

def chat_content():
    state = me.state(State)
    with me.box(
        key="chat_container",
        style=me.Style(
            flex_grow=1,
            color="#1f1f1f",
            padding=me.Padding(
                top=15,
                bottom=20,
                left=20,
                right=20,
            ),
            line_height="1.5rem",
            overflow_y="auto",
            flex_direction="column-reverse",
        ),
    ):
        for i in range(len(state.messages)):
            with me.box(style=me.Style(margin=me.Margin(top=24))):
                if state.messages[i].role == "model":
                    assistant_content(state.messages[i])

                elif state.messages[i].role == "user":
                    user_content(state.messages[i])
                
def user_content(
    message: Message,
):
    with me.box(
        style=me.Style(
            display="flex",
            align_items="flex-start",
            gap=15,
            justify_content="end",
        )
    ):
        with me.box(
            key=message.id,
            style=me.Style(
                background=me.theme_var("surface-container-low"),
                border_radius=10,
                color=me.theme_var("on-surface-variant"),
                padding=me.Padding.symmetric(vertical=0, horizontal=10),
                max_width="80%",
                font_family="Google Sans",
            ),
        ):
            me.markdown(
                message.content,
                style=me.Style(
                    padding=me.Padding(left=4),
                    color="black" if me.theme_brightness() == "light" else "white",
                ),
            )

def assistant_content(
    message: Message,
    show_loader: bool = False,
):
    state = me.state(State)

    me.box(style=me.Style(height=12))
    with me.box(
        key="gemini-content", style=me.Style(display="flex", align_items="flex-start")
    ):
        me.image(
            src="https://www.gstatic.com/lamda/images/gemini_sparkle_v002_d4735304ff6292a690345.svg",
            style=me.Style(width=28, height=28),
        )
        with me.box(
            key=message.id,
            style=me.Style(width="95%", padding=me.Padding(right=5, left=5)),
        ):
            me.markdown(
                message.content,
                style=me.Style(
                    padding=me.Padding(left=4),
                    color="black" if me.theme_brightness() == "light" else "white",
                ),
            )

def chat_input():
    state = me.state(State)
    surface_container = "#202124" if me.theme_brightness() == "dark" else "#f0f4f9"
    text_color = "white" if me.theme_brightness() == "dark" else "rgba(0,0,0,0.87)"
    with me.box(
        key="chat_input_box",
        style=me.Style(
            display="flex",
            align_items="center",
            background=surface_container,
            margin=me.Margin.all(8),
            border_radius=60,
            padding=me.Padding.all(12),
        ),
    ):
        border_side = me.BorderSide(width=0)
        with me.box(style=me.Style(flex_grow=1)):
            me.native_textarea(
                value=state.prompt_value,
                key=str(state.prompt_key),
                autosize=True,
                max_rows=10,
                on_input=handlers.on_input,
                placeholder="Enter prompt here",
                shortcuts={me.Shortcut(key="enter"): handlers.send_prompt},
                style=me.Style(
                    box_sizing="content-box",
                    border=me.Border(
                        left=border_side,
                        right=border_side,
                        top=border_side,
                        bottom=border_side,
                    ),
                    color=text_color,
                    padding=me.Padding(top=10, bottom=10, right=10, left=10),
                    align_items="center",
                    background=surface_container,
                    width="100%",
                    outline="none",
                    overflow_y="hidden",
                ),
            )

        with me.content_button(
            type="icon",
            on_click=handlers.send_prompt,
            style=me.Style(
                color="black" if me.theme_brightness() == "light" else "white"
            ),
        ):
            me.icon(
                "send",
                style=me.Style(
                    color="black" if me.theme_brightness() == "light" else "white"
                ),
            )