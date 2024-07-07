from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from database import add_student

router = Router()


class StudentForm(StatesGroup):
    name = State()
    age = State()
    grade = State()


@router.message(CommandStart())
async def start_command(message: Message, state: FSMContext):
    await message.answer("Привет! Я бот для регистрации студентов. Введите ваше имя:")
    await state.set_state(StudentForm.name)


@router.message(Command(commands=["help"]))
async def help_command(message: Message):
    help_text = (
        "Этот бот умеет выполнять следующие команды:\n"
        "/start - Запустить бота\n"
        "/help - Получить помощь по командам бота\n"
    )
    await message.answer(help_text)


@router.message(StudentForm.name)
async def process_name(message: Message, state: FSMContext):
    if len(message.text.strip()) == 0:
        await message.answer("Имя не может быть пустым. Пожалуйста, введите ваше имя:")
        return
    await state.update_data(name=message.text.strip())
    await message.answer("Введите ваш возраст:")
    await state.set_state(StudentForm.age)


@router.message(StudentForm.age)
async def process_age(message: Message, state: FSMContext):
    if not message.text.isdigit() or not (5 <= int(message.text)):
        await message.answer("Возраст должен быть числом не меньше 5. Пожалуйста, введите ваш возраст:")
        return
    await state.update_data(age=int(message.text))
    await message.answer("Введите ваш класс:")
    await state.set_state(StudentForm.grade)


@router.message(StudentForm.grade)
async def process_grade(message: Message, state: FSMContext):
    if len(message.text.strip()) == 0:
        await message.answer("Класс не может быть пустым. Пожалуйста, введите ваш класс:")
        return
    user_data = await state.get_data()
    name = user_data['name']
    age = user_data['age']
    grade = message.text.strip()

    try:
        add_student(name, age, grade)
        await message.answer(f"Спасибо! Данные сохранены.\nИмя: {name}\nВозраст: {age}\nКласс: {grade}")
    except Exception as e:
        await message.answer(f"Произошла ошибка при сохранении данных: {e}")
    await state.clear()


def register_handlers(dp):
    dp.include_router(router)
