## Jogo de Adivinhação de Números

Este é um jogo simples onde o jogador deve adivinhar um número aleatório gerado pelo computador, dentro de um intervalo de 1 a 100. O jogador tem um número limitado de tentativas, dependendo do nível de dificuldade escolhido, para acertar o número. O jogo oferece feedback sobre se a tentativa do jogador foi "muito alta" ou "muito baixa" até que o número correto seja adivinhado ou as tentativas se esgotem.

### O que foi aprendido:
- **Geração de números aleatórios:** Utilização da função `randint` para gerar números aleatórios dentro de um intervalo especificado.
- **Função de checagem de respostas:** Criação de uma função `check_answer` para comparar a tentativa do jogador com o número real, fornecendo dicas como "muito alto" ou "muito baixo".
- **Controle de fluxo:** Uso de estruturas condicionais (`if`, `else`) e loops (`while`) para manter o jogo em andamento até que o jogador vença ou perca.
- **Entrada do usuário e validação:** O código permite ao jogador escolher um nível de dificuldade, que determina o número de tentativas, e também recebe e valida as entradas do jogador.
- **Exibição de mensagens:** Utilização de mensagens amigáveis para interagir com o jogador, informando sobre o status do jogo e o número de tentativas restantes.

### O que o código faz:
1. **Configuração inicial:** O código começa com a exibição de um logo do jogo e uma introdução para o jogador.
2. **Escolha da dificuldade:** O jogador escolhe entre dois níveis de dificuldade, "fácil" (10 tentativas) ou "difícil" (5 tentativas).
3. **Geração de número aleatório:** O computador escolhe um número aleatório entre 1 e 100.
4. **Entrada de tentativas:** O jogador faz uma tentativa de adivinhar o número. Se o palpite estiver errado, o número de tentativas restantes diminui.
5. **Feedback sobre o palpite:** O código informa ao jogador se o palpite foi muito alto ou muito baixo. Se o palpite estiver correto, o jogo termina.
6. **Fim do jogo:** O jogo termina quando o jogador acerta o número ou quando as tentativas acabam. Se o jogador ficar sem tentativas, uma mensagem é exibida informando que o jogo acabou.

### Exemplo de execução:
```plaintext
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.

Choose a difficulty. Type 'easy' or 'hard': easy

You have 10 attempts remaining to guess the number.
Make a guess: 50
Too high.

You have 9 attempts remaining to guess the number.
Make a guess: 25
Too low.

You have 8 attempts remaining to guess the number.
Make a guess: 35
You got it! The answer was 35.
