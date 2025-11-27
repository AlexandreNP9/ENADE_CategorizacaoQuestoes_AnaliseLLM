# ENADE_CategorizacaoQuestoes_AnaliseLLM
Projeto para categorização das questões do ENADE de acordo com os descritores e habilidades previstas nas [Diretrizes Curriculares Nacionais (DNCs)](https://www.gov.br/mec/pt-br/cne/normas-classificadas-por-assunto/diretrizes-curriculares-cursos-de-graduacao).
Este repositório faz parte de um projeto com subsistemas distribuído.

Repositório Geral:
https://github.com/AlexandreNP9/ENADE_CategorizacaoQuestoes_GERAL

# Objetivos deste repositório
Envio do enunciado e gabarito para uma LLM  
Identificar o conteúdo principal, habilidade associada, metadados e justificativas das altertanivas


# Especifidades técnicas
## Programas e bibliotecas
Linux Mint 22.1  
Python 3  
API do Gemini Flash 2.5

# Antes de executar o código
Espera-se que já tenha o python3 instalado

## Criar variável de ambiente (caso necessário)
```
python3 -m venv venv  
source venv/bin/activate  
```

## Para instalar o OpenAI
```
pip install google-generativeai
```

Obter API key no Google AI Studio
https://aistudio.google.com/app/api-keys

Adicionar ao código na variável de ambiente com:

export GEMINI_API_KEY="SUA_CHAVE_AQUI"