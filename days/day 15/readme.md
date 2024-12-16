# Máquina de Café Interativa ☕️

Este é um programa que simula o funcionamento básico de uma máquina de café, permitindo ao usuário escolher entre três tipos de bebida: **espresso**, **latte** e **cappuccino**. O programa gerencia recursos, calcula transações e fornece relatórios.

## O que foi aprendido:
- **Estruturas de dados:** Uso de dicionários aninhados para armazenar informações sobre o menu e recursos disponíveis.
- **Funções e modularidade:** Criação de funções para processar moedas, verificar recursos, validar transações e preparar bebidas.
- **Controle de fluxo:** Uso de loops `while` e estruturas condicionais para interações contínuas com o usuário.
- **Manipulação de entrada do usuário:** Validação de opções e processamento dinâmico de valores inseridos.
- **Gerenciamento de estado:** Controle de recursos disponíveis e dinheiro acumulado na máquina.

## O que o código faz:
1. **Exibição inicial:** O programa solicita ao usuário que escolha entre `espresso`, `latte` ou `cappuccino`, ou que insira um comando especial (`report` ou `off`).
2. **Verificação de recursos:** Antes de preparar a bebida, o programa verifica se há ingredientes suficientes.
3. **Processamento de moedas:** Calcula o valor inserido pelo usuário e valida se é suficiente para a bebida escolhida.
4. **Preparo da bebida:** Deduz os ingredientes usados dos recursos disponíveis e entrega a bebida ao usuário.
5. **Relatório:** Mostra os recursos restantes e o total de dinheiro acumulado quando solicitado.
6. **Desligamento:** O programa é encerrado ao receber o comando `off`.

## Exemplo de execução:
```plaintext
What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
How many quarters? 10
How many dimes? 0
How many nickels? 0
How many pennies? 0
Here is 7.5 dollars in change.
Here is your latte. Enjoy!

What would you like? (espresso/latte/cappuccino): report
Water: 100ml 
Milk: 50ml 
Coffee: 76g 
Money: $2.5

What would you like? (espresso/latte/cappuccino): off
