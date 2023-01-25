import pyautogui as bot

email = bot.prompt(text="Digite seu email", title="E-mail")
senha = bot.password(text="Digite sua senha", title="Senha", mask="*")

bot.hotkey('win', 'r')
bot.typewrite("notepad")
bot.press('enter')
bot.sleep(2)
bot.typewrite(email)
bot.press('enter')
bot.typewrite(senha)