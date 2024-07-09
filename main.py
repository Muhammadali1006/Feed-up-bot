import asyncio
from aiogram import Dispatcher, Bot, filters, types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

bot = Bot(token="7331395047:AAFAtgw3_P_pxdfr7NfWcyyd2EhYgLphBMw")
dp = Dispatcher(bot=bot)


class Registration(StatesGroup):
    first_name = State()
    last_name = State()
    number = State()


class Card(StatesGroup):
    card_number = State()
    card_number_2 = State()


class Card_1(StatesGroup):
    card_number = State()
    card_number_2 = State()


contact_button = types.ReplyKeyboardMarkup(keyboard=[
    [types.KeyboardButton(text="Kontakt jo'natish", request_contact=True)]
], resize_keyboard=True)

til = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Uzb 🇺🇿")],
    [KeyboardButton(text="Rus 🇷🇺")]
], resize_keyboard=True)

til_1 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="O'zbek tili 🇺🇿")],
    [KeyboardButton(text="Русский язык 🇷🇺")]
], resize_keyboard=True)

kb = [
    [KeyboardButton(text="🌭 Hot dog"), KeyboardButton(text="🌯 Lavash menu")],
    [KeyboardButton(text="🍔 Burger menu"), KeyboardButton(text="🍹 Ichimliklar")],
    [KeyboardButton(text="🍟 Qo'shimcha"), KeyboardButton(text="🎂 Shirinliklar"), KeyboardButton(text="🔙 Orqaga")]
]
mb = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

kb_1 = [
    [KeyboardButton(text="🔍 Menu"), KeyboardButton(text="🛒 Savat"), KeyboardButton(text="Ma'lumot")],
    [KeyboardButton(text="📲 My info"), KeyboardButton(text="Yordam"), KeyboardButton(text="Tilni o'zgartirish")]
]
mb_1 = ReplyKeyboardMarkup(keyboard=kb_1, resize_keyboard=True)

savat_button = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Sotib olish"), KeyboardButton(text="🚮 Savatni tozalash")],
    [KeyboardButton(text="🗑 Savatni ko'rish"), KeyboardButton(text="🔙 Orqaga")]
], resize_keyboard=True)

mb_hd = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🌭 Classic Hot dog", callback_data="Classic_Hot_dog"),
     InlineKeyboardButton(text="🌭 Combo Hot dog", callback_data="Combo_Hot_dog")],
    [InlineKeyboardButton(text="🌭 Sirli Hot dog", callback_data="Sirli_Hot_dog"),
     InlineKeyboardButton(text="🌭 Double Hot dog", callback_data="Double_Hot_dog")],
])

mb_burger = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🍔 Mini burger", callback_data="Mini_burger"),
     InlineKeyboardButton(text="🍔 Gamburger", callback_data="Gamburger")],
    [InlineKeyboardButton(text="🍔 Cheese burger", callback_data="Cheese_burger"),
     InlineKeyboardButton(text="🍔 Chicken burger", callback_data="Chicken_burger")],
    [InlineKeyboardButton(text="🍔 Combo burger", callback_data="Combo_burger")],
])

mb_lavash = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🌯 Lavash", callback_data="Lavash"),
     InlineKeyboardButton(text="🌯 Combo Tandir Lavash", callback_data="Combo_Tandir_Lavash")],
    [InlineKeyboardButton(text="🌯 Tandir Lavash", callback_data="Tandir_Lavash"),
     InlineKeyboardButton(text="🌯 Combo Lavash", callback_data="Combo_Lavash")],
])

mb_i = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🥤 Love is", callback_data="Love_is"),
     InlineKeyboardButton(text="🥤 Tropic", callback_data="Tropic")],
    [InlineKeyboardButton(text="🥤 Pulpy", callback_data="Pulpy"),
     InlineKeyboardButton(text="🍹 Moxito", callback_data="Moxito")],
])

mb_q = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🍟 Free", callback_data="Free"),
     InlineKeyboardButton(text="🍖 KFC", callback_data="KFC")],
    [InlineKeyboardButton(text="🥫 Ketchup", callback_data="Ketchup"),
     InlineKeyboardButton(text="🥫 Mayanez", callback_data="Mayanez")],
])

mb_sh = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🍹 Kokteyl", callback_data="Kokteyl"),
     InlineKeyboardButton(text="🍰 Tort", callback_data="Tort")],
    [InlineKeyboardButton(text="🍩 Bulochka", callback_data="Bulochka"),
     InlineKeyboardButton(text="🍦 Muzqaymoq", callback_data="Muzqaymoq")],
])

pay_1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_2")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_3")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_4 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_4")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_5 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_5")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_6 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_6")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_7 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_7")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_8 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_8")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_9 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_9")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_10 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_10")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_11 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_11")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_12 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_12")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_13 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_13")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_14 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_14")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_15 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_15")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_16 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_16")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_17 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_17")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_18 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_18")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_19 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_19")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_20 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_20")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_21 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_21")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_22 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_22")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_23 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_23")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_24 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_24")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

pay_25 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Buyurtmani olish", callback_data="random_25")],
    [InlineKeyboardButton(text="❌ Buyurtmani qaytarish", callback_data="random_uz")],
])

cart = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="💳 Uzcard", callback_data="Uzcard")],
    [InlineKeyboardButton(text="💳 Humo", callback_data="Humo")],
])

balance = 50000
orders = []


@dp.message(filters.Command("start"))
async def start_function(message: types.Message):
    await message.answer(f"\n \n Salom {message.from_user.full_name}, botga xush kelibsiz !!!", reply_markup=til)


@dp.callback_query(F.data == "Menu")
async def start_function(call: types.CallbackQuery):
    await call.answer_photo(
        photo="https://avatars.mds.yandex.net/get-altay/9728306/2a0000018a6fc3054db52240e707fb55e28f/L_height",
        caption="\n \n Salom feed up menu bilan tanishing. \n 1 Hot_dog \n 2 Gamburger \n 3 Lavash_menu \n 4 Ichimliklar \n 5 Qo'shimcha \n 6 Shirinliklar \n \n \n",
        reply_markup=mb)


@dp.message(F.text == "🔍 Menu")
async def start_function(message: types.Message):
    await message.answer_photo(
        photo="https://avatars.mds.yandex.net/get-altay/9728306/2a0000018a6fc3054db52240e707fb55e28f/L_height",
        caption="\n \n Salom feed up menu bilan tanishing. \n 1 Hot_dog \n 2 Gamburger \n 3 Lavash_menu \n 4 Ichimliklar \n 5 Qo'shimcha \n 6 Shirinliklar \n \n \n",
        reply_markup=mb)


@dp.message(F.text == "🔙 Orqaga")
async def ortga_function(message: types.Message):
    await message.answer("Siz ortga qaytdiz", reply_markup=mb_1)


@dp.message(F.text == "📲 My info")
async def info_function(message: types.Message):
    await message.answer(
        f"\n \n Sizning ismingiz {message.from_user.full_name} \n Sizning user name {message.from_user.username} \n Sizning id ingiz {message.from_user.id} \n \n",
        reply_markup=mb_1)


@dp.message(F.text == "Uzb 🇺🇿")
async def start(message: types.Message, state: FSMContext):
    await state.set_state(Registration.first_name)
    await message.answer("Xush kelibsiz\nIsmingizni kiriting: ")


@dp.message(Registration.first_name)
async def first_name_function(message: types.Message, state: FSMContext):
    await state.update_data(first_name=message.text)
    await state.set_state(Registration.last_name)
    await message.answer("Yaxshi endi familya kiriting: ")


@dp.message(Registration.last_name)
async def last_name_function(message: types.Message, state: FSMContext):
    await state.update_data(last_name=message.text)
    await state.set_state(Registration.number)
    await message.answer("Yaxshi endi number kiriting: ", reply_markup=contact_button)


@dp.message(Registration.number)
async def phone_function(message: types.Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(
        f"Gap yo'q!\nSizning ismingiz: {data['first_name']}\nSizning familyangiz: {data['last_name']}\nSizning nomeringiz: {data['number']}",
        reply_markup=mb_1)
    await state.clear()


@dp.message(F.text == "🌭 Hot dog")
async def echo_function(message: types.Message):
    await message.answer(text="Tanlang", reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(
        photo="https://sun9-16.userapi.com/impf/c852024/v852024787/1b00ec/nh17wVjmwIw.jpg?size=640x333&quality=96&sign=ac5dcb5df8feb82b1ccbf2f81e56adec&c_uniq_tag=AoaV9UZx--Xsue7NGHnjIh8QJc7P0U9saxrGdxWqU5A&type=album",
        caption=f"\n \n Salom {message.from_user.full_name} siz Hot doglar bo'limini tanladingiz.", reply_markup=mb_hd)


@dp.callback_query(F.data == "Classic_Hot_dog")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://avatars.mds.yandex.net/get-eda/3490335/46368596e993177dbd46616cefc0f3d1/M_height",
        caption="\n \n Classic Hot dog 14 000 so'm \n \n To'lov turini tanlang Uzcard yoki Humo orqali to'lash",
        reply_markup=pay_1)


@dp.callback_query(F.data == "random")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Classic_Hot_dog narxi: 14000")
    global balance
    balance = balance - 14000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.callback_query(F.data == "Sirli_Hot_dog")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://avatars.mds.yandex.net/get-eda/3506707/10f01c187799f1ea0345822dbe475f59/M_height",
        caption="\n \n Sirli Hot dog 16 000 so'm \n \n To'lov turini tanlang Uzcard yoki Humo orqali to'lash",
        reply_markup=pay_2)


@dp.callback_query(F.data == "random_2")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Sirli_Hot_dog narxi: 16000")
    global balance
    balance = balance - 16000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.callback_query(F.data == "Double_Hot_dog")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://img.iamcook.ru/2022/upl/recipes/byusers/misc/9661/mobile/48e7636ccc941eb606c5b0b3bf824cb8-2022.jpg",
        caption="\n \n Double Hot dog 22 000 so'm \n \n To'lov turini tanlang Uzcard yoki Humo orqali to'lash",
        reply_markup=pay_3)


@dp.callback_query(F.data == "random_3")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Double_Hot_dog narxi: 22000")
    global balance
    balance = balance - 22000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.callback_query(F.data == "Combo_Hot_dog")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://avatars.mds.yandex.net/get-eda/3793239/39f9a17282975e92a218e17cc006980c/M_height",
        caption="\n \n Combo Hot dog 26 000 so'm \n \n To'lov turini tanlang Uzcard yoki Humo orqali to'lash",
        reply_markup=pay_4)


@dp.callback_query(F.data == "random_4")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Combo_Hot_dog narxi: 26000")
    global balance
    balance = balance - 26000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.message(F.text == "🍔 Burger menu")
async def echo_function(message: types.Message):
    await message.answer(text="Tanlang", reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(
        photo="https://img.freepik.com/premium-vector/vector-burger-media-social-feed-design-template_844390-50.jpg",
        caption=f"\n \n Salom {message.from_user.full_name} siz Burgerlar bo'limini tanladingiz.",
        reply_markup=mb_burger)


@dp.callback_query(F.data == "Mini_burger")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://img.delo-vcusa.ru/2015/07/86.jpg",
                                    caption="\n \n Mini_burger 16 000 so'm \n \n To'lov turini tanlang Uzcard yoki Humo orqali to'lash",
                                    reply_markup=pay_5)


@dp.callback_query(F.data == "random_5")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Mini_burger narxi: 16 000")
    global balance
    balance = balance - 16000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.callback_query(F.data == "Gamburger")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://feedup.uz/_next/image?url=https%3A%2F%2Fapi.feedup.uz%2Fapi%2Fmedia%2Fproducts%2Fimg_46.png&w=640&q=75",
        caption="\n \n Gamburger 20 000 so'm \n \n To'lov turini tanlang Uzcard yoki Humo orqali to'lash",
        reply_markup=pay_6)


