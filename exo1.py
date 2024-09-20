import random

def Gen1():
    # Générons une clé aléatoire
    return random.randint(1, 25) # On exclu 0 car 0 ne modifierait pas le message

# Chiffrement, Déchiffrement et fixation de la longueur du message

def E1(k, m):
    # Fixation et chiffrement du message
    if len(m) != 32:
        raise ValueError("Le message doit avoir une longueur fixe de 32 caractères !!!")
    # Chiffrement
    return ''.join(chr((ord(char) - ord('a') + k) % 26 + ord('a')) for char in m)

# Déchiffrement du message
def D1(k, c):
    return ''.join(chr((ord(char) - ord('a') - k) % 26 + ord('a')) for char in c)


# On va créer la fonction scénario
def scenario ():
    m = 'ceciestlemessageclairadechiffrer'
    k = Gen1()
    c = E1(k, m)
    eve_crypto = c
    bob_message = D1(k, c)
    return m, k, c, eve_crypto, bob_message

# Exécutons le scénario
for i in range(3):
    m, k, c, eve_crypto, bob_message = scenario()
    print(f"\n--- Exécution Scénario {i+1}: ---") 
    print(f"Message en texte clair de Alice : {m}")
    print(f"Clé convenue entre Alice et Bob : {k}")
    print(f"Cryptogramme de Alice : {c}")
    print(f"Eve detecte le Cryptogramme de Alice : {eve_crypto}")
    print(f"Bob recoit le message chiffré de Alice : {c}")
    print(f"Bob uilise la clé choisie avec Alice : {k}")
    print(f"Bob déchiffre le message de Alice : {bob_message}")
    print()

    print(f"\n")

# Réponse question numéro b)
print(f" b) Pour chacune de ces trois exécutions est-ce que Eve peut déchiffrer le message m ?")
print(f"Réponse: Non, Eve ne peut pas déchiffrer le message m avec l'information qu'elle voit à travers le cryptogramme de Alice.")
print(f"Sans la clé secrète, Eve devrait tenter tout les décalages possible pour essayer de déchiffrer le message Original.")






    