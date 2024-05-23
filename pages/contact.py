import reflex as rx

from components.navbar import navbar
from components.contact_form import contact_form

def contact():
    return rx.box(
        navbar(),
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