@dp.callback_query(F.data == "random_6")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Gamburger narxi: 20 000")
    global balance
    balance = balance - 20000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.callback_query(F.data == "Cheese_burger")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://recipes.av.ru//media/recipes/100608_picture_XNlaEKL.jpg",
                                    caption="\n \n Cheese_burger 24 000 so'm \n \n To'lov turini tanlang Uzcard yoki Humo orqali to'lash",
                                    reply_markup=pay_7)


@dp.callback_query(F.data == "random_7")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Cheese_burger narxi: 24 000")
    global balance
    balance = balance - 24000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.callback_query(F.data == "Chicken_burger")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://feedup.uz/_next/image?url=https%3A%2F%2Fapi.feedup.uz%2Fapi%2Fmedia%2Fproducts%2Fimg_11.png&w=640&q=75",
        caption="\n \n Chicken_burger 28 000 so'm \n \n To'lov turini tanlang Uzcard yoki Humo orqali to'lash",
        reply_markup=pay_8)


@dp.callback_query(F.data == "random_8")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Chicken_burger narxi: 28 000")
    global balance
    balance = balance - 28000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.callback_query(F.data == "Combo_burger")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://feedup.uz/_next/image?url=https%3A%2F%2Fapi.feedup.uz%2Fapi%2Fmedia%2Fproducts%2Fimg_4.png&w=640&q=75",
        caption="\n \n Combo_burger 32 000 so'm \n \n To'lov turini tanlang Uzcard yoki Humo orqali to'lash",
        reply_markup=pay_9)


@dp.callback_query(F.data == "random_9")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Combo_burger narxi: 32 000")
    global balance
    balance = balance - 32000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.message(F.text == "🌯 Lavash menu")
async def echo_function(message: types.Message):
    await message.answer(text="Tanlang", reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(
        photo="https://s.yimg.com/ny/api/res/1.2/2vDhmS8Igz2.CsalAiOsSg--/YXBwaWQ9aGlnaGxhbmRlcjt3PTY0MDtoPTQyNw--/https://media.zenfs.com/en/food_wine_804/7452b51d817330b4071c7aff64de72f4",
        caption=f"\n \n Salom {message.from_user.full_name} siz Lavashlar bo'limini tanladingiz.",
        reply_markup=mb_lavash)


@dp.callback_query(F.data == "Lavash")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://feedup.uz/_next/image?url=https%3A%2F%2Fapi.feedup.uz%2Fapi%2Fmedia%2Fproducts%2Fbbq1.png&w=640&q=75",
        caption="\n \n Lavash 20 000 so'm \n \n To'lov turini tanlang Uzcard yoki Humo orqali to'lash",
        reply_markup=pay_10)


@dp.callback_query(F.data == "random_10")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Lavash narxi: 20 000")
    global balance
    balance = balance - 20000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.callback_query(F.data == "Tandir_Lavash")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://feedup.uz/_next/image?url=https%3A%2F%2Fapi.feedup.uz%2Fapi%2Fmedia%2Fproducts%2Flavash_gavyadina_sir.png&w=640&q=75",
        caption="\n \n Tandir Lavash 24 000 so'm \n \n To'lov turini tanlang Uzcard yoki Humo orqali to'lash",
        reply_markup=pay_11)


@dp.callback_query(F.data == "random_11")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Tandir_Lavash narxi: 24 000")
    global balance
    balance = balance - 24000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.callback_query(F.data == "Combo_Lavash")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://feedup.uz/_next/image?url=https%3A%2F%2Fapi.feedup.uz%2Fapi%2Fmedia%2Fproducts%2Fbbq_kombo.png&w=640&q=75",
        caption="\n \n Combo Lavash 28 000 so'm \n \n To'lov turini tanlang Uzcard yoki Humo orqali to'lash",
        reply_markup=pay_12)


@dp.callback_query(F.data == "random_12")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Combo_Lavash narxi: 28 000")
    global balance
    balance = balance - 28000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.callback_query(F.data == "Combo_Tandir_Lavash")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://feedup.uz/_next/image?url=https%3A%2F%2Fapi.feedup.uz%2Fapi%2Fmedia%2Fproducts%2Fimg_31.png&w=640&q=75",
        caption="\n \n Combo Tandir Lavash 30 000 so'm \n \n To'lov turini tanlang Uzcard yoki Humo orqali to'lash",
        reply_markup=pay_13)


@dp.callback_query(F.data == "random_13")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Combo_Tandir_Lavash narxi: 30 000")
    global balance
    balance = balance - 30000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.message(F.text == "🍹 Ichimliklar")
async def echo_function(message: types.Message):
    await message.answer(text="Tanlang", reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(photo="https://storage.kun.uz/source/4/Pgv76ozIYAq6G2_Q1MWhy8Fw0-HOeiuZ.jpg",
                               caption=f"\n \n Salom {message.from_user.full_name} siz Ichimliklar bo'limini tanladingiz.",
                               reply_markup=mb_i)


@dp.callback_query(F.data == "Love_is")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://exportal.io/files/images/items/0/393vf513f2da.jpg",
                                    caption="\n \n Ichimlik Love is 18 000 so'm \n \n To'lov turini tanlang Uzcard yoki Humo orqali to'lash",
                                    reply_markup=pay_14)


@dp.callback_query(F.data == "random_14")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Love_is narxi: 18 000")
    global balance
    balance = balance - 18000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.callback_query(F.data == "Pulpy")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://yukber.uz/image/cache/catalog/product/YK3368/3368-600x600.jpg",
                                    caption="\n \n Ichimlik Pulpy 12 000 so'm \n \n To'lov turini tanlang Uzcard yoki Humo orqali to'lash",
                                    reply_markup=pay_15)


@dp.callback_query(F.data == "random_15")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Pulpy narxi: 12 000")
    global balance
    balance = balance - 12000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.callback_query(F.data == "Tropic")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://yukber.uz/image/cache/catalog/product/YK0182/YK0182_1-600x600.jpg",
                                    caption="\n \n Ichimlik Tropic 6 000 so'm \n \n To'lov turini tanlang Uzcard yoki Humo orqali to'lash",
                                    reply_markup=pay_16)


@dp.callback_query(F.data == "random_16")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Tropic narxi: 6 000")
    global balance
    balance = balance - 6000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.callback_query(F.data == "Moxito")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://www.gazeta.uz/media/img/2021/05/hxSClG16221972734019_l.jpg",
                                    caption="\n \n Ichimlik Moxito 16 000 so'm \n \n To'lov turini tanlang Uzcard yoki Humo orqali to'lash",
                                    reply_markup=pay_17)


@dp.callback_query(F.data == "random_17")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Moxito narxi: 16 000")
    global balance
    balance = balance - 16000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.message(F.text == "🍟 Qo'shimcha")
async def echo_function(message: types.Message):
    await message.answer(text="Tanlang", reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(photo="https://img.freepik.com/free-vector/fast-food-icon-set_1284-4716.jpg",
                               caption=f"\n \n Salom {message.from_user.full_name} siz Qo'shimchalar bo'limini tanladingiz.",
                               reply_markup=mb_q)


@dp.callback_query(F.data == "Free")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://media-cdn.tripadvisor.com/media/photo-p/13/f2/7b/59/photo0jpg.jpg",
                                    caption="\n \n Qo'shimchalar bo'limidan Free 12 000 so'm \n \n To'lov turini tanlang Uzcard yoki Humo orqali to'lash",
                                    reply_markup=pay_18)


@dp.callback_query(F.data == "random_18")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Free narxi: 12 000")
    global balance
    balance = balance - 12000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.callback_query(F.data == "KFC")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://content.jdmagicbox.com/comp/kolhapur/m4/0231px231.x231.230616003906.d5m4/catalogue/kfc-kolhapur-fried-chicken-restaurants-sfezk9nknv.jpg",
        caption="\n \n Qo'shimchalar bo'limidan KFC 14 000 so'm \n \n To'lov turini tanlang Uzcard yoki Humo orqali to'lash",
        reply_markup=pay_19)


@dp.callback_query(F.data == "random_19")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" KFC narxi: 14 000")
    global balance
    balance = balance - 14000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.callback_query(F.data == "Ketchup")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://images.prom.ua/2127414866_w400_h400_krahmal-dlya-sousov.jpg",
                                    caption="\n \n Qo'shimchalar bo'limidan Ketchup 2 000 so'm \n \n To'lov turini tanlang Uzcard yoki Humo orqali to'lash",
                                    reply_markup=pay_20)


@dp.callback_query(F.data == "random_20")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Ketchup narxi: 2 000")
    global balance
    balance = balance - 2000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.callback_query(F.data == "Mayanez")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://images.prom.ua/4235079938_w640_h640_chasnikovij-sous-dlya.jpg",
                                    caption="\n \n Qo'shimchalar bo'limidan Mayanez 2 000 so'm \n \n To'lov turini tanlang Uzcard yoki Humo orqali to'lash",
                                    reply_markup=pay_21)


@dp.callback_query(F.data == "random_21")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Mayanez narxi: 2 000")
    global balance
    balance = balance - 2000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.message(F.text == "🎂 Shirinliklar")
async def echo_function(message: types.Message):
    await message.answer(text="Tanlang", reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(
        photo="https://www.tastingtable.com/img/gallery/ranking-fast-food-desserts-from-worst-to-best/l-intro-1682970849.jpg",
        caption=f"\n \n Salom {message.from_user.full_name} siz Shirinliklar bo'limini tanladingiz.",
        reply_markup=mb_sh)


@dp.callback_query(F.data == "Kokteyl")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://www.projuice.co.uk/app/uploads/2023/02/strawberry.jpg",
                                    caption="\n \n Shirinlik Kokteyl 18 000 so'm \n \n To'lov turini tanlang Uzcard yoki Humo orqali to'lash",
                                    reply_markup=pay_22)


@dp.callback_query(F.data == "random_22")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Kokteyl narxi: 18 000")
    global balance
    balance = balance - 18000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.callback_query(F.data == "Bulochka")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://media.hswstatic.com/eyJidWNrZXQiOiJjb250ZW50Lmhzd3N0YXRpYy5jb20iLCJrZXkiOiJnaWZcL3BsYXlcLzUzZTdmMTQ0LTZkNDItNGQzZi04ZjA1LTBlOWMzMWFmODg2ZS0xMjEwLTY4MC5qcGciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjgyOH19fQ==",
        caption="\n \n Shirinlik Bulochka 8 000 so'm \n \n To'lov turini tanlang Uzcard yoki Humo orqali to'lash",
        reply_markup=pay_23)


@dp.callback_query(F.data == "random_23")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Bulochka narxi: 8 000")
    global balance
    balance = balance - 8000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.callback_query(F.data == "Tort")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://s.yimg.com/ny/api/res/1.2/Lh08_pIBgfyDd8Wc3wU2gA--/YXBwaWQ9aGlnaGxhbmRlcjt3PTY0MDtoPTY0MQ--/https://media.zenfs.com/en/aol_cheapism_430/3ac3777c7c460a8e1268c877144ce652",
        caption="\n \n Shirinlik Tort 24 000 so'm \n \n To'lov turini tanlang Uzcard yoki Humo orqali to'lash",
        reply_markup=pay_24)


@dp.callback_query(F.data == "random_24")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Tort narxi: 24 000")
    global balance
    balance = balance - 24000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.callback_query(F.data == "Muzqaymoq")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://i.pinimg.com/736x/6d/f2/7b/6df27b2153f813f033d124c0bb30a86f.jpg",
                                    caption="\n \n Shirinlik Muzqaymoq 15 000 so'm \n \n To'lov turini tanlang Uzcard yoki Humo orqali to'lash",
                                    reply_markup=pay_25)


@dp.callback_query(F.data == "random_25")
async def send_random_value(callback: types.CallbackQuery):
    orders.append(" Muzqaymoq narxi: 15 000")
    global balance
    balance = balance - 15000
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !\n \n To'lov turini tanlang !!!", reply_markup=mb)


