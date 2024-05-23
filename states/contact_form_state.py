import reflex as rx

class contactFormState(rx.State):
    contact_data: dict = {}

    def handle_submit(self, contact_data: dict):
        """Handle the form submit."""
        self.contact_data = contact_data