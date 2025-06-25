from aiogram import types, Router, F
from aiogram.filters import Command
from sqlalchemy import select, insert
from db import async_session, User
from .keyboard import keyboard_start, keyboard
from utils.parser import parse_codewars_profile
import logging, re

router = Router()

status_string = "UserId: {}\nUserName: {}"
codewars_pattern = re.compile(r'^https?://(www\.)?codewars\.com/users/[^\s]+/?$')


@router.message(Command("start"))
async def start_handler(message: types.Message):
    async with async_session() as session:
        user = (await session.execute(select(User).where(User.user_id == message.from_user.id))).scalar()
        msg = "Чтобы продолжить, вызовите команду /status" if user else "Выберите роль"
        await message.answer(msg, reply_markup=None if user else keyboard_start)
    logging.info(f"user {message.from_user.id} started the bot")


@router.message(Command("status"))
async def status_handler(message: types.Message):
    async with async_session() as session:
        user = (await session.execute(select(User).where(User.user_id == message.from_user.id))).scalar()
        if not user:
            return await message.answer("Пользователь не найден.")
        if user.tutorcode:
            text = f"{status_string}\nКод преподавателя: {user.tutorcode}"
        elif user.subscribe:
            tutor = (await session.execute(select(User).where(User.tutorcode == str(user.subscribe)))).scalar()
            tutor_name = tutor.username if tutor else "не найден"
            text = f"{status_string}\nПреподаватель: {tutor_name}"
        else:
            text = status_string
        await message.answer(text.format(user.user_id, user.username))
    logging.info(f"user {message.from_user.id} checked status")


@router.message(F.text.startswith("tutorcode-"))
async def add_student_handler(message: types.Message):
    code = message.text.split("-", 1)[1]
    async with async_session() as session:
        try:
            await session.execute(insert(User).values(
                user_id=message.from_user.id,
                username=message.from_user.username,
                subscribe=code
            ))
            await session.commit()
            await message.answer("Пользователь добавлен как студент!")
        except Exception as e:
            await message.answer("Ошибка добавления. Возможно, вы уже зарегистрированы.")
            logging.warning(f"Ошибка добавления {message.from_user.id}: {e}")


@router.message(Command("load"))
async def load_profiles_handler(message: types.Message):
    parts = message.text.split(" ", 1)
    if len(parts) < 2:
        return await message.answer("После /load отправьте ссылки через запятую.")

    links = [l.strip() for l in parts[1].split(",") if codewars_pattern.match(l.strip())]
    if not links:
        logging.info(f"Invalid links from {message.from_user.id}")
        return await message.answer("Ссылки должны быть в формате https://www.codewars.com/users/...")

    results = []
    for link in links:
        tasks = parse_codewars_profile(link)
        results.append(f"Задачи для {link}:\n" + "\n".join(tasks) if tasks else f"Не удалось получить задачи: {link}")
    await message.answer("\n\n".join(results))
    logging.info(f"user {message.from_user.id} загрузил ссылки: {links}")


@router.message(Command("getres"))
async def get_results_handler(message: types.Message):
    async with async_session() as session:
        tutor = (await session.execute(select(User).where(User.user_id == message.from_user.id))).scalar()
        if not tutor or not tutor.tutorcode:
            return await message.answer("Вы не являетесь преподавателем.")

        students = (await session.execute(select(User).where(User.subscribe == str(tutor.tutorcode)))).scalars().all()

    if not students:
        return await message.answer("У вас пока нет студентов.")

    tasks = set()
    for s in students:
        if not s.username:
            continue
        profile_url = f"https://www.codewars.com/users/{s.username.replace(' ', '%20')}"
        tasks.update(parse_codewars_profile(profile_url))

    msg = "Пройденные задачи:\n\n" + "\n".join(sorted(tasks)) if tasks else "Не удалось получить задачи студентов."
    await message.answer(msg)


@router.message(Command("checked"))
async def notify_students_handler(message: types.Message):
    async with async_session() as session:
        tutor = (await session.execute(select(User).where(User.user_id == message.from_user.id))).scalar()
        if not tutor or not tutor.tutorcode:
            return await message.answer("Вы не являетесь преподавателем.")

        students = (await session.execute(select(User).where(User.subscribe == str(tutor.tutorcode)))).scalars().all()

    if not students:
        return await message.answer("У вас пока нет студентов.")

    count = 0
    for s in students:
        try:
            await message.bot.send_message(s.user_id, "Ваши задачи проверены преподавателем.")
            count += 1
        except Exception as e:
            logging.warning(f"Не удалось отправить студенту {s.user_id}: {e}")

    await message.answer(f"Отправлено уведомлений: {count}")


@router.message(Command("help"))
async def help_handler(message: types.Message):
    await message.answer(
        "📘 Команды:\n"
        "/start — запустить бота\n"
        "/status — ваш статус\n"
        "/load — загрузить ссылки Codewars\n"
        "/getres — собрать задачи студентов\n"
        "/checked — уведомить студентов\n"
        "/menu — открыть меню\n"
        "/help — помощь"
    )


@router.message(Command("menu"))
async def menu_handler(message: types.Message):
    await message.answer("Выберите пункт меню:", reply_markup=keyboard())


@router.message()
async def echo_handler(message: types.Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")
