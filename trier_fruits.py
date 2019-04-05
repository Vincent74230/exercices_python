inventaire = [
("pommes", 22),
("melons", 4),
("poires", 18),
("fraises", 76),
("prunes", 51),
]

inventaire_reverse = [[nb,fruit] for fruit,nb in inventaire]

[inventaire_reverse.sort() for nb in inventaire_reverse]

print (inventaire_reverse)