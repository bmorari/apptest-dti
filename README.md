## 🚧 Limitações

Infelizmente, devido a limitações de hardware, não consegui executar o emulador Android, pois meu computador não suporta. Tive a ideia de criar a estrutura de como teria feito e alguns códigos um pouco mais genéricos que demonstram o raciocínio.

Obrigado pela oportunidade de participar deste desafio e caso queiram conversar a respeito fico totalmente disponível.

## 🚀 Tecnologias Utilizadas

Linguagem: Python

Framework de Testes: Appium

Gerenciador de Pacotes: pip

IDE: VS Code

BDD: Gherkin

## 🗂️ Estrutura de Pastas

 ```bash
apptest-dti/
├── features/
│   ├── login.feature
│   ├── purchase.feature
│   └── sort_products.feature
├── steps/
│   ├── login_steps.py
│   ├── purchase_steps.py
│   └── sort_products_steps.py
├── tests/
│   └── test_runner.py
├── utils/
│   └── capabilities.py
├── requirements.txt
└── README.md
 ```

## ✍️ Cenários de Teste (BDD)

### 1. Realizar uma Compra no App
```bash
Feature: Compra de produtos
  Scenario: Usuário realiza uma compra com sucesso
    Given que o usuário está logado no aplicativo
    When ele adiciona um produto ao carrinho
    Then o pedido é finalizado com sucesso
```

### 2. Login Inválido
```bash
Feature: Login de usuário
  Scenario: Tentativa de login com credenciais inválidas
    Given que o usuário está na tela de login
    When ele insere credenciais inválidas
    Then uma mensagem de erro é exibida
 ```

### 3. Ordenação de Produtos do Mais Barato para o Mais Caro
```bash
Feature: Ordenação de produtos
  Scenario: Ordenar produtos do mais barato para o mais caro
    Given que o usuário está na lista de produtos
    When ele seleciona a opção de ordenação do mais barato para o mais caro
    Then os produtos são exibidos na ordem correta
```

## 📦 Como Rodar o Projeto

### 1. Clone o repositório:
```bash
git clone https://github.com/bmorari/apptest-dti.git
cd apptest-dti
```

### 2. Instale as dependências:
```bash
pip install -r requirements.txt
```

### 3. Execute os testes:
```bash
pytest tests
```

