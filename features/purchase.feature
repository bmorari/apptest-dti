Feature: Compra de produtos
  Scenario: Usuário realiza uma compra com sucesso
    Given que o usuário está logado no aplicativo
    When ele adiciona um produto ao carrinho
    Then o pedido é finalizado com sucesso