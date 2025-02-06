# Gerador Automático de Convites 🎉

Este projeto cria convites personalizados automaticamente a partir de um modelo pré-definido e uma lista de nomes. O programa substitui `[name]` pelo nome de cada convidado e gera arquivos de convite individuais.

## 📚 O que foi aprendido:
- **Manipulação de arquivos (`open`, `read`, `write`)** para ler e escrever convites personalizados.
- **Uso de `split()`** para extrair nomes de uma lista de convidados.
- **Formatação de strings (`replace`)** para substituir marcadores no texto.
- **Automação de tarefas** para gerar arquivos automaticamente com base nos dados de entrada.

## ⚙️ Como funciona:
1. **Leitura do modelo de convite**  
   - O script abre e lê o conteúdo do arquivo `starting_letters.txt`, que contém um texto com `[name]` como espaço reservado para o nome do convidado.

2. **Leitura dos nomes dos convidados**  
   - O programa lê `invited_names.txt`, que contém uma lista de nomes.

3. **Geração automática dos convites**  
   - Para cada nome na lista, o `[name]` no convite é substituído pelo nome do convidado.
   - O convite personalizado é salvo na pasta `./output/readyToSend/` com um nome de arquivo correspondente ao convidado.