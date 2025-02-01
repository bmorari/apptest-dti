Feature: Login de usuário
  Scenario: Tentativa de login com credenciais inválidas
    Given que o usuário está na tela de login
    When ele insere credenciais inválidas
    Then uma mensagem de erro é exibida