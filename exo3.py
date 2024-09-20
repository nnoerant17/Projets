import random
import string

def Gen3():
    # Génère une clé aléatoire de longueur 32 sur l'alphabet a-z
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(32))

def E3(k, m):
    if len(m) != 32 or len(k) != 32:
        raise ValueError("Le message et la clé doivent avoir une longueur de 32 caractères")
    return ''.join(chr((ord(m[i]) - ord('a') + ord(k[i]) - ord('a')) % 26 + ord('a')) for i in range(32))

def D3(k, c):
    if len(c) != 32 or len(k) != 32:
        raise ValueError("Le cryptogramme et la clé doivent avoir une longueur de 32 caractères")
    return ''.join(chr((ord(c[i]) - ord(k[i]) + 26) % 26 + ord('a')) for i in range(32))

def scenario():
    m = 'ceciestlemessageclairadechiffrer'
    k = Gen3()
    c = E3(k, m)
    eve_c = c
    bob_m = D3(k, c)
    return m, k, c, eve_c, bob_m

# Exécution du scénario trois fois
for i in range(3):
    m, k, c, eve_c, bob_m = scenario()
    print(f"\n--- Exécution Scénario {i+1}: ---\n")
    print(f"Message en texte clair de Alice : {m}")
    print(f"AClé convenue entre Alice et Bob : {k}")
    print(f"Cryptogramme de Alice : {c}")
    print(f"Eve detecte le Cryptogramme de Alice : {eve_c}")
    print(f"Bob reçoit le message chiffré de Alice : {c}")
    print(f"Bob uilise la clé choisie avec Alice : {k}")
    print(f"Bob déchiffre le message de Alice : {bob_m}")
    print()

# Réponse question numéro b)
print(f"Réponse b) Eve ne peut pas déchiffrer le message avec l'information qu'elle voit.")
print(f"Contrairement au chiffrement de César classique, chaque lettre du message est chiffrée avec une clé différente,")
print(f"ce qui rend l'analyse de fréquence inefficace.")
print(f"Cependant, ce schéma n'offre pas une sécurité parfaite comme le masque jetable (One-Time Pad)")
print(f"car la clé est réutilisable et le chiffrement n'est pas parfaitement aléatoire.\n")

# Scénario avec modification par Eve
def eve_modify(c):
    c_list = list(c)
    c_list[2] = chr((ord(c_list[2]) - ord('a') + 9) % 26 + ord('a'))
    c_list[3] = chr((ord(c_list[3]) - ord('a') + 18) % 26 + ord('a'))
    return ''.join(c_list)

print("Scénario avec modification par Eve:")
for i in range(3):
    m, k, c, _, _ = scenario()
    c_modified = eve_modify(c)
    bob_m_modified = D3(k, c_modified)
    print(f"\n--- Exécution Scénario {i+1}: ---\n")
    print(f"Message en texte clair de Alice : {m}")
    print(f"Eve modifie le cryptogramme de Alice : {c_modified}")
    print(f"Bob déchiffre le message de Alice : {bob_m_modified}")
    print(f"Différences: {''.join(['*' if m[i] != bob_m_modified[i] else ' ' for i in range(32)])}")
    print()