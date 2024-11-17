## Cifra de César

O Cifra de César é uma técnica simples de criptografia em que cada letra do texto é substituída por outra letra do alfabeto, movendo-se um número específico de posições para frente ou para trás no alfabeto. Este projeto implementa tanto a codificação quanto a decodificação usando essa técnica.

### O que foi aprendido:
- **Manipulação de strings e loops**: O uso de loops e condições para iterar sobre cada caractere do texto e aplicar o deslocamento adequado para codificação ou decodificação.
- **Uso de listas e operadores de índice**: Manipulação da lista `alphabet` para determinar a posição das letras e aplicar a transformação desejada.
- **Entrada de usuário**: Receber a mensagem, o número de deslocamentos e decidir entre codificação e decodificação baseando-se na entrada do usuário.

### Como funciona o código:
1. **Entrada da mensagem**: O usuário insere o texto que deseja codificar ou decodificar.
2. **Escolha do deslocamento**: O usuário especifica o número de posições para frente ou para trás no alfabeto (positivo ou negativo).
3. **Tratamento das letras**:
   - Cada letra do texto é verificada. Se não for uma letra do alfabeto, ela é adicionada diretamente à mensagem resultante.
   - Para cada letra do alfabeto, a nova posição é calculada com base no número de deslocamentos, usando a operação `mod` para manter o ciclo do alfabeto.
4. **Resultado**: A mensagem codificada ou decodificada é exibida.

### Exemplo de execução:
```plaintext
Type your message:
HELLO WORLD
Type the shift number:
3
Here is the encoded result: khoor zruog

Type "encode" to encrypt or type "decode" to decrypt:
decode
Type your message:
khoor zruog
Type the shift number:
-3
Here is the decoded result: hello world
