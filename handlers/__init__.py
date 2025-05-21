# handlers/__init__.py

from .menu_handler import register_handlers as register_menu_handlers

def init_handlers(bot):
    register_menu_handlers(bot)