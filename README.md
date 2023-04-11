## Exemplo API

```Python
@api_bp.route("/exemplo1/api/v1.0/task")
def exemplo1():
    """Limit e offset """
    #produtos = Produtos.query.all()
    produtos = db.session.execute(select(Produtos).order_by(Produtos.cod_produto).limit(5).offset(1))
    #Gen
    dictsp = (prod.__dict__ for produto in produtos for prod in produto)
    #Mapeando usando list comp/Filtrando campos desejados
    new_dict = [{"sku":item["sku"],"valor":item["valor"],"data_atualizacao":item["data_atualizacao"]} for item in dictsp]
    print(new_dict)
    return jsonify(*new_dict)

```

<br>
Com a consulta produtos esta sendo usando um "limit(5)" ou seja 5 itens por pagina e o offset é a pagina 1. A ideia é pegar uma consulta que traria uma grande quantidade de resultados e dividir, inclusive o valor passado no limite e offset pode-se usar parametros do proprio endpoint. Outro ponto interessante é no dictsp eu basicamente estou pegando o retorno da query do ORM e convertendo em dicionarios e depois faço um mapeamento com um listcomp pegand apenas os campos que eu quero.

</br>


#Closures Function

<br>
Explicação simplificada:
A Ideia é simples Na parte de "Cima" se posso dizer assim, é feita a requisição na API externa, realiza-se normalmente, com o valor retornando, pode pegar na "parte de baixo" e fazer o return com jsonify, ou qualquer outra ação.

Explicação mais técnica

<br/>

```Python
#Closures Function
@api_bp.route("/exemplo2/api/v1.0/task")
def exemplo2():
    """faz requisição com requests"""
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
    r = requests.get(url)
    data = r.json()
    print(data)

    def retorna_json(*args, **kwds):
        """Retorna usando jsonify ou faz qualquer outra coisa que precisar"""
        return 
    return jsonify(data)

```
<br>
o exemplo acima, defino  a retorna_json() função dentro da função exemplo2()

Aqui, retorna_json()é uma função aninhada. A função aninhada funciona de maneira semelhante à função normal. Ele executa quando retorna_json()é chamado dentro da função exemplo2().
<br/>