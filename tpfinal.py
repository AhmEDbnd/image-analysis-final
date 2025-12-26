import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# ============================================
# ÉTAPE 1 : Charger l'image en niveaux de gris
# ============================================

image = cv2.imread(cv2.samples.findFile('sample.jpg'), cv2.IMREAD_GRAYSCALE)

print(f"Taille de l'image : {image.shape}")
print(f"Type de données : {image.dtype}")

# ============================================
# ÉTAPE 2 : Calculer l'histogramme manuellement
# ============================================
def calcul_histogramme_manuel(img):
    """Calcule l'histogramme en utilisant des boucles"""
    # Initialiser un tableau pour les 256 niveaux de gris
    hist_manuel = np.zeros(256, dtype=int)
    
    # Parcourir tous les pixels
    hauteur, largeur = img.shape
    for i in range(hauteur):
        for j in range(largeur):
            niveau_gris = img[i, j]
            hist_manuel[niveau_gris] += 1
    
    return hist_manuel

hist_manuel = calcul_histogramme_manuel(image)
print(f"\n✓ Histogramme manuel calculé : {len(hist_manuel)} valeurs")

# ============================================
# ÉTAPE 3 : Vérifier avec cv2.calcHist
# ============================================
hist_opencv = cv2.calcHist([image], [0], None, [256], [0, 256])
hist_opencv = hist_opencv.flatten().astype(int)

# Vérifier si les deux méthodes donnent le même résultat
difference = np.sum(np.abs(hist_manuel - hist_opencv))
print(f"✓ Différence entre manuel et OpenCV : {difference}")
print(f"  {'✓ Les histogrammes sont identiques !' if difference == 0 else '✗ Il y a une différence'}")

# ============================================
# ÉTAPE 4 : Calculer l'histogramme cumulé
# ============================================
hist_cumule = np.cumsum(hist_manuel)

print(f"\n✓ Histogramme cumulé calculé")
print(f"  Total pixels : {hist_cumule[-1]}")

# ============================================
# ÉTAPE 5 : Égalisation globale
# ============================================
image_egalisee = cv2.equalizeHist(image)
hist_egalisee = cv2.calcHist([image_egalisee], [0], None, [256], [0, 256]).flatten()

print(f"\n✓ Égalisation globale appliquée")

# ============================================
# ÉTAPE 6 : Appliquer CLAHE
# ============================================
# CLAHE = Contrast Limited Adaptive Histogram Equalization
# clipLimit : limite le contraste pour éviter la sur-amplification
# tileGridSize : taille des régions pour l'égalisation adaptative
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
image_clahe = clahe.apply(image)
hist_clahe = cv2.calcHist([image_clahe], [0], None, [256], [0, 256]).flatten()

print(f"✓ CLAHE appliquée")
print(f"  clipLimit=2.0, tileGridSize=(8,8)")

# ============================================
# ÉTAPE 8 : Calculer la dynamique
# ============================================
def calculer_dynamique(img, nom):
    """Calcule min, max et dynamique d'une image"""
    min_val = np.min(img)
    max_val = np.max(img)
    dynamique = max_val - min_val
    print(f"\n{nom}:")
    print(f"  Min: {min_val}, Max: {max_val}, Dynamique: {dynamique}")
    return min_val, max_val, dynamique

dyn_orig = calculer_dynamique(image, "Image originale")
dyn_egal = calculer_dynamique(image_egalisee, "Image égalisée")
dyn_clahe = calculer_dynamique(image_clahe, "Image CLAHE")

# ============================================
# VISUALISATION COMPLÈTE
# ============================================
fig = plt.figure(figsize=(16, 12))
gs = GridSpec(3, 4, figure=fig, hspace=0.3, wspace=0.3)

# Ligne 1 : Images
ax1 = fig.add_subplot(gs[0, 0])
ax1.imshow(image, cmap='gray', vmin=0, vmax=255)
ax1.set_title('Image Originale', fontsize=12, fontweight='bold')
ax1.axis('off')

ax2 = fig.add_subplot(gs[0, 1])
ax2.imshow(image_egalisee, cmap='gray', vmin=0, vmax=255)
ax2.set_title('Égalisation Globale', fontsize=12, fontweight='bold')
ax2.axis('off')

