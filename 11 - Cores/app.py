# quais são os passos manuais que devo transformar em código
import pyautogui
from time import sleep

pyautogui.click(1472, 374, duration=1)

# Retorna as coord da cor buscada
if pyautogui.pixelMatchesColor(1364, 310, (0, 0, 0)):
    pass