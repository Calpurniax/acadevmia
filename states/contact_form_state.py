import reflex as rx

from db.firebase import add_comment

class contactFormState(rx.State):
    contact_data: dict = {}

    def handle_submit(self, contact_data: dict):
        """Handle the form submit."""
        self.contact_data = contact_data
        add_comment(contact_data)