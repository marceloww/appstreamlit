import time  # Biblioteca para manipulação de tempo.
import os  # Biblioteca para interação com o sistema operacional.
import streamlit as st  # Framework para criação de aplicativos web em Python.
import pandas as pd  # Biblioteca para manipulação e análise de dados em Python.
import yfinance as yf  # API para obter dados históricos de preços de ações.
from datetime import datetime  # Biblioteca para manipulação de datas e horas.
import firebase_admin  # SDK para integração com o Firebase.
from firebase_admin import credentials, firestore  # Componentes específicos do Firebase.
import base64  # Biblioteca para codificação e decodificação de dados no formato base64(Para permitir o download do arquivo CSV gerado).


def inicializar_firebase():
    print("Inicializando o Firebase...")
    if not firebase_admin._apps:
        try:
            cred = credentials.Certificate(os.environ.get('FIREBASE_CREDENTIALS'))
            firebase_admin.initialize_app(cred)
            print("Firebase inicializado com sucesso!")
        except ValueError as e:
            print(f"Erro ao inicializar o aplicativo Firebase: {e}")

# Chamar a função para inicializar o Firebase
inicializar_firebase()




# Função para obter dados da ação
def obter_dados_acao(symbol, start_date, end_date):
    df = yf.download(symbol, start=start_date, end=end_date)
    return df


# Função para salvar comentários no Firestore
def salvar_comentario_firestore(symbol, usuario, comentario):
    db = firestore.client()
    data = {"Symbol": symbol, "Username": usuario, "Content": comentario, "Timestamp": datetime.now()}
    db.collection("Comentarios").add(data)


# Função para validar os dados do usuário
def validar_dados(usuario, comentario):
    if not usuario or not comentario:
        return False
    return True

# Função para exportar dados para CSV
def exportar_para_csv(dados_acao, symbol):
    # Certifique-se de que o diretório 'exports' exista
    if not os.path.exists('exports'):
        os.makedirs('exports')

    # Nome do arquivo CSV
    nome_arquivo = f'exports/{symbol}_dados_acao.csv'

    # Exportar dados para CSV
    dados_acao.to_csv(nome_arquivo, index=False)

    # Criar link de download
    with open(nome_arquivo, 'rb') as f:
        dados = f.read()
        b64 = base64.b64encode(dados).decode()
        link = f'<a href="data:file/csv;base64,{b64}" download="{nome_arquivo}">Clique aqui para baixar o CSV</a>'

    st.markdown(link, unsafe_allow_html=True)
    st.success(f'Dados exportados para {nome_arquivo}')


# Função para criar a lista de exemplos de ações
def criar_lista_acoes_exemplos():
    return {
        "Microsoft Corporation": "MSFT",
        "Google (Alphabet Inc.)": "GOOGL",
        "Amazon.com Inc.": "AMZN",
        "Tesla Inc.": "TSLA",
        "Johnson & Johnson": "JNJ",
        "Procter & Gamble Co.": "PG",
        "Coca-Cola Company": "KO",
        "Apple Inc.": "AAPL",
        "Intel Corporation": "INTC",
        "Visa Inc.": "V",
        "Netflix Inc.": "NFLX",
        "Adobe Inc.": "ADBE"
    }


# Função para exibir gráfico e tabela da ação
def exibir_grafico_e_tabela(symbol, dados_acao):
    st.line_chart(dados_acao['Close'])
    st.header(f"Informações da Ação {symbol}")
    st.table(dados_acao.describe().transpose())


# Função para exibir formulário de comentário
def exibir_formulario_comentario():
    usuario = st.text_input("Nome de Usuário", max_chars=50)
    comentario = st.text_area("Comentário (Aqui pode salvar dados de pesquisa ou alguma sugestão)", max_chars=400)
    return usuario, comentario


# Função para exibir e salvar comentários
def exibir_e_salvar_comentarios(symbol):
    st.header("Comentários Existentes")
    comentarios = firestore.client().collection("Comentarios").order_by("Timestamp",
                                                                        direction=firestore.Query.DESCENDING).stream()
    for comentario in comentarios:
        data = comentario.to_dict()
        timestamp = data.get('Timestamp', datetime.now())
        formatted_timestamp = timestamp.strftime("%d/%m/%Y %H:%M:%S")
        st.write(f"({formatted_timestamp}) {data['Username']}: {data['Content']}")

    # Botão para excluir comentários existentes
    if st.button("Excluir Comentários"):
        comentarios = firestore.client().collection("Comentarios").list_documents()
        for comentario in comentarios:
            comentario.delete()
        st.success("Todos os comentários foram excluídos!")

        time.sleep(1)
        st.experimental_rerun()

# Página principal
def main():
    st.title("App de Análise de Ações")

    # Sidebar com filtros
    st.sidebar.header("Escolha uma ação:")

    # Criar lista de exemplos de ações
    acoes_exemplos = criar_lista_acoes_exemplos()

    # Adicionando botões clicáveis para exemplos de ações
    acao_escolhida = st.sidebar.radio("Selecione uma ação:", list(acoes_exemplos.keys()))

    # Adicionando o sub-título dinâmico
    st.subheader(f"Ação da {acao_escolhida}")

    # Obter dados da ação escolhida
    symbol = acoes_exemplos[acao_escolhida]
    start_date = st.sidebar.date_input("Data de início:", datetime(2022, 1, 1))
    end_date = st.sidebar.date_input("Data de término:", datetime.now())
    dados_acao = obter_dados_acao(symbol, start_date, end_date)

    # Exibir gráfico e tabela
    exibir_grafico_e_tabela(symbol, dados_acao)

    # Botão para exportar dados para CSV
    if st.button("Exportar para CSV"):
        exportar_para_csv(dados_acao, symbol)

    # Exibir formulário de comentário
    usuario, comentario = exibir_formulario_comentario()

    # Botão para salvar no Firebase
    if st.button("Salvar Comentário"):
        if validar_dados(usuario, comentario):
            salvar_comentario_firestore(symbol, usuario, comentario)
            st.success("Comentário salvo com sucesso!")
            usuario = ""
            comentario = ""
            time.sleep(1)
            st.experimental_rerun()
        else:
            st.warning("Por favor, preencha todos os campos.")

    # Exibir e salvar comentários
    exibir_e_salvar_comentarios(symbol)

# Executar o app
if __name__ == "__main__":
    main()
