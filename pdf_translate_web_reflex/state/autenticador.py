"""The authentication state."""
import os
import reflex as rx
from sqlmodel import select
from passlib.context import CryptContext
from dotenv import load_dotenv
from .base import Base, User

load_dotenv('.env')

pwd_context = CryptContext(schemes=[os.getenv('SCHEMES_CRYPT')], deprecated="auto")

class AuthState(Base):
    """The authentication state for sign up and login page."""

    username: str 
    fullname: str
    email: str
    password: str
    confirm_password: str

    @rx.var
    def User_name(self):
        """Get the current user."""
        return self.username

    def signup(self):
        """Sign up a user."""
        with rx.session() as session:
            if self.password != self.confirm_password:
                return rx.window_alert("las contraseñas no coinciden.")
            if session.exec(select(User).where(User.username == self.username)).first():
                return rx.window_alert("El usuario ya pertenece a alguien.")
            if session.exec(select(User).where(User.email == self.email)).first():
                return rx.window_alert("El email ya pertenece a alguien")
            self.user = User(username=self.username, fullname= self.fullname, email=self.email, password=pwd_context.hash(self.password))
            session.add(self.user)
            session.expire_on_commit = False
            session.commit()
            return rx.redirect("/login")
        
    def login(self):
        """Log in a user."""
        with rx.session() as session:
            user = session.exec(
                select(User).where(User.username == self.username)
            ).first()
            if user and pwd_context.verify(self.password, user.password):
                self.user = user
                return rx.redirect("/")
            else:
                return rx.window_alert("Usuario y contraseña incorrecta.")
            
    