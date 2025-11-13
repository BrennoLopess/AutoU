AutoU – Classificador Inteligente de Produtividade
==================================================

1. Visão Geral do Projeto
O AutoU é uma aplicação web desenvolvida para classificar mensagens como Produtivas ou Improdutivas utilizando IA generativa (Claude 3.5 Haiku). O sistema também gera uma resposta profissional curta e educada com base no texto analisado. É um projeto completo, cobrindo frontend, backend, processamento de arquivos (PDF e TXT), engenharia de prompts e integração com API de IA.

2. Problema Resolvido
Ambientes de trabalho possuem grande volume de mensagens. O AutoU ajuda a:
- Identificar rapidamente se uma mensagem é relevante.
- Evitar distrações.
- Automatizar respostas profissionais.

3. Arquitetura da Solução
Frontend:
- HTML, CSS e Jinja.
- Interface simples, limpa e responsiva.

Backend:
- Flask (Python).
- Tratamento de uploads.
- Extração de textos.
- Comunicação com o modelo via OpenRouter.

IA:
- Modelo: Claude 3.5 Haiku.
- Dois prompts:
  - Classificação binária (Produtivo / Improdutivo).
  - Geração de resposta curta.

4. Funcionalidades
- Classificação binária.
- Upload de PDF.
- Upload de TXT.
- Geração automática de respostas.
- Tratamento de erros.
- Interface amigável.

5. Estrutura do Projeto
AutoU/
│── app.py
│── requirements.txt
│── README.md
│
├── templates/
│   ├── home.html
│   ├── index.html
│   └── analise.html
│
├── static/
│   ├── style.css
│   ├── img/
│       └── autou-logo.png

6. Testes Realizados
- Textos produtivos: OK
- Textos improdutivos: OK
- PDF produtivo: OK
- PDF improdutivo: OK
- TXT produtivo/improdutivo: OK

7. Tecnologias Utilizadas
Backend: Flask, Python, PyPDF2  
IA: Claude 3.5 Haiku (OpenRouter)  
Frontend: HTML5, CSS3, Jinja2  

8. Instalação
1. Clone:
   git clone https://github.com/SEU_USUARIO/AutoU.git

2. Ambiente:
   python -m venv venv
   source venv/bin/activate

3. Instale dependências:
   pip install -r requirements.txt

4. Crie .env com sua chave:
   OPENROUTER_API_KEY=suachave

5. Execute:
   python app.py

9. Possíveis Melhorias
- Suporte a DOCX.
- Histórico de análises.
- Modo API.
- Painel administrativo.

10. Conclusão
O AutoU demonstra capacidade técnica em:
- IA aplicada.
- Desenvolvimento end-to-end.
- Processamento de arquivos.
- Engenharia de prompts.
- Arquitetura limpa e escalável.

Projeto pronto para ser apresentado a recrutadores.

Desenvolvido por Brenno Lopes.
