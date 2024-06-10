import networkx as nx
import qrcode

# L'URL que vous souhaitez coder dans le code QR
url = "http://10.1.165.139:5000/"

# Générer le code QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Créer une image du code QR
img = qr.make_image(fill='black', back_color='white')

# Enregistrer l'image
img.save("qrcode.png")








from datetime import datetime

def verifier_affluence():
    heure_actuelle = datetime.now().time()

    # Définir les intervalles de forte affluence
    intervalles_forte_affluence = [
        (datetime.strptime("07:50", "%H:%M").time(), datetime.strptime("08:15", "%H:%M").time()),
        (datetime.strptime("11:15", "%H:%M").time(), datetime.strptime("11:45", "%H:%M").time()),
        (datetime.strptime("13:00", "%H:%M").time(), datetime.strptime("13:30", "%H:%M").time()),
        (datetime.strptime("19:00", "%H:%M").time(), datetime.strptime("19:30", "%H:%M").time())
    ]

    # Vérifier si l'heure actuelle est dans l'un des intervalles de forte affluence
    for debut, fin in intervalles_forte_affluence:
        if debut <= heure_actuelle <= fin:
            return "Forte affluence"

    return "Affluence normale"











# Création du graphe orienté
G = nx.DiGraph()

# Ajout des arêtes avec des poids
edges = [
    ("BatERDCD", "BatE-1D", 4), ("BatERDCD", "BatE1D", 4), ("BatERDCD", "BatERDCG", 16), ("BatERDCD", "BatERDCM", 8),
    ("BatERDCG", "BatERDCD", 16), ("BatERDCG", "BatE-1G", 4), ("BatERDCG", "BatE1G", 4), ("BatERDCG", "BatERDCM", 8),
    ("BatERDCM", "BatERDCD", 8), ("BatERDCM", "BatERDCG", 8), ("BatERDCM", "BatE-1M", 4), ("BatERDCM", "BatE1M", 4),
    ("BatE1M", "BatE1D", 8), ("BatE1M", "BatE1G", 8), ("BatE1M", "BatERDCM", 4), ("BatE1M", "BatE2M", 4),
    ("BatE1D", "BatERDCD", 4), ("BatE1D", "BatE2D", 4), ("BatE1D", "BatE162", 1), ("BatE1D", "BatE1G", 16), ("BatE1D", "BatE1M", 8),
    ("BatE1G", "BatERDCG", 4), ("BatE1G", "BatE2G", 4), ("BatE1G", "BatE1D", 16), ("BatE1G", "BatE1M", 8), ("BatE1G", "BatE102", 1),
    ("BatE-1G", "BatE-1D", 16), ("BatE-1G", "BatERDCG", 4), ("BatE-1G", "BatE-1M", 8),
    ("BatE-1M", "BatE-1G", 8), ("BatE-1M", "BatERDCM", 4), ("BatE-1M", "BatE-1D", 8),
    ("BatE-1D", "BatE-1G", 16), ("BatE-1D", "BatERDCD", 4), ("BatE-1D", "BatE-1M", 8),
    ("BatE2M", "BatE2D", 8), ("BatE2M", "BatE2G", 8), ("BatE2M", "BatE1M", 4),
    ("BatE2D", "BatE1D", 4), ("BatE2D", "BatE2G", 16), ("BatE2D", "BatE2M", 8),
    ("BatE2G", "BatE1G", 20), ("BatE2G", "BatE2D", 16), ("BatE2G", "BatE2M", 8),
    ("BatE162", "BatE1D", 1), ("BatE162", "BatE160", 2),
    ("BatE160", "BatE162", 2), ("BatE160", "BatE158", 2),
    ("BatE158", "BatE160", 2), ("BatE158", "BatE156", 2),
    ("BatE156", "BatE158", 2), ("BatE156", "BatE154", 2),
    ("BatE154", "BatE156", 2), ("BatE154", "BatE152", 2),
    ("BatE152", "BatE154", 2), ("BatE152", "BatE116", 2),
    ("BatE116", "BatE152", 4), ("BatE116", "BatE114", 2),
    ("BatE114", "BatE116", 2), ("BatE114", "BatE112", 2),
    ("BatE112", "BatE114", 2), ("BatE112", "BatE110", 2),
    ("BatE110", "BatE112", 2), ("BatE110", "BatE108", 2),
    ("BatE108", "BatE110", 2), ("BatE108", "BatE106", 2),
    ("BatE106", "BatE108", 2), ("BatE106", "BatE104", 2),
    ("BatE104", "BatE106", 2), ("BatE104", "BatE102", 2),
    ("BatE102", "BatE104", 2), ("BatE102", "BatE1G", 1),
]


# Ajouter les arêtes au graphe
G.add_weighted_edges_from(edges)

# Fonction pour trouver le chemin le plus court en utilisant l'algorithme de Dijkstra, par exemple
def find_path(source, target):
    try:
        path = nx.dijkstra_path(G, source=source, target=target, weight='weight')
        return path
    except nx.NetworkXNoPath:
        return f"No path between {source} and {target}"

# Exemple d'utilisation
print(find_path("BatE156", "BatE108"))
