import pyautogui as bot
import pyperclip


#Pyperclip - faz utilizacao de caracteres especiais.
def escrever_frase(frase):
    pyperclip.copy(frase)
    bot.hotkey('ctrl','v')

bot.click(x=-1165,y=982, clicks=1, duration=0)
escrever_frase("O'la , bom dia!")
bot.click(x=-215,y=977, clicks=1, duration=0)