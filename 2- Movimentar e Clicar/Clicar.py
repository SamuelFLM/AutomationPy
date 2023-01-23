import pyautogui as bot

#Clique personalizado
bot.click(x=-1068, y=719, clicks=1000, interval=0.1, button="left", duration=0)

#Clique na posicao atual(botao esquerdo)
bot.click()
bot.click(button="left")
bot.click(button="right")
bot.click(button="middle")

#Clicar X vezes
bot.click(clicks=10)

#Fucao prontas para clicks
bot.doubleClick()
bot.rightClick()
bot.middleClick()
bot.tripleClick()