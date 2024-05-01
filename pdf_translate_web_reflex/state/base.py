from typing import Optional

import reflex as rx
from pdf_translate_web_reflex.models.db import User

class Base(rx.State):
    """The base state for the app."""

    user: Optional[User] = None

    def logout(self):
        """Log out a user."""
        self.reset()
        return rx.redirect("/")

    def check_login(self):
        """Check if a user is logged in."""
        if not self.logged_in:
            return rx.redirect("/login")
        
    @rx.var
    def logged_in(self):
        """Check if a user is logged in."""
        return self.user is not None
    
