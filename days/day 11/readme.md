## Jogo de Blackjack

Este é um jogo de **Blackjack**, onde o jogador compete contra o computador para obter o máximo de pontos possível, sem ultrapassar 21. O jogo utiliza cartas numeradas de 2 a 10, com as figuras (J, Q, K) representadas como 10 pontos, e o Ás representando 1 ou 11, dependendo da situação.

### O que foi aprendido:
- **Uso de listas e manipulação de dados:** O código utiliza listas para armazenar as cartas do jogador e do computador, além de manipular essas listas para calcular a pontuação de cada participante.
- **Controle de fluxo e tomadas de decisão:** Utiliza loops `while` e condicionais para gerenciar o andamento do jogo, controlando quando o jogador pode tirar mais cartas e quando o jogo termina.
- **Interação com o usuário:** O jogador pode escolher, por meio de comandos de entrada, se deseja continuar tirando cartas ou passar, afetando o fluxo do jogo.
- **Cálculo de pontuação:** O código implementa a lógica do Blackjack para calcular a pontuação com base nas cartas do jogador e do computador.
- **Simulação de jogo de cartas:** A escolha aleatória de cartas é feita através da função `random.choice()`, simulando o sorteio de cartas.

### O que o código faz:
1. **Distribuição das cartas:** O jogador e o computador começam com duas cartas cada, escolhidas aleatoriamente da lista de cartas disponíveis.
2. **Exibição das cartas:** O código exibe as cartas do jogador e a primeira carta do computador.
3. **Entrada do jogador:** O jogador pode optar por continuar pegando cartas ou parar, digitando 'y' ou 'n'. O jogo é controlado por esse input.
4. **Regras de pontuação:** Se o jogador ou o computador tiver 21 pontos (ou um "Blackjack"), o jogo termina imediatamente.
5. **Cartas adicionais para o computador:** O computador pega cartas até atingir uma pontuação mínima de 17 pontos.
6. **Resultado do jogo:** O vencedor é decidido com base na pontuação final de ambos os jogadores, com o objetivo de ter a maior pontuação sem ultrapassar 21.

### Exemplo de execução:
```plaintext
Do you want to play a game of Blackjack? Type 'y' or 'n': y
______________________________
    Welcome to Blackjack!

    Your cards: [10, 7] current score: 17
    Computer's first card: 3
Type 'y' to get another card, type 'n' to pass: n

    Your final hand: [10, 7], final score: 17
    Computer's final hand: [3, 10, 5], final score: 18
You lose
