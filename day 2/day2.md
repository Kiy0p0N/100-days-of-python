## Calculadora de Gorjetas

Este projeto contém um script em Python que calcula o valor individual que cada pessoa deve pagar em uma conta compartilhada, incluindo a gorjeta.

### O que foi aprendido:
- **Uso de condicionais (`if`, `else`) em um loop `while`:** Garantir que a entrada do usuário seja válida.
- **Operações matemáticas básicas em Python:** Calcular o valor da gorjeta e dividir o total entre os participantes.
- **Formatação de números (`f-strings`):** Exibir resultados financeiros com duas casas decimais.
- **Uso de entrada do usuário (`input()`):** Capturar informações como total da conta, porcentagem da gorjeta e número de participantes.

### O que o código faz:
1. **Exibe uma mensagem de boas-vindas.**
2. **Recebe as seguintes entradas do usuário:**
   - Total da conta (`total`).
   - Porcentagem de gorjeta (10%, 12% ou 15%), validada dentro de um loop `while`.
   - Número de pessoas para dividir a conta.
3. **Calcula:**
   - O total com a gorjeta incluída.
   - O valor individual que cada pessoa deve pagar.
4. **Exibe o resultado formatado no console.**

### Exemplo de execução:
```plaintext
Welcome to the tip calculator!
What was the total bill? $100
How much tip would you like to give, 10, 12 or 15? 12
How many people to split to bill? 4
Each person should pay: $28.00
