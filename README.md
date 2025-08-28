# 🌾 Meu Registro Rural

Painel Interativo para Simulação de Plataforma de Regularização Fundiária.

## ✅ Sobre o Projeto

Este projeto fictício simula a área logada da plataforma Registro Rural, focando em visualização e gestão de imóveis rurais por meio de um painel interativo. Idealizado para demonstrar domínio em desenvolvimento web com Django, Bootstrap e jQuery, ele representa um ambiente premium com recursos avançados — todos utilizando dados simulados.

---

## 🧠 Objetivo

Criar um painel funcional e visual para usuários simulados, com foco em clareza, interatividade e experiência do usuário (UX). A proposta é demonstrar:

- Estrutura de uma aplicação web com Django.
- Capacidade de simular dados e fluxos reais.
- Interface rica e responsiva com Bootstrap.

---

## 🖥️ Funcionalidades

- Visualização de imóveis com status (completo/incompleto)
- Gráfico de status (completo, faltando CCIR, etc.)
- Mini-mapa com os imóveis plotados via Leaflet.js
- Linha do tempo de atividades e eventos fundiários
- Comparador de dois imóveis
- Cards explicativos sobre documentação (CAR, CCIR, etc.)
- Modo Simulado com aviso inicial
- Gerenciamento de equipe (visual)

---

## 🛠️ Tecnologias Utilizadas

- Python (Django)
- HTML + CSS (Bootstrap 5)
- JavaScript (jQuery)
- Jinja2 (Templates)
- Chart.js (gráficos)
- Leaflet.js (mapas)

---

## 🚀 Como Rodar Localmente

1. Clone o repositório:
  ```bash
   git clone https://github.com/augustofranca0701/meu_registro_rural
   cd meu_registro_rural
  ```

2. Crie e ative um ambiente virtual:
  ```bash
  python -m venv venv    #para criar
  venv\Scripts\activate  #para ativar

  #py -3 -m venv .venv
  #.\.venv\Scripts\Activate.ps1

```

3. Instale as dependências:
  ```bash
   pip install -r requirements.txt
```

4. Aplique as migrações do banco:
  ```bash
   python manage.py migrate
```

5. Carregue os dados de exemplo:
```bash
   python manage.py loaddata fixtures_painel.json
```

6. Rode o servidor:
  ```bash
   python manage.py runserver
```
7. Acesse em: http://127.0.0.1:8000
---

## 🔮 Próximos Passos (Visão Futurista)

- Integrações reais com CAR, CCIR, Receita Federal
- Upload de documentos e análises automatizadas
- Sistema de planos e créditos real
- Interface mobile aprimorada

---

## 🎯 Resultado Esperado

Este projeto serve como prova de conceito para aplicações do setor rural digital, com foco em UX, responsividade e visão de produto.
