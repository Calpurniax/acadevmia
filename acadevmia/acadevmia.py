import reflex as rx
from pages.index import index
from pages.contact import contact


app = rx.App(
    theme = rx.theme(
        appearance="light",
        radius="large",        
    )
)
app.add_page(index, route="/")
app.add_page(contact, route="/contacto")
