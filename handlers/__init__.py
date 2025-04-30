from .handlers import router  # Импортируем router вместо register_message_handlers
from .commands import set_my_commands

__all__ = ['router', 'set_my_commands']  # Обновляем список экспортируемых объектов