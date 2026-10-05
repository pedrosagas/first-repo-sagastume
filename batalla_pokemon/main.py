from random import choice
from time import sleep

#Pokemon
pikachu = {
    "nombre": "Pikachu",
    "tipo": "electrico",
    "hp": 60,
    "ad": 15
}

chikorita = {
    "nombre": "Chikorita",
    "tipo": "planta",
    "hp": 45,
    "ad": 10
}

charmander = {
    "nombre": "Charmander",
    "tipo": "fuego",
    "hp": 40,
    "ad": 10
}
froakie = {
    "nombre": "Froakie",
    "tipo": "agua",
    "hp": 40,
    "ad": 20
}


pokemon_posibles = [pikachu, chikorita, charmander,froakie]

#tiempo de pausa 
def waiting():
    print("\n...")
    sleep(0.5)


#eleccion random de pokemon
poke_1 = choice(pokemon_posibles)
poke_2 = choice(pokemon_posibles)

while poke_2 == poke_1:
    poke_2 = choice(pokemon_posibles)

# info pokemon elegido 
print("\n Pokemon Elegidos")

waiting()

print(f"\nPokemon 1: {poke_1['nombre']} (HP: {poke_1['hp']} , AD: {poke_1['ad']})")
print(f"Pokemon 2: {poke_2['nombre']} (HP: {poke_2['hp']} , AD: {poke_2['ad']})")

# perdida de vida pokemon
def damage(pokemon, hp_lost):
    pokemon["hp"] = pokemon["hp"] - hp_lost

#definir ataques 
def attack(attacker, rival):
    if attacker["tipo"] == "electrico":
        ataque = "Impactrueno"
    elif attacker["tipo"] == "planta":
        ataque = "Hoja navaja"
    elif attacker["tipo"] == "fuego":
        ataque = "Llamarada"
    else:
        ataque = "Cañon de agua"

    damage(rival, attacker["ad"])

    print(f"\n({attacker['nombre']}) Ataca con {ataque} | -{attacker['ad']}")

    #turnos en pelea

while True:
    waiting()
    attack(poke_1, poke_2)

    if poke_2["hp"] <= 0:
        print(f"\nGAME OVER: {poke_1['nombre']} venció a {poke_2['nombre']}")
        break

    waiting()
    attack(poke_2, poke_1)

    if poke_1["hp"] <= 0:
        print(f"\nGAME OVER: {poke_2['nombre']} venció a {poke_1['nombre']}")
        break

    waiting()
    print("\nHPs restantes")
    print(f"{poke_1['nombre']}: {poke_1['hp']}")
    print(f"{poke_2['nombre']}: {poke_2['hp']}")
