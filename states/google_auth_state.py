import reflex as rx
import functools
import json
import os
import time

from components.react_oauth_google import GoogleOAuthProvider, GoogleLogin
from components.navbar import navbar
from dotenv import load_dotenv
from google.auth.transport import requests
from google.oauth2.id_token import verify_oauth2_token


load_dotenv()

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