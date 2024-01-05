App de Análise de Ações
Este é um aplicativo desenvolvido em Streamlit para análise de ações. Ele fornece uma interface simples para visualizar gráficos históricos de preços de ações, bem como permitir que os usuários deixem comentários sobre a ação escolhida. Além disso, oferece a funcionalidade de exportar os dados da ação para um arquivo CSV.

Como Usar o App
Escolha uma Ação:

No painel lateral, você pode selecionar uma ação entre diversas opções clicáveis, incluindo Microsoft Corporation, Google, Amazon, Tesla, e outras.
Visualize o Gráfico e Tabela:

Após escolher uma ação, o app exibirá um gráfico interativo com o histórico de preços de fechamento da ação. Uma tabela com estatísticas descritivas também é apresentada.
Exporte Dados para CSV:

Logo abaixo do gráfico, você encontrará um botão "Exportar para CSV". Clique nesse botão para baixar os dados da ação em formato CSV.
Deixe um Comentário:

Abaixo da tabela, você pode inserir seu nome de usuário e deixar um comentário sobre a ação. Clique em "Salvar Comentário" para registrar sua opinião.
Visualize e Exclua Comentários:

Abaixo do formulário de comentário, você pode visualizar os comentários existentes ordenados por timestamp. Há também um botão "Excluir Comentários" para limpar todos os comentários.
Tecnologias Utilizadas
Streamlit: Biblioteca de criação de aplicativos web simples e interativos em Python.
Pandas: Para manipulação de dados e criação de tabelas.
YFinance: Para obter dados históricos de preços de ações.
Firebase: Para armazenar e recuperar comentários dos usuários.
Base64: Para permitir o download de arquivos CSV gerados.