@dp.callback_query(F.data == "Uzcard")
async def pey_function(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(Card.card_number)
    await call.message.answer("Karta raqamini kiriting: ")


@dp.message(Card.card_number)
async def card_number_function(message: types.Message, state: FSMContext):
    text = message.text
    if text.isdigit() and len(text) == 16:
        await state.update_data(card_number=message.text)
        await message.answer(
            f"\n \n Rahmat {message.from_user.full_name} siz to'lovni Uzcard kartasi orqali omalga oshirdingiz. \nBizdan harid qilganingiz uchun rahmat!!! \nYana harid qilmoqchi bo'lsangiz menu bo'limiga o'ting.",
            reply_markup=mb_1)
    else:
        await message.answer("Boshidan urinib ko'ring !!!")
    await state.clear()


@dp.callback_query(F.data == "Humo")
async def pay_function(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(Card.card_number_2)
    await call.message.answer("Karta raqamini kiriting: ")


@dp.message(Card.card_number_2)
async def card_number_function(message: types.Message, state: FSMContext):
    text = message.text
    if text.isdigit() and len(text) == 16:
        await state.update_data(card_number=message.text)
        await message.answer(
            f"\n \n Rahmat {message.from_user.full_name} siz Humo kartasi orqali to'lovni omalga oshirdingiz. \nBizdan harid qilganingiz uchun rahmat!!! \nYana harid qilmoqchi bo'lsangiz menu bo'limiga o'ting.",
            reply_markup=mb_1)
    else:
        await message.answer("Boshidan urinib ko'ring !!!")
    await state.clear()


@dp.callback_query(F.data == "random")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer(
        text="\n \n Rahmat siz buyurtma qildingiz !!!", reply_markup=mb)


@dp.callback_query(F.data == "random_uz")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer(text="\n \n Siz buyurtma qilmadingiz!", reply_markup=mb)


@dp.message(F.text == "Sotib olish")
async def savat_function(message: types.Message):
    await message.answer("To'lov turini tanlang Uzcard yoki Humo orqali to'lash", reply_markup=cart)


@dp.message(F.text == "🛒 Savat")
async def savat_function(message: types.Message):
    await message.answer("Siz savat bo'limini tanladingiz !", reply_markup=savat_button)


@dp.message(F.text == "🗑 Savatni ko'rish")
async def orders_function(message: types.Message):
    await message.answer(f"Sizda bor narsalar ro'yxati !!!")
    await message.answer(f"{"\n".join(orders)}", reply_markup=mb_1)


@dp.message(F.text == "🚮 Savatni tozalash")
async def ordersdell_function(message: types.Message):
    orders.clear()
    await message.answer("Siz barcha mahsulotlarni o'chirib yubordingiz !!!", reply_markup=mb_1)


@dp.message(F.text == "Yordam")
async def balance_function(message: types.Message):
    await message.answer(
        f"Salom siz yordam bo'limini tanladingiz \nAgar sizda qandaydir muommo bo'lsa pastdagi raqamlarga telefon qilishingiz mumkin \n \nTelefon raqam: +998 93 514-06-10",
        reply_markup=mb_1)


@dp.message(F.text == "Ma'lumot")
async def balance_function(message: types.Message):
    await message.answer(
        f"Salom siz ma'lumot bo'limini tanladingiz \nBu bo'limda siz shu bot haqida ma'lumot olishingiz mumkin \nBu bot orqali siz taomlar buyurtma qila olasiz \nBu bot o'zingiz haqingizda ma'lumot bera oladi. \nBu bot orqali siz o'z telegram raqamingizni bila olasiz.",
        reply_markup=mb_1)


@dp.message(F.text == "Tilni o'zgartirish")
async def balance_function(message: types.Message):
    await message.answer(f"Siz tilni oʻzgartirishni tanladingiz \nTilni oʻzgartiring", reply_markup=til_1)


@dp.message(F.text == "O'zbek tili 🇺🇿")
async def balance_function(message: types.Message):
    await message.answer(f"Siz O'zbek tilga o'zgartirdingiz", reply_markup=mb_1)


class Registration_1(StatesGroup):
    first_name = State()
    last_name = State()
    number_one = State()
    cart_1_numb1er = State()


contact_button_1 = types.ReplyKeyboardMarkup(keyboard=[
    [types.KeyboardButton(text="Отправить контакт", request_contact=True)]
], resize_keyboard=True)

# til = ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text="Uzb 🇺🇿")],
#     [KeyboardButton(text="Rus 🇷🇺")]
# ], resize_keyboard=True)

kb = [
    [KeyboardButton(text="🌭 Hotdog"), KeyboardButton(text="🌯 Lavash Меню")],
    [KeyboardButton(text="🍔 Burger Меню"), KeyboardButton(text="🍹 Напитоки")],
    [KeyboardButton(text="🍟 Дополнительный"), KeyboardButton(text="🎂 Сладость"), KeyboardButton(text="🔙 Назад")]
]
mb1 = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

kb1_1 = [
    [KeyboardButton(text="🔍 Меню"), KeyboardButton(text="🛒 Корзина"), KeyboardButton(text="О нас")],
    [KeyboardButton(text="📲 Ваша информация"), KeyboardButton(text="Поддерживать"),
     KeyboardButton(text="Изменить язык")]
]
mb1_2 = ReplyKeyboardMarkup(keyboard=kb1_1, resize_keyboard=True)

savat_button_1 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Покупка"), KeyboardButton(text="🚮 Очистить корзину")],
    [KeyboardButton(text="🗑 Посмотреть корзину"), KeyboardButton(text="🔙 Назад")]
], resize_keyboard=True)

mb1_hd = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🌭 Classic Hotdog", callback_data="Classic_Hot_dog_1"),
     InlineKeyboardButton(text="🌭 Comb1o Hotdog", callback_data="Comb1o_Hot_dog_1")],
    [InlineKeyboardButton(text="🌭 Sirli Hotdog", callback_data="Sirli_Hot_dog_1"),
     InlineKeyboardButton(text="🌭 Double Hotdog", callback_data="Double_Hot_dog_1")],
])

mb1_burger = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🍔Mini burger", callback_data="Mini_burger_1"),
     InlineKeyboardButton(text="🍔Gamburger", callback_data="Gamb1urger_1")],
    [InlineKeyboardButton(text="🍔Cheese burger", callback_data="Cheese_burger_1"),
     InlineKeyboardButton(text="🍔Chicken burger", callback_data="Chicken_burger_1")],
    [InlineKeyboardButton(text="🍔Combo burger", callback_data="Comb1o_burger_1")],
])

mb1_lavash = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🌯Lavash", callback_data="Lavash_1"),
     InlineKeyboardButton(text="🌯Combo Tandir Lavash", callback_data="Comb1o_Tandir_Lavash_1")],
    [InlineKeyboardButton(text="🌯Tandir Lavash", callback_data="Tandir_Lavash_1"),
     InlineKeyboardButton(text="🌯Combo Lavash", callback_data="Comb1o_Lavash_1")],
])

mb1_i = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🥤Love is", callback_data="Love_is_1"),
     InlineKeyboardButton(text="🥤Tropic", callback_data="Tropic_1")],
    [InlineKeyboardButton(text="🥤Pulpy", callback_data="Pulpy_1"),
     InlineKeyboardButton(text="🍹Moxito", callback_data="Moxito_1")],
])

mb1_q = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🍟Free", callback_data="Free_1"),
     InlineKeyboardButton(text="🍖KFC", callback_data="KFC_1")],
    [InlineKeyboardButton(text="🥫Ketchup", callback_data="Ketchup_1"),
     InlineKeyboardButton(text="🥫Mayanez", callback_data="Mayanez_1")],
])

mb1_sh = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🍹Kokteyl", callback_data="Kokteyl_1"),
     InlineKeyboardButton(text="🍰Tort", callback_data="Tort_1")],
    [InlineKeyboardButton(text="🍩Bulochka", callback_data="Bulochka_1"),
     InlineKeyboardButton(text="🍦 Мороженое", callback_data="Мороженое_1")],
])

pay1_1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_2")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_3")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_4 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_4")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_5 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_5")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_6 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_6")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_7 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_7")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_8 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_8")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_9 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_9")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_10 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_10")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_11 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_11")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_12 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_12")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_13 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_13")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_14 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_14")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_15 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_15")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_16 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_16")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_17 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_17")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_18 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_18")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_19 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_19")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_20 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_20")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_21 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_21")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_22 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_22")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_23 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_23")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_24 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_24")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

pay1_25 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Получите ваш заказ", callback_data="1_random_25")],
    [InlineKeyboardButton(text="❌ Вернуть заказ", callback_data="1_random_uz")],
])

cart_1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="💳Uzcard", callback_data="Uzcard_1")],
    [InlineKeyboardButton(text="💳Humo", callback_data="Humo_1")],
])


@dp.message(filters.Command("start"))
async def start_function(message: types.Message):
    await message.answer(
        f"\n \n Salom {message.from_user.full_name}, botga xush kelibsiz !!! \n \n Здравствуйте, {message.from_user.full_name}, добро пожаловать в бот !!!",
        reply_markup=til)


@dp.callback_query(F.data == "Меню")
async def start_function(call: types.CallbackQuery):
    await call.answer_photo(
        photo="https://avatars.mds.yandex.net/get-altay/9728306/2a0000018a6fc3054db52240e707fb55e28f/L_height",
        caption="\n \n Привет, feed up. Познакомься с меню. \n 1 Hot_dog \n 2 Gamb1urger \n 3 Lavash_Меню \n 4 Напитокиlar \n 5 Дополнительный \n 6 Сладостьlar \n \n \n",
        reply_markup=mb1)


@dp.message(F.text == "🔍 Меню")
async def start_function(message: types.Message):
    await message.answer_photo(
        photo="https://avatars.mds.yandex.net/get-altay/9728306/2a0000018a6fc3054db52240e707fb55e28f/L_height",
        caption="\n \n Привет, feed up. Познакомься с меню. \n 1 Hot_dog \n 2 Gamb1urger \n 3 Lavash_Меню \n 4 Напитокиlar \n 5 Дополнительный \n 6 Сладостьlar \n \n \n",
        reply_markup=mb1)


@dp.message(F.text == "🔙 Назад")
async def ortga_function(message: types.Message):
    await message.answer("Вы вернулись", reply_markup=mb1_2)


@dp.message(F.text == "📲 Ваша информация")
async def info_function(message: types.Message):
    await message.answer(
        f"\n \n Ваше имя {message.from_user.full_name} \nВаше user name {message.from_user.username} \nВаше id {message.from_user.id} \n \n",
        reply_markup=mb1_2)


@dp.message(F.text == "Rus 🇷🇺")
async def start(message: types.Message, state: FSMContext):
    await state.set_state(Registration_1.first_name)
    await message.answer("Добро пожаловать\nВведите свое имя: ")


@dp.message(Registration_1.first_name)
async def first_name_function(message: types.Message, state: FSMContext):
    await state.update_data(first_name=message.text)
    await state.set_state(Registration_1.last_name)
    await message.answer("Хорошо, теперь введите фамилия: ")


@dp.message(Registration_1.last_name)
async def last_name_function(message: types.Message, state: FSMContext):
    await state.update_data(last_name=message.text)
    await state.set_state(Registration_1.number_one)
    await message.answer("Хорошо, теперь введите номер: ", reply_markup=contact_button_1)


