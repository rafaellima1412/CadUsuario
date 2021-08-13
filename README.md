
# API RESTful de usuários + login

Criar aplicação que exponha uma API RESTful de criação de usuários com login.

A aplicação deve aceitar e responder apenas em JSON.

```json
    {"message": "Error message", "errorCode": 123}
```

## /signup

* Essa rota espera um usuário com os campos abaixo:
  * firstName [String]
  * lastName [String]
  * email [String]
  * password [String]
  * phones [List]
    * number [Number]
    * area_code [Number]
    * country_code [String]
* Segue abaixo um exemplo do formato:

```json
    {
        "firstName": "Hello",
        "lastName": "World",
        "email": "hello@world.com"
        "password": "hunter2",
        "phones": [
            {
                "number": 988887888,
                "area_code": 81,
                "country_code": "+55"
            }
        ]
    }
```

Obs: O id do usuário pode ser um sequencial gerado pelo banco ou um id único.

* Responder o código de status HTTP apropriado
* Em caso de sucesso você deve retornar:
  * `token`: token de acesso da API (JWT) com informações do usuário cadastrado;

* Em caso de erro:
  * E-mail existente [retornar um erro com a mensagem "E-mail already exists"];
  * Campos inválidos [retornar um erro com a mensagem "Invalid fields"];
  * Campos não preenchidos [retornar um erro com a mensagem "Missing fields"];

## /signin

* Essa rota espera um objeto com os campos abaixo:
  * email [String]
  * password [String]

* Em caso de sucesso você deve retornar:
  * `token`: token de acesso da API (JWT) com informaçÕes do usuário logado;
* Em caso de erro:
  * E-mail inexistente ou senha errada [retornar um erro com a mensagem "Invalid e-mail or password"];
  * Campos não preenchidos [retornar um erro com a mensagem "Missing fields"];

## /me

* Essa rota espera o token da api (via header):
  * Authorization [JWT Token]

* Em caso de sucesso você deve retornar:
  * `firstName`: Nome do usuário;
  * `lastName`: Sobrenome do usuário;
  * `email`: E-mail do usuário;
  * `phones`: Lista de telefones do usuário;
  * `created_at`: Data da criação do usuário;
  * `last_login`: Data da última vez que o usuário realizou login;
* Em caso de erro:
  * Token não enviado [retornar um erro com a mensagem "Unauthorized"];
  * Token expirado [retornar um erro com a mensagem "Unauthorized - invalid session"];

## Requisitos

* Framework Django.
* Banco de dados em memória, como SQLite.
* Persistência com Django ORM.
* Disponibilizar a API rodando em algum host (Heroku, AWS).
* Servidor deve estar embutido na aplicação (Gunicorn)
* Utiliziar no mínimo Python 3
* Testes unitários
* JWT como token
* Senha deve ser criptografada

### **Observações**

## 🚀 Começando para instalação local

\* Uma opção e clonar o projeto do github -->($git clone)[GitHub](https://github.com/rafaellima1412/desafio-python-django)

\* No terminal dentro da pasta

\* Instale as dependências

​    1)pip install -r requirements.txt

​    2)python manage.py runserver

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

### 🔧 Integração no Heroku

No heroku  o link do app: [AppHeroku](https://entrevistarafael.herokuapp.com)

**## ⚙️ Executando os testes na aplicação.**

Nesse projeto para rodar todos os testes ---> python manage.py test cadUsuarios

## 📦 Desenvolvimento

# ⚒️ Construído com

* [Phyton] - Linguagem programação.

* [djangoRestFramework] - framework backend.

* [Django] - O framework web usado.

# ⚒️ **Observações**

* os LInsk Me/Signup requerem autorização do Auth. Onde no link:<https://entrevistarafael.herokuapp.com/signin/>

  {
    "email": [
      "Este campo é obrigatório."
    ],
    "password": [
      "Este campo é obrigatório."
    ]
  }

  E gerado o token de acesso e refresh.

  * no link <https://entrevistarafael.herokuapp.com/me/> e solicitado o Auth Beare token, que libera o acesso ao app. Somento usuarios cadastrados no Admin (Auth) receberão o token de acesso.

* O signup estar dividido em usuario e telefone sendo o cadastro separadamente.

"signup/usuario": "https://entrevistarafael.herokuapp.com/signup/",
