AutoU – FlowSense 🚀

Classificação Inteligente de Mensagens com IA • Flask • OpenRouter • Deploy na Render

O AutoU – FlowSense é um projeto completo desenvolvido com o objetivo de
aplicar Inteligência Artificial no mundo real.
Ele utiliza classificação automática de produtividade em mensagens e
sugere respostas inteligentes com base em IA.

Este projeto representa minha evolução como desenvolvedor, desde o
design até o deploy em produção – e agora está disponível publicamente.

------------------------------------------------------------------------

🌟 Visão Geral do Projeto

O FlowSense permite que qualquer usuário envie: - ✍️ Um texto digitado
- 📄 Um arquivo PDF
- 📄 Um arquivo .txt

E receba automaticamente: - 🔍 Classificação Produtivo / Improdutivo
- 🤖 Sugestão de resposta profissional
- 📊 Visualização clara e elegante do resultado

Tudo isso com: - Flask no backend
- HTML + CSS com animações premium no frontend
- OpenRouter API usando Claude Haiku
- Deploy completo na Render (produção)
- Integração com Gunicorn para produção segura

------------------------------------------------------------------------

🛠️ Tecnologias Utilizadas

🔧 Backend

-   Python 3
-   Flask
-   Gunicorn
-   PyPDF2 (extração de texto)
-   OpenRouter (LLM Claude 3.5 Haiku)

🎨 Frontend

-   HTML
-   CSS (glassmorphism + animações + gradientes dinâmicos)
-   UX simples, profissional e limpa

☁️ Deploy

-   Render (Web Service)
-   Variáveis de ambiente seguras
-   Pipeline automatizado via render.yaml

------------------------------------------------------------------------

📂 Estrutura do Projeto

    AutoU/
    │
    ├── app.py                # Backend Flask + Rotas + IA
    ├── requirements.txt      # Dependências
    ├── render.yaml           # Configuração para deploy
    │
    ├── templates/            # Páginas HTML
    │   ├── home.html
    │   ├── index.html
    │   └── analise.html
    │
    ├── static/
    │   ├── style.css         # Estilos gerais + animações
    │   └── img/autoU-logo.png
    │
    └── data/                 # Dataset (inspiração do projeto)

------------------------------------------------------------------------

✨ Funcionalidades

✔ Classificação Inteligente

O usuário envia texto ou arquivo.
O sistema envia para a IA:
- Extração automática (PDF/TXT)
- Prompt preparado para classificação binária
- Resposta limitada e limpa (Produtivo / Improdutivo)

✔ Sugestão de Resposta

Claude Haiku gera: - Resposta curta
- Educada
- Profissional
- Máximo 3 linhas

✔ Design Premium

-   Glassmorphism moderno
-   Gradiente animado
-   Cartões com blur
-   Animações suaves de entrada
-   Totalmente responsivo

------------------------------------------------------------------------

🚀 Deploy em Produção

O projeto está online:
👉 https://autou-5bhb.onrender.com

Rodando com:

    build: pip install -r requirements.txt
    start: gunicorn app:app

------------------------------------------------------------------------

🧠 Lições Aprendidas

-   Estrutura avançada com Flask
-   Integração com OpenRouter
-   Processamento seguro de arquivos
-   UI moderna e animada
-   Deploy profissional com Gunicorn + Render
-   Variáveis de ambiente seguras
-   Como estruturar projetos para portfólio

------------------------------------------------------------------------

📌 Próximos Passos

-   API pública
-   Dashboard
-   Autenticação
-   Histórico de análises
-   Modelo ML próprio
-   Versão mobile/PWA
-   Implementação com React


------------------------------------------------------------------------

👨‍💻 Autor

Brenno Lopes
Desenvolvedor • Eng. de Software • Apaixonado por IA                    
LinkedIn: https://www.linkedin.com/in/brennolopes/
GitHub: https://github.com/BrennoLopess

------------------------------------------------------------------------


