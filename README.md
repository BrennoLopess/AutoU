## 🧠 FlowSense – Classificação de Produtividade com IA

<p align="center">
  <img src="static/img/autoU-logo.png" alt="FlowSense Logo" width="150">
</p>

**FlowSense** é uma aplicação web que utiliza **Inteligência Artificial (Zero-Shot Classification)** 
para analisar textos, e-mails e mensagens corporativas, identificando se o conteúdo é 
**produtivo** ou **improdutivo**, com base em contexto, tom e objetivo.

O sistema foi desenvolvido com **Flask + Transformers (Hugging Face)** e apresenta uma interface 
moderna, responsiva e intuitiva, com telas animadas e feedback visual em tempo real.

---

### 🚀 Demonstração

<p align="center">
  <img src="preview/demo.gif" alt="Demonstração do FlowSense" width="700">
</p>

---

### ⚙️ Tecnologias Utilizadas

- 🧩 **Flask** — Backend leve e rápido em Python  
- 🤖 **Hugging Face Transformers** — Modelo `mDeBERTa-v3-base-xnli-multilingual-nli-2mil7`  
- 🎨 **HTML5 + CSS3 + JavaScript** — Frontend com transições e animações  
- 🔥 **Torch** — Suporte a GPU e processamento de embeddings  
- 🧭 **Design Customizado** — Gradientes e efeitos suaves  

---

### 🧩 Estrutura do Projeto

FlowSense/
├── app.py
├── models/
│   └── zero_shot_classifier.py
├── templates/
│   ├── home.html
│   ├── index.html
│   └── analysis.html
├── static/
│   ├── style.css
│   └── img/
│       └── autoU-logo.png
└── README.md

---

### 💡 Como Executar Localmente

**1️⃣ Clone o repositório**
```bash
git clone https://github.com/seuusuario/flowsense.git
cd flowsense
```

**2️⃣ Crie um ambiente virtual**
```bash
python -m venv venv
venv\Scripts\activate  # (Windows)
# ou
source venv/bin/activate  # (Linux/Mac)
```

**3️⃣ Instale as dependências**
```bash
pip install -r requirements.txt
```

**4️⃣ Execute o app**
```bash
python app.py
```

Acesse em:  
👉 http://127.0.0.1:5000

---

### 🧠 Como Funciona

1. O usuário insere o texto ou mensagem no campo de análise.  
2. O modelo zero-shot da Hugging Face avalia o texto com base em dois rótulos:  
   - **Produtivo**  
   - **Improdutivo**  
3. A IA retorna o rótulo mais provável e a **porcentagem de confiança**.  

---

### 🎨 Design & Experiência

O FlowSense foi projetado com foco em **simplicidade e imersão**:
- Tela inicial com animações suaves  
- Gradiente institucional azul e laranja  
- Transição fluida entre páginas  
- Feedback visual dinâmico durante a análise  

---

### 🧾 Licença

Este projeto está sob a licença MIT.  
Sinta-se livre para usar, modificar e distribuir.

---

### 👨‍💻 Autor

**Brenno Lopes**  
💼 Engenharia de Software — IDP  
📧 brenno.lopes@example.com  
🔗 [linkedin.com/in/brenno-lopes](#)