@dp.message(Registration_1.number_one)
async def phone_function(message: types.Message, state: FSMContext):
    await state.update_data(numb1er=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(
        f"Нет проблем!\nВаше имя: {data['first_name']}\nВаша фамилия: {data['last_name']}\nВаш номер: {data['number']}",
        reply_markup=mb1_2)
    await state.clear()


@dp.message(F.text == "🌭 Hotdog")
async def echo_function(message: types.Message):
    await message.answer(text="Tanlang", reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(
        photo="https://sun9-16.userapi.com/impf/c852024/v852024787/1b00ec/nh17wVjmwIw.jpg?size=640x333&quality=96&sign=ac5dcb5df8feb82b1ccbf2f81e56adec&c_uniq_tag=AoaV9UZx--Xsue7NGHnjIh8QJc7P0U9saxrGdxWqU5A&type=album",
        caption=f"\n \n Здравствуйте, {message.from_user.full_name}! Вы выбрали раздел «Хот-доги».",
        reply_markup=mb1_hd)


@dp.callback_query(F.data == "Classic_Hot_dog_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://avatars.mds.yandex.net/get-eda/3490335/46368596e993177dbd46616cefc0f3d1/M_height",
        caption="\n \n Classic Hot dog 14 000 so'm", reply_markup=pay1_1)


@dp.callback_query(F.data == "1_random")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Classic_Hot_dog расходы: 14000")
    global balance
    balance = balance - 14000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.callback_query(F.data == "Sirli_Hot_dog_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://avatars.mds.yandex.net/get-eda/3506707/10f01c187799f1ea0345822dbe475f59/M_height",
        caption="\n \n Sirli Hot dog 16 000 so'm", reply_markup=pay1_2)


@dp.callback_query(F.data == "1_random_2")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Sirli_Hot_dog расходы: 16000")
    global balance
    balance = balance - 16000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.callback_query(F.data == "Double_Hot_dog_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://img.iamcook.ru/2022/upl/recipes/byusers/misc/9661/mobile/48e7636ccc941eb606c5b0b3bf824cb8-2022.jpg",
        caption="\n \n Double Hot dog 22 000 so'm", reply_markup=pay1_3)


@dp.callback_query(F.data == "1_random_3")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Double_Hot_dog расходы: 22000")
    global balance
    balance = balance - 22000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.callback_query(F.data == "Comb1o_Hot_dog_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://avatars.mds.yandex.net/get-eda/3793239/39f9a17282975e92a218e17cc006980c/M_height",
        caption="\n \n Comb1o Hot dog 26 000 so'm", reply_markup=pay1_4)


@dp.callback_query(F.data == "1_random_4")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Comb1o_Hot_dog расходы: 26000")
    global balance
    balance = balance - 26000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.message(F.text == "🍔 Burger Меню")
async def echo_function(message: types.Message):
    await message.answer(text="Tanlang", reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(
        photo="https://img.freepik.com/premium-vector/vector-burger-media-social-feed-design-template_844390-50.jpg",
        caption=f"Здравствуйте, {message.from_user.full_name}, вы выбрали Бургеры.", reply_markup=mb1_burger)


@dp.callback_query(F.data == "Mini_burger_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://img.delo-vcusa.ru/2015/07/86.jpg",
                                    caption="\n \n Mini_burger 16 000 so'm", reply_markup=pay1_5)


@dp.callback_query(F.data == "1_random_5")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Mini_burger расходы: 16 000")
    global balance
    balance = balance - 16000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.callback_query(F.data == "Gamb1urger_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://feedup.uz/_next/image?url=https%3A%2F%2Fapi.feedup.uz%2Fapi%2Fmedia%2Fproducts%2Fimg_46.png&w=640&q=75",
        caption="\n \n Gamb1urger 20 000 so'm", reply_markup=pay1_6)


@dp.callback_query(F.data == "1_random_6")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Gamb1urger расходы: 20 000")
    global balance
    balance = balance - 20000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.callback_query(F.data == "Cheese_burger_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://recipes.av.ru//media/recipes/100608_picture_XNlaEKL.jpg",
                                    caption="\n \n Cheese_burger 24 000 so'm", reply_markup=pay1_7)


@dp.callback_query(F.data == "1_random_7")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Cheese_burger расходы: 24 000")
    global balance
    balance = balance - 24000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.callback_query(F.data == "Chicken_burger_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://feedup.uz/_next/image?url=https%3A%2F%2Fapi.feedup.uz%2Fapi%2Fmedia%2Fproducts%2Fimg_11.png&w=640&q=75",
        caption="\n \n Chicken_burger 28 000 so'm", reply_markup=pay1_8)


@dp.callback_query(F.data == "1_random_8")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Chicken_burger расходы: 28 000")
    global balance
    balance = balance - 28000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.callback_query(F.data == "Comb1o_burger_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://feedup.uz/_next/image?url=https%3A%2F%2Fapi.feedup.uz%2Fapi%2Fmedia%2Fproducts%2Fimg_4.png&w=640&q=75",
        caption="\n \n Comb1o_burger 32 000 so'm", reply_markup=pay1_9)


@dp.callback_query(F.data == "1_random_9")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Comb1o_burger расходы: 32 000")
    global balance
    balance = balance - 32000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.message(F.text == "🌯 Lavash Меню")
async def echo_function(message: types.Message):
    await message.answer(text="Tanlang", reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(
        photo="https://s.yimg.com/ny/api/res/1.2/2vDhmS8Igz2.CsalAiOsSg--/YXBwaWQ9aGlnaGxhbmRlcjt3PTY0MDtoPTQyNw--/https://media.zenfs.com/en/food_wine_804/7452b51d817330b4071c7aff64de72f4",
        caption=f"Здравствуйте, {message.from_user.full_name}, вы выбрали раздел Лаваш..", reply_markup=mb1_lavash)


@dp.callback_query(F.data == "Lavash_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://feedup.uz/_next/image?url=https%3A%2F%2Fapi.feedup.uz%2Fapi%2Fmedia%2Fproducts%2Fbbq1.png&w=640&q=75",
        caption="\n \n Lavash 20 000 so'm", reply_markup=pay1_10)


@dp.callback_query(F.data == "1_random_10")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Lavash расходы: 20 000")
    global balance
    balance = balance - 20000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.callback_query(F.data == "Tandir_Lavash_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://feedup.uz/_next/image?url=https%3A%2F%2Fapi.feedup.uz%2Fapi%2Fmedia%2Fproducts%2Flavash_gavyadina_sir.png&w=640&q=75",
        caption="\n \n Tandir Lavash 24 000 so'm", reply_markup=pay1_11)


@dp.callback_query(F.data == "1_random_11")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Tandir_Lavash расходы: 24 000")
    global balance
    balance = balance - 24000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.callback_query(F.data == "Comb1o_Lavash_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://feedup.uz/_next/image?url=https%3A%2F%2Fapi.feedup.uz%2Fapi%2Fmedia%2Fproducts%2Fbbq_komb1o.png&w=640&q=75",
        caption="\n \n Comb1o Lavash 28 000 so'm", reply_markup=pay1_12)


@dp.callback_query(F.data == "1_random_12")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Combo_Lavash расходы: 28 000")
    global balance
    balance = balance - 28000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.callback_query(F.data == "Comb1o_Tandir_Lavash_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://feedup.uz/_next/image?url=https%3A%2F%2Fapi.feedup.uz%2Fapi%2Fmedia%2Fproducts%2Fimg_31.png&w=640&q=75",
        caption="\n \n Comb1o Tandir Lavash 30 000 so'm", reply_markup=pay1_13)


@dp.callback_query(F.data == "1_random_13")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Comb1o_Tandir_Lavash расходы: 30 000")
    global balance
    balance = balance - 30000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.message(F.text == "🍹 Напитоки")
async def echo_function(message: types.Message):
    await message.answer(text="Tanlang", reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(photo="https://storage.kun.uz/source/4/Pgv76ozIYAq6G2_Q1MWhy8Fw0-HOeiuZ.jpg",
                               caption=f"Здравствуйте, {message.from_user.full_name}! Вы выбрали «Напитки».",
                               reply_markup=mb1_i)


@dp.callback_query(F.data == "Love_is_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://exportal.io/files/images/items/0/393vf513f2da.jpg",
                                    caption="\n \n Напитоки Love is 18 000 so'm", reply_markup=pay1_14)


@dp.callback_query(F.data == "1_random_14")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Love_is расходы: 18 000")
    global balance
    balance = balance - 18000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.callback_query(F.data == "Pulpy_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://yukber.uz/image/cache/catalog/product/YK3368/3368-600x600.jpg",
                                    caption="\n \n Напитоки Pulpy 12 000 so'm", reply_markup=pay1_15)


@dp.callback_query(F.data == "1_random_15")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Pulpy расходы: 12 000")
    global balance
    balance = balance - 12000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.callback_query(F.data == "Tropic_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://yukber.uz/image/cache/catalog/product/YK0182/YK0182_1-600x600.jpg",
                                    caption="\n \n Напитоки Tropic 6 000 so'm", reply_markup=pay1_16)


@dp.callback_query(F.data == "1_random_16")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Tropic расходы: 6 000")
    global balance
    balance = balance - 6000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.callback_query(F.data == "Moxito_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://www.gazeta.uz/media/img/2021/05/hxSClG16221972734019_l.jpg",
                                    caption="\n \n Напитоки Moxito 16 000 so'm", reply_markup=pay1_17)


@dp.callback_query(F.data == "1_random_17")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Moxito расходы: 16 000")
    global balance
    balance = balance - 16000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.message(F.text == "🍟 Дополнительный")
async def echo_function(message: types.Message):
    await message.answer(text="Tanlang", reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(photo="https://img.freepik.com/free-vector/fast-food-icon-set_1284-4716.jpg",
                               caption=f"Здравствуйте, {message.from_user.full_name}! Вы выбрали дополнения..",
                               reply_markup=mb1_q)


@dp.callback_query(F.data == "Free_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://media-cdn.tripadvisor.com/media/photo-p/13/f2/7b/59/photo0jpg.jpg",
                                    caption="\n \n Дополнительный из отдела Free 12 000 so'm", reply_markup=pay1_18)


@dp.callback_query(F.data == "1_random_18")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Free расходы: 12 000")
    global balance
    balance = balance - 12000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.callback_query(F.data == "KFC_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://content.jdmagicbox.com/comp/kolhapur/m4/0231px231.x231.230616003906.d5m4/catalogue/kfc-kolhapur-fried-chicken-restaurants-sfezk9nknv.jpg",
        caption="\n \n Дополнительный из отдела KFC 14 000 so'm", reply_markup=pay1_19)


@dp.callback_query(F.data == "1_random_19")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" KFC расходы: 14 000")
    global balance
    balance = balance - 14000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.callback_query(F.data == "Ketchup_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://images.prom.ua/2127414866_w400_h400_krahmal-dlya-sousov.jpg",
                                    caption="\n \n Дополнительный из отдела Ketchup 2 000 so'm", reply_markup=pay1_20)


@dp.callback_query(F.data == "1_random_20")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Ketchup расходы: 2 000")
    global balance
    balance = balance - 2000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.callback_query(F.data == "Mayanez_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://images.prom.ua/4235079938_w640_h640_chasnikovij-sous-dlya.jpg",
                                    caption="\n \n Дополнительный из отдела Mayanez 2 000 so'm", reply_markup=pay1_21)


@dp.callback_query(F.data == "1_random_21")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Mayanez расходы: 2 000")
    global balance
    balance = balance - 2000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.message(F.text == "🎂 Сладость")
async def echo_function(message: types.Message):
    await message.answer(text="Tanlang", reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(
        photo="https://www.tastingtable.com/img/gallery/ranking-fast-food-desserts-from-worst-to-best/l-intro-1682970849.jpg",
        caption=f"Здравствуйте, {message.from_user.full_name}! Вы выбрали Сладости.", reply_markup=mb1_sh)


@dp.callback_query(F.data == "Kokteyl_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://www.projuice.co.uk/app/uploads/2023/02/strawberry.jpg",
                                    caption="\n \n Сладость Kokteyl 18 000 so'm", reply_markup=pay1_22)


@dp.callback_query(F.data == "1_random_22")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Kokteyl расходы: 18 000")
    global balance
    balance = balance - 18000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.callback_query(F.data == "Bulochka_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://media.hswstatic.com/eyJidWNrZXQiOiJjb250ZW50Lmhzd3N0YXRpYy5jb20iLCJrZXkiOiJnaWZcL3BsYXlcLzUzZTdmMTQ0LTZkNDItNGQzZi04ZjA1LTBlOWMzMWFmODg2ZS0xMjEwLTY4MC5qcGciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjgyOH19fQ==",
        caption="\n \n Сладость Bulochka 8 000 so'm", reply_markup=pay1_23)


@dp.callback_query(F.data == "1_random_23")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Bulochka расходы: 8 000")
    global balance
    balance = balance - 8000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.callback_query(F.data == "Tort_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://s.yimg.com/ny/api/res/1.2/Lh08_pIBgfyDd8Wc3wU2gA--/YXBwaWQ9aGlnaGxhbmRlcjt3PTY0MDtoPTY0MQ--/https://media.zenfs.com/en/aol_cheapism_430/3ac3777c7c460a8e1268c877144ce652",
        caption="\n \n Сладость Tort 24 000 so'm", reply_markup=pay1_24)


@dp.callback_query(F.data == "1_random_24")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Tort расходы: 24 000")
    global balance
    balance = balance - 24000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.callback_query(F.data == "Мороженое_1")
async def echo_function(call: types.CallbackQuery):
    await call.message.answer_photo(photo="https://i.pinimg.com/736x/6d/f2/7b/6df27b2153f813f033d124c0bb30a86f.jpg",
                                    caption="\n \n Сладость Мороженое 15 000 so'm", reply_markup=pay1_25)


@dp.callback_query(F.data == "1_random_25")
async def send_1_random_value(callback: types.CallbackQuery):
    orders.append(" Мороженое расходы: 15 000")
    global balance
    balance = balance - 15000
    await callback.message.answer(
        text="Спасибо за заказ!", reply_markup=mb1)


@dp.callback_query(F.data == "Uzcard_1")
async def pey_function(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(Card_1.card_number)
    await call.message.answer("Введите номер карты: ")


@dp.message(Card_1.card_number)
async def card_number_function(message: types.Message, state: FSMContext):
    text = message.text
    if text.isdigit() and len(text) == 16:
        await state.update_data(card_number=message.text)
        await message.answer(
            f"Спасибо {message.from_user.full_name}, вы произвели оплату картой Uzcard. \nСпасибо, что делаете покупки у нас!!! \nЕсли вы хотите купить еще раз, перейдите в раздел «Меню».",
            reply_markup=mb1_2)
    else:
        await message.answer("Попробуйте с начала!!!")
    await state.clear()


@dp.callback_query(F.data == "Humo_1")
async def pay_function(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(Card_1.card_number_2)
    await call.message.answer("Введите номер карты: ")


@dp.message(Card_1.card_number_2)
async def card_number_function(message: types.Message, state: FSMContext):
    text = message.text
    if text.isdigit() and len(text) == 16:
        await state.update_data(card_number=message.text)
        await message.answer(
            f"Спасибо {message.from_user.full_name}, вы произвели оплату картой Humo. \nСпасибо, что делаете покупки у нас!!! \nЕсли вы хотите купить еще раз, перейдите в раздел «Меню».",
            reply_markup=mb1_2)
    else:
        await message.answer("Попробуйте с начала!!!")
    await state.clear()


@dp.callback_query(F.data == "1_random")
async def send_1_random_value(callback: types.CallbackQuery):
    await callback.message.answer(
        text="Спасибо за заказ!!!", reply_markup=mb1)


@dp.callback_query(F.data == "1_random_uz")
async def send_1_random_value(callback: types.CallbackQuery):
    await callback.message.answer(text="Вы не заказывали!", reply_markup=mb1)


@dp.message(F.text == "Покупка")
async def savat_function(message: types.Message):
    await message.answer("Вы приобрели товар \nСпасибо за покупку", reply_markup=cart_1)


@dp.message(F.text == "🛒 Корзина")
async def savat_function(message: types.Message):
    await message.answer("Вы выбрали раздел «Корзина»!", reply_markup=savat_button_1)


@dp.message(F.text == "🗑 Посмотреть корзину")
async def orders_function(message: types.Message):
    await message.answer(f"Список того, что у вас есть!!!")
    await message.answer(f"{"\n".join(orders)}", reply_markup=mb1_2)


@dp.message(F.text == "🚮 Очистить корзину")
async def ordersdell_function(message: types.Message):
    orders.clear()
    await message.answer("Вы удалили все товары!!!", reply_markup=mb1_2)


@dp.message(F.text == "Поддерживать")
async def balance_function(message: types.Message):
    await message.answer(
        f"Здравствуйте, вы выбрали раздел помощи \nЕсли у вас возникли проблемы, вы можете позвонить по номерам ниже \n \n Телефон: +998 93 514-06-10",
        reply_markup=mb1_2)


@dp.message(F.text == "О нас")
async def balance_function(message: types.Message):
    await message.answer(
        f"Здравствуйте, вы выбрали информационный раздел\nВ этом разделе вы можете получить информацию об этом боте \n Через этого бота вы можете заказать еду \n Этот бот может предоставить информацию о себе. \n Через этого бота вы можете узнать свой номер телеграма.",
        reply_markup=mb1_2)


@dp.message(F.text == "Изменить язык")
async def balance_function(message: types.Message):
    await message.answer(f"Вы выбрали смену языка\nИзменить язык", reply_markup=til_1)


@dp.message(F.text == "Русский язык 🇷🇺")
async def balance_function(message: types.Message):
    await message.answer(f"Вы пер ешли на русский", reply_markup=mb1_2)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

# main_button = ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text="🚙 Cars"), KeyboardButton(text="🛒 Orders")],
#     [KeyboardButton(text="💸 Balance"), KeyboardButton(text="📲 My_info")]
# ], resize_keyboard=True)
#
# cars_button = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="Uzb cars", callback_data="uzb"), InlineKeyboardButton(text="Euro cars", callback_data="euro")],
# ])
#
# uzb_car_button = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="Matiz", callback_data="matiz"), InlineKeyboardButton(text="Spark", callback_data="spark"), InlineKeyboardButton(text="Nexia", callback_data="nexia")],
#     [InlineKeyboardButton(text="Malibu", callback_data="malibu"), InlineKeyboardButton(text="Cobalt", callback_data="cobalt"), InlineKeyboardButton(text="Jentra", callback_data="jentra")],
# ])
#
# matiz_button = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="⬛️ Qora rangli Matiz", callback_data="qora_matiz"), InlineKeyboardButton(text="⬜️ Oq rangli Matiz", callback_data="oq_matiz"), InlineKeyboardButton(text="🟥 Qizil rangli Matiz", callback_data="qizil_matiz")],
#     [InlineKeyboardButton(text="🟨 Sariq rangli Matiz", callback_data="sariq_matiz"), InlineKeyboardButton(text="🟦 Moviy rangli Matiz", callback_data="moviy_matiz"), InlineKeyboardButton(text="🟩 Yashil rangli Matiz", callback_data="yashil_matiz")],
# ])
#
# matiz_btn = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="🛒 Savatga solish", callback_data="savat_solish_mz"), InlineKeyboardButton(text="🛒 Savatdan olish", callback_data="savat_olish_mz")],
#     [InlineKeyboardButton(text="💸 Sotib olish", callback_data="sotib_ol"), InlineKeyboardButton(text="🔍 Menu", callback_data="menu")],
# ])
#
# spark_button = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="⬛️ Qora rangli Spark", callback_data="qora_spark"), InlineKeyboardButton(text="⬜️ Oq rangli Spark", callback_data="oq_spark"), InlineKeyboardButton(text="🟥 Qizil rangli Matiz", callback_data="qizil_spark")],
#     [InlineKeyboardButton(text="🟨 Sariq rangli Spark", callback_data="sariq_spark"), InlineKeyboardButton(text="🟦 Moviy rangli Spark", callback_data="moviy_spark"), InlineKeyboardButton(text="🟩 Yashil rangli Matiz", callback_data="yashil_spark")],
# ])
#
# spark_btn = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="🛒 Savatga solish", callback_data="savat_solish_sk"), InlineKeyboardButton(text="🛒 Savatdan olish", callback_data="savat_olish_sk")],
#     [InlineKeyboardButton(text="💸 Sotib olish", callback_data="sotib_ol"), InlineKeyboardButton(text="🔍 Menu", callback_data="menu")],
# ])
#
# euro_car_button = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="BMW", callback_data="bmw"), InlineKeyboardButton(text="Porsche", callback_data="porsche"), InlineKeyboardButton(text="Tesla", callback_data="tesla")],
#     [InlineKeyboardButton(text="Mersadez-Benz", callback_data="mers"), InlineKeyboardButton(text="Lamborghini", callback_data="lambo"), InlineKeyboardButton(text="Mustang", callback_data="ford")],
# ])
#
# bmw_button = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="⬛️ Qora rangli BMW", callback_data="qora_bmw"), InlineKeyboardButton(text="⬜️ Oq rangli BMW", callback_data="oq_bmw"), InlineKeyboardButton(text="🟥 Qizil rangli BMW", callback_data="qizil_bmw")],
#     [InlineKeyboardButton(text="🟨 Sariq rangli BMW", callback_data="sariq_bmw"), InlineKeyboardButton(text="🟦 Moviy rangli BMW", callback_data="moviy_bmw"), InlineKeyboardButton(text="🟩 Binafsha rangli BMW", callback_data="binafsha_bmw")],
# ])
#
# bmw_btn = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="🛒 Savatga solish", callback_data="savat_solish_b"), InlineKeyboardButton(text="🛒 Savatdan olish", callback_data="savat_olish_b")],
#     [InlineKeyboardButton(text="💸 Sotib olish", callback_data="sotib_ol"), InlineKeyboardButton(text="🔍 Menu", callback_data="menu")],
# ])
#
# porsh_button = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="⬛️ Qora rangli Porsche", callback_data="qora_porsh"), InlineKeyboardButton(text="⬜️ Oq rangli Porsche", callback_data="oq_porsh"), InlineKeyboardButton(text="🟥 Qizil rangli Porsche", callback_data="qizil_porsh")],
#     [InlineKeyboardButton(text="🟨 Sariq rangli Porsche", callback_data="sariq_porsh"), InlineKeyboardButton(text="🟦 Moviy rangli Porsche", callback_data="moviy_porsh"), InlineKeyboardButton(text="🟩 Yashil rangli Porsche", callback_data="yashil_porsh")],
# ])
#
# porsh_btn = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="🛒 Savatga solish", callback_data="savat_solish_p"), InlineKeyboardButton(text="🛒 Savatdan olish", callback_data="savat_olish_p")],
#     [InlineKeyboardButton(text="💸 Sotib olish", callback_data="sotib_ol"), InlineKeyboardButton(text="🔍 Menu", callback_data="menu")],
# ])
#
# tesla_button = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="⬛️ Qora rangli Tesla", callback_data="qora_tesla"), InlineKeyboardButton(text="⬜️ Oq rangli Tesla", callback_data="oq_tesla"), InlineKeyboardButton(text="🟥 Qizil rangli Tesla", callback_data="qizil_tesla")],
#     [InlineKeyboardButton(text="🟨 Sariq rangli Tesla", callback_data="sariq_tesla"), InlineKeyboardButton(text="🟦 Moviy rangli Tesla", callback_data="moviy_tesla"), InlineKeyboardButton(text="🔸 Tilla rangli Tesla", callback_data="tilla_tesla")],
# ])
#
# tesla_btn = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="🛒 Savatga solish", callback_data="savat_solish_t"), InlineKeyboardButton(text="🛒 Savatdan olish", callback_data="savat_olish_t")],
#     [InlineKeyboardButton(text="💸 Sotib olish", callback_data="sotib_ol"), InlineKeyboardButton(text="🔍 Menu", callback_data="menu")],
# ])
#
# mers_button = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="⬛️ Qora rangli Mers", callback_data="qora_mers"), InlineKeyboardButton(text="⬜️ Oq rangli Mers", callback_data="oq_mers"), InlineKeyboardButton(text="🟥 Qizil rangli Mers", callback_data="qizil_mers")],
#     [InlineKeyboardButton(text="🟨 Sariq rangli Mers", callback_data="sariq_mers"), InlineKeyboardButton(text="🟦 Moviy rangli Mers", callback_data="moviy_mers"), InlineKeyboardButton(text="🟩 Yashil rangli Mers", callback_data="yashil_mers")],
# ])
#
# mers_btn = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="🛒 Savatga solish", callback_data="savat_solish_m"), InlineKeyboardButton(text="🛒 Savatdan olish", callback_data="savat_olish_m")],
#     [InlineKeyboardButton(text="💸 Sotib olish", callback_data="sotib_ol"), InlineKeyboardButton(text="🔍 Menu", callback_data="menu")],
# ])
#
# lambo_button = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="⬛️ Qora rangli Lamborghini", callback_data="qora_lambo"), InlineKeyboardButton(text="⬜️ Oq rangli Lamborghini", callback_data="oq_lambo"), InlineKeyboardButton(text="🟥 Qizil rangli Lamborghini", callback_data="qizil_lambo")],
#     [InlineKeyboardButton(text="🟨 Sariq rangli Lamborghini", callback_data="sariq_lambo"), InlineKeyboardButton(text="🟦 Moviy rangli Lamborghini", callback_data="moviy_lambo"), InlineKeyboardButton(text="🟩 Yashil rangli Lamborghini", callback_data="yashil_lambo")],
# ])
#
# lambo_btn = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="🛒 Savatga solish", callback_data="savat_solish_l"), InlineKeyboardButton(text="🛒 Savatdan olish", callback_data="savat_olish_l")],
#     [InlineKeyboardButton(text="💸 Sotib olish", callback_data="sotib_ol"), InlineKeyboardButton(text="🔍 Menu", callback_data="menu")],
# ])
#
# ford_button = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="⬛️ Qora rangli Mustang", callback_data="qora_ford"), InlineKeyboardButton(text="⬜️ Oq rangli Mustang", callback_data="oq_ford"), InlineKeyboardButton(text="🟥 Qizil rangli Mustang", callback_data="qizil_ford")],
#     [InlineKeyboardButton(text="🟨 Sariq rangli Mustang", callback_data="sariq_ford"), InlineKeyboardButton(text="🟦 Moviy rangli Mustang", callback_data="moviy_ford"), InlineKeyboardButton(text="🟩 Yashil rangli Mustang", callback_data="yashil_ford")],
# ])
#
# ford_btn = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="🛒 Savatga solish", callback_data="savat_solish_f"), InlineKeyboardButton(text="🛒 Savatdan olish", callback_data="savat_olish_f")],
#     [InlineKeyboardButton(text="💸 Sotib olish", callback_data="sotib_ol"), InlineKeyboardButton(text="🔍 Menu", callback_data="menu")],
# ])
#
# kart_button = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="💳 Uzcard", callback_data="uzcard"), InlineKeyboardButton(text="💳 Humo", callback_data="humo")],
#     [InlineKeyboardButton(text="🔍 Menu", callback_data="menu")]
# ])
#
# balance = 500000
# orders = []
#
#
# @dp.message(filters.Command("start"))
# async def start(message: types.Message):
#     await message.answer(f"Xush kelibsiz {message.from_user.full_name}, sizga mashinalar yoqadimi ?", reply_markup=main_button)
#
#
# @dp.message(F.text == "🚙 Cars")
# async def cars_function(message: types.Message):
#     await message.answer("Xush kelibsiz !!!", reply_markup=ReplyKeyboardRemove())
#     await message.answer("Qaysi turdagi moshinani tanlisiz?", reply_markup=cars_button)
#
#
# @dp.message(F.text == "📲 My_info")
# async def info_function(message: types.Message):
#     await message.answer(f"\n \n Sizning ismingiz {message.from_user.full_name} \n Sizning user name {message.from_user.username} \n Sizning id ingiz {message.from_user.id} \n \n", reply_markup=main_button)
#
#
# @dp.callback_query(F.data == "menu")
# async def menu_function(call: types.CallbackQuery):
#     await call.message.answer("Siz Menu bo'limiga o'tdingiz", reply_markup=main_button)
#
#
# @dp.callback_query(F.data == "euro")
# async def cars_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://hips.hearstapps.com/hmg-prod/amv-prod-cad-assets/images/media/671589/2017-10best-cars-the-best-cars-for-sale-in-america-today-feature-car-and-driver-photo-672522-s-original.jpg?resize=640:*",
#                                     caption="Siz Euro mashinalar bo'limini tanladingiz !!!", reply_markup=euro_car_button)
#
# @dp.callback_query(F.data == "uzb")
# async def cars_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://daryo.uz/cache/2018/07/gm-680x453.jpg",
#                                     caption="Siz Uzbek mashinalar bo'limini tanladingiz !!!", reply_markup=uzb_car_button)
#
# @dp.callback_query(F.data == "bmw")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://www.carsome.my/news/wp-content/uploads/2023/07/BMW-M-Cars.jpg", caption="Siz BMW bo'limini tanladingiz. \n Bu yerdan siz o'zizga yoqqan ranglisini tanlay olasiz !!!", reply_markup=bmw_button)
#
#
# @dp.callback_query(F.data == "qora_bmw")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://cdn.kodixauto.ru/media/image/6100204caf109ce030c18fe6",
#                                     caption="Siz qora rangli BMWni tanladingiz. \n Mahsulot nomi: BMW \n Narxi: 40000 \n Rangi: qora \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n", reply_markup=bmw_btn)
#
#
# @dp.callback_query(F.data == "oq_bmw")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://quto.ru/imgs/2021/12/01/14/5067227/301b8c6e781b4dee30c4b9fd58ddb870abe7ca3a.jpeg",
#                                     caption="Siz oq rangli BMWni tanladingiz. \n Mahsulot nomi: BMW \n Narxi: 40000 \n Rangi: oq \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n", reply_markup=bmw_btn)
#
#
# @dp.callback_query(F.data == "qizil_bmw")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://avatars.mds.yandex.net/get-verba/1030388/2a0000018da1f30251e347a41305d485f160/cattouchretcr",
#                                     caption="Siz qizil rangli BMWni tanladingiz. \n Mahsulot nomi: BMW \n Narxi: 40000 \n Rangi: qizil \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n", reply_markup=bmw_btn)
#
#
# @dp.callback_query(F.data == "sariq_bmw")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://cdn.motor1.com/images/mgl/mr32B/s3/bmw-m4.jpg",
#                                     caption="Siz sariq rangli BMWni tanladingiz. \n Mahsulot nomi: BMW \n Narxi: 40000 \n Rangi: sariq \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n", reply_markup=bmw_btn)
#
#
# @dp.callback_query(F.data == "moviy_bmw")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://www.bmw-kz.com/content/dam/bmw/common/all-models/m-series/series-overview/bmw-m-series-seo-overview-ms-08.jpg",
#                                     caption="Siz movif rangli BMWni tanladingiz. \n Mahsulot nomi: BMW \n Narxi: 40000 \n Rangi: moviy \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n", reply_markup=bmw_btn)
#
#
# @dp.callback_query(F.data == "binafsha_bmw")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://carsdo.ru/job/CarsDo/photo/model/bmw-2-coupe-2-model.jpg",
#                                     caption="Siz binafsha rangli BMWni tanladingiz. \n Mahsulot nomi: BMW \n Narxi: 40000 \n Rangi: Binafsha \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n", reply_markup=bmw_btn)
#
#
# @dp.callback_query(F.data == "savat_solish_b")
# async def savat_function(call: types.CallbackQuery):
#     global balance
#     balance = balance - 40000
#     orders.append(" BMW narxi: 40000$")
#     await call.message.answer("Siz BMWni savat soldingiz", reply_markup=main_button)
#
#
# @dp.callback_query(F.data == "savat_olish_b")
# async def savat_function(call: types.CallbackQuery):
#     global balance
#     balance = balance + 40000
#     orders.remove(" BMW narxi: 40000$")
#     await call.message.answer("Siz BMWni savat oldingiz", reply_markup=main_button)
#
#
# @dp.callback_query(F.data == "porsche")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://newsroom.porsche.com/.imaging/mte/porsche-templating-theme/image_1290x726/dam/pnr/2021/Company/Porsche-achieves-robust-level-of-deliveries-in-2020-/Porsche-achieves-robust-level-of-deliveries-in-2020.jpeg0/jcr:content/Porsche%20achieves%20robust%20level%20of%20deliveries%20in%202020.jpeg",
#                                     caption="Siz Porsche bo'limini tanladingiz. \n Bu yerdan siz o'zizga yoqqan ranglisini tanlay olasiz !!!", reply_markup=porsh_button)
#
#
# @dp.callback_query(F.data == "qora_porsh")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://storage.googleapis.com/pod_public/750/183511.jpg",
#                                     caption="Siz qora rangli Porscheni tanladingiz. \n Mahsulot nomi: Porsche \n Narxi: 38000 \n Rangi: qora \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n", reply_markup=porsh_btn)
#
#
# @dp.callback_query(F.data == "oq_porsh")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://hips.hearstapps.com/hmg-prod/images/2025-porsche-taycan-118-660b044a263dd.jpg?crop=0.807xw:0.603xh;0.0732xw,0.324xh&resize=640:*",
#                                     caption="Siz oq rangli Porscheni tanladingiz. \n Mahsulot nomi: Porsche \n Narxi: 38000 \n Rangi: oq \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n", reply_markup=porsh_btn)
#
#
# @dp.callback_query(F.data == "qizil_porsh")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://newsroom.porsche.com/.imaging/mte/porsche-templating-theme/image_1290x726/dam/pnr/2022/Company/Porsche-deliveries-2021/The-all-electric-Porsche-Taycan-saw-an-outstanding-increase-with-41,296-units.jpeg/jcr:content/The%20all-electric%20Porsche%20Taycan%20saw%20an%20outstanding%20increase%20with%2041,296%20units.jpeg",
#                                     caption="Siz qizil rangli Porscheni tanladingiz. \n Mahsulot nomi: Porsche \n Narxi: 38000 \n Rangi: qizil \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n", reply_markup=porsh_btn)
#
#
# @dp.callback_query(F.data == "sariq_porsh")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://newsroom.porsche.com/.imaging/mte/porsche-templating-theme/image_1290x726/dam/AU_local/2022/Products_AU/911-GTS--Product-Highlights/911-GTS-Australian-images---exterior-static/PORSCHE_TAYCANGTS_911GTS_DKIMG_0920.jpg/jcr:content/PORSCHE_TAYCANGTS_911GTS_DKIMG_0920.jpg",
#                                     caption="Siz sariq rangli Porscheni tanladingiz. \n Mahsulot nomi: Porsche \n Narxi: 38000 \n Rangi: sariq \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n", reply_markup=porsh_btn)
#
#
# @dp.callback_query(F.data == "moviy_porsh")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://editorial.pxcrush.net/carsales/general/editorial/2023-porsche-718-boxster-style-edition-08.jpg",
#                                     caption="Siz movif rangli Porscheni tanladingiz. \n Mahsulot nomi: Porsche \n Narxi: 38000 \n Rangi: moviy \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n", reply_markup=porsh_btn)
#
#
# @dp.callback_query(F.data == "yashil_porsh")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://static.autox.com/uploads/2024/03/Porsche-911-Carrera-T.jpg",
#                                     caption="Siz yashil rangli Porscheni tanladingiz. \n Mahsulot nomi: Porsche \n Narxi: 38000 \n Rangi: Yashil \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n", reply_markup=porsh_btn)
#
#
# @dp.callback_query(F.data == "savat_solish_p")
# async def savat_function(call: types.CallbackQuery):
#     global balance
#     balance = balance - 38000
#     orders.append(" Porsche narxi: 38000$")
#     await call.message.answer("Siz Porscheni savat soldingiz", reply_markup=main_button)
#
#
# @dp.callback_query(F.data == "savat_olish_p")
# async def savat_function(call: types.CallbackQuery):
#     global balance
#     balance = balance + 38000
#     orders.remove(" Porsche narxi: 38000$")
#     await call.message.answer("Siz Porscheni savat oldingiz", reply_markup=main_button)
#
#
# @dp.callback_query(F.data == "tesla")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://electrek.co/wp-content/uploads/sites/3/2021/05/Tesla-Logo-Hero.jpg?quality=82&strip=all&w=1024",
#                                     caption="Siz Tesla bo'limini tanladingiz. \n Bu yerdan siz o'zizga yoqqan ranglisini tanlay olasiz !!!", reply_markup=tesla_button)
#
#
# @dp.callback_query(F.data == "qora_tesla")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://kapital.uz/wp-content/uploads/2021/08/5ea6dd8dec05c41134000004_large.jpg",
#                                     caption="Siz qora rangli Teslani tanladingiz. \n Mahsulot nomi: Tesla \n Narxi: 32000 \n Rangi: qora \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n", reply_markup=tesla_btn)
#
#
# @dp.callback_query(F.data == "oq_tesla")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://media.cnn.com/api/v1/images/stellar/prod/gettyimages-2113300644.jpg?c=16x9&q=h_833,w_1480,c_fill",
#                                     caption="Siz oq rangli Teslani tanladingiz. \n Mahsulot nomi: Tesla \n Narxi: 32000 \n Rangi: oq \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n", reply_markup=tesla_btn)
#
#
# @dp.callback_query(F.data == "qizil_tesla")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://car-images.bauersecure.com/wp-images/3033/021_tesla_model_3.jpg",
#                                     caption="Siz qizil rangli Teslani tanladingiz. \n Mahsulot nomi: Tesla \n Narxi: 32000 \n Rangi: qizil \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n", reply_markup=tesla_btn)
#
#
# @dp.callback_query(F.data == "sariq_tesla")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://s1.cdn.autoevolution.com/images/news/nyc-yellow-cab-fleet-now-includes-tesla-model-3-138684-7.jpg",
#                                     caption="Siz sariq rangli Teslani tanladingiz. \n Mahsulot nomi: Tesla \n Narxi: 32000 \n Rangi: sariq \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n", reply_markup=tesla_btn)
#
#
# @dp.callback_query(F.data == "moviy_tesla")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://d2hucwwplm5rxi.cloudfront.net/wp-content/uploads/2021/12/09084606/tesla-2020-129020210149.jpg",
#                                     caption="Siz movif rangli Teslani tanladingiz. \n Mahsulot nomi: Tesla \n Narxi: 32000 \n Rangi: moviy \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n", reply_markup=tesla_btn)
#
#
# @dp.callback_query(F.data == "tilla_tesla")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://masterpiecer-images.s3.yandex.net/95afff9999dd11eea07a5ece24738c58:upscaled",
#                                     caption="Siz tilla rangli Teslani tanladingiz. \n Mahsulot nomi: Tesla \n Narxi: 32000 \n Rangi: Tilla \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n", reply_markup=tesla_btn)
#
#
# @dp.callback_query(F.data == "savat_solish_t")
# async def savat_function(call: types.CallbackQuery):
#     global balance
#     balance = balance - 32000
#     orders.append(" Tesla narxi: 32000$")
#     await call.message.answer("Siz Teslani savat soldingiz", reply_markup=main_button)
#
#
# @dp.callback_query(F.data == "savat_olish_t")
# async def savat_function(call: types.CallbackQuery):
#     global balance
#     balance = balance + 32000
#     orders.remove(" Tesla narxi: 32000$")
#     await call.message.answer("Siz Teslani savat oldingiz", reply_markup=main_button)
#
#
# @dp.callback_query(F.data == "mers")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://gorliniya.ru/wp-content/uploads/2020/02/Avtosalon-Mersedes-Bents-.jpg",
#                                     caption="Siz Mers bo'limini tanladingiz. \n Bu yerdan siz o'zizga yoqqan ranglisini tanlay olasiz !!!", reply_markup=mers_button)
#
#
# @dp.callback_query(F.data == "qora_mers")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://repost.uz/storage/uploads/370-1656401821-avto-post-material.jpeg",
#                                     caption="Siz qora rangli Mersni tanladingiz. \n Mahsulot nomi: Tesla \n Narxi: 42000 \n Rangi: qora \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n", reply_markup=mers_btn)
#
#
# @dp.callback_query(F.data == "oq_mers")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://sales.mercedes-sheremetevo.ru/images/news/news_card_collage/crop_6277654.jpg",
#                                     caption="Siz oq rangli Mersni tanladingiz. \n Mahsulot nomi: Tesla \n Narxi: 42000 \n Rangi: oq \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n", reply_markup=mers_btn)
#
#
# @dp.callback_query(F.data == "qizil_mers")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://journalauto.com/wp-content/uploads/2023/12/Classe-E.jpg",
#                                     caption="Siz qizil rangli Mersni tanladingiz. \n Mahsulot nomi: Tesla \n Narxi: 42000 \n Rangi: qizil \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n", reply_markup=mers_btn)
#
#
# @dp.callback_query(F.data == "sariq_mers")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://carsdo.ru/job/CarsDo/photo/model/mercedes-benz-a-class-new-1-model.jpg",
#                                     caption="Siz sariq rangli Mersni tanladingiz. \n Mahsulot nomi: Tesla \n Narxi: 42000 \n Rangi: sariq \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n", reply_markup=mers_btn)
#
#
# @dp.callback_query(F.data == "moviy_mers")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://mercedes-benz-uzbekistan.uz/wp-content/uploads/2022/02/image.mq6_.12.20211027111239.webp",
#                                     caption="Siz movif rangli Mersni tanladingiz. \n Mahsulot nomi: Tesla \n Narxi: 42000 \n Rangi: moviy \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n", reply_markup=mers_btn)
#
#
# @dp.callback_query(F.data == "yashil_mers")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://cdn-1.motorsport.com/images/amp/6xEgEAr0/s1000/mercedes-amg-sl63-s-e-performa.jpg",
#                                     caption="Siz yashil rangli Mersni tanladingiz. \n Mahsulot nomi: Tesla \n Narxi: 42000 \n Rangi: Yashil \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n", reply_markup=mers_btn)
#
#
# @dp.callback_query(F.data == "savat_solish_m")
# async def savat_function(call: types.CallbackQuery):
#     global balance
#     balance = balance - 42000
#     orders.append(" Mers narxi: 42000$")
#     await call.message.answer("Siz Mersni savat soldingiz", reply_markup=main_button)
#
#
# @dp.callback_query(F.data == "savat_olish_m")
# async def savat_function(call: types.CallbackQuery):
#     global balance
#     balance = balance + 42000
#     orders.remove(" Mers narxi: 42000$")
#     await call.message.answer("Siz Mersni savat oldingiz", reply_markup=main_button)
#
#
# @dp.callback_query(F.data == "lambo")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://hips.hearstapps.com/hmg-prod/images/limitedlambos2-1618325640.jpg",
#                                     caption="Siz Lamborghini bo'limini tanladingiz. \n Bu yerdan siz o'zizga yoqqan ranglisini tanlay olasiz !!!", reply_markup=lambo_button)
#
#
# @dp.callback_query(F.data == "qora_lambo")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://media.cnn.com/api/v1/images/stellar/prod/191104152639-14-lamborghini-special.jpg?q=w_3077,h_1994,x_0,y_0,c_fill",
#                                     caption="Siz qora rangli Lamborghinini tanladingiz. \n Mahsulot nomi: TLamborghini \n Narxi: 40000 \n Rangi: qora \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n", reply_markup=lambo_btn)
#
#
# @dp.callback_query(F.data == "oq_lambo")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://cdn.motor1.com/images/mgl/OozxwY/0:1003:8000:5993/2024-lamborghini-aventador-successor-rendering.webp",
#                                     caption="Siz oq rangli Lamborghinini tanladingiz. \n Mahsulot nomi: TLamborghini \n Narxi: 40000 \n Rangi: oq \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n", reply_markup=lambo_btn)
#
#
# @dp.callback_query(F.data == "qizil_lambo")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://repost.uz/storage/uploads/0-1679466294-avto11-post-material.png",
#                                     caption="Siz qizil rangli Lamborghinini tanladingiz. \n Mahsulot nomi: TLamborghini \n Narxi: 40000 \n Rangi: qizil \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n", reply_markup=lambo_btn)
#
#
# @dp.callback_query(F.data == "sariq_lambo")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://hips.hearstapps.com/hmg-prod/images/2023-lamborghini-huracan-sterrato127-6467c8f12dcce.jpg?crop=0.595xw:0.445xh;0.174xw,0.447xh&resize=1200:*",
#                                     caption="Siz sariq rangliLamborghinisni tanladingiz. \n Mahsulot nomi: TLamborghini \n Narxi: 40000 \n Rangi: sariq \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n", reply_markup=lambo_btn)
#
#
# @dp.callback_query(F.data == "moviy_lambo")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://s3-prod-europe.autonews.com/s3fs-public/styles/1200x630/public/Lamborghini%20Huracan%20STO%20web.jpg",
#                                     caption="Siz movif rangli Lamborghinini tanladingiz. \n Mahsulot nomi: TLamborghini \n Narxi: 40000 \n Rangi: moviy \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n", reply_markup=lambo_btn)
#
#
# @dp.callback_query(F.data == "yashil_lambo")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://repost.uz/storage/uploads/0-1649788058-avto-post-material.jpeg",
#                                     caption="Siz yashil rangli Lamborghinini tanladingiz. \n Mahsulot nomi: TLamborghini \n Narxi: 40000 \n Rangi: Yashil \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n", reply_markup=lambo_btn)
#
#
# @dp.callback_query(F.data == "savat_solish_l")
# async def savat_function(call: types.CallbackQuery):
#     global balance
#     balance = balance - 40000
#     orders.append(" Lamborghini narxi: 40000$")
#     await call.message.answer("Siz Lamborghinini savat soldingiz", reply_markup=main_button)
#
#
# @dp.callback_query(F.data == "savat_olish_l")
# async def savat_function(call: types.CallbackQuery):
#     global balance
#     balance = balance + 40000
#     orders.remove(" Lamborghini narxi: 40000$")
#     await call.message.answer("Siz Lamborghinini savat oldingiz", reply_markup=main_button)
#
#
# @dp.callback_query(F.data == "ford")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://avatars.mds.yandex.net/get-vertis-journal/4080458/4.jpg_1649844806431/orig",
#                                     caption="Siz Mustang bo'limini tanladingiz. \n Bu yerdan siz o'zizga yoqqan ranglisini tanlay olasiz !!!", reply_markup=ford_button)
#
#
# @dp.callback_query(F.data == "qora_ford")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://cdn.dealeraccelerate.com/rkm/1/7040/447761/790x1024/1967-ford-mustang-eleanor-tribute",
#                                     caption="Siz qora rangli Mustangni tanladingiz. \n Mahsulot nomi: Mustang \n Narxi: 41000 \n Rangi: qora \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n", reply_markup=ford_btn)
#
#
# @dp.callback_query(F.data == "oq_ford")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://www.telegraph.co.uk/cars/images/2017/05/05/TELEMMGLPICT000127811726_1_trans_NvBQzQNjv4BqpVlberWd9EgFPZtcLiMQfyf2A9a6I9YchsjMeADBa08.jpeg?imwidth=680",
#                                     caption="Siz oq rangli Mustangni tanladingiz. \n Mahsulot nomi: Mustang \n Narxi: 41000 \n Rangi: oq \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n", reply_markup=ford_btn)
#
#
# @dp.callback_query(F.data == "qizil_ford")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://www.autobild.es/sites/navi.axelspringer.es/public/media/image/2019/04/roush-mustang-stage-3-2019.jpg",
#                                     caption="Siz qizil rangli Mustangni tanladingiz. \n Mahsulot nomi: Mustang \n Narxi: 41000 \n Rangi: qizil \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n", reply_markup=ford_btn)
#
#
# @dp.callback_query(F.data == "sariq_ford")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://mediacloud.carbuyer.co.uk/image/private/s--X-WVjvBW--/f_auto,t_content-image-full-desktop@1/v1646649059/carbuyer/2022/03/Ford%20Mustang%20California%20Special%20convertible-2.jpg",
#                                     caption="Siz sariq rangli Mustangni tanladingiz. \n Mahsulot nomi: Mustang \n Narxi: 41000 \n Rangi: sariq \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n", reply_markup=ford_btn)
#
#
# @dp.callback_query(F.data == "moviy_ford")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://claveyscorner.com/wp-content/uploads/2019/08/2019-Ford-Mustang-EcoBoost-Convertible-Three-Quarter-Front.jpg",
#                                     caption="Siz movif rangli Mustangni tanladingiz. \n Mahsulot nomi: Mustang \n Narxi: 41000 \n Rangi: moviy \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n", reply_markup=ford_btn)
#
#
# @dp.callback_query(F.data == "yashil_ford")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://assets-eu-01.kc-usercontent.com/3b3d460e-c5ae-0195-6b86-3ac7fb9d52db/0d0e8029-5c51-4dab-bd7c-df1932d90e4f/Ford%20Mustang%20%285%29.jpg?width=1750&fm=jpg&auto=format",
#                                     caption="Siz yashil rangli Mustangni tanladingiz. \n Mahsulot nomi: Mustang \n Narxi: 41000 \n Rangi: Yashil \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n", reply_markup=ford_btn)
#
#
# @dp.callback_query(F.data == "savat_solish_f")
# async def savat_function(call: types.CallbackQuery):
#     global balance
#     balance = balance - 41000
#     orders.append(" Mustang narxi: 41000$")
#     await call.message.answer("Siz Mustangni savat soldingiz", reply_markup=main_button)
#
#
# @dp.callback_query(F.data == "savat_olish_f")
# async def savat_function(call: types.CallbackQuery):
#     global balance
#     balance = balance + 41000
#     orders.remove(" Mustang narxi: 41000$")
#     await call.message.answer("Siz Mustangni savat oldingiz", reply_markup=main_button)
#
#
# # @dp.callback_query(F.data == "sotib_ol")
# # async def sotib_function(call: types.CallbackQuery):
# #     await call.message.answer("Siz sotib olish bo'limiga o'tdingiz. \n Siz to'lovni 2 usulda amalga oshira olasiz. \n 1-usul Uzcard kartasi orqali \n 2-usul Humo kartasi orqali", reply_markup=kart_button)
#
#
# @dp.callback_query(F.data == "matiz")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://masterpiecer-images.s3.yandex.net/e7c5d0a0854011ee9e561ad242dc1d78:upscaled",
#                                     caption="Siz Matiz bo'limini tanladingiz. \n Bu yerdan siz o'zizga yoqqan ranglisini tanlay olasiz !!!", reply_markup=matiz_button)
#
#
# @dp.callback_query(F.data == "qora_matiz")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://avangard29.com/media/posts/80/daewoo-matiz-2012-0001.jpg",
#                                     caption="Siz qora rangli Matizni tanladingiz. \n Mahsulot nomi: Matiz \n Narxi: 6000 \n Rangi: qora \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n", reply_markup=matiz_btn)
#
#
# @dp.callback_query(F.data == "oq_matiz")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://frankfurt.apollo.olxcdn.com/v1/files/mh2extxrmal42-UZ/image;s=1632x1088",
#                                     caption="Siz oq rangli Matizni tanladingiz. \n Mahsulot nomi: Matiz \n Narxi: 6000 \n Rangi: oq \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n", reply_markup=matiz_btn)
#
#
# @dp.callback_query(F.data == "qizil_matiz")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Daewoo_Matiz_front_20090920.jpg/1200px-Daewoo_Matiz_front_20090920.jpg",
#                                     caption="Siz qizil rangli Matizni tanladingiz. \n Mahsulot nomi: Matiz \n Narxi: 6000 \n Rangi: qizil \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n", reply_markup=matiz_btn)
#
#
# @dp.callback_query(F.data == "sariq_matiz")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://avatars.mds.yandex.net/get-verba/787013/2a000001609bd8dcc792cd4ee02367a24886/cattouch",
#                                     caption="Siz sariq rangli Matizni tanladingiz. \n Mahsulot nomi: Matiz \n Narxi: 6000 \n Rangi: sariq \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n", reply_markup=matiz_btn)
#
#
# @dp.callback_query(F.data == "moviy_matiz")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQUbHwsMNtZBvHMdgtb6OUKD_4iU0EqC4K1uGFSpIKRjtGbfWQZTfU2qfepV2GYVTE40nY&usqp=CAU",
#                                     caption="Siz movif rangli Matizni tanladingiz. \n Mahsulot nomi: Matiz \n Narxi: 6000 \n Rangi: moviy \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n", reply_markup=matiz_btn)
#
#
# @dp.callback_query(F.data == "yashil_matiz")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://storage.kun.uz/source/3/NvRMxGaa2aXAcIY-o87DDl9NUHrgGLp3.jpg",
#                                     caption="Siz yashil rangli Matizni tanladingiz. \n Mahsulot nomi: Matiz \n Narxi: 6000 \n Rangi: Yashil \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n", reply_markup=matiz_btn)
#
#
# @dp.callback_query(F.data == "savat_solish_mz")
# async def savat_function(call: types.CallbackQuery):
#     global balance
#     balance = balance - 6000
#     orders.append(" Matiz narxi: 6000$")
#     await call.message.answer("Siz Matizni savat soldingiz", reply_markup=main_button)
#
#
# @dp.callback_query(F.data == "savat_olish_mz")
# async def savat_function(call: types.CallbackQuery):
#     global balance
#     balance = balance + 6000
#     orders.remove(" Matiz narxi: 6000$")
#     await call.message.answer("Siz Matizni savat oldingiz", reply_markup=main_button)
#
#
# @dp.callback_query(F.data == "spark")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://www.autostrada.uz/wp-content/uploads/2018/09/Chevrolet-Spark-Tashkent.jpg",
#                                     caption="Siz Spark bo'limini tanladingiz. \n Bu yerdan siz o'zizga yoqqan ranglisini tanlay olasiz !!!", reply_markup=spark_button)
#
#
# @dp.callback_query(F.data == "qora_spark")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://car24.uz/wp-content/uploads/2024/01/4c78fd8c-654e-41b8-9c1a-5868d6af06c34-1.jpg",
#                                     caption="Siz qora rangli Sparkni tanladingiz. \n Mahsulot nomi: Spark \n Narxi: 8000 \n Rangi: qora \n Yili: 2021 \n Mahsulot sifati: A'lo \n \n", reply_markup=spark_btn)
#
#
# @dp.callback_query(F.data == "oq_spark")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://files.glotr.uz/company/000/013/254/products/2021/01/12/2021-01-12-20-38-08-737413-35b85a161b36adca0f6308234ffae3ab.jpg?_=ozbol",
#                                     caption="Siz oq rangli Sparkni tanladingiz. \n Mahsulot nomi: Spark \n Narxi: 6000 \n Rangi: oq \n Yili: 2021 \n Mahsulot sifati: A'lo \n \n", reply_markup=spark_btn)
#
#
# @dp.callback_query(F.data == "qizil_spark")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://lionmotors.uz/wp-content/uploads/2020/11/spark3.jpg",
#                                     caption="Siz qizil rangli Sparkni tanladingiz. \n Mahsulot nomi: Spark \n Narxi: 6000 \n Rangi: qizil \n Yili: 2021 \n Mahsulot sifati: A'lo \n \n", reply_markup=spark_btn)
#
#
# @dp.callback_query(F.data == "sariq_spark")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://www.kochamyauta.pl/wp-content/uploads/2013/10/sparky2-1.jpg",
#                                     caption="Siz sariq rangli Sparkni tanladingiz. \n Mahsulot nomi: Spark \n Narxi: 8000 \n Rangi: sariq \n Yili: 2021 \n Mahsulot sifati: A'lo \n \n", reply_markup=spark_btn)
#
#
# @dp.callback_query(F.data == "moviy_spark")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://files.glotr.uz/company/000/013/254/products/2021/01/12/2021-01-12-21-15-07-756714-81ffe7aeff28ef1c35b5fa281a817333.jpg?_=ozbol",
#                                     caption="Siz movif rangli Sparkni tanladingiz. \n Mahsulot nomi: Spark \n Narxi: 8000 \n Rangi: moviy \n Yili: 2021 \n Mahsulot sifati: A'lo \n \n", reply_markup=spark_btn)
#
#
# @dp.callback_query(F.data == "yashil_spark")
# async def bmw_function(call: types.CallbackQuery):
#     await call.message.answer_photo(photo="https://www.gazeta.uz/media/img/2010/05/1379_m.jpg",
#                                     caption="Siz yashil rangli Sparkni tanladingiz. \n Mahsulot nomi: Spark \n Narxi: 8000 \n Rangi: Yashil \n Yili: 2024 \n Mahsulot sifati: A'lo \n \n", reply_markup=spark_btn)
#
#
# @dp.callback_query(F.data == "savat_solish_sk")
# async def savat_function(call: types.CallbackQuery):
#     global balance
#     balance = balance - 8000
#     orders.append(" Spark narxi: 6000$")
#     await call.message.answer("Siz Sparkni savat soldingiz", reply_markup=main_button)
#
#
# @dp.callback_query(F.data == "savat_olish_sk")
# async def savat_function(call: types.CallbackQuery):
#     global balance
#     balance = balance + 8000
#     orders.remove(" Spark narxi: 6000$")
#     await call.message.answer("Siz Sparkni savat oldingiz", reply_markup=main_button)
#
#
#
# @dp.callback_query(F.data == "sotib_ol")
# async def sotib_function(call: types.CallbackQuery):
#     await call.message.answer("Siz sotib olish bo'limiga o'tdingiz. \n Siz to'lovni 2 usulda amalga oshira olasiz. \n 1-usul Uzcard kartasi orqali \n 2-usul Humo kartasi orqali", reply_markup=kart_button)
#
#
#
# @dp.callback_query(F.data == "uzcard")
# async def uzcard_function(call: types.CallbackQuery):
#     await call.message.answer("Siz to'lovni Uzcard kartasi orqali amalga oshirdingiz. \n To'lovingiz uchun rahmat \n Mahsulot yoqqan bo'lsa biz hursandmiz \n Yana bizdan foydalanishni unutmang. \n Boshiga qaytmoqchi bo'lsangiz Menu bo'limiga o'ting", reply_markup=main_button)
#
#
# @dp.callback_query(F.data == "humo")
# async def humo_function(call: types.CallbackQuery):
#     await call.message.answer("Siz to'lovni Humo kartasi orqali amalga oshirdingiz. \n To'lovingiz uchun rahmat \n Mahsulot yoqqan bo'lsa biz hursandmiz \n Yana bizdan foydalanishni unutmang. \n Boshiga qaytmoqchi bo'lsangiz Menu bo'limiga o'ting", reply_markup=main_button)
#
#
# @dp.message(F.text == "🛒 Orders")
# async def orders_function(message: types.Message):
#     await message.answer(f"Siz bor narsalar ro'yxati !!!")
#     for i in orders:
#         await message.answer(f"Moshina nomi: {i}", reply_markup=main_button)
#
#
# @dp.message(F.text == "💸 Balance")
# async def balance_function(message: types.Message):
#     await message.answer(f"Sizning qolgan mablag'ingiz: {balance}", reply_markup=main_button)
#
#
# async def main():
#     await dp.start_polling(bot)
#
#
# if __name__ == '__main__':
#     asyncio.run(main())
