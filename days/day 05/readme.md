## Gerador de Senhas Aleatórias

Este projeto contém um script em Python que gera senhas aleatórias com base no número de caracteres especificado pelo usuário. A senha gerada pode incluir letras, números e símbolos.

### O que foi aprendido:
- **Uso de listas para armazenar dados:** Utilização de listas para representar diferentes categorias de caracteres (letras, números e símbolos).
- **Geração de números aleatórios (`random.randint()` e `random.choice()`):** Seleção aleatória de caracteres a partir das listas fornecidas.
- **Construção de senhas dinâmicas:** Criação de senhas com diferentes tipos de caracteres e quantidade variável de caracteres, conforme a solicitação do usuário.
- **Concatenar strings:** A senha é construída adicionando caracteres gerados aleatoriamente em uma string.

### O que o código faz:
1. **Captura o número de caracteres:** O código solicita ao usuário quantos caracteres devem ter a senha.
2. **Geração de senha aleatória:** Utiliza listas de letras, números e símbolos para criar uma senha:
   - A cada iteração, escolhe aleatoriamente entre letras (maiúsculas e minúsculas), números e símbolos.
   - Adiciona o caractere escolhido à senha.
3. **Exibe a senha gerada:** Após o número de caracteres especificado, a senha completa é exibida no console.

### Exemplo de execução:
```plaintext
How many caracteres would you like in your password?
12
&7Zg9lP5w2S!4
