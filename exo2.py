import random

def Gen2():
    # Générons une clé aléatoire de 512 bits
    return ''.join(random.choice('01') for _ in range(512))

def chaine_en_binaire(s):
    # Convertissons la chaine de caractères en binaire en utilisant 16 bits par caractère
    return ''.join(format(ord(c), '016b') for c in s)

def binaire_en_chaine(b):
    #Convertissons les chaînes binaire en caractère
    return ''.join(chr(int(b[i:i+16], 2)) for i in range(0, len(b), 16))

def E2(k, m):
    # convertissons le message en format binaire
    m_bin = chaine_en_binaire(m)
    # Effectuons un XOR bit à bit entre le message et la clé
    return ''.join(str(int(a) ^ int(b)) for a, b in zip(m_bin, k))

def D2(k, c):
    #Effectuons un XOR bit à bit entre le cryptogramme et la clé
    m_bin = ''.join(str(int(a) ^ int(b)) for a, b in zip(c, k))
    #Convertissons le résultat binaire en chaîne de caratères
    return binaire_en_chaine(m_bin)

def scenario():
    m = 'ceciestlemessageclairadechiffrer'
    k = Gen2()
    c = E2(k, m)
    eve_c = c
    bob_m = D2(k, c)
    return m, k, c, eve_c, bob_m

# Exécution du scénario trois fois
for i in range(3):
    m, k, c, eve_c, bob_m = scenario()
    print(f"\n--- Exécution Scénario {i+1}: ---\n")
    print(f"Message en texte clair de Alice : {m}")
    print(f"Conversion du message d'Alice en binaire : \n {chaine_en_binaire(m)}")
    print(f"Clé convenue entre Alice et Bob : \n{k}")
    print(f"Cryptogramme de Alice : \n{c}")
    print(f"Eve detecte le Cryptogramme de Alice : \n{eve_c}")
    print(f"Bob reçoit le message chiffré de Alice : \n{c}")
    print(f"Bob uilise la clé choisie avec Alice : \n{k}")
    print(f"Bob déchiffre le message de Alice : {bob_m}")
    print()

print("(b) Eve peut-elle déchiffrer le message ?")
print("Non, Eve ne peut pas déchiffrer le message avec l'information qu'elle voit.")
print("Car le chiffrement du masque jetable aussi appelé Chiffre de Vernam est un chiffrement parfaitement sûr.")
print("Sans la clé, Eve n'a aucun moyen de retrouver le message original,")
print("car chaque bit du cryptogramme a une probabilité égale d'être 0 ou 1, indépendamment du message.")


