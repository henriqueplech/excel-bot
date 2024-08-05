import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Tabela de Dados", page_icon=":bar_chart:", layout="wide")

st.title("Visualizador de Planilhas Excel")

# Função para carregar o arquivo XLSX
def load_data(file):
    data = pd.read_excel(file)
    return data

# Botão para upload do arquivo
uploaded_file = st.file_uploader("Selecione um arquivo Excel (.xlsx)", type=["xlsx"])

if uploaded_file is not None:
    df = load_data(uploaded_file)
    
    # Campo de busca
    search = st.text_input("Buscar nos dados")
    
    # Ordenação
    sort_by = st.selectbox("Ordenar por", df.columns)

    # Filtragem dos dados
    if search:
        df = df[df.apply(lambda row: search.lower() in row.astype(str).str.lower().values, axis=1)]

    # Ordenar os dados
    df = df.sort_values(by=sort_by)
    
    # Paginação
    n = st.number_input("Linhas por página", min_value=1, max_value=len(df), value=10)
    page_number = st.number_input("Página", min_value=1, max_value=(len(df) // n) + 1, value=1)
    
    start_idx = (page_number - 1) * n
    end_idx = start_idx + n
    
    paginated_df = df.iloc[start_idx:end_idx]

    # Exibição da tabela
    st.write(paginated_df)

    # Exibir informações sobre a tabela
    st.write(f"Mostrando página {page_number} de {(len(df) // n) + 1}")

else:
    st.info("Por favor, carregue um arquivo Excel para visualizar os dados.")