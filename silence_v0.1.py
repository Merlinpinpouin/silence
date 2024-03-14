import sqlite3

# Connexion à la base de données
conn = sqlite3.connect('silence.db')
c = conn.cursor()

# Création de la table des biomes
c.execute('''CREATE TABLE Biomes (
    biome_id INTEGER PRIMARY KEY,
    biome_name TEXT UNIQUE
)''')

# Insertion des données dans la table des biomes
biomes_data = [
    ('desert',),
    ('plaine',),
    ('Neige',),
    ('forêt',),
    ('sakura',),
    ('plage',),
    ('montagne',)
]
c.executemany('INSERT INTO Biomes (biome_name) VALUES (?)', biomes_data)

# Création de la table des aliments
c.execute('''CREATE TABLE Foods (
    food_id INTEGER PRIMARY KEY,
    food_name TEXT UNIQUE,
    biome_id INTEGER REFERENCES Biomes(biome_id)
)''')

# Insertion des données dans la table des aliments
foods_data = [
    ('La figue de Barbarie', 1),
    ('Moussaka', 1),
    ('Tajine', 1),
    ('couscous', 1),
    ('Thé à la menthe', 1),
    ('pain', 2),
    ('pizza', 2),
    ('Pavé de boeuf', 2),
    ('omelette', 2),
    ('ratatouille', 2),
    ('raclette', 3),
    ('Fondue', 3),
    ('Viande de Renne', 3),
    ('poisson séché', 3),
    ('Soupe', 3),
    ('Pomme de pin', 4),
    ('Framboise', 4),
    ('Champignon', 4),
    ('Carottes sauvages', 4),
    ('lapin', 4),
    ('pétale de cerisier', 5),
    ('Ramen', 5),
    ('Saké', 5),
    ('Nouille instantanée', 5),
    ('sushi', 5),
    ('Crabe', 6),
    ('moules', 6),
    ('algues', 6),
    ('poisson', 6),
    ('coquillages', 6),
    ('myrtilles', 7),
    ('chevreuille', 7),
    ('Chèvre', 7),
    ('Chocolat chaud', 7),
    ('Aligot', 7)
]
c.executemany('INSERT INTO Foods (food_name, biome_id) VALUES (?, ?)', foods_data)

# Création de la table des animaux
c.execute('''CREATE TABLE Animals (
    animal_id INTEGER PRIMARY KEY,
    animal_name TEXT UNIQUE,
    biome_id INTEGER REFERENCES Biomes(biome_id)
)''')

# Insertion des données dans la table des animaux
animals_data = [
    ('serpent', 1),
    ('scorpion', 1),
    ('cheval', 2),
    ('lièvre', 2),
    ('ours polaire', 3),
    ('yak', 3),
    ('poisson', 4),
    ('sanglier', 4),
    ('panda', 5),
    ('papillon', 5),
    ('crabe', 6),
    ('tortue', 6),
    ('marmotte', 7),
    ('bouc', 7)
]
c.executemany('INSERT INTO Animals (animal_name, biome_id) VALUES (?, ?)', animals_data)

# Création de la table des armes
c.execute('''CREATE TABLE Weapons (
    weapon_id INTEGER PRIMARY KEY,
    weapon_name TEXT,
    biome_id INTEGER REFERENCES Biomes(biome_id)
)''')

# Insertion des données dans la table des armes
weapons_data = [
    ('Sabre oriental', 1),
    ('arbalète', 1),
    ('miroir', 1),
    ('cimeterre', 1),
    ('lance', 2),
    ('lance-pierre', 2),
    ('fronde', 2),
    ('épée', 2),
    ('boule de neige', 3),
    ('stalactite', 3),
    ('arc', 3),
    ('gourdin', 3),
    ('arbalète', 4),
    ('harpon', 4),
    ('corde', 4),
    ('piège à loup', 4),
    ('katana', 5),
    ('jupe de lycéenne', 5),
    ('dragon ball', 5),
    ('éventail', 5),
    ('parasol', 6),
    ('pistolet à eau', 6),
    ('dent de requin', 6),
    ('hallebarde', 7),
    ('sifflet', 7),
    ('pioche', 7),
    ('silex', 7)
]
c.executemany('INSERT INTO Weapons (weapon_name, biome_id) VALUES (?, ?)', weapons_data)

# Sauvegarde des modifications et fermeture de la connexion
conn.commit()
conn.close()
