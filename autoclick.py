import pyautogui
import time
import keyboard

# Define as coordenadas do local onde deseja clicar
x, y = 500, 500

# Loop infinito
while True:
    # Move o cursor para as coordenadas especificadas e clica
    pyautogui.click(x, y)

    # Aguarda um pequeno intervalo antes de clicar novamente (evitar detecção)
    time.sleep(1)

    #parar o programa
    if keyboard.is_pressed('y'):
        break
