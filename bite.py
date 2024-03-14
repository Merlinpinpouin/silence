#https://www.mindmeister.com/app/map/3192942585?t=VbEM41UIYJ


import sqlite3

conn = sqlite3.connect('silence.db')
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS biomes(desert INT, plaine INT, neige INT, foret INT, sakura INT, plage INT, montagne INT)")
cur.execute("INSERT INTO biomes(desert,plaine,neige,foret,sakura,plage,montagne) VALUES(13\
                                                                                        ,13\
                                                                                        ,13\
                                                                                        ,13\
                                                                                        ,9\
                                                                                        ,13\
                                                                                        ,13)")

cur.execute("CREATE TABLE IF NOT EXISTS nourriture_desert(figue_de_barbarie INT, moussaka INT, Tajine INT, Couscous INT, Thé_a_la_menthe INT)")
cur.execute("INSERT INTO nourriture_desert(figue_de_barbarie,moussaka,Tajine,Couscous,Thé_a_la_menthe) VALUES(10\
                                                                                                            ,15\
                                                                                                            ,25\
                                                                                                            ,20\
                                                                                                            ,30)")

cur.execute("CREATE TABLE IF NOT EXISTS nourriture_plaine(pain INT, pizza INT, Pavé_de_boeuf INT, omelette INT, ratatouille INT)")
cur.execute("INSERT INTO nourriture_plaine(pain,pizza,Pavé_de_boeuf,omelette,ratatouille) VALUES(30\
                                                                                                ,15\
                                                                                                ,10\
                                                                                                ,20\
                                                                                                ,25)")

cur.execute("CREATE TABLE IF NOT EXISTS nourriture_neige(raclette INT, fondue INT, renne INT, poisson_séché INT, soupe INT)")
cur.execute("INSERT INTO nourriture_neige(raclette,fondue,renne,poisson_séché,soupe) VALUES(25\
                                                                                            ,15\
                                                                                            ,30\
                                                                                            ,20\
                                                                                            ,10)")


cur.execute("CREATE TABLE IF NOT EXISTS nourriture_foret(pomme_de_pin INT, Framboise INT, champigon INT, carottes_sauvages INT, civet_de_lapin INT)")
cur.execute("INSERT INTO nourriture_foret(pomme_de_pin,Framboise,champigon,carottes_sauvages,civet_de_lapin) VALUES(25\
                                                                                            ,15\
                                                                                            ,30\
                                                                                            ,20\
                                                                                            ,10)")



conn.commit()

cur.close()
conn.close()



