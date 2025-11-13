from flask import Flask, render_template, request
from openai import OpenAI
import os
from werkzeug.utils import secure_filename
import tempfile
import PyPDF2

# ===========================
# CONFIGURAÇÃO DO OPENROUTER
# ===========================
OPENROUTER_API_KEY = "CHAVE"

client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

app = Flask(__name__)

# ===========================
# EXTRAÇÃO DE TEXTO DE PDF
# ===========================
def extract_text_from_pdf(file_path):
    text = ""
    try:
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"
    except Exception as e:
        print("[ERRO PDF]:", e)
        text = ""
    return text.strip()


# ===========================
# CLASSIFICAÇÃO VIA IA
# ===========================
def classify_email(texto):
    prompt = f"""
Você é um classificador binário. Sua tarefa é decidir se a mensagem abaixo é PRODUTIVA ou IMPRODUTIVA.

REGRAS:
- PRODUTIVO: relacionado a trabalho, tarefas, demandas, reuniões, tickets, prazos.
- IMPRODUTIVO: papo casual, memes, brincadeiras, assuntos pessoais, emojis, fofoca.

Responda SOMENTE com:
PRODUTIVO
IMPRODUTIVO

TEXTO:
\"\"\"{texto}\"\"\"
"""

    try:
        response = client.chat.completions.create(
            model="anthropic/claude-3.5-haiku",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=5,
        )

        output = response.choices[0].message.content.strip().lower()

        if output == "produtivo":
            return "Produtivo"
        elif output == "improdutivo":
            return "Improdutivo"
        else:
            print("DEBUG CLASSIFICACAO (inesperado):", output)
            return "Improdutivo"

    except Exception as e:
        print("[ERRO IA CLASSIFICAÇÃO]:", e)
        return "Improdutivo"


# ===========================
# SUGESTÃO DE RESPOSTA
# ===========================
def sugestao_resposta(texto):

    prompt = f"""
Gere uma resposta educada, curta (máximo 3 linhas) e profissional para o texto abaixo:

\"\"\"{texto}\"\"\"
"""

    try:
        response = client.chat.completions.create(
            model="anthropic/claude-3.5-haiku",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=128,
            temperature=0.5
        )
        resposta = response.choices[0].message.content.strip()

        return resposta

    except Exception as e:
        print("[ERRO IA RESPOSTA]:", e)
        return "Não foi possível gerar sugestão de resposta."


# ===========================
# ROTAS PRINCIPAIS
# ===========================
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/inicio")
def inicio():
    return render_template("index.html")


@app.route("/analise", methods=["POST"])
def analisar():

    texto = ""

    # Caso tenha texto digitado
    if "email_text" in request.form:
        texto = request.form["email_text"].strip()

    # Upload de arquivo
    if "file" in request.files:
        file = request.files["file"]

        if file.filename != "":
            filename = secure_filename(file.filename)

            # Salvando arquivo temporariamente
            with tempfile.NamedTemporaryFile(delete=False) as tmp:
                file.save(tmp.name)

                # PDF
                if filename.lower().endswith(".pdf"):
                    texto = extract_text_from_pdf(tmp.name)

                # TXT
                elif filename.lower().endswith(".txt"):
                    try:
                        with open(tmp.name, "r", encoding="utf-8", errors="ignore") as f:
                            texto = f.read()
                    except Exception as e:
                        print("[ERRO TXT]:", e)
                        texto = ""

                # Outros formatos (descartados)
                else:
                    texto = ""

    # Se estiver vazio
    if texto.strip() == "":
        return render_template(
            "analise.html",
            texto="Nenhum texto encontrado.",
            classificacao="Erro",
            sugestao="Não foi possível analisar."
        )

    # Executa IA
    classificacao = classify_email(texto)
    resposta_sugerida = sugestao_resposta(texto)

    return render_template(
        "analise.html",
        texto=texto,
        classificacao=classificacao,
        sugestao=resposta_sugerida
    )


if __name__ == "__main__":
    app.run(debug=True)
