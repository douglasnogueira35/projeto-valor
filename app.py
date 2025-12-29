import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

# -------------------------------
# Configuração inicial
# -------------------------------
st.set_page_config(
    page_title="Exercício Completo com Streamlit",
    page_icon="C:/Users/dougl/Downloads/telmarketing_icon.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------
# Tema escuro com fundo preto
# -------------------------------
st.markdown(
    """
    <style>
    .stApp {
        background-color: #000000;
        color: #f0f0f0;
    }
    h1 {
        color: #ffffff;
        text-align: center;
        font-weight: bold;
    }
    h2, h3 {
        color: #ffcc00;
    }
    .stButton>button {
        background-color: #333333;
        color: #ffffff;
        border-radius: 8px;
        padding: 8px 16px;
        font-weight: bold;
        border: 1px solid #ffffff;
    }
    .stButton>button:hover {
        background-color: #ffcc00;
        color: #000000;
    }
    .css-1d391kg {
        background-color: #111111;
        color: #f0f0f0;
    }
    .stTextInput>div>div>input,
    .stSelectbox>div>div>div,
    .stMultiSelect>div>div>div {
        background-color: #222222;
        color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Imagem no topo
st.image("C:/Users/dougl/Downloads/telmarketing_icon.png", width=120)

# Título e descrição
st.title("Exercício Completo com Streamlit")
st.write("Laboratório interativo de dados 🚀")
st.markdown("---")

# -------------------------------
# Cache para acelerar
# -------------------------------
@st.cache_data
def carregar_dados():
    data = pd.DataFrame({
        "Categoria": ["A", "B", "C", "A", "B", "C"],
        "Valor": [10, 20, 30, 40, 50, 60],
        "Ano": [2020, 2021, 2022, 2020, 2021, 2022],
        "Região": ["Norte", "Sul", "Leste", "Oeste", "Norte", "Sul"],
        "Produto": ["X", "Y", "Z", "X", "Y", "Z"],
        "Cliente": ["João", "Maria", "Pedro", "Ana", "Lucas", "Carla"],
        "Canal": ["Online", "Loja", "Online", "Loja", "Online", "Loja"],
        "Status": ["Ativo", "Inativo", "Ativo", "Ativo", "Inativo", "Ativo"],
        "Nota": [7, 8, 9, 6, 5, 10]
    })
    return data

df = carregar_dados()

# -------------------------------
# Criando abas
# -------------------------------
aba1, aba2, aba3, aba4, aba5 = st.tabs(
    ["📊 Filtros e Gráficos", "📝 Formulário", "🎛️ Filtros múltiplos", "📂 Upload/Download", "📈 Colunas e Métricas"]
)

# -------------------------------
# Aba 1 - Filtros e Gráficos
# -------------------------------
with aba1:
    st.subheader("Filtros na barra lateral")
    filtro_valor = st.sidebar.slider("Selecione o valor mínimo", min_value=0, max_value=60, value=10)
    df_filtrado = df[df["Valor"] >= filtro_valor]

    categorias = st.sidebar.multiselect("Escolha categorias", df["Categoria"].unique(), df["Categoria"].unique())
    df_filtrado = df_filtrado[df_filtrado["Categoria"].isin(categorias)]

    st.write("### Dados após filtros")
    st.write(df_filtrado)

    fig, ax = plt.subplots(1, 2, figsize=(8,4))
    sns.barplot(data=df, x="Categoria", y="Valor", ax=ax[0])
    ax[0].set_title("Dados brutos", fontweight="bold")

    sns.barplot(data=df_filtrado, x="Categoria", y="Valor", ax=ax[1])
    ax[1].set_title("Dados filtrados", fontweight="bold")

    st.write("### Comparação dos dados")
    st.pyplot(fig)

# -------------------------------
# Aba 2 - Formulário
# -------------------------------
with aba2:
    st.subheader("Formulário de exemplo")
    with st.form("formulario"):
        nome = st.text_input("Digite seu nome")
        enviar = st.form_submit_button("Enviar")
        if enviar:
            st.success(f"Formulário enviado por {nome}!")

# -------------------------------
# Aba 3 - Filtros múltiplos
# -------------------------------
with aba3:
    st.subheader("Filtros múltiplos (9 colunas)")
    colunas = ["Categoria","Ano","Região","Produto","Cliente","Canal","Status","Nota","Valor"]
    filtros = {}
    for col in colunas:
        opcoes = st.multiselect(f"Filtrar por {col}", df[col].unique())
        if opcoes:
            filtros[col] = opcoes

    df_multi = df.copy()
    for col, opcoes in filtros.items():
        df_multi = df_multi[df_multi[col].isin(opcoes)]

    st.write("Resultado dos filtros múltiplos:", df_multi)

# -------------------------------
# Aba 4 - Upload/Download
# -------------------------------
with aba4:
    st.subheader("Upload de arquivo CSV")
    arquivo = st.file_uploader("Carregue um arquivo CSV")
    if arquivo:
        df_upload = pd.read_csv(arquivo)
        st.write(df_upload.head())

    st.subheader("Download de dados")
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("Baixar dataset filtrado", csv, "dados.csv", "text/csv")

# -------------------------------
# Aba 5 - Colunas e Métricas
# -------------------------------
with aba5:
    st.subheader("Visualização com colunas")
    col1, col2 = st.columns(2)

    with col1:
        escolha = st.radio("Escolha uma métrica", ["Valor", "Nota"])
        fig2, ax2 = plt.subplots()
        sns.boxplot(data=df, x="Categoria", y=escolha, ax=ax2)
        st.pyplot(fig2)

    with col2:
        st.write("Resumo estatístico")
        st.write(df[escolha].describe())