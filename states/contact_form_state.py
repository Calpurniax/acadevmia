import reflex as rx

from db.firebase import add_comment

class contactFormState(rx.State):
    status_response: bool = False,
    contact_data: dict = {}

    def handle_submit(self, contact_data: dict):
        """Handle the form submit."""
        self.contact_data = contact_data
        response = add_comment(contact_data)
        if response == True:
           self.status_response = True
        else:
            self.status_response = False
        
   
   
    #def handle_response(self, response):        
        

