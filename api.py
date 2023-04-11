from flask import Blueprint, make_response, jsonify, abort
from ..models.models import Produtos,Usuarios,OrderItem,Pedidos
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import  select
from sqlalchemy.orm import class_mapper
import json
from app import db
import requests

api_bp = Blueprint("api",__name__)

@api_bp.errorhandler(404)
def invalid_api_usage(e):
    return jsonify(e.to_dict()), e.status_code


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
   


#Closures Function
@api_bp.route("/exemplo2/api/v1.0/task")
def exemplo2():
    """faz requisição com requests"""
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
    r = requests.get(url)
    data = r.json()
    print(data)

    def wrapper(*args, **kwds):
        """Retorna usando jsonify ou faz qualquer outra coisa que precisar"""
        return 
    return jsonify(data)


      


    
  

    
  

  
    
   