ax3 = fig.add_subplot(gs[0, 2])
ax3.imshow(image_clahe, cmap='gray', vmin=0, vmax=255)
ax3.set_title('CLAHE', fontsize=12, fontweight='bold')
ax3.axis('off')

# Ligne 2 : Histogrammes
ax4 = fig.add_subplot(gs[1, 0])
ax4.bar(range(256), hist_manuel, color='blue', alpha=0.7, width=1)
ax4.set_title('Histogramme Original', fontsize=11)
ax4.set_xlabel('Niveau de gris')
ax4.set_ylabel('Nombre de pixels')
ax4.grid(True, alpha=0.3)

ax5 = fig.add_subplot(gs[1, 1])
ax5.bar(range(256), hist_egalisee, color='green', alpha=0.7, width=1)
ax5.set_title('Histogramme Égalisé', fontsize=11)
ax5.set_xlabel('Niveau de gris')
ax5.set_ylabel('Nombre de pixels')
ax5.grid(True, alpha=0.3)

ax6 = fig.add_subplot(gs[1, 2])
ax6.bar(range(256), hist_clahe, color='red', alpha=0.7, width=1)
ax6.set_title('Histogramme CLAHE', fontsize=11)
ax6.set_xlabel('Niveau de gris')
ax6.set_ylabel('Nombre de pixels')
ax6.grid(True, alpha=0.3)

# Ligne 3 : Histogramme cumulé et comparaison
ax7 = fig.add_subplot(gs[2, :2])
ax7.plot(hist_cumule, color='purple', linewidth=2, label='Cumulé original')
ax7.set_title('Histogramme Cumulé (Original)', fontsize=11, fontweight='bold')
ax7.set_xlabel('Niveau de gris')
ax7.set_ylabel('Nombre cumulé de pixels')
ax7.grid(True, alpha=0.3)
ax7.legend()

# Comparaison des dynamiques
ax8 = fig.add_subplot(gs[2, 2:])
categories = ['Original', 'Égalisée', 'CLAHE']
dynamiques = [dyn_orig[2], dyn_egal[2], dyn_clahe[2]]
colors = ['blue', 'green', 'red']
bars = ax8.bar(categories, dynamiques, color=colors, alpha=0.7)
ax8.set_title('Comparaison de la Dynamique', fontsize=11, fontweight='bold')
ax8.set_ylabel('Dynamique (max - min)')
ax8.grid(True, alpha=0.3, axis='y')
# Ajouter les valeurs sur les barres
for bar, val in zip(bars, dynamiques):
    height = bar.get_height()
    ax8.text(bar.get_x() + bar.get_width()/2., height,
             f'{val}', ha='center', va='bottom', fontweight='bold')

plt.suptitle('Projet 1 : Analyse et Manipulation d\'Histogrammes - Photographie Numérique', 
             fontsize=14, fontweight='bold', y=0.98)

plt.tight_layout()
plt.savefig('projet1_resultats.png', dpi=150, bbox_inches='tight')
print("\n✓ Figure sauvegardée : projet1_resultats.png")
plt.show()

# ============================================
# ANALYSE ET INTERPRÉTATION
# ============================================
print("\n" + "="*60)
print("ANALYSE DES RÉSULTATS (8-10 lignes)")
print("="*60)

analyse = """
L'analyse de l'histogramme révèle la distribution des intensités dans l'image.
L'image originale montre une concentration des pixels dans certaines zones,
limitant le contraste global. L'égalisation globale redistribue uniformément
les intensités sur toute la plage [0-255], augmentant significativement la
dynamique de {orig} à {egal}. Cette méthode améliore le contraste mais peut
sur-amplifier le bruit dans les zones homogènes.

La méthode CLAHE offre un compromis optimal en appliquant l'égalisation de
manière adaptative sur des régions locales (8×8 pixels). Elle préserve mieux
les détails fins et évite la saturation excessive observée avec l'égalisation
globale. La dynamique CLAHE ({clahe}) reste élevée tout en maintenant un
rendu plus naturel. Pour la photographie numérique, CLAHE est préférée car
elle améliore le contraste local sans créer d'artefacts artificiels.
""".format(orig=dyn_orig[2], egal=dyn_egal[2], clahe=dyn_clahe[2])

print(analyse)

print("\n✓ Projet 1 terminé avec succès !")
print("\nFichiers générés :")
print("  - projet1_resultats.png : Figure complète avec toutes les visualisations")