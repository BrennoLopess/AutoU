
AutoU – FlowSense
=================

Classificação Inteligente de Mensagens com IA • Flask • OpenRouter • Deploy na Render  
Um projeto completo, profissional e desenvolvido do zero para demonstrar domínio técnico, visão de produto e execução ponta a ponta.

INTRODUÇÃO
----------

O **AutoU – FlowSense** é mais do que um simples case técnico: é um projeto construído para mostrar minha capacidade de transformar um problema real em uma solução funcional, escalável, bonita e pronta para uso em produção.

Desde o início, entendi que este desafio não era apenas classificar mensagens.  
Era sobre **pensar como engenheiro de software, designer, arquiteto de soluções e profissional de IA ao mesmo tempo**.

Este readme foi projetado para guiar qualquer recrutador, avaliador ou desenvolvedor pelo processo completo:  
**do desafio → ao raciocínio → às escolhas técnicas → à implementação → ao deploy**.

---

1. CONTEXTO DO DESAFIO
----------------------

O desafio proposto simulava a rotina de uma grande empresa do setor financeiro que recebe centenas de mensagens todos os dias e precisava classificá‑las automaticamente entre:

- **Produtivo**  
- **Improdutivo**

Além disso, a solução deveria:

- Sugerir uma resposta automática apropriada  
- Funcionar via web  
- Aceitar arquivos ou texto digitado  
- Ser hospedada publicamente  
- Utilizar inteligência artificial real

A solução precisava ser simples, clara, intuitiva e profissional, tanto no frontend quanto no backend.

---

2. OBJETIVO DA SOLUÇÃO
-----------------------

Meu objetivo foi criar um sistema:

- 100% funcional  
- Com design moderno  
- Experiência suave e páginas elegantes  
- IA realmente integrada  
- Deploy real usando boas práticas  
- Código limpo, modular e organizado  

Ao final, o projeto deveria comunicar maturidade técnica e atenção aos detalhes.

---

3. A JORNADA DE DESENVOLVIMENTO
-------------------------------

### **3.1. Primeiros passos**

Antes de escrever qualquer código, planejei:

- arquitetura geral  
- estrutura das páginas  
- fluxo do usuário  
- prompts da IA  
- integração com LLM  
- deploy final  

### **3.2. Escolha da IA (por que OpenRouter + Claude Haiku)**

Inicialmente testei alternativas como:

- modelos open-source  
- APIs locais  
- Transformers offline  

Mas entendi que para garantir:

✔ velocidade  
✔ baixo custo  
✔ precisão  
✔ linguagem profissional  
✔ estabilidade  

O modelo **Claude 3.5 Haiku**, via **OpenRouter**, foi a escolha perfeita.

### **3.3. Construção do Backend**

O backend foi escrito em **Flask**, pela leveza e simplicidade.

Inclui:

- tratamento de arquivos PDF e TXT  
- extração de texto com PyPDF2  
- sanitização do input  
- chamada ao endpoint da OpenRouter  
- prompt engineering  
- geração de classificação + sugestão  
- envio seguro ao frontend  

Tudo empacotado em rotas limpas e bem organizadas.

### **3.4. Construção do Frontend**

O frontend foi pensado para impactar visualmente:

- glassmorphism  
- gradientes em movimento  
- cartões com blur  
- botões animados  
- interface intuitiva  
- centralização fluida  
- animação de loading personalizada  

Minha referência principal era entregar algo com **qualidade de landing page profissional**, não um simples HTML estático.

### **3.5. Integração Front + Back**

A integração foi feita com:

- Submit do formulário  
- Envio dos dados (texto ou arquivo)  
- Backend processa, analisa e devolve  
- Tela de resultado recebe tudo renderizado  

Usei boas práticas de UX, como:

- botões desabilitados durante processamento  
- feedback visual  
- animação de carregamento  
- limpeza automática após resultado  

### **3.6. Deploy na Render**

O deploy foi uma parte crítica: precisava ser **empresa‑ready**.

Implementei:

- gunicorn como servidor de produção  
- render.yaml para pipeline automatizado  
- variáveis de ambiente seguras  
- dependências bem definidas  
- serviço escalável  

O deploy ficou disponível em:

https://autou-5bhb.onrender.com

