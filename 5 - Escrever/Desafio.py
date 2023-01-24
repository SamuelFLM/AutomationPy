import pyautogui as bot


bot.hotkey("win", "r")
bot.typewrite("notepad")
bot.press('enter')
bot.click(334,237, duration=0.2)
bot.typewrite("Automacao e incrivel")