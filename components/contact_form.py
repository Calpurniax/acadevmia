import reflex as rx

from states.contact_form_state import contactFormState
import styles 

def contact_form():
    rx.console.log('hola desde el formulario de contacto')
    return rx.form(        
        rx.flex(
            rx.input(
                placeholder="Nombre",
                name="contact_name",
                 color_scheme='amber',   
                ),
            rx.input(
                placeholder="Email",
                name="contact_email",
                 color_scheme='amber',   
                ),
            rx.input(
                placeholder="Asunto",
                name="contact_theme",
                 color_scheme='amber',   
                ),   
            rx.text_area(
                placeholder="Mensaje",
                name="contact_msg",                
                color_scheme='amber',   
                required=True,               
                ),              
            rx.button("Enviar", type="submit", margin_top='1em', background_color=styles.verde_oscuro, border='solid 1px white'),            
            direction="column",
            align="center",
            gap='1em',  
            width='100%',
        ),
        on_submit=contactFormState.handle_submit,
        reset_on_submit=True,     
    )

    