# Máquina de Café Orientada a Objetos ☕️

Este projeto recria uma máquina de café interativa, utilizando **Programação Orientada a Objetos (POO)** para organizar funcionalidades em classes pré-definidas. A máquina permite que o usuário escolha entre opções de bebidas, gerencie recursos e processe pagamentos.

## O que foi aprendido:
- **Estruturas de classes:** Organização de funcionalidades em classes específicas como `Menu`, `CoffeeMaker` e `MoneyMachine`.
- **Interação entre classes:** Implementação de métodos que utilizam atributos e funcionalidades de múltiplas classes para atingir um objetivo comum.
- **Boas práticas em POO:** Encapsulamento de lógica em métodos e abstração de detalhes no fluxo principal.
- **Controle de fluxo e validação:** Uso de condicionais e loops para interagir com o usuário e validar operações.

## Estrutura das classes utilizadas:
- **`Menu`:** Gerencia os itens disponíveis e fornece métodos para exibição e seleção de bebidas.
- **`CoffeeMaker`:** Verifica e gerencia os recursos necessários para preparar bebidas.
- **`MoneyMachine`:** Processa pagamentos e mantém o controle de dinheiro acumulado.

## O que o código faz:
1. **Exibição do menu:** Lista as opções de bebidas disponíveis para o usuário.
2. **Relatórios:** Gera relatórios sobre os recursos disponíveis (água, leite, café) e o total de dinheiro acumulado.
3. **Verificação de recursos:** Valida se há ingredientes suficientes para preparar a bebida solicitada.
4. **Processamento de pagamentos:** Calcula e valida o pagamento do usuário.
5. **Preparo da bebida:** Deduz os ingredientes necessários dos recursos e serve a bebida.

## Exemplo de execução:
```plaintext
What would you like? espresso/latte/cappuccino: latte
Please insert coins.
How many quarters? 10
How many dimes? 0
How many nickels? 0
How many pennies? 0
Here is $7.5 dollars in change.
Here is your latte. Enjoy!

What would you like? espresso/latte/cappuccino: report
Water: 200ml
Milk: 150ml
Coffee: 24g
Money: $2.5

What would you like? espresso/latte/cappuccino: off
