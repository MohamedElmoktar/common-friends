# src/common_friends.py

from pyspark import SparkContext

def parse_line(line):
    # Format attendu : <user_id> <Nom> <friend_id1>,<friend_id2>,...
    line = line.strip()
    if not line or line.startswith("#"):
        return None
    parts = line.split()
    if len(parts) < 2:
        return None
    try:
        user_id = int(parts[0])
    except ValueError:
        return None
    name = parts[1]
    friends = list(map(int, parts[2].split(','))) if len(parts) > 2 else []
    return (user_id, name, friends)

def generate_friend_pairs(user_id, name, friends):
    # Génère des couples triés (min, max) pour chaque ami
    pairs = []
    for friend_id in friends:
        pair = tuple(sorted((user_id, friend_id)))
        pairs.append((pair, set(friends)))
    return pairs

def main():
    sc = SparkContext(appName="CommonFriends")
    # Charger les données
    lines = sc.textFile("data/friends.txt")
    # Parser les lignes
    users = lines.map(parse_line).filter(lambda x: x is not None)
    # Associer chaque user_id à son nom
    user_names = users.map(lambda x: (x[0], x[1])).collectAsMap()
    # Générer les couples d'amis
    pairs = users.flatMap(lambda x: generate_friend_pairs(x[0], x[1], x[2]))
    # Grouper par couple et agréger les listes d'amis
    grouped = pairs.reduceByKey(lambda a, b: a & b)
    # Filtrer pour la paire (1, 2)
    result = grouped.filter(lambda x: x[0] == (1, 2)).collect()
    # Afficher le résultat
    for ((id1, id2), common) in result:
        name1 = user_names.get(id1, str(id1))
        name2 = user_names.get(id2, str(id2))
        print(f"{id1}<{name1}>{id2}<{name2}>{sorted(list(common))}")

    sc.stop()

if __name__ == "__main__":
    main()
