import sqlite3
import random

# Fonction pour générer une liste de probabilités qui somme à 100
def generate_probabilities(n):
    total = 100
    probabilities = sorted(random.choices(range(1, total), k=n - 1))
    probabilities.append(total)
    return [probabilities[i + 1] - probabilities[i] for i in range(n - 1)]

try:
    # Connexion à la base de données
    conn = sqlite3.connect('silence_gay.db')
    c = conn.cursor()

    # Création de la table des biomes
    c.execute('''CREATE TABLE IF NOT EXISTS Biomes (
        biome_id INTEGER PRIMARY KEY,
        biome_name TEXT UNIQUE,
        probability INT
    )''')

    # Création de la table des types de nourriture
    c.execute('''CREATE TABLE IF NOT EXISTS FoodTypes (
        food_type_id INTEGER PRIMARY KEY,
        food_type_name TEXT UNIQUE,
        probability INT
    )''')

    # Création de la table des aliments
    c.execute('''CREATE TABLE IF NOT EXISTS Foods (
        food_id INTEGER PRIMARY KEY,
        food_name TEXT UNIQUE,
        food_type_id INTEGER REFERENCES FoodTypes(food_type_id),
        probability INT
    )''')

    # Création de la table des animaux
    c.execute('''CREATE TABLE IF NOT EXISTS Animals (
        animal_id INTEGER PRIMARY KEY,
        animal_name TEXT UNIQUE,
        biome_id INTEGER REFERENCES Biomes(biome_id),
        probability INT
    )''')

    # Création de la table des armes
    c.execute('''CREATE TABLE IF NOT EXISTS Weapons (
        weapon_id INTEGER PRIMARY KEY,
        weapon_name TEXT UNIQUE,
        biome_id INTEGER REFERENCES Biomes(biome_id),
        probability INT
    )''')

    # Insertion des données dans la table des biomes avec des probabilités égales à 100
    biomes_data = [
        ('desert', *generate_probabilities(7)[0]),
        ('plaine', *generate_probabilities(7)[1]),
        ('Neige', *generate_probabilities(7)[2]),
        ('forêt', *generate_probabilities(7)[3]),
        ('sakura', *generate_probabilities(7)[4]),
        ('plage', *generate_probabilities(7)[5]),
        ('montagne', *generate_probabilities(7)[6])
    ]
    c.executemany('INSERT OR IGNORE INTO Biomes (biome_name, probability) VALUES (?, ?)', biomes_data)

    # Insertion des données dans la table des types de nourriture avec des probabilités égales à 100
    food_types_data = [
        ('desert', *generate_probabilities(7)[0]),
        ('plaine', *generate_probabilities(7)[1]),
        ('Neige', *generate_probabilities(7)[2]),
        ('forêt', *generate_probabilities(7)[3]),
        ('sakura', *generate_probabilities(7)[4]),
        ('plage', *generate_probabilities(7)[5]),
        ('montagne', *generate_probabilities(7)[6])
    ]
    c.executemany('INSERT OR IGNORE INTO FoodTypes (food_type_name, probability) VALUES (?, ?)', food_types_data)

    # Insertion des données dans la table des aliments avec des probabilités égales à 100 pour chaque type de nourriture
    foods_data = [
        ('La figue de Barbarie', 1, *generate_probabilities(5)[0]),
        ('Moussaka', 1, *generate_probabilities(5)[1]),
        ('Tajine', 1, *generate_probabilities(5)[2]),
        ('couscous', 1, *generate_probabilities(5)[3]),
        ('Thé à la menthe', 1, *generate_probabilities(5)[4]),
        ('pain', 2, *generate_probabilities(5)[0]),
        ('pizza', 2, *generate_probabilities(5)[1]),
        ('Pavé de boeuf', 2, *generate_probabilities(5)[2]),
        ('omelette', 2, *generate_probabilities(5)[3]),
        ('ratatouille', 2, *generate_probabilities(5)[4]),
        ('raclette', 3, *generate_probabilities(5)[0]),
        ('Fondue', 3, *generate_probabilities(5)[1]),
        ('Viande de Renne', 3, *generate_probabilities(5)[2]),
        ('poisson séché', 3, *generate_probabilities(5)[3]),
        ('Soupe', 3, *generate_probabilities(5)[4]),
        ('Pomme de pin', 4, *generate_probabilities(5)[0]),
        ('Framboise', 4, *generate_probabilities(5)[1]),
        ('Champignon', 4, *generate_probabilities(5)[2]),
        ('Carottes sauvages', 4, *generate_probabilities(5)[3]),
        ('lapin', 4, *generate_probabilities(5)[4]),
        ('pétale de cerisier', 5, *generate_probabilities(5)[0]),
        ('Ramen', 5, *generate_probabilities(5)[1]),
        ('Saké', 5, *generate_probabilities(5)[2]),
        ('Nouille instantanée', 5, *generate_probabilities(5)[3]),
        ('sushi', 5, *generate_probabilities(5)[4]),
        ('Crabe', 6, *generate_probabilities(5)[0]),
        ('moules', 6, *generate_probabilities(5)[1]),
        ('algues', 6, *generate_probabilities(5)[2]),
        ('poisson', 6, *generate_probabilities(5)[3]),
        ('coquillages', 6, *generate_probabilities(5)[4]),
        ('myrtilles', 7, *generate_probabilities(5)[0]),
        ('chevreuille', 7, *generate_probabilities(5)[1]),
        ('Chèvre', 7, *generate_probabilities(5)[2]),
        ('Chocolat chaud', 7, *generate_probabilities(5)[3]),
        ('Aligot', 7, *generate_probabilities(5)[4])
    ]
    c.executemany('INSERT OR IGNORE INTO Foods (food_name, food_type_id, probability) VALUES (?, ?, ?)', foods_data)

    # Insertion des données dans la table des animaux avec des probabilités égales à 100 pour chaque biome
    animals_data = [
        ('serpent', 1, *generate_probabilities(7)[0]),
        ('scorpion', 1, *generate_probabilities(7)[1]),
        ('cheval', 2, *generate_probabilities(7)[0]),
        ('lièvre', 2, *generate_probabilities(7)[1]),
        ('ours polaire', 3, *generate_probabilities(7)[0]),
        ('yak', 3, *generate_probabilities(7)[1]),
        ('poisson', 4, *generate_probabilities(7)[0]),
        ('sanglier', 4, *generate_probabilities(7)[1]),
        ('panda', 5, *generate_probabilities(7)[0]),
        ('papillon', 5, *generate_probabilities(7)[1]),
        ('crabe', 6, *generate_probabilities(7)[0]),
        ('tortue', 6, *generate_probabilities(7)[1]),
        ('marmotte', 7, *generate_probabilities(7)[0]),
        ('bouc', 7, *generate_probabilities(7)[1])
    ]
    c.executemany('INSERT OR IGNORE INTO Animals (animal_name, biome_id, probability) VALUES (?, ?, ?)', animals_data)

    # Insertion des données dans la table des armes avec des probabilités égales à 100 pour chaque biome
    weapons_data = [
        ('Sabre oriental', 1, *generate_probabilities(7)[0]),
        ('arbalète', 1, *generate_probabilities(7)[1]),
        ('miroir', 1, *generate_probabilities(7)[2]),
        ('cimeterre', 1, *generate_probabilities(7)[3]),
        ('lance', 2, *generate_probabilities(7)[0]),
        ('lance-pierre', 2, *generate_probabilities(7)[1]),
        ('fronde', 2, *generate_probabilities(7)[2]),
        ('épée', 2, *generate_probabilities(7)[3]),
        ('boule de neige', 3, *generate_probabilities(7)[0]),
        ('stalactite', 3, *generate_probabilities(7)[1]),
        ('arc', 3, *generate_probabilities(7)[2]),
        ('gourdin', 3, *generate_probabilities(7)[3]),
        ('arbalète', 4, *generate_probabilities(7)[0]),
        ('harpon', 4, *generate_probabilities(7)[1]),
        ('corde', 4, *generate_probabilities(7)[2]),
        ('piège à loup', 4, *generate_probabilities(7)[3]),
        ('katana', 5, *generate_probabilities(7)[0]),
        ('jupe de lycéenne', 5, *generate_probabilities(7)[1]),
        ('dragon ball', 5, *generate_probabilities(7)[2]),
        ('éventail', 5, *generate_probabilities(7)[3]),
        ('parasol', 6, *generate_probabilities(7)[0]),
        ('pistolet à eau', 6, *generate_probabilities(7)[1]),
        ('dent de requin', 6, *generate_probabilities(7)[2]),
        ('harpon', 6, *generate_probabilities(7)[3]),
        ('hallebarde', 7, *generate_probabilities(7)[0]),
        ('sifflet', 7, *generate_probabilities(7)[1]),
        ('pioche', 7, *generate_probabilities(7)[2]),
        ('silex', 7, *generate_probabilities(7)[3])
    ]
    c.executemany('INSERT OR IGNORE INTO Weapons (weapon_name, biome_id, probability) VALUES (?, ?, ?)', weapons_data)

    # Sauvegarde des modifications et fermeture de la connexion
    conn.commit()
except sqlite3.Error as e:
    print("Erreur lors de l'interaction avec la base de données :", e)
finally:
    conn.close()