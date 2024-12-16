## Higher vs Lower Game

Este é um jogo interativo onde o jogador deve comparar duas contas do Instagram e adivinhar qual delas possui mais seguidores. O objetivo é acertar o máximo de rodadas consecutivas, acumulando pontos enquanto compara as contas apresentadas.

### O que foi aprendido:
- **Geração de números aleatórios:** Uso da função `randint` para selecionar contas aleatórias de uma lista.
- **Manipulação de listas e dicionários:** Acessar e comparar informações de uma lista de dicionários que representa as contas do Instagram.
- **Controle de fluxo:** Estruturas condicionais (`if`, `elif`, `else`) para avaliar a escolha do jogador e loops `while` para manter o jogo em execução.
- **Validação de entrada do usuário:** Receber e validar a escolha entre 'A' ou 'B', garantindo uma experiência fluida.
- **Mensagens dinâmicas:** Feedback ao jogador com mensagens amigáveis e pontuação atualizada.

### O que o código faz:
1. **Exibição inicial:** O jogo começa exibindo um logo com arte ASCII.
2. **Seleção de contas:** Duas contas são escolhidas aleatoriamente de uma lista pré-definida.
3. **Comparação:** O jogador deve adivinhar qual conta possui mais seguidores.
4. **Pontuação:** Cada acerto aumenta a pontuação, e a conta com mais seguidores é mantida para a próxima rodada.
5. **Fim do jogo:** O jogo termina quando o jogador erra ou escolhe uma opção inválida, exibindo a pontuação final.

### Exemplo de execução:
```plaintext
Welcome to Higher vs Lower!
Compare A: Cristiano Ronaldo, a football player, from Portugal.
VS
Compare B: Taylor Swift, a Singer, from United States.

Who has more followers? Type 'A' or 'B': a

You're right! Current score: 1.

Compare A: Cristiano Ronaldo, a football player, from Portugal.
VS
Compare B: Selena Gomez, a singer/actress, from South Africa.

Who has more followers? Type 'A' or 'B': b

Sorry, that's wrong. Final score: 1
