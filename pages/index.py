import reflex as rx

# from rxconfig import config
import states.google_auth_state
import styles 

def index() -> rx.page:
    # Welcome Page (Index)
    return rx.box(
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
            background="linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('/hero.jpg')",
            background_size="cover",
            background_position="center",
            height="100vh",
            display="flex",
            flex_direction="column",
            justify_content="center",
            align_items="center",
        ),
        rx.section(
             rx.box(
                rx.box(
                    rx.heading('Accede a las mejores clases de música desde donde quieras', as_='h2', font_size='1em'),
                    rx.text('A tu ritmo y desde cualquier dispositivo, podrás seguir tus clases online en streaming directo o conectarte en el horario que puedas.'),  
                 ), 
                rx.flex(
                    rx.image(src='/laptop_headphones.jpg', width='50%', height='auto', alt='Estudiante online utilizando su portátil'),   
                    margin_top='1em',
                    justify='center',
                    align='center',
                ),                  
                margin_left='1em',
                display=["block", "block", "block", "flex", "flex"]
            ),
        ), 
        rx.section(
            rx.box(
                rx.box(
                    rx.heading('Grandes profesionales del mundo de la música', as_='h2', font_size='1em'),
                    rx.text('Conecta con los mejores profesores para formarte en lo que tú elijas'),
                    text_align='left'
                ),
                rx.flex(
                    rx.image(src='/keyboard_guitar.jpg', width='50%', height='auto', alt='Estudiante online utilizando su móvil'),
                    margin_top='1em',
                    justify='center',
                    align='center',
                    
                ),
                margin_left='1em',
                display=["block", "block", "block", "flex", "flex"]
            ),
        ),  
         rx.section(
            rx.flex(
                rx.box(
                    rx.heading('Ofrecemos distintos planes de estudio', as_='h2', font_size='1em'),
                    rx.text('Elige la forma de pago que más te interese'),
                ),                
                rx.link(rx.button('Contacto', background_color=styles.verde_oscuro, height='auto'), href="/contacto"),        
                margin_left='1em',  
                justify='between',
                align='start'              
            ),
            width='90vw',
        ),           
          
    )
    
        
        

    
