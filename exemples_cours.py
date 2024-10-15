# Condition if
port = 22
if port == 22:
    print("Le port 22 est ouvert : SSH activé.")



# # Vérification du protocole de connexion

protocole_connexion = "HTTP"  

if protocole_connexion == "HTTPS":
    print("Connexion sécurisée via HTTPS.")
else:
    print("Alerte : Connexion non sécurisée via HTTP. Veuillez passer à HTTPS.")


# elif
tentatives_connexion = 4
tentatives_max = 3

if tentatives_connexion == 0:
    print("Aucune tentative de connexion.")
elif tentatives_connexion <= tentatives_max:
    print("Connexion autorisée.")
else:
    print("Alerte : Trop de tentatives de connexion, compte bloqué.")



# Opérations logiques
pare_feu = True
antivirus = True

if pare_feu and antivirus:
    print("Le serveur est sécurisé.")
else:
    print("Le serveur est vulnérable.")

# Utilisation de match case

protocol = "HTTP"

match protocol:
    case "HTTP":
        print("Connexion non sécurisée : HTTP détecté.")
    case "HTTPS":
        print("Connexion sécurisée : HTTPS détecté.")
    case "FTP":
        print("Connexion FTP détectée.")
    case _:
        print("Protocole inconnu.")


# Condition imbriquées

age = 20
citoyen = True

if age >= 18:
    if citoyen:
        print("Vous pouvez voter.")
    else:
        print("Vous devez être citoyen pour voter.")
else:
    print("Vous êtes trop jeune pour voter.")



# Opérateurs ternaires
age = 20
statut = "majeur" if age >= 18 else "mineur"
print(statut)  # Affiche "majeur"


# Gestion des erreurs

try:
    age = int(input("Entrez votre âge : "))
    if age >= 18:
        print("Vous êtes majeur.")
    else:
        print("Vous êtes mineur.")
except:
    print("Erreur : Veuillez entrer un nombre valide.")




    #  Un exemple 


utilisateur = "John Doe"
role = "admin"  # Peut être "admin", "moderateur", ou "utilisateur"
mot_de_passe = "12345"
mot_de_passe_saisi = input("Entrez le mot de passe : ")

# Vérification du mot de passe
if mot_de_passe_saisi == mot_de_passe:
    # Vérification du rôle utilisateur
    if role == "admin":
        print(f"Bienvenue {utilisateur}, vous avez un accès complet en tant qu'administrateur.")
    elif role == "moderateur":
        print(f"Bienvenue {utilisateur}, vous avez un accès limité en tant que modérateur.")
    else:
        print(f"Bienvenue {utilisateur}, vous avez un accès restreint en tant qu'utilisateur.")
else:
    print("Erreur : Mot de passe incorrect.")


    



# connexion_reseau = ("192.168.1.100", 443, "HTTPS")



# etudiant = {"nom": "Alice", "age": 21}


# print(etudiant["nom"])  # Affiche "Alice"
# etudiant["âge"] = 22  # Mise à jour de l'âge


# nombres = [x for x in range(10) if x % 2 == 0]
# print(nombres)  # [0, 2, 4, 6, 8]


# for i in range(1, 4):
#     for j in range(1, 3):
#         print(f"i={i}, j={j}")

logs = ["info: démarrage", "erreur: port fermé", "info: connexion établie"]

for log in logs:
    if "info" in log:
        continue  # Ignore les logs d'information
    print(f"Analyse du log : {log}")
