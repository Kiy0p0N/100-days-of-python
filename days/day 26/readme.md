# NATO Phonetic Alphabet Converter 🎙️

Este projeto é um conversor de palavras para o **alfabeto fonético da OTAN (NATO Phonetic Alphabet)**, desenvolvido em Python utilizando a biblioteca `pandas`. O programa solicita uma palavra ao usuário e retorna a versão fonética correspondente, substituindo cada letra por seu equivalente no alfabeto fonético.

## O que foi aprendido:
- **Leitura de arquivos CSV com `pandas`** para importar e manipular dados tabulares.
- **Compreensão de dicionários em Python** para armazenar e recuperar valores rapidamente.
- **List Comprehension** para transformar palavras em suas representações fonéticas.
- **Manipulação de strings** para converter entradas do usuário para o formato adequado.

## O que o código faz:
1. **Carregamento dos dados:**
   - Lê um arquivo CSV contendo o alfabeto fonético da OTAN.
   - Converte os dados em um dicionário onde a chave é a letra e o valor é sua representação fonética.

2. **Interação com o usuário:**
   - Solicita que o usuário digite uma palavra.
   - Converte a entrada para letras maiúsculas para garantir a compatibilidade com o dicionário.

3. **Conversão fonética:**
   - Substitui cada letra da palavra digitada por sua forma fonética correspondente.
   - Exibe a lista resultante na tela.

## Como usar:
1. Execute o script `main.py`.
2. Digite uma palavra quando solicitado.
3. O programa retornará a palavra convertida para o alfabeto fonético da OTAN.

## Exemplo de execução:
```
Enter a word: ChatGPT
['Charlie', 'Hotel', 'Alpha', 'Tango', 'Golf', 'Papa', 'Tango']
```

