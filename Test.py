import random

# Génération de la clé de longueur 32
def Gen3():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key = ''.join(random.choice(alphabet) for _ in range(32))
    return key

# Chiffrement avec la clé k
def E3(m, k):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    c = []
    for i in range(len(m)):
        shift = alphabet.index(k[i])
        new_char = alphabet[(alphabet.index(m[i]) + shift) % 26]
        c.append(new_char)
    return ''.join(c)

# Déchiffrement avec la clé k
def D3(c, k):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    m = []
    for i in range(len(c)):
        shift = alphabet.index(k[i])
        new_char = alphabet[(alphabet.index(c[i]) - shift) % 26]
        m.append(new_char)
    return ''.join(m)

# Message à chiffrer
m = "ceciestlemessageclairadechiffrer"

# Scénario de communication entre Alice, Bob et Eve
def scenario():
    # Alice génère une clé secrète
    k = Gen3()
    
    # Alice chiffre le message avec la clé k
    c = E3(m, k)
    
    # Alice envoie le cryptogramme c à Bob via Eve
    # Eve ne modifie pas le cryptogramme
    c_eve = c
    
    # Bob reçoit le cryptogramme c et le déchiffre avec la clé k
    m_bob = D3(c_eve, k)
    
    return m, k, c, c_eve, m_bob

# Scénario de communication avec modification par Eve
def scenario_with_eve_modification():
    # Alice génère une clé secrète
    k = Gen3()
    
    # Alice chiffre le message avec la clé k
    c = E3(m, k)
    
    # Eve modifie le troisième symbole avec un décalage de 9 lettres
    # et le quatrième symbole avec un décalage de 18 lettres
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    c_list = list(c)
    c_list[2] = alphabet[(alphabet.index(c_list[2]) + 9) % 26]
    c_list[3] = alphabet[(alphabet.index(c_list[3]) + 18) % 26]
    c_eve = ''.join(c_list)
    
    # Bob reçoit le cryptogramme modifié c_eve et le déchiffre avec la clé k
    m_bob = D3(c_eve, k)
    
    return m, k, c, c_eve, m_bob

# Exécution du scénario sans modification par Eve trois fois
print("Scénario sans modification par Eve:")
for i in range(3):
    m, k, c, c_eve, m_bob = scenario()
    print(f"Exécution {i+1}:")
    print(f"Alice: m = {m}, k = {k}, c = {c}")
    print(f"Eve: c = {c_eve}")
    print(f"Bob: c = {c_eve}, k = {k}, m = {m_bob}")
    print()

# Exécution du scénario avec modification par Eve trois fois
print("Scénario avec modification par Eve:")
for i in range(3):
    m, k, c, c_eve, m_bob = scenario_with_eve_modification()
    print(f"Exécution {i+1}:")
    print(f"Alice: m = {m}, k = {k}, c = {c}")
    print(f"Eve: c = {c_eve}")
    print(f"Bob: c = {c_eve}, k = {k}, m = {m_bob}")
    print()