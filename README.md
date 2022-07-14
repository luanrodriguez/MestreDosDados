# MestreDosDados

- Python 3.10.1

Para executar o bot, é necessário criar um ambiente virtual para instalação das dependências.

- pip install virtualenv
- virtualenv venv

Após isso, é preciso ativar o ambiente virtual.

Windows:

- .\venv\Scripts\activate

Linux:

- source venv/bin/activate

Com o ambiente ativo é possível instalar as dependências somente nesse projeto, com o seguinte comando.

-pip install -r requirements.txt

---

Para executar o bot é necessário colocar o token como parametro da função "bot.run()" no arquivo "run_bot.py" ou adicionar o token a uma variável de ambiente em sua máquina. Após adicionar o token, basta executar o arquivo "run_bot.py".

- python run_bot.py

Esse projeto conta com testes unitários, presentes na pasta "tests", para executá-los basta digitar pytest no terminal.

- pytest
