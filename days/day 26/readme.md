# NATO Phonetic Alphabet Converter 🎙️  

Este projeto é um conversor de palavras para o **alfabeto fonético da OTAN (NATO Phonetic Alphabet)**, desenvolvido em Python utilizando a biblioteca `pandas`. O programa solicita uma palavra ao usuário e retorna a versão fonética correspondente, substituindo cada letra por seu equivalente no alfabeto fonético.  

## 📚 O que foi aprendido  
- **Leitura de arquivos CSV com `pandas`** para importar e manipular dados de forma eficiente.  
- **Dicionários em Python** para mapear letras às suas representações fonéticas.  
- **List Comprehension** para transformar palavras em sequências fonéticas de maneira concisa.  
- **Tratamento de exceções (`try-except`)** para garantir que a entrada do usuário contenha apenas letras do alfabeto.  

## ⚙️ O que o código faz  

### 1️⃣ Carregamento dos dados  
- Lê um arquivo CSV contendo o alfabeto fonético da OTAN.  
- Converte os dados em um dicionário onde a **chave** é a letra e o **valor** é sua representação fonética.  

### 2️⃣ Interação com o usuário  
- Solicita que o usuário digite uma palavra.  
- Converte a entrada para **letras maiúsculas** para garantir a compatibilidade com o dicionário.  

### 3️⃣ Conversão fonética  
- Substitui cada letra da palavra digitada por sua forma fonética correspondente.  
- Exibe a lista resultante na tela.  
- Caso o usuário insira caracteres inválidos (**números ou símbolos**), exibe uma mensagem de erro e solicita uma nova entrada.  

## ▶️ Como usar  
1. Certifique-se de que o arquivo `nato_phonetic_alphabet.csv` está na mesma pasta do script.  
2. Execute o script `main.py`.  
3. Digite uma palavra quando solicitado.  
4. O programa retornará a palavra convertida para o alfabeto fonético da OTAN.  

## 📌 Exemplo de execução  
```bash
Enter a word: ChatGPT
['Charlie', 'Hotel', 'Alpha', 'Tango', 'Golf', 'Papa', 'Tango']
```
Caso o usuário insira caracteres inválidos:
```bash
Enter a word: Hello123
Sorry, only letters in the alphabet.
Enter a word: Python
['Papa', 'Yankee', 'Tango', 'Hotel', 'Oscar', 'November']
```