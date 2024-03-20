Este é um simples script em Python que automatiza cliques em uma posição específica da tela.
Ele utiliza a biblioteca pyautogui para controlar o cursor do mouse e realizar os cliques, e keyboard para permitir a interrupção do programa.

Requisitos
Python 3.x

Bibliotecas Python: pyautogui, keyboard

Uso
Certifique-se de ter o Python instalado em sua máquina.
Instale as bibliotecas necessárias executando o comando pip install pyautogui keyboard.
Execute o script auto_click.py.
Posicione o cursor do mouse onde deseja que os cliques sejam realizados.
O script começará a clicar na posição especificada automaticamente.
Para interromper o programa, pressione a tecla 'y'.

Detalhes dos Scripts
auto_click.py: Este script automatiza cliques em uma posição específica da tela. Ele entra em um loop infinito,
clicando na posição especificada e aguardando um intervalo de tempo antes de clicar novamente. O programa pode ser interrompido pressionando a tecla 'y'.

x_y.py: Este script imprime as coordenadas (x, y) atuais do cursor do mouse após um breve intervalo de tempo.
Ele serve como uma ferramenta para identificar as coordenadas desejadas para o script auto_click.py.
