import reflex as rx
import functools
import json
import os
import time

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


# Autenticacion con Google

CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")

class Google_auth_state(rx.State):
    id_token_json: str = rx.LocalStorage()

    def on_success(self, id_token: dict):
        self.id_token_json = json.dumps(id_token)

    @rx.cached_var
    def tokeninfo(self) -> dict[str, str]:
        try:
            return verify_oauth2_token(
                json.loads(self.id_token_json)["credential"],
                requests.Request(),
                CLIENT_ID,
            )
        except Exception as exc:
            if self.id_token_json:
                print(f"Error verifying token: {exc}")
        return {}

    def logout(self):
        self.id_token_json = ""

    @rx.var
    def token_is_valid(self) -> bool:
        try:
            return bool(
                self.tokeninfo
                and (int(self.tokeninfo.get("exp", 0))) > time.time()
            )
        except Exception:
            return False

    @rx.cached_var
    def protected_content(self) -> str:
        if self.token_is_valid:
            return f"Este área está restringida para usuarios autenticados. Bienvenido {self.tokeninfo['name']}"
        return "No ha iniciado sesion"

def require_google_login(page) -> rx.Component:
    @functools.wraps(page)
    def _auth_wrapper() -> rx.Component:
        return GoogleOAuthProvider.create(
            rx.cond(
                Google_auth_state.is_hydrated,
                rx.cond(Google_auth_state.token_is_valid, 
                    page(), 
                    login()
                ),
                rx.spinner(),
            ),
            client_id=CLIENT_ID,
        )
    return _auth_wrapper

def show_navbar() -> rx.Component:
    return rx.cond(
            Google_auth_state.token_is_valid,
            navbar(True, Google_auth_state.tokeninfo["name"]),
            navbar(False, "Identificate"),
        ),

def login() -> rx.Component:
    return rx.flex(
        show_navbar(),
        rx.box(
            GoogleLogin.create(on_success=Google_auth_state.on_success),
            rx.button("Inicio", on_click=rx.redirect("/")),
            background="linear-gradient(rgba(0, 0, 0, 0.25), rgba(0, 0, 0, 0.25))",
            background_size="cover",
            background_position="center",
            height="100vh",
            display="flex",
            flex_direction="column",
            justify_content="center",
            align_items="center",
        ),

        width="100%",
        direction="column",
    )

def user_info(tokeninfo: dict) -> rx.Component:
    return rx.hstack(
        rx.heading(tokeninfo["name"], size="3"),
        rx.text(tokeninfo["email"]),
        align_items="flex-start",
    )

@rx.page(route="/login", title="Identificacion")
@require_google_login
def client_area() -> rx.Component:
    return rx.flex(
        show_navbar(),
        rx.box(
            rx.text(Google_auth_state.protected_content),
            rx.button("Inicio", on_click=rx.redirect("/")),
            background="linear-gradient(rgba(0, 0, 0, 0.25), rgba(0, 0, 0, 0.25))",
            background_size="cover",
            background_position="center",
            height="100vh",
            display="flex",
            flex_direction="column",
            justify_content="center",
            align_items="center",
        ),

        width="100%",
        direction="column",
    )


# Pagina principal

@rx.page(route="/", title="Academia de música")
def index() -> rx.page:
    # Welcome Page (Index)
    return rx.flex(
        show_navbar(),
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
app.add_page(client_area)
