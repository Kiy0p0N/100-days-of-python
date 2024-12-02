## Programa de Leilão Secreto

Este programa permite que vários participantes façam lances secretos e, ao final, o vencedor é determinado com base no maior lance feito.

### O que foi aprendido:
- **Manipulação de dicionários**: O uso de um dicionário para armazenar os lances de cada participante e suas respectivas ofertas.
- **Entrada de usuário**: Receber o nome e o valor do lance de cada participante.
- **Estruturas de controle**: Utilização de loops e condições para permitir que os participantes façam lances, com a possibilidade de adicionar novos lances ou terminar o leilão.
- **Funções**: Criação de uma função para comparar os lances e determinar o vencedor.

### Como funciona o código:
1. **Entrada de dados**:
   - O programa solicita o nome e o lance de cada participante.
   - O nome e o valor do lance são armazenados em um dicionário `bidding_dictionary`.
2. **Continuação ou término do leilão**:
   - Após cada lance, o programa pergunta se há mais lances. Se a resposta for "sim", o programa limpa a tela e permite novos lances.
   - Caso contrário, o programa termina o leilão e chama a função `compare_bid` para determinar o vencedor.
3. **Comparação de lances**:
   - A função `compare_bid` percorre o dicionário para encontrar o maior lance e imprime o vencedor e o valor do seu lance.

### Exemplo de execução:
```plaintext
Welcome to the secret auction program
What is your name? Alice
What is your bid? $100
Are there any other bidders? Type "yes" or "no". yes

What is your name? Bob
What is your bid? $200
Are there any other bidders? Type "yes" or "no". no

The winner is Bob with a bid of $200.
