import webbrowser
import pyautogui as bot

#Abrir site
webbrowser.open("https://cursoautomacao.netlify.app/")

#Scroll Pagina
bot.sleep(1)
bot.click(893,188)
bot.scroll(-150)


#Digitar nome e aperta em alert
bot.click(1412,953, duration=1)
bot.typewrite("SAMUEL")
bot.click(1435,995, duration=0.5)

# Fecha alerta
bot.press('enter')

#Suba para cima
bot.scroll(150)

"""
Desça apenas o suficiente para conseguir chegar até a secção que contém os arquivos para o quais irá fazer o
download e click no botão de download para realizar o downlaod dos arquivos excel e pdf.
"""

bot.scroll(-1000)

bot.click(417,831, clicks=2)
for i in range(2):
    bot.move(200,0, duration=0.5)
    bot.click(clicks=2)

bot.move(200,50)
bot.click(clicks=2)
bot.move(200,-50)
bot.click(clicks=2)
bot.move(200,50)
bot.click(clicks=2)
bot.confirm(text="Automacao finalizada", title="AUTOMACAO", buttons=["OK"])
