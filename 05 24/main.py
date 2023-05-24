from flask import *
import psycopg2

class Conexao:

    def __init__(self, dbname, host, port, user, password):
        self._dbname = dbname
        self._host = host
        self._port = port
        self._user = user
        self._password = password

    def consultarBanco(self, sql):
        try:
            con = psycopg2.connect(dbname=self._dbname, host=self._host, port = self._port, user = self._user, password = self._password)
            cursor = con.cursor()

            cursor.execute(sql)

            resultado = cursor.fetchall()



            cursor.close()
            con.close()


            return resultado
        except(Exception, psycopg2.Error) as error:
            print("Ocorreu um erro no objeto Conexão:", error)

            return False

    def manipularBanco(self, sql):
        try:
            con = psycopg2.connect(dbname=self._dbname, host=self._host, port = self._port, user = self._user, password = self._password)
            cursor = con.cursor()

            cursor.execute(sql)


            con.commit()

            cursor.close()
            con.close()

            return True
        except(Exception, psycopg2.Error) as error:
            print("Ocorreu um erro:", error)

            return False
        
app = Flask(__name__)
conexaoBanco = Conexao("Pokemon","Localhost","5432","postgres","postgres")

@app.route('/')
def index():
    
    return render_template("index.html")

@app.route('/home')
def verPokemons():

    pokemons = conexaoBanco.consultarBanco('''
    Select * from "Pokedex"
    Order by "Id" ASC
    ''')
    
    if pokemons:
        return "Goodbye World"
    
    else:
        return "Ocorreu um erro"

if __name__ == "__main__":
    app.run(debug=True, port=5050)