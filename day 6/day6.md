## Desafio do Labirinto - Reeborg

Este código resolve o desafio do labirinto no Reeborg, um ambiente de programação onde o objetivo é guiar um robô até o objetivo, utilizando comandos simples como `move()`, `turn_left()`, e `front_is_clear()`.

### O que foi aprendido:
- **Uso de funções e loops:** Criar uma função (`turn_right()`) e utilizar loops `while` para controlar o movimento do robô até alcançar o objetivo.
- **Lógica de navegação em labirinto:** Utilizar condições (`if`, `elif`, `else`) para decidir o movimento do robô, fazendo-o virar à direita quando possível e seguir em frente quando não há obstáculos.
- **Estrutura de controle de fluxo:** Como usar condicionais para gerenciar o movimento do robô e garantir que ele alcance o objetivo de forma eficiente.

### O que o código faz:
1. **Função `turn_right()`:** Define a função para o robô virar à direita, que é feita ao girar três vezes à esquerda (`turn_left()` é chamado três vezes).
2. **Movimento até o fim do caminho:** O robô move-se até encontrar um obstáculo ou alcançar o objetivo.
3. **Navegação pelo labirinto:** Em seguida, o robô toma decisões:
   - Se o caminho à direita estiver livre, ele vira à direita e move.
   - Se o caminho à frente estiver livre, ele apenas se move.
   - Se não houver caminho à frente ou à direita, ele vira à esquerda.
4. **Objetivo:** O robô continua se movendo até alcançar o objetivo.

### Exemplo de execução:
O código não tem saída diretamente visível no console, mas ele instrui o robô a navegar pelo labirinto até o ponto de destino.

---

Este código é uma solução para o desafio de navegação em um labirinto no Reeborg, usando lógica simples de navegação baseada em condições.
