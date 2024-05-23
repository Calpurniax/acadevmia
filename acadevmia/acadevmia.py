import reflex as rx
import functools
import json
import os
import time

import states.google_auth_state

from rxconfig import config
from components.navbar import navbar
from components.react_oauth_google import GoogleOAuthProvider, GoogleLogin
from dotenv import load_dotenv

from google.auth.transport import requests
from google.oauth2.id_token import verify_oauth2_token

class State(rx.State):
    """The app state."""

    ...

load_dotenv()

# Pagina principal

@rx.page(route="/", title="Academia de música")
def index() -> rx.page:
    # Welcome Page (Index)
    return rx.flex(
        states.google_auth_state.show_navbar(),
        rx.box(
            rx.heading(
                'Accede a las mejores clases de música desde donde quieras',
                color="white",
                align="center",
            ),
            rx.text(
                'A tu ritmo y desde cualquier dispositivo, podrás seguir tus clases online en streaming directo o conectarte en el horario que puedas.',
                color="white",
                align="center",
            ),
            background="linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('/laptop_headphones.jpg')",
            background_size="cover",
            background_position="center",
            height="100vh",
            display="flex",
            flex_direction="column",
            justify_content="center",
            align_items="center",
        ),
        rx.box(
            rx.heading(
                'Grandes profesionales del mundo de la música',
                color="white",
                align="center",
            ),
            rx.text(
                'Conecta con los mejores profesores para formarte en lo que tú elijas',
                color="white",
                align="center",
            ),
            background="linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('/hero.jpg')",
            background_size="cover",
            background_position="center",
            width="100%",
            height="50vh",
            display="flex",
            flex_direction="column",
            justify_content="center",
            align_items="center",
        ),
        rx.box(
            rx.heading(
                'Ofrecemos distintos planes de estudio',
                color="white",
                align="center",
            ),
            rx.text(
                'Elige la forma de pago que más te interese',
                color="white",
                align="center",
            ),
            rx.link(
                rx.button('Contacto'), 
                href="/contacto",
                padding_top=15,
                align="center",
            ),
            background="linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('/keyboard_guitar.jpg')",
            background_size="cover",
            background_position="center",
            width="100%",
            height="50vh",
            display="flex",
            flex_direction="column",
            justify_content="center",
            align_items="center", 
            ),                
        width="100%",
        direction="column",
    )

app = rx.App(
    theme = rx.theme(
        appearance="light",
        radius="large",
        accent_color="cyan",
    )
)
app.add_page(index)
