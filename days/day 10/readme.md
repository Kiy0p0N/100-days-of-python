## Calculadora Interativa

Este programa é uma calculadora simples que permite realizar várias operações matemáticas, com a possibilidade de continuar os cálculos a partir do resultado anterior, começar um novo cálculo ou encerrar a sessão a qualquer momento.

### O que foi aprendido:
- **Funções**: Como criar funções para realizar operações matemáticas (adição, subtração, multiplicação, divisão).
- **Dicionários**: Utilização de um dicionário para associar operações matemáticas a funções.
- **Entrada e saída do usuário**: Como receber entradas do usuário para escolher operações e fornecer resultados.
- **Recursão**: O programa permite continuar o cálculo com o resultado anterior ou reiniciar o cálculo, utilizando recursão para repetir o processo.
- **Controle de fluxo**: O programa usa condicionais para permitir que o usuário decida se deseja continuar calculando, reiniciar ou finalizar a sessão.

### Como funciona o código:
1. **Funções de operações**:
   - A calculadora possui funções para **adicionar**, **subtrair**, **multiplicar** e **dividir** dois números.
   - Cada operação é selecionada pelo usuário ao digitar o símbolo correspondente.
   
2. **Entrada de números**:
   - O usuário é solicitado a fornecer dois números para realizar a operação. Após o primeiro número ser informado, o usuário escolhe a operação e o segundo número.
   
3. **Processamento da operação**:
   - A operação escolhida é executada e o resultado é mostrado.
   - O programa pergunta se o usuário quer continuar calculando, reiniciar ou encerrar a sessão.

4. **Opções de continuidade**:
   - Se o usuário deseja continuar, o resultado da operação é utilizado como o primeiro número para o próximo cálculo.
   - Se o usuário deseja reiniciar, o processo começa novamente com um novo cálculo.
   - Se o usuário deseja parar, o programa encerra a sessão.

### Exemplo de execução:

```plaintext
Welcome to the Calculator

Enter the first number: 5
Choose the operation:
+
-
*
/
+
Enter the second number: 3
5.0 + 3.0 = 8.0
Type "y" to continue calculating with 8.0, "n" to start a new calculation, or "s" to stop the session: y

Enter the second number: 2
8.0 + 2.0 = 10.0
Type "y" to continue calculating with 10.0, "n" to start a new calculation, or "s" to stop the session: n

Enter the first number: 10
Choose the operation:
+
-
*
/
-
Enter the second number: 4
10.0 - 4.0 = 6.0
Type "y" to continue calculating with 6.0, "n" to start a new calculation, or "s" to stop the session: s
