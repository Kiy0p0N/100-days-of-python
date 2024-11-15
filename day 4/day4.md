## Jogo Pedra, Papel e Tesoura

Este projeto contém uma versão simples do jogo "Pedra, Papel e Tesoura", onde o usuário joga contra o computador.

### O que foi aprendido:
- **Uso de listas em Python:** Armazenar as opções do jogo (pedra, papel e tesoura) em uma lista.
- **Geração de números aleatórios (`random.randint()`):** Permitir que o computador faça uma escolha aleatória.
- **Uso de condicionais para determinar o vencedor:** Comparar as escolhas do usuário e do computador para determinar o vencedor.
- **Exibição de arte em ASCII:** Representar as opções de pedra, papel e tesoura usando arte em texto.

### O que o código faz:
1. **Início do jogo:** O usuário é saudado e instruído a escolher entre 0 (pedra), 1 (papel) ou 2 (tesoura).
2. **Escolha do computador:** O computador faz uma escolha aleatória entre pedra, papel e tesoura.
3. **Exibição das escolhas:** O código exibe a escolha do usuário e a escolha do computador.
4. **Determinação do vencedor:** O código compara as escolhas e determina o resultado do jogo:
   - Empate, vitória ou derrota para o usuário.
5. **Verificação de entradas inválidas:** Se o usuário digitar um número fora do intervalo permitido, o jogo avisa que o número é inválido e o usuário perde.

### Exemplo de execução:
```plaintext
Welcome to game!
Enter 0 for Rock, 1 for Paper or 2 for Scissors: 1

Your choice: 

    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

Computer choice: 

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

You WIN!
