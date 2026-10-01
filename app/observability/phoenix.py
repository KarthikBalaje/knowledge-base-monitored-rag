import phoenix as px
from app.config import settings

def launch_phoenix():
    return px.launch_app(host=settings.phoenix_host, port=settings.phoenix_port)
