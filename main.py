from pokedex import Pokedex

dex = Pokedex("Pokedex", "Pokemons")

print("Mostrando o pokemon numero 151")
print(dex.get_pokemon_by_id(151))
print()

print("Pokemons com Speed maiores ou igual a 100:")
pokemons = dex.get_pokemons_by_Speed()
for pokemon in pokemons:
    print(pokemon)
print()

print("Pokemons com Attack maiores ou igual a 120:")
pokemons = dex.get_pokemons_by_Atk()
for pokemon in pokemons:
    print(pokemon)
print()

print("Pokemons com Defense menores ou igual a 50:")
pokemons = dex.get_pokemons_by_Def()
for pokemon in pokemons:
    print(pokemon)
print()

print("Pokemons do tipo dragao:")
pokemons = dex.get_pokemons_by_type(["Dragon"])
for pokemon in pokemons:
    print(pokemon)
