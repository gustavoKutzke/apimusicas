import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request
import datetime
import json
from flask import Response

# ===========================================================================================
# Generos
# ===========================================================================================

@app.route('/generos/criar', methods=['POST'])
def post_generos():
    try:        
        _json = request.json
        _descricao = _json['descricao']

        if _descricao and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)		
            sqlQuery = "INSERT INTO generos (descricao) VALUES (%s)"
            bindData = (_descricao)            
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            cursor.close() 
            respone = jsonify('Genero criado com sucesso!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as err:
        print(err)
    finally:
        
        conn.close()          
    
@app.route('/generos')
def get_generos():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT genero_id, descricao FROM generos")
        empRows = cursor.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as err:
        print(err)
    finally:
        cursor.close() 
        conn.close()  

@app.route('/generos/<int:genero_id>')
def get_generos_id(genero_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT genero_id, descricao FROM generos WHERE genero_id =%s", genero_id)
        empRow = cursor.fetchone()
        respone = jsonify(empRow)
        respone.status_code = 200
        return respone
    except Exception as err:
        print(err)
    finally:
        cursor.close() 
        conn.close() 

@app.route('/generos/atualizar', methods=['PUT'])
def put_generos():
    try:
        _json = request.json
        _genero_id = _json['genero_id']
        _descricao = _json['descricao']

        if _descricao and _genero_id and request.method == 'PUT':			
            sqlQuery = "UPDATE generos SET descricao=%s WHERE genero_id=%s"
            bindData = (_descricao, _genero_id,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Genero atualizado com sucesso!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as err:
        print(err)
    finally:
        cursor.close() 
        conn.close() 

@app.route('/generos/deletar/<int:genero_id>', methods=['DELETE'])
def delete_generos(genero_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM generos WHERE genero_id =%s", (genero_id,))
        conn.commit()
        respone = jsonify('Genero deletado com sucesso!')
        respone.status_code = 200
        return respone
    except Exception as err:
        print(err)
    finally:
        cursor.close() 
        conn.close()
        
@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Registro nao encontrado: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone

# ===========================================================================================
# Musicas
# ===========================================================================================

@app.route('/musicas/criar', methods=['POST'])
def post_musicas():
    try:        
        _json = request.json
        _nome = _json['nome']
        _genero_id = _json['genero_id']
        _duracao = str(_json['duracao'])
        _lancamento = str(_json['lancamento'])

        if _nome and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)		
            sqlQuery = "INSERT INTO musicas (nome, genero_id, duracao, lancamento) VALUES (%s, %s, %s, %s)"
            bindData = (_nome, _genero_id, _duracao, _lancamento,)            
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            cursor.close() 
            respone = jsonify('Musica criada com sucesso!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as err:
        print(err)
    finally:
        
        conn.close()

@app.route('/musicas')
def get_musicas():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT musica_id, nome, genero_id, CAST(duracao AS CHAR) AS duracao, CAST(lancamento AS CHAR) AS lancamento FROM musicas")
        empRows = cursor.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as err:
        print(err)
    finally:
        cursor.close()
        conn.close()

@app.route('/musicas/<int:musica_id>')
def get_musicas_id(musica_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT musica_id, nome, genero_id, CAST(duracao AS CHAR) AS duracao, CAST(lancamento AS CHAR) AS lancamento FROM musicas WHERE musica_id =%s", musica_id)
        empRow = cursor.fetchone()
        respone = jsonify(empRow)
        respone.status_code = 200
        return respone
    except Exception as err:
        print(err)
    finally:
        cursor.close() 
        conn.close() 

@app.route('/musicas/atualizar', methods=['PUT'])
def put_musicas():
    try:
        _json = request.json
        _musica_id = _json['musica_id']
        _nome = _json['nome']
        _genero_id = _json['genero_id']
        _duracao = str(_json['duracao'])
        _lancamento = str(_json['lancamento'])

        if _nome and _genero_id and _musica_id and request.method == 'PUT':			
            sqlQuery = "UPDATE musicas SET nome=%s, genero_id=%s, duracao=%s, lancamento=%s WHERE musica_id=%s"
            bindData = (_nome, _genero_id, _duracao, _lancamento, _musica_id,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Musica atualizada com sucesso!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as err:
        print(err)
    finally:
        cursor.close() 
        conn.close() 

@app.route('/musicas/deletar/<int:musica_id>', methods=['DELETE'])
def delete_musicas(musica_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM musicas WHERE musica_id =%s", (musica_id,))
        conn.commit()
        respone = jsonify('Musica deletada com sucesso!')
        respone.status_code = 200
        return respone
    except Exception as err:
        print(err)
    finally:
        cursor.close() 
        conn.close()
        
@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Registro nao encontrado: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone

# ===========================================================================================
# Gravadoras
# ===========================================================================================

@app.route('/gravadoras/criar', methods=['POST'])
def post_gravadoras():
    try:        
        _json = request.json
        _nome = _json['nome']
        _valor_contrato = str(_json['valor_contrato'])
        _vencimento_contrato = str(_json['vencimento_contrato'])

        if _nome and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)		
            sqlQuery = "INSERT INTO gravadoras (nome, valor_contrato, vencimento_contrato) VALUES (%s, %s, %s)"
            bindData = (_nome, _valor_contrato, _vencimento_contrato,)            
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            cursor.close() 
            respone = jsonify('Gravadora criada com sucesso!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as err:
        print(err)
    finally:
        
        conn.close()

@app.route('/gravadoras')
def get_gravadoras():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT gravadora_id, nome, valor_contrato, CAST(vencimento_contrato AS CHAR) AS vencimento_contrato FROM gravadoras")
        empRows = cursor.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as err:
        print(err)
    finally:
        cursor.close() 
        conn.close()  

@app.route('/gravadoras/<int:gravadora_id>')
def get_gravadoras_id(gravadora_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT gravadora_id, nome, valor_contrato, CAST(vencimento_contrato AS CHAR) AS vencimento_contrato FROM gravadoras WHERE gravadora_id =%s", gravadora_id)
        empRow = cursor.fetchone()
        respone = jsonify(empRow)
        respone.status_code = 200
        return respone
    except Exception as err:
        print(err)
    finally:
        cursor.close() 
        conn.close() 

@app.route('/gravadoras/atualizar', methods=['PUT'])
def put_gravadoras():
    try:
        _json = request.json
        _gravadora_id = _json['gravadora_id']
        _nome = _json['nome']

        if _nome and _gravadora_id and request.method == 'PUT':			
            sqlQuery = "UPDATE gravadoras SET nome=%s, valor_contrato=%s, vencimento_contrato=%s WHERE gravadora_id=%s"
            bindData = (_nome, _gravadora_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Gravadora atualizada com sucesso!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as err:
        print(err)
    finally:
        cursor.close() 
        conn.close() 

@app.route('/gravadoras/deletar/<int:gravadora_id>', methods=['DELETE'])
def delete_gravadoras(gravadora_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM gravadoras WHERE gravadora_id =%s", (gravadora_id,))
        conn.commit()
        respone = jsonify('Gravadora deletada com sucesso!')
        respone.status_code = 200
        return respone
    except Exception as err:
        print(err)
    finally:
        cursor.close() 
        conn.close()
        
@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Registro nao encontrado: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone

# ===========================================================================================
# Artistas
# ===========================================================================================

@app.route('/artistas/criar', methods=['POST'])
def post_artistas():
    try:        
        _json = request.json
        _nome = _json['nome']
        _gravadora_id = _json['gravadora_id']

        if _nome and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)		
            sqlQuery = "INSERT INTO artistas (nome, gravadora_id) VALUES (%s, %s)"
            bindData = (_nome, _gravadora_id)            
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            cursor.close() 
            respone = jsonify('Artista criado com sucesso!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as err:
        print(err)
    finally:
        
        conn.close()

@app.route('/artistas')
def get_artistas():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT artista_id, nome, gravadora_id FROM artistas")
        empRows = cursor.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as err:
        print(err)
    finally:
        cursor.close() 
        conn.close()  

@app.route('/artistas/<int:artista_id>')
def get_artistas_id(artista_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT artista_id, nome, gravadora_id FROM artistas WHERE artista_id =%s", artista_id)
        empRow = cursor.fetchone()
        respone = jsonify(empRow)
        respone.status_code = 200
        return respone
    except Exception as err:
        print(err)
    finally:
        cursor.close() 
        conn.close() 

@app.route('/artistas/atualizar', methods=['PUT'])
def put_artistas():
    try:
        _json = request.json
        _artista_id = _json['artista_id']
        _nome = _json['nome']
        _gravadora_id = _json['gravadora_id']

        if _nome and _gravadora_id and _artista_id and request.method == 'PUT':			
            sqlQuery = "UPDATE artistas SET nome=%s, gravadora_id=%s WHERE artista_id=%s"
            bindData = (_nome, _gravadora_id, _artista_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Artista atualizado com sucesso!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as err:
        print(err)
    finally:
        cursor.close() 
        conn.close() 

@app.route('/artistas/deletar/<int:artista_id>', methods=['DELETE'])
def delete_artistas(artista_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM artistas WHERE artista_id =%s", (artista_id,))
        conn.commit()
        respone = jsonify('Artista deletado com sucesso!')
        respone.status_code = 200
        return respone
    except Exception as err:
        print(err)
    finally:
        cursor.close() 
        conn.close()
        
@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Registro nao encontrado: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone

# ===========================================================================================
# Musicas_has_artistas
# ===========================================================================================

@app.route('/musicas_has_artistas/criar', methods=['POST'])
def post_musicas_has_artistas():
    try:        
        _json = request.json
        _musica_id = _json['musica_id']
        _artista_id = _json['artista_id']

        if _musica_id and _artista_id and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)		
            sqlQuery = "INSERT INTO musicas_has_artistas (musica_id, artista_id) VALUES (%s, %s)"
            bindData = (_musica_id, _artista_id)       
            cursor.execute(sqlQuery, bindData)  
            conn.commit()
            cursor.close() 
            respone = jsonify('Musica_has_artista criado com sucesso!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as err:
        print(err)
    finally:
        
        conn.close()

@app.route('/musicas_has_artistas')
def get_musicas_has_artistas():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT musica_has_artista_id, musica_id, artista_id FROM musicas_has_artistas")
        empRows = cursor.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as err:
        print(err)
    finally:
        cursor.close() 
        conn.close()  

@app.route('/musicas_has_artistas/<int:musica_has_artista_id>')
def get_musicas_has_artistas_id(musica_has_artista_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT musica_has_artista_id, musica_id, artista_id FROM musicas_has_artistas WHERE musica_has_artista_id =%s", musica_has_artista_id)
        empRow = cursor.fetchone()
        respone = jsonify(empRow)
        respone.status_code = 200
        return respone
    except Exception as err:
        print(err)
    finally:
        cursor.close() 
        conn.close() 

@app.route('/musicas_has_artistas/atualizar', methods=['PUT'])
def put_musicas_has_artistas():
    try:
        _json = request.json
        _musica_has_artista_id = _json['musica_has_artista_id']
        _musica_id = _json['musica_id']
        _artista_id = _json['artista_id']

        if _musica_id and _artista_id and _musica_has_artista_id and request.method == 'PUT':			
            sqlQuery = "UPDATE musicas_has_artistas SET musica_id=%s, artista_id=%s WHERE musica_has_artista_id=%s"
            bindData = (_musica_id, _artista_id, _musica_has_artista_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Musica_has_artista atualizado com sucesso!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as err:
        print(err)
    finally:
        cursor.close() 
        conn.close() 

@app.route('/musicas_has_artistas/deletar/<int:musica_has_artista_id>', methods=['DELETE'])
def delete_musicas_has_artistas(musica_has_artista_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM musicas_has_artistas WHERE musica_has_artista_id =%s", (musica_has_artista_id,))
        conn.commit()
        respone = jsonify('Musica_has_artista deletado com sucesso!')
        respone.status_code = 200
        return respone
    except Exception as err:
        print(err)
    finally:
        cursor.close() 
        conn.close()
        
@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Registro nao encontrado: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone

# ===========================================================================================
# Planos
# ===========================================================================================

@app.route('/planos/criar', methods=['POST'])
def post_planos():
    try:        
        _json = request.json
        _descricao = _json['descricao']
        _limite = _json['limite']
        _valor = str(_json['valor'])

        if _descricao and _limite and _valor and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)		
            sqlQuery = "INSERT INTO planos (descricao, limite, valor) VALUES (%s, %s, %s)"
            bindData = (_descricao, _limite, _valor,)            
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            cursor.close() 
            respone = jsonify('Plano criado com sucesso!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as err:
        print(err)
    finally:
        
        conn.close()

@app.route('/planos')
def get_planos():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT plano_id, descricao, limite, CAST(valor AS CHAR) AS valor FROM planos")
        empRows = cursor.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as err:
        print(err)
    finally:
        cursor.close() 
        conn.close()  

@app.route('/planos/<int:plano_id>')
def get_planos_id(plano_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT plano_id, descricao, limite, CAST(valor AS CHAR) AS valor FROM planos WHERE plano_id =%s", plano_id)
        empRow = cursor.fetchone()
        respone = jsonify(empRow)
        respone.status_code = 200
        return respone
    except Exception as err:
        print(err)
    finally:
        cursor.close() 
        conn.close() 

@app.route('/planos/atualizar', methods=['PUT'])
def put_planos():
    try:
        _json = request.json
        _plano_id = _json['plano_id']
        _descricao = _json['descricao']
        _limite = _json['limite']

        if _descricao and _limite and _plano_id and request.method == 'PUT':			
            sqlQuery = "UPDATE planos SET descricao=%s, limite=%s, valor=%s WHERE plano_id=%s"
            bindData = (_descricao, _limite, _plano_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Plano atualizado com sucesso!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as err:
        print(err)
    finally:
        cursor.close() 
        conn.close() 

@app.route('/planos/deletar/<int:plano_id>', methods=['DELETE'])
def delete_planos(plano_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM planos WHERE plano_id =%s", (plano_id,))
        conn.commit()
        respone = jsonify('Plano deletado com sucesso!')
        respone.status_code = 200
        return respone
    except Exception as err:
        print(err)
    finally:
        cursor.close() 
        conn.close()
        
@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Registro nao encontrado: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone

# ===========================================================================================
# Clientes
# ===========================================================================================

@app.route('/clientes/criar', methods=['POST'])
def post_clientes():
    try:        
        _json = request.json
        _login = _json['login']
        _senha = _json['senha']
        _email = _json['email']
        _plano_id = _json['plano_id']

        if _login and _senha and _email and _plano_id and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)		
            sqlQuery = "INSERT INTO clientes (login, senha, email, plano_id) VALUES (%s, %s, %s, %s)"
            bindData = (_login, _senha, _email, _plano_id)            
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            cursor.close() 
            respone = jsonify('Cliente criado com sucesso!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as err:
        print(err)
    finally:
        
        conn.close()

@app.route('/clientes')
def get_clientes():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT cliente_id, login, senha, email, plano_id FROM clientes")
        empRows = cursor.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as err:
        print(err)
    finally:
        cursor.close() 
        conn.close()  

@app.route('/clientes/<int:cliente_id>')
def get_clientes_id(cliente_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT cliente_id, login, senha, email, plano_id FROM clientes WHERE cliente_id =%s", cliente_id)
        empRow = cursor.fetchone()
        respone = jsonify(empRow)
        respone.status_code = 200
        return respone
    except Exception as err:
        print(err)
    finally:
        cursor.close() 
        conn.close() 

@app.route('/clientes/atualizar', methods=['PUT'])
def put_clientes():
    try:
        _json = request.json
        _cliente_id = _json['cliente_id']
        _login = _json['login']
        _senha = _json['senha']
        _email = _json['email']
        _plano_id = _json['plano_id']

        if _login and _senha and _email and _plano_id and _cliente_id and request.method == 'PUT':			
            sqlQuery = "UPDATE clientes SET login=%s, senha=%s, email=%s, plano_id=%s WHERE cliente_id=%s"
            bindData = (_login, _senha, _email, _plano_id, _cliente_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Cliente atualizado com sucesso!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as err:
        print(err)
    finally:
        cursor.close() 
        conn.close() 

@app.route('/clientes/deletar/<int:cliente_id>', methods=['DELETE'])
def delete_clientes(cliente_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM clientes WHERE cliente_id =%s", (cliente_id,))
        conn.commit()
        respone = jsonify('Cliente deletado com sucesso!')
        respone.status_code = 200
        return respone
    except Exception as err:
        print(err)
    finally:
        cursor.close() 
        conn.close()
        
@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Registro nao encontrado: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone

# ===========================================================================================
# Musicas_has_clientes
# ===========================================================================================

@app.route('/musicas_has_clientes/criar', methods=['POST'])
def post_musicas_has_clientes():
    try:        
        _json = request.json
        _musica_id = _json['musica_id']
        _cliente_id = _json['cliente_id']
        _data = str(_json['data'])

        if _musica_id and _cliente_id and _data and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)		
            sqlQuery = "INSERT INTO musicas_has_clientes (musica_id, cliente_id, data) VALUES (%s, %s, %s)"
            bindData = (_musica_id, _cliente_id, _data,)       
            cursor.execute(sqlQuery, bindData)  
            conn.commit()
            cursor.close() 
            respone = jsonify('Musica_has_cliente criado com sucesso!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as err:
        print(err)
    finally:
        
        conn.close()

@app.route('/musicas_has_clientes')
def get_musicas_has_clientes():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT musica_has_cliente_id, musica_id, cliente_id, CAST(data AS CHAR) AS data FROM musicas_has_clientes")
        empRows = cursor.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as err:
        print(err)
    finally:
        cursor.close() 
        conn.close()  

@app.route('/musicas_has_clientes/<int:musica_has_cliente_id>')
def get_musicas_has_clientes_id(musica_has_cliente_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT musica_has_cliente_id, musica_id, cliente_id, CAST(data AS CHAR) AS data FROM musicas_has_clientes WHERE musica_has_cliente_id =%s", musica_has_cliente_id)
        empRow = cursor.fetchone()
        respone = jsonify(empRow)
        respone.status_code = 200
        return respone
    except Exception as err:
        print(err)
    finally:
        cursor.close() 
        conn.close() 

@app.route('/musicas_has_clientes/atualizar', methods=['PUT'])
def put_musicas_has_clientes():
    try:
        _json = request.json
        _musica_has_cliente_id = _json['musica_has_cliente_id']
        _musica_id = _json['musica_id']
        _cliente_id = _json['cliente_id']

        if _musica_id and _cliente_id and _musica_has_cliente_id and request.method == 'PUT':			
            sqlQuery = "UPDATE musicas_has_clientes SET musica_id=%s, cliente_id=%s, data=%s WHERE musica_has_cliente_id=%s"
            bindData = (_musica_id, _cliente_id, _musica_has_cliente_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Musica_has_cliente atualizado com sucesso!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as err:
        print(err)
    finally:
        cursor.close() 
        conn.close() 

@app.route('/musicas_has_clientes/deletar/<int:musica_has_cliente_id>', methods=['DELETE'])
def delete_musicas_has_clientes(musica_has_cliente_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM musicas_has_clientes WHERE musica_has_cliente_id =%s", (musica_has_cliente_id,))
        conn.commit()
        respone = jsonify('Musica_has_cliente deletado com sucesso!')
        respone.status_code = 200
        return respone
    except Exception as err:
        print(err)
    finally:
        cursor.close() 
        conn.close()
        
@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Registro nao encontrado: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone

# ===========================================================================================
# Pagamentos
# ===========================================================================================

@app.route('/pagamentos/criar', methods=['POST'])
def post_pagamentos():
    try:        
        _json = request.json
        _data = str(_json['data'])

        if _data and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)		
            sqlQuery = "INSERT INTO pagamentos (data) VALUES (%s)"
            bindData = (_data,)            
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            cursor.close() 
            respone = jsonify('Pagamento criado com sucesso!',)
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as err:
        print(err)
    finally:
        
        conn.close()

@app.route('/pagamentos')
def get_pagamentos():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT pagamento_id, CAST(data AS CHAR) AS data FROM pagamentos")
        empRows = cursor.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as err:
        print(err)
    finally:
        cursor.close() 
        conn.close()  

@app.route('/pagamentos/<int:pagamento_id>')
def get_pagamentos_id(pagamento_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT pagamento_id, CAST(data AS CHAR) AS data FROM pagamentos WHERE pagamento_id =%s", pagamento_id)
        empRow = cursor.fetchone()
        respone = jsonify(empRow)
        respone.status_code = 200
        return respone
    except Exception as err:
        print(err)
    finally:
        cursor.close() 
        conn.close() 

@app.route('/pagamentos/atualizar', methods=['PUT'])
def put_pagamentos():
    try:
        _json = request.json
        _pagamento_id = _json['pagamento_id']
        _data = _json['data']

        if _data and _pagamento_id and request.method == 'PUT':			
            sqlQuery = "UPDATE pagamentos SET data=%s WHERE pagamento_id=%s"
            bindData = (_data, _pagamento_id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Pagamento atualizado com sucesso!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as err:
        print(err)
    finally:
        cursor.close() 
        conn.close() 

@app.route('/pagamentos/deletar/<int:pagamento_id>', methods=['DELETE'])
def delete_pagamentos(pagamento_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM pagamentos WHERE pagamento_id =%s", (pagamento_id,))
        conn.commit()
        respone = jsonify('Pagamento deletado com sucesso!')
        respone.status_code = 200
        return respone
    except Exception as err:
        print(err)
    finally:
        cursor.close() 
        conn.close()
        
@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Registro nao encontrado: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone

# ==============================================================================================          
        
if __name__ == "__main__":
    app.run()