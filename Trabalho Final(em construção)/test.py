from conexao import Conexao
import dotenv 
import os
from pokemon import pokemons

dotenv.load_dotenv()

conexaoBanco = Conexao(os.getenv("NAMEDB"), os.getenv("HOSTDB"), os.getenv("PORTDB"), os.getenv("USERNAMEDB"), os.getenv("PASSWORDDB"))

# conexaoBanco.manipularBanco(pokemons)

print(conexaoBanco.consultarBanco('''Select * from "Pokedex"'''))