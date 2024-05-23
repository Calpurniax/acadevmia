import reflex as rx
import states.google_auth_state

def navbar(user_logged: bool, text: str) -> rx.Component:
    return rx.flex(
        rx.hstack(
            rx.heading("Academia de música"),
            color="white",
        ),
        rx.spacer(),
        rx.hstack(
            rx.color_mode.button(color="white"),
            rx.cond(
                user_logged,
                rx.menu.root(
                    rx.menu.trigger(
                        rx.button(text),
                    ),
                    rx.menu.content(
                        rx.menu.item("Cerrar sesion"),
                        on_click=states.google_auth_state.Google_auth_state.logout,
                    ),
                ),
                rx.button(text, on_click=rx.redirect("/login")),
            ),
            
        ),
        position="fixed",
        top="0px",
        background_color="rgba(0, 0, 0, 0.5)",
        padding="1em",
        height="4em",
        width="100%",
        z_index="5",
    )