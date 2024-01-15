def calculate_probability(k, nb_rouge, nb_blanche, nb_noire):
    total_combinations = nb_rouge * nb_blanche * nb_noire
    favorable_combinations = k * (k - 1) * (k - 2)
    probability = favorable_combinations / total_combinations
    return probability
# Exemple d'utilisation
k = 3
nb_rouge = 5
nb_blanche = 7
nb_noire = 4
result = calculate_probability(k, nb_rouge, nb_blanche, nb_noire)
print(f"La probabilité d'obtenir une boule de chaque couleur est : {result}")