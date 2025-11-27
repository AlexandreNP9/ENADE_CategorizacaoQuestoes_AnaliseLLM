import google.generativeai as genai
import os
import json

# ========= CONFIGURAÇÃO =========

# genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

MODEL_NAME = "gemini-2.5-flash"  # modelo rápido e barato

DIR = "textos_extraidos"
OUTPUT_DIR = "resultados"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ========= CARREGAR ARQUIVOS =========

with open(os.path.join(DIR, "gabarito.txt"), "r", encoding="utf-8") as f:
    gabarito = f.read()

with open(os.path.join(DIR, "padrao_resposta.txt"), "r", encoding="utf-8") as f:
    padrao_resposta = f.read()

with open(os.path.join(DIR, "dcn.txt"), "r", encoding="utf-8") as f:
    dcn_texto = f.read()

# ========= FUNÇÃO DE ANÁLISE =========

def analisar_questao(numero, enunciado):
    prompt = f"""
Você receberá uma questão do ENADE de Ciência da Computação. Sua tarefa é:

1. Identificar o **conteúdo principal** cobrado.
2. A **justificativa da alternativa correta**, com base no gabarito e padrão de resposta.
3. A **justificativa das alternativas erradas**.
4. Relacionar com os **objetos de conhecimento da DCN** de Ciência da Computação.
5. Classificar o nível cognitivo (Baixo / Médio / Alto).

--- QUESTÃO ---
Número: {numero}
Enunciado:
{enunciado}

--- GABARITO ---
{gabarito}

--- PADRÃO DE RESPOSTA ---
{padrao_resposta}

--- DIRETRIZES CURRICULARES (DCN) ---
{dcn_texto}

Responda estritamente no seguinte formato JSON:

{{
  "numero": "{numero}",
  "conteudo_principal": "",
  "justificativa_correta": "",
  "justificativas_erradas": {{}},
  "dcn_relacionadas": [],
  "nivel_cognitivo": "",
  "tags": []
}}
"""

    model = genai.GenerativeModel(MODEL_NAME)
    resposta = model.generate_content(prompt)
    return resposta.text


# ========= PROCESSAR QUESTÕES OBJETIVAS =========

def processar_objetivas():
    arquivos = sorted([f for f in os.listdir(DIR) if f.endswith(".txt") and f[:2].isdigit()])

    for nome in arquivos:
        numero = nome.replace(".txt", "")
        print(f"Processando questão {numero}...")

        with open(os.path.join(DIR, nome), "r", encoding="utf-8") as f:
            enunciado = f.read()

        resposta_json = analisar_questao(numero, enunciado)

        # salvar
        out_path = os.path.join(OUTPUT_DIR, f"{numero}.json")
        with open(out_path, "w", encoding="utf-8") as out:
            out.write(resposta_json)

    print("Processamento concluído!")


# ========= EXECUTAR =========

if __name__ == "__main__":
    processar_objetivas()
