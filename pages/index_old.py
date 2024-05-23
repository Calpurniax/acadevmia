# import reflex as rx
# import states.google_auth_state

# @rx.page(route="/", title="Academia de música")
# def index() -> rx.page:
#     # Welcome Page (Index)
#     return rx.flex(
#         states.google_auth_state.show_navbar(),
#         rx.box(
#             rx.heading(
#                 'Accede a las mejores clases de música desde donde quieras',
#                 color="white",
#                 align="center",
#             ),
#             rx.text(
#                 'A tu ritmo y desde cualquier dispositivo, podrás seguir tus clases online en streaming directo o conectarte en el horario que puedas.',
#                 color="white",
#                 align="center",
#             ),
#             background="linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('/hero.jpg')",
#             background_size="cover",
#             background_position="center",
#             height="100vh",
#             display="flex",
#             flex_direction="column",
#             justify_content="center",
#             align_items="center",
#         ),
#         rx.box(
#             rx.heading(
#                 'Grandes profesionales del mundo de la música',
#                 color="white",
#                 align="center",
#             ),
#             rx.text(
#                 'Conecta con los mejores profesores para formarte en lo que tú elijas',
#                 color="white",
#                 align="center",
#             ),
#             background="linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('/hero.jpg')",
#             background_size="cover",
#             background_position="center",
#             width="100%",
#             height="50vh",
#             display="flex",
#             flex_direction="column",
#             justify_content="center",
#             align_items="center",
#         ),
#         rx.box(
#             rx.heading(
#                 'Ofrecemos distintos planes de estudio',
#                 color="white",
#                 align="center",
#             ),
#             rx.text(
#                 'Elige la forma de pago que más te interese',
#                 color="white",
#                 align="center",
#             ),
#             rx.link(
#                 rx.button('Contacto'), 
#                 href="/contacto",
#                 padding_top=15,
#                 align="center",
#             ),
#             background="linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('/keyboard_guitar.jpg')",
#             background_size="cover",
#             background_position="center",
#             width="100%",
#             height="50vh",
#             display="flex",
#             flex_direction="column",
#             justify_content="center",
#             align_items="center", 
#             ),                
#         width="100%",
#         direction="column",
#     )