Funcionando exatamente como em ambiente local.

---

4. FUNCIONALIDADES COMPLETAS
----------------------------

### ✔ Upload de Arquivos

O sistema aceita:

- .txt  
- .pdf  

Com extração automática do conteúdo.

### ✔ Input Manual

Caixa de texto estilizada com espaço para análise rápida.

### ✔ Classificação Inteligente

A IA recebe um prompt específico preparado para:

- identificar se o texto é Produtivo ou Improdutivo  
- entender contexto de e-mail  
- priorizar instruções  
- padronizar respostas  

### ✔ Sugestão de Resposta Profissional

Sempre:

- curta  
- objetiva  
- educada  
- de 1 a 3 linhas  
- tom corporativo  

### ✔ Interface de Alto Nível

- animações fluidas  
- responsividade  
- arquivo CSS único e organizado  
- visual limpo e agradável  

### ✔ Animação de Loading

Durante a análise:

- surge um overlay  
- com blur  
- ícone animado  
- texto “Analisando com IA…”  

Fica suave, elegante e dá clareza ao usuário.

### ✔ Resultado da Análise

Exibe:

- texto analisado  
- classificação com destaque visual  
- sugestão gerada  
- botão de nova análise  

---

5. ARQUITETURA DO PROJETO
-------------------------

AutoU/  
│  
├── app.py → Backend + rotas + LLM  
├── requirements.txt → Dependências  
├── render.yaml → Deploy automatizado  
│  
├── templates/  
│   ├── index.html  
│   ├── home.html  
│   └── analise.html  
│  
├── static/  
│   ├── style.css  
│   └── img/  
│       ├── autoU-logo.png  
│       └── TelaDeInicio-foto.png  
│  
└── data/ (opcional)

---

6. TECNOLOGIAS UTILIZADAS
-------------------------

### Backend
- Python 3  
- Flask  
- Gunicorn  
- OpenRouter API  
- PyPDF2  
- OS / Secure env handling  

### Frontend
- HTML5  
- CSS3 (+ blur, gradients, animations)  
- UX Design orientado a clareza  

### Deploy
- Render Web Services  
- Variáveis de ambiente  
- render.yaml  
- Servidor Gunicorn  

---

7. APRENDIZADOS E EVOLUÇÃO PESSOAL
----------------------------------

Este projeto consolidou várias habilidades importantes:

### **✔ Engenharia de Software**
- modularização  
- rotas  
- boas práticas de produção  
- tratamento seguro de arquivos  

### **✔ Arquitetura de IA**
- prompt engineering  
- integrar modelos de terceiros  
- controlar temperatura, limites e tokens  
- formatar respostas previsíveis  

### **✔ DevOps / Cloud**
- pipeline com render.yaml  
- variáveis de ambiente  
- gunicorn  
- deploy escalável  

### **✔ UX/UI Profissional**
- centralização fluida  
- glassmorphism  
- design minimalista  
- experiência 100% linear  

### **✔ Pensamento de Produto**
- entender dores do usuário  
- projetar para simplicidade  
- criar solução prática e intuitiva  

---

8. PRÓXIMOS PASSOS
------------------

O FlowSense pode evoluir rapidamente para:

- API pública  
- Autenticação de usuários  
- Histórico de análises  
- Dashboard em tempo real  
- Painel administrativo  
- Versão PWA/mobile  
- ML local treinado com dataset próprio  

---

9. COMO EXECUTAR LOCALMENTE
---------------------------

Instale dependências:

```
pip install -r requirements.txt
```

Execute:

```
python app.py
```

Acesse:

```
http://127.0.0.1:5000
```

---

10. COMO FOI FEITO O DEPLOY
---------------------------

A Render executa:

```
build: pip install -r requirements.txt
start: gunicorn app:app
```

Com tudo configurado via render.yaml.

---

11. LINKS IMPORTANTES
---------------------

### 🔗 Repositório GitHub  
https://github.com/BrennoLopess/AutoU

### 🌐 Aplicação Publicada  
https://autou-5bhb.onrender.com

### 👤 Autor  

Brenno Lopes
Desenvolvedor • Eng. de Software • Apaixonado por IA   
                 
LinkedIn: https://www.linkedin.com/in/brennolopes/

GitHub: https://github.com/BrennoLopess


