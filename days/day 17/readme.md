# Quiz Interativo com POO 🎯

Este projeto implementa um **Quiz interativo** utilizando **Programação Orientada a Objetos (POO)**. O programa lê perguntas de um banco de dados e interage com o usuário para registrar respostas, validar a precisão e acompanhar a pontuação.

## O que foi aprendido:
- **Estruturas de classes:** Criação de classes específicas para organizar dados (`Question`) e lógica de funcionamento (`QuizBrain`).
- **Manipulação de listas:** Gerenciamento de um banco de perguntas para iterar e exibir perguntas.
- **Encapsulamento:** Organização da lógica em métodos que tornam o código modular e reutilizável.
- **Interação com o usuário:** Uso de entrada de dados (`input()`) para capturar respostas e exibir feedback.

## Estrutura das classes utilizadas:
1. **`Question`:**
   - Atributos:
     - `q_text` (texto da pergunta)
     - `q_answer` (resposta correta)
   - Objetivo: Representa cada pergunta com seu texto e resposta associada.
2. **`QuizBrain`:**
   - Atributos:
     - `question_number` (controla o índice da pergunta atual)
     - `question_list` (lista de perguntas)
     - `score` (pontuação atual)
   - Métodos:
     - `next_question`: Exibe a próxima pergunta ao usuário e valida a resposta.
     - `still_has_question`: Verifica se ainda há perguntas não respondidas.
     - `check_answer`: Compara a resposta do usuário com a resposta correta e ajusta a pontuação.

## O que o código faz:
1. **Inicialização:** Importa um banco de dados de perguntas e cria objetos da classe `Question` para cada entrada.
2. **Exibição do Quiz:** Itera por todas as perguntas, exibindo uma de cada vez e solicitando respostas.
3. **Validação:** Verifica se a resposta está correta e ajusta a pontuação.
4. **Feedback ao Usuário:** Exibe mensagens indicando a precisão da resposta e o progresso no quiz.
5. **Resultado Final:** Após responder todas as perguntas, exibe a pontuação final do usuário.
