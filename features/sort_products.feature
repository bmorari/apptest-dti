Feature: Ordenação de produtos
  Scenario: Ordenar produtos do mais barato para o mais caro
    Given que o usuário está na lista de produtos
    When ele seleciona a opção de ordenação do mais barato para o mais caro
    Then os produtos são exibidos na ordem correta