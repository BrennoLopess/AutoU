from transformers import pipeline
import torch

def classify_text(text):
    """
    Classifica um texto como 'Produtivo' ou 'Improdutivo' usando zero-shot classification.
    Sempre retorna {'label': ..., 'score': ...}, mesmo em caso de erro.
    """

    # Inicializa pipeline com modelo multilíngue compatível
    try:
        device = 0 if torch.cuda.is_available() else -1
        dtype = torch.float16 if torch.cuda.is_available() else torch.float32

        clf = pipeline(
            "zero-shot-classification",
            model="MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7",
            device=device,
            torch_dtype=dtype
        )
    except Exception as e:
        print(f"[ERRO] Falha ao carregar modelo: {e}")
        return {"label": "Erro ao carregar modelo", "score": 0.0}

    # Faz a classificação propriamente dita
    candidate_labels = ["Produtivo", "Improdutivo"]

    try:
        result = clf(
            sequences=text,
            candidate_labels=candidate_labels,
            hypothesis_template="Este texto é {}."
        )

        label = result["labels"][0]
        score = result["scores"][0]
        print(f"[INFO] Classificação concluída: {label} ({score:.2f})")

        return {"label": label, "score": float(score)}

    except Exception as e:
        print(f"[ERRO] Falha na classificação: {e}")
        return {"label": "Indefinido", "score": 0.0}
