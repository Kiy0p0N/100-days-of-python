## Debugging em Python

Neste desafio, exploramos técnicas de **debugging** para identificar e corrigir erros em um programa Python. O foco foi entender como encontrar problemas e ajustar o código para que funcione conforme o esperado.

### O que foi aprendido:
- **Tipos de Erros Comuns:**
  - Erros de sintaxe, como falta de `:` ou parênteses.
  - Erros de lógica, como condições incorretas.
  - Erros de execução, como tentar acessar um índice inexistente de uma lista.
- **Uso de Ferramentas de Debugging:**
  - Uso de **breakpoints** para pausar a execução do código e inspecionar variáveis.
  - Uso de IDEs (como VSCode ou PyCharm) para depuração eficiente.
- **Métodos Manuais de Depuração:**
  - Adição de `print()` em pontos estratégicos do código para verificar o estado das variáveis.
  - Isolamento de trechos do código para testes individuais.
- **Leitura de Tracebacks:**
  - Interpretação de mensagens de erro fornecidas pelo Python para identificar a linha problemática.
- **Pensamento Crítico:**
  - A importância de entender o problema antes de tentar resolvê-lo.

### O que o código faz:
O programa utilizado para praticar debugging é um exemplo simples de **calculadora**. Ele realiza as operações básicas de soma, subtração, multiplicação e divisão, mas contém alguns erros que precisam ser corrigidos.

1. **Recebendo entradas:** O programa solicita ao usuário dois números e a operação desejada.
2. **Realizando cálculos:** Processa os números com base na operação selecionada.
3. **Corrigindo erros:** Foram encontrados e corrigidos problemas como:
   - Divisão por zero.
   - Validação de entradas não numéricas.
   - Operações inválidas ou desconhecidas.

### Exemplo de execução:
```plaintext
Bem-vindo à Calculadora!
Digite o primeiro número: 10
Digite o segundo número: 0
Escolha uma operação (+, -, *, /): /

Erro: Não é possível dividir por zero.
