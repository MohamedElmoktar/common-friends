# Mini Projet Spark : Amis Communs

## Objectif

Développer un programme PySpark pour découvrir la liste des amis communs entre deux utilisateurs dans un graphe social à partir d’un fichier texte.

## Jeu de données

- Format :  
  `<user_id> <Nom> <friend_id1>,<friend_id2>,...`
- Exemple :  
  `1 Sidi 2,3,4`  
  signifie que l'utilisateur 1 (Sidi) est ami avec les utilisateurs 2, 3 et 4.

- Les amitiés sont mutuelles.

- Placez le fichier téléchargé dans `data/friends.txt`.

## Structure du projet

```
tp-spark/
├── data/
│   └── friends.txt
├── src/
│   └── common_friends.py
├── tests/
│   └── test_common_friends.py
├── results/
│   └── output.txt
├── README.md
└── requirements.txt
```

## Installation

```bash
pip install -r requirements.txt
```

## Exécution

```bash
spark-submit src/common_friends.py
```

Le résultat pour la paire Sidi (ID 1) et Mohamed (ID 2) s’affichera au format :

```
1<Sidi>2<Mohamed>[liste_amis_communs]
```

## Tests

Des tests unitaires sont disponibles dans `tests/test_common_friends.py`.

## Auteur

Projet réalisé pour l’initiation à Spark (PySpark).
