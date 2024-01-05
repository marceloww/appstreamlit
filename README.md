<!DOCTYPE html>
<html>

<head>
    <title>App de Análise de Ações</title>
</head>

<body>

    <h1>App de Análise de Ações</h1>
    <p>Este é um aplicativo desenvolvido em Streamlit para análise de ações. Ele fornece uma interface simples para
        visualizar gráficos históricos de preços de ações, bem como permitir que os usuários deixem comentários sobre a
        ação escolhida. Além disso, oferece a funcionalidade de exportar os dados da ação para um arquivo CSV.</p>

    <h2>Como Usar o App</h2>

    <h3>Escolha uma Ação:</h3>
    <p>No painel lateral, você pode selecionar uma ação entre diversas opções clicáveis, incluindo Microsoft Corporation,
        Google, Amazon, Tesla, e outras.</p>

    <h3>Visualize o Gráfico e Tabela:</h3>
    <p>Após escolher uma ação, o app exibirá um gráfico interativo com o histórico de preços de fechamento da ação. Uma
        tabela com estatísticas descritivas também é apresentada.</p>

    <h3>Exporte Dados para CSV:</h3>
    <p>Logo abaixo do gráfico, você encontrará um botão "Exportar para CSV". Clique nesse botão para baixar os dados da
        ação em formato CSV.</p>

    <h3>Deixe um Comentário:</h3>
    <p>Abaixo da tabela, você pode inserir seu nome de usuário e deixar um comentário sobre a ação. Clique em "Salvar
        Comentário" para registrar sua opinião.</p>

    <h3>Visualize e Exclua Comentários:</h3>
    <p>Abaixo do formulário de comentário, você pode visualizar os comentários existentes ordenados por timestamp. Há
        também um botão "Excluir Comentários" para limpar todos os comentários.</p>

    <h2>Tecnologias Utilizadas</h2>
    <ul>
        <li><strong>Streamlit:</strong> Biblioteca de criação de aplicativos web simples e interativos em Python.</li>
        <li><strong>Pandas:</strong> Para manipulação de dados e criação de tabelas.</li>
        <li><strong>YFinance:</strong> Para obter dados históricos de preços de ações.</li>
        <li><strong>Firebase:</strong> Para armazenar e recuperar comentários dos usuários.</li>
        <li><strong>Base64:</strong> Para permitir o download de arquivos CSV gerados.</li>
    </ul>

    <h2>Como Executar o App Locamente</h2>
    <ol>
        <li>Certifique-se de ter todas as bibliotecas necessárias instaladas. Você pode instalá-las executando o seguinte
            comando:
            <pre>pip install streamlit pandas yfinance firebase-admin</pre>
        </li>
        <li>Faça o download do arquivo JSON da chave de serviço do Firebase e coloque-o no mesmo diretório do script
            com o nome <code>avaliacaoagro-707693a85b8c.json</code>.</li>
        <li>Execute o seguinte comando no terminal para iniciar o aplicativo:
            <pre>streamlit run nome_do_script.py</pre>
            Substitua <code>nome_do_script.py</code> pelo nome do seu script.
        </li>
        <li>O aplicativo estará acessível em seu navegador local.</li>
    </ol>

    <p>Divirta-se explorando e analisando ações!</p>

</body>

</html>
