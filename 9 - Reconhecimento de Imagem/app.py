import pyautogui as bot

# # Encontrar as coord proximas de onde aquela imagem esta
print(bot.locateOnScreen('9 - Reconhecimento de Imagem//4.png'))

# # Encontar a coordenada do centro de uma imagem
print(bot.locateCenterOnScreen('9 - Reconhecimento de Imagem//4.png'))
bot.click(x=1273, y=539, clicks=2, duration=0.5)
bot.click(x=1509, y=487, clicks=1, duration=0.5)
bot.click(x=1351, y=539, clicks=2, duration=0.5)
bot.click(x=1507, y=645, clicks=1, duration=0.5)

