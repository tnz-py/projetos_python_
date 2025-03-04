import json
import os
import platform
import socket
import getpass
import pwd
import subprocess
import uuid
import psutil

limpar = "cls" if os.name == "nt" else "clear"


def ver_info_pc():
    try:
        nome = socket.gethostname()
        ip_local = socket.gethostbyname(nome)

        mac = ':'.join(f'{(uuid.getnode() >> i) & 0xff:02x}' for i in range(0, 48, 8))
        
        memoria = psutil.virtual_memory()
        discos = psutil.disk_partitions()
        
        info_pc = {
            'Systema_operacional': platform.system(),
            'Versao_sistema': platform.release(),
            'Arquitetura_do_pc': platform.architecture(),
            'Tipo_de_sistema': platform.machine(),
            'Informacoes_processador': platform.processor(),
            'Nome_usuario': getpass.getuser(),
            'Informacoes_detalhadas_usuario': pwd.getpwuid(os.getuid()),
            'ID_usuario': os.getuid(),
            'Usuarios_logados_sistema': subprocess.getoutput("who"),
            'IP_local_usuario': ip_local,
            'Nome_do_usuario': socket.gethostname(),
            'Endereco_mac_decimal': uuid.getnode(),
            'Endereco_mac_normal': mac,
            'Memoria_total': memoria.total,
            'Memoria_usada': memoria.used,
            'Memoria_livre': memoria.free,
            'Memoria_percentual': memoria.percent,
        }

        try:

            arquivo_json = json.dumps(info_pc, indent=4)

            with open("info_pc_user", "w") as jsonobject:
                jsonobject.write(arquivo_json)

            with open("info_pc_user", "r") as jsonlerobjeto:
                arquivo_json = json.load(jsonlerobjeto)

            print(arquivo_json)

            input("Enter para voltar ao menu:")
            
        except FileNotFoundError as e:
            print(f"Error pelo motivo: {e}")

        except PermissionError as e:
            print(f"Error pelo motivo: {e}")

        except OSError as e:
            print(f"Error pelo motivo: {e}")

    except PermissionError as e:
        print(f"Error em: {e}")

    except TypeError as e:
        print(f"Error em {e}")

    except Exception as e:
        print(f"Error em: {e}")

def menu():
    try:
        while True:
            os.system(limpar)
            print("-="*17)
            print("----- Informações do computador -----")
            print("-="*17)
            print("Escolha uma opção:")
            print("1 - Ver informações do computador")
            print("2 - Sair")

            escolha_usuario = int(input("Digite a sua escolha, [1, 2]:"))

            if escolha_usuario == 1:
                ver_info_pc()
            elif escolha_usuario == 2:
                os.system(limpar)
                break
            else:
                print("Opção inválida! Tente novamente.")

    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

menu()
