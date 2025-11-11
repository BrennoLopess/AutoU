# models/text_classifier.py
# Classificador simples Produtivo vs Improdutivo
# Pipeline: TF-IDF + LogisticRegression
# Fornece funções: train(), predict(text), save_model(), load_model()

from __future__ import annotations
from dataclasses import dataclass
from typing import List, Tuple
import os
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

MODEL_PATH = os.path.join(os.path.dirname(__file__), "email_clf.joblib")

# Dataset inicial simples (podemos ampliar depois)
# Frases curtas em pt-br com rótulos: 1 = Produtivo, 0 = Improdutivo
DATA: List[Tuple[str, int]] = [
    ("Segue o relatório mensal anexado para revisão", 1),
    ("Concluí a análise dos indicadores do último trimestre", 1),
    ("Preciso de suporte para acessar o sistema de chamados", 1),
    ("Atualização: chamado #543 aberto e em andamento", 1),
    ("Favor revisar a proposta e enviar aprovação", 1),
    ("Bom dia! Parabéns pelo excelente trabalho", 1),
    ("Poderia compartilhar o status do projeto até amanhã?", 1),
    ("Encaminhando a documentação solicitada", 1),
    ("Consigo uma reunião para alinharmos os próximos passos?", 1),
    ("Solicito acesso à planilha do financeiro", 1),

    ("Feliz natal", 0),
    ("Bom fim de semana", 0),
    ("Oi, tudo bem?", 0),
    ("Apenas passando para agradecer", 0),
    ("Ok, combinado", 0),
    ("hahaha que legal", 0),
    ("Olha esse meme", 0),
    ("Sem assunto", 0),
    ("Obrigado!", 0),
    ("Podemos falar depois?", 0),
]

@dataclass
class EmailClassifier:
    pipeline: Pipeline

    @staticmethod
    def build_pipeline() -> Pipeline:
        return Pipeline([
            ("tfidf", TfidfVectorizer(
                lowercase=True,
                ngram_range=(1, 2),  # unigram + bigram
                min_df=1,
                max_features=5000
            )),
            ("clf", LogisticRegression(max_iter=1000))
        ])

    @classmethod
    def train(cls, data: List[Tuple[str, int]] = DATA) -> "EmailClassifier":
        texts, labels = zip(*data)
        X_train, X_test, y_train, y_test = train_test_split(
            list(texts), list(labels), test_size=0.25, random_state=42, stratify=labels
        )

        pipe = cls.build_pipeline()
        pipe.fit(X_train, y_train)

        # Relatório rápido (dev)
        y_pred = pipe.predict(X_test)
        print("\n[Relatório de validação]")
        print(classification_report(y_test, y_pred, target_names=["Improdutivo", "Produtivo"]))

        return cls(pipeline=pipe)

    def predict(self, text: str) -> Tuple[str, float]:
        """Retorna (classe_str, prob_produtivo)."""
        probas = self.pipeline.predict_proba([text])[0]
        idx_prod = 1  # classe 1 = Produtivo
        classe = "Produtivo" if probas[idx_prod] >= 0.5 else "Improdutivo"
        return classe, float(probas[idx_prod])

    def save(self, path: str = MODEL_PATH) -> None:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        joblib.dump(self.pipeline, path)
        print(f"[OK] Modelo salvo em: {path}")

    @staticmethod
    def load(path: str = MODEL_PATH) -> "EmailClassifier":
        pipeline = joblib.load(path)
        return EmailClassifier(pipeline=pipeline)


# Execução direta para treinar e testar rapidamente:
if __name__ == "__main__":
    clf = EmailClassifier.train(DATA)
    clf.save()

    # Teste rápido
    exemplos = [
        "Você pode enviar o status do chamado 123 ainda hoje?",
        "Feliz aniversário!",
        "Anexei a planilha com a projeção financeira.",
        "hehe kkkkk valeu"
    ]
    for txt in exemplos:
        rotulo, p = clf.predict(txt)
        print(f"Texto: {txt}\n => {rotulo} (prob_produtivo={p:.2f})\n")
