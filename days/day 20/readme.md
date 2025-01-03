# Snake Game (Part 1) 🐍

Este projeto implementa o clássico jogo da cobrinha (Snake) utilizando a biblioteca `turtle` do Python. O jogador controla a direção da cobra enquanto ela se move pela tela, com o objetivo de continuar jogando sem colidir consigo mesma ou com as bordas (essa funcionalidade pode ser expandida).

## O que foi aprendido:
- **Uso da biblioteca `turtle`:** Criação de gráficos 2D e manipulação de objetos visuais para animar o jogo.
- **Estruturas de classe no Python:** Modularização do código por meio de classes (`Snake`), separando responsabilidades como movimento e controle da direção.
- **Laços e animações:** Uso de loops para atualizar a tela e criar movimento contínuo da cobra.
- **Manipulação de eventos:** Detecção de teclas pressionadas pelo usuário para controlar a direção da cobra.

## O que o código faz:
1. **Configuração da tela:**
   - Cria uma tela de jogo com tamanho de 600x600 pixels.
   - Define o fundo preto e desativa atualizações automáticas para otimizar as animações.

2. **Criação da cobra:**
   - A cobra é composta por múltiplos segmentos (pequenos quadrados), inicialmente posicionados em uma linha horizontal.

3. **Controle do movimento:**
   - A cobra se move continuamente para frente.
   - O jogador pode mudar a direção da cobra utilizando as teclas direcionais (`Up`, `Down`, `Left`, `Right`), respeitando as regras de movimento (não pode fazer um giro de 180°).

4. **Loop principal:**
   - Atualiza a tela a cada 0,1 segundo para criar animação fluida.
   - Move a cobra e atualiza suas posições.

5. **Interação do usuário:**
   - O jogo permanece em execução até o jogador fechar a janela.

## Exemplo de execução
<video width="560" height="315" autoplay muted loop>
  <source src="video/snake-game%20(part%201).mp4" type="video/mp4">
  Seu navegador não suporta o vídeo.
</video>