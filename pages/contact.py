import reflex as rx

import states.google_auth_state
from components.contact_form import contact_form

def contact():
    return rx.box(
        states.google_auth_state.show_navbar(),
        rx.flex(
            rx.heading('¿Tienes alguna pregunta?', as_='h2', margin_bottom='1em'),
            contact_form(),
            margin_top='6em', 
            direction="column",
            align="center",
            justify="center",
        ), 
        width='90vw', 
        height='90vh'
    ),