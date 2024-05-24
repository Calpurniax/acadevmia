import reflex as rx
import styles 

import states.google_auth_state

def navbar(user_logged: bool, text: str) -> rx.Component:
    return rx.flex(
        rx.hstack(
            rx.link(rx.heading("Academia de música online", as_="h1", font_size="1.5em", color='black'), href='/'
            ),
        ),
        rx.spacer(),
        rx.hstack(           
            rx.cond(
                user_logged,
                rx.menu.root(
                    rx.menu.trigger(
                        rx.button(text, background_color=styles.verde_oscuro),
                    ),
                    rx.menu.content(
                        rx.menu.item("Acceder al área privada", on_click=rx.redirect("/private-area")),
                        rx.menu.item("Cerrar sesion", on_click=states.google_auth_state.Google_auth_state.logout),
                    ),
                ),
                rx.button(text, background_color=styles.verde_oscuro, on_click=rx.redirect("/private-area")),
            ),
            
        ),
        position="fixed",
        top="0px",
        background_color=styles.naranja_oscuro,
        padding="1em",
        height="5em",
        width="100%",
        z_index="5",
        align="center"
    )