# start_server_script_python

<p>Script para subir automaticamente os serviços de meu servidor.</p>
<p>Este script foi criado para resolver um problema recorrente. Sempre que eu precisava iniciar os
serviços em meu servidor (por alguma queda de energia ou manutenção programada), precisava conectar o 
teclado no servidor, que fica na sala, na estante da TV, logar no Ubuntu, abrir várias janelas e 
executar todos os comandos "na mão", demorando cerca de 5 minutos para subir todos os sistemas.</p>

<p>Atualmante, o script inicia automaticamente meus sistemas:</p>

<br>Sico: sistema MVC Java;</br>
<br>MyRH: microsserviço Java;</br>
<br>MyAccess V2: microsserviço Java;</br>
<br>Mycar: microsserviço Java;</br>
<br>Jenkins: CI/CD que gerencia grande parte das tarefas do servidor.</br>


## Ferramentas utilizadas

- Python 3.12
- Paramiko 3.5.0

## Preparação do ambiente
<p>Caso queira utilizar para iniciar seus microsserviços, abra o script e adapte as informações de seu servidor.</p>

<p>Após adaptar o script conforme sua necessidade, instale as dependências com o comando:</p>

````python
pip install -r requirements.txt
````

**Comando para rodar o script**:

````python
python start_server.py
````

## Links úteis.

- [Documentação oficial do Python)](https://www.python.org/)
- [Configurar o virtual env do projeto](https://docs.python.org/pt-br/3/library/venv.html)
