import pytest
from fixtures import mock_message, mock_router
from handlers.handlers import process_help_command, process_start_command
from aiogram.types import InlineKeyboardMarkup
from unittest.mock import AsyncMock


@pytest.mark.asyncio
async def test_process_help_command(mock_router, mock_message):
    # Вызываем хендлер
    await process_help_command(mock_message)

    # Проверяем, что ответ был отправлен
    assert mock_message.answer.called, "message.answer не был вызван"

    # Получаем аргументы вызова
    called_args, called_kwargs = mock_message.answer.call_args

    # Проверяем текст сообщения (исправлено на актуальный)
    assert called_args[0] == "Помощь пришла!"

    # Проверяем наличие Inline-клавиатуры
    markup = called_kwargs["reply_markup"]
    assert isinstance(markup, InlineKeyboardMarkup), "reply_markup не является Inline-клавиатурой"


@pytest.mark.asyncio
async def test_command_start_handler(mock_router, mock_message):
    # Настраиваем mock-пользователя
    mock_message.from_user.id = 12345
    mock_message.from_user.username = "test_user"
    mock_message.reply = AsyncMock()

    # Вызываем обработчик
    await process_start_command(mock_message)

    # Проверяем вызов reply
    mock_message.reply.assert_called_once()

    # Проверяем содержимое ответа
    response_text = mock_message.reply.call_args[0][0]
    assert str(mock_message.from_user.id) in response_text
    assert mock_message.from_user.username in response_text