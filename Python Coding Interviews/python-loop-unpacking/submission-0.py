from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    meilleur_nom =""
    meilleur_score=-1
    for nom,score in scores:
        if score >meilleur_score:
            meilleur_score = score
            meilleur_nom = nom
    return meilleur_nom




# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
