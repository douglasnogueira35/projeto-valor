# Exercício Completo com Streamlit 🚀

Este projeto é um **laboratório interativo de dados** desenvolvido em **Python** utilizando a biblioteca [Streamlit](https://streamlit.io).  
O objetivo é demonstrar como criar aplicações web simples para análise de dados, com filtros, gráficos, formulários e upload/download de arquivos.

---

## 📌 Funcionalidades

- **Configuração inicial** com título, ícone e sidebar expandida.
- **Filtros na barra lateral**:
  - Slider para selecionar valores mínimos.
  - Multiselect para escolher categorias.
- **Gráficos comparativos**:
  - Visualização lado a lado (dados brutos vs filtrados).
  - Gráficos de barras e boxplots com Seaborn/Matplotlib.
- **Formulário interativo**:
  - Campo de texto para nome.
  - Botão de envio com mensagem de sucesso.
- **Filtros múltiplos (9 colunas)**:
  - Seleção dinâmica em várias colunas do dataset.
- **Upload de arquivo CSV**:
  - Carregamento de dados externos.
- **Download de dados filtrados**:
  - Exportação para CSV.
- **Layout com colunas e métricas**:
  - Comparação de métricas (Valor e Nota).
  - Resumo estatístico.

---

## 🛠️ Tecnologias utilizadas

- [Python 3.x](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [Pillow](https://python-pillow.org/) (para imagens)

---

## ▶️ Como executar

1. Clone este repositório ou copie o arquivo `app.py`.
2. Instale as dependências:
   ```bash
   pip install streamlit pandas matplotlib seaborn pillow
