import reflex as rx
from pages import index

app = rx.App(
    theme = rx.theme(
        appearance="light",
        radius="large",
        accent_color="cyan",
    )
)
app.add_page(index)
