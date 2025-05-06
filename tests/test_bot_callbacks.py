import pytest
from fixtures import mock_message, mock_router
from handlers.callbacks import callback_message, callback_message

@pytest.mark.asyncio
async def test_callback_message(mock_message):
    # mock_callback_query.message = mock_message

    # Вызов коллбека
    await callback_message(mock_message)

    called_args, called_kwargs = mock_message.message.answer.call_args

    assert called_args[0] == "продолжаешь жить своей унылой жизнью"

@pytest.mark.asyncio
async def test_callback_message(mock_message):
    # mock_callback_query.message = mock_message

    # Вызов коллбека
    await callback_message(mock_message)

    called_args, called_kwargs = mock_message.message.answer.call_args

    assert called_args[0] == "то же самое, только клубничная"