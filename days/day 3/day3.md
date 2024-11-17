## Caça ao Tesouro Interativa

Este projeto contém um jogo simples em Python, onde o usuário faz escolhas para avançar por diferentes caminhos e, dependendo das escolhas, pode ter um final feliz ou um final trágico.

### O que foi aprendido:
- **Uso de condicionais (`if`, `elif`, `else`) para ramificação:** Criar diferentes caminhos de acordo com as escolhas do usuário.
- **Uso de `input()` para capturar entradas do usuário:** Permitir que o usuário interaja com o jogo, fazendo escolhas durante o jogo.
- **Estrutura de fluxo condicional para criar um jogo interativo:** Simular um jogo de aventura com diferentes cenários e finais baseados nas decisões do jogador.

### O que o código faz:
1. **Introdução ao jogo:** O usuário é saudado e recebe a primeira escolha sobre qual caminho seguir.
2. **Primeira escolha:** O jogador escolhe entre ir para a direita ou para a esquerda. A escolha afeta diretamente o que acontecerá a seguir.
3. **Segunda escolha (se a primeira escolha for 'right'):** O usuário escolhe se deseja contornar ou atravessar um lago. Cada opção leva a diferentes resultados.
4. **Terceira escolha (se a segunda escolha for '2', ou seja, atravessar o lago):** O usuário entra em uma caverna e deve escolher entre três passagens, cada uma levando a um resultado diferente.
5. **Finais do jogo:** Dependendo das escolhas, o jogador pode encontrar um final onde ganha um prêmio (chegar a uma sala cheia de ouro) ou um final de falha (ser derrotado por um dragão, um monstro, etc.).

### Exemplo de execução:
```plaintext
Welcome to the Treasure Hunt
Choose a path: right or left
right
Good choice, you walked a safe path until you arrived in front of the lake. 

Now choose: 
1- go around the lake. 
2- cross the lake in a small boat.
2
Good choice, you crossed the lake safely and reached a cave.
Inside the cave, you find 3 forks. 
1- You don't hear or feel anything. 
2- you feel a light breeze coming off of it. 
3- you hear some strange sounds 
3
Congratulations!!!!!!!!!!!! 
You arrive in a room full of gold, the noise you heard was just the sound of fairies playing.
