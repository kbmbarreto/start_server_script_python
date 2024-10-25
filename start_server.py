import paramiko
import time


def start_services(server_ip, username, password):
    commands = [
        "source ~/.bashrc && cd Documents/sistemas/sico && nohup java -jar sico-1.0.1.jar &",
        "source ~/.bashrc && cd Documents/sistemas/myrh && nohup java -jar myrh-1.0.0.jar &",
        "source ~/.bashrc && cd Documents/sistemas/myaccessv2 && nohup java -jar myaccess-java-1.0.0.jar &",
        "source ~/.bashrc && cd Documents/sistemas/mycar && nohup java -jar mycar-1.0.0.jar &",
        "source ~/.bashrc && cd /opt && nohup java -jar jenkins &"
    ]

    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(server_ip, username=username, password=password)

        shell = ssh.invoke_shell()

        for command in commands:
            print(f"Executando: {command}")
            shell.send(command + "\n")
            time.sleep(2)

            output = shell.recv(65535).decode('utf-8')
            print(output)

        shell.close()
        ssh.close()
        print("Todos os serviços foram iniciados com sucesso.")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")


if __name__ == "__main__":
    server_ip = "{IP_DO_SERVIDOR}"
    username = "{USUARIO_SSH}"
    password = "{SENHA_SSH}"

    start_services(server_ip, username, password)
