import pytest
from unittest.mock import AsyncMock
from aiogram.types import Message
from aiogram import Router

# Фикстуры в pytest позволяют выносить в отдельные функции типовые действия
# например: настройка тестового окружения, создание тестовых данных, выполнение завершающие действия
# https://habr.com/ru/articles/731296/

@pytest.fixture
def mock_message():
    """Mock сообщение"""
    mock_msg = AsyncMock(spec=Message)
    mock_msg.answer = AsyncMock()
    return mock_msg


@pytest.fixture
def mock_router():
    """Mock роутер"""
    router = Router()
    return router
