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

---

Com o bot em execução e adicionado em um servidor, basta digitar !dado (numero entre 1 e 10001) para que um número pseudoaleatório seja mostrado, como no exemplo abaixo:

![image](https://user-images.githubusercontent.com/83316964/179639464-ab575e8c-3c56-4c8f-bae5-b36e05a5369a.png)

No entanto, os emotes utilizados por padrão no bot estão presentes somente no servidor do exemplo acima. Para alterar os emotes que serão utilizados, basta entrar no código do bot, ir na pasta "commands/dados" e alterar as variaveis presentes no arquivo "emotes_and_gifs_settings.py". A URL a seguir conta com explicações sobre o funcionamento de emotes personalizados no Discord: https://gist.github.com/scragly/b8d20aece2d058c8c601b44a689a47a0.

![image](https://user-images.githubusercontent.com/83316964/179639874-28efd523-9d3f-4c05-9878-e6b248378a75.png)

Quando o dado "cai" no número máximo escolhido, o emote dos números serão diferentes e um gif engraçado/feliz será enviado junto. A mesma coisa ocorre quando o dado "cai" no número 1. Esses gifs e emotes também podem ser alterados no arquivo de configurações.

![image](https://user-images.githubusercontent.com/83316964/179640042-59e2fc4a-dea3-4bfc-a0cd-10fb34ea09d2.png)
![image](https://user-images.githubusercontent.com/83316964/179640127-4c4cb54e-c5cd-4e01-acba-715bbbed77b4.png)


