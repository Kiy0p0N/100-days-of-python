## Jogo da Forca

Este é um jogo simples de forca, onde o jogador deve adivinhar uma palavra secreta, uma letra por vez, antes que suas vidas acabem. O código usa uma lista de palavras e um conjunto de imagens do "homem da forca" para ilustrar o progresso do jogo.

### O que foi aprendido:
- **Uso de listas para armazenar palavras e letras:** A palavra secreta é escolhida aleatoriamente a partir de uma lista (`word_list`), e a exibição do progresso da palavra é feita com uma lista de underscores (`display`).
- **Laços e condicionais:** Utilização de loops (`while`) e condicionais para o fluxo do jogo, verificando se o jogador ainda tem vidas e se a palavra foi completamente adivinhada.
- **Entrada de usuário e manipulação de strings:** O jogador insere uma letra de cada vez, e o código verifica se a letra faz parte da palavra.
- **Integração com listas e gráficos:** O jogo exibe o estado atual da palavra oculta e uma imagem do "homem da forca" com base nas vidas restantes.

### O que o código faz:
1. **Escolha da palavra:** O código escolhe uma palavra aleatória da lista `word_list`.
2. **Exibição inicial:** A palavra é mostrada com underscores representando as letras ainda não adivinhadas.
3. **Entrada do jogador:** O jogador digita uma letra e o código verifica se a letra está presente na palavra secreta.
4. **Atualização da palavra oculta:** Se a letra estiver correta, a palavra oculta é atualizada com a letra adivinhada nas posições corretas.
5. **Perda de vida:** Se a letra estiver errada, o número de vidas diminui.
6. **Fim do jogo:**
   - Se o jogador adivinhar todas as letras, o jogo termina com vitória.
   - Se o jogador perder todas as suas vidas, o jogo termina com derrota, revelando a palavra secreta.

### Exemplo de execução:
```plaintext
WELCOME TO HANGMAN GAME!
_ _ _ _ _
Guess a letter: a
_ _ _ _ a
Lifes: 6/6
['a']
  +---+
  |   |
      |
      |
      |
      |
=========

Guess a letter: e
_ e _ _ a
Lifes: 6/6
['a', 'e']
  +---+
  |   |
      |
      |
      |
      |
=========

Guess a letter: t
t e _ _ a
Lifes: 6/6
['a', 'e', 't']
  +---+
  |   |
      |
      |
      |
      |
=========

Guess a letter: r
t e r r a
Lifes: 6/6
['a', 'e', 't', 'r']
  +---+
  |   |
      |
      |
      |
      |
=========

Congratulations!
You win!
