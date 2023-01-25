import pyautogui as bot

bot.alert(text="E ai meu nobre", title="Test", button="OK")

#input
email = bot.prompt(text="Digite seu e-mail", title= "Informacao")

#Confirmar se algo deve ou nao acontecer

resposta = bot.confirm(text="Continuar rodando a automacao", title="Aviso", buttons=["OK","CANCELAR"])

if resposta == "OK":
    print("Continuando")
else:
    print("Fechando")

bot.password(text="Digite sua senha", title="Aviso", mask="*")