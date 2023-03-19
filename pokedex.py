from database import Database
from save_json import writeAJson


class Pokedex:
    def __init__(self, nome_database, nome_collection):
        self.db = Database(nome_database, nome_collection)

    def get_pokemon_by_id(self, pokemon_id):
        retorno = self.db.collection.find_one({"id": pokemon_id})
        writeAJson(retorno, "get_pokemon_by_id")
        return retorno

    def get_pokemons_by_Atk(self):
        retorno = list(self.db.collection.find({"base.Attack": {"$gte": 120}}))
        writeAJson(retorno, "get_pokemons_by_Atk")
        return retorno

    def get_pokemons_by_Speed(self):
        retorno = list(self.db.collection.find({"base.Speed": {"$gte": 100}}))
        writeAJson(retorno, "get_pokemons_by_Speed")
        return retorno

    def get_pokemons_by_type(self, pokemon_type):
        retorno = list(self.db.collection.find({"type": {"$in": pokemon_type}}))
        writeAJson(retorno, "get_pokemon_by_type")
        return retorno

    def get_pokemons_by_Def(self):
        retorno = list(self.db.collection.find({"base.Defense": {"$lte": 50}}))
        writeAJson(retorno, "get_pokemons_by_Def")
        return retorno
