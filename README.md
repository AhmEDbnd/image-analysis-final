# Projet 1 : Analyse et Manipulation d'Histogrammes

## 📸 Photographie Numérique

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)
![NumPy](https://img.shields.io/badge/NumPy-latest-orange.svg)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-red.svg)

---

## 📋 Description du Projet

Ce projet explore l'analyse et la manipulation d'histogrammes d'images en niveaux de gris, avec une application spécifique à la **photographie numérique**. L'objectif est de comprendre comment améliorer le contraste d'une image en utilisant différentes techniques d'égalisation d'histogramme.

### 🎯 Objectifs

- Calculer et analyser l'histogramme d'une image
- Comprendre le rôle de l'histogramme cumulé
- Appliquer l'égalisation d'histogramme globale
- Utiliser la méthode CLAHE (Contrast Limited Adaptive Histogram Equalization)
- Comparer les résultats et évaluer la qualité des améliorations

---

## 🛠️ Technologies Utilisées

- **Python 3.8+**
- **OpenCV** : Traitement d'images
- **NumPy** : Calculs numériques
- **Matplotlib** : Visualisation des résultats

---

## 📦 Installation

### Prérequis

Assurez-vous d'avoir Python 3.8 ou supérieur installé sur votre système.

### Installation des dépendances

```bash
pip install opencv-python numpy matplotlib
```

Ou utilisez le fichier `requirements.txt` :

```bash
pip install -r requirements.txt
```

**Contenu de `requirements.txt` :**
```
opencv-python>=4.5.0
numpy>=1.19.0
matplotlib>=3.3.0
```

---

## 🚀 Utilisation

### Option 1 : Utiliser l'image d'exemple

Exécutez simplement le script :

```bash
python projet1_histogrammes.py
```

Le script génère automatiquement une image d'exemple pour la démonstration.

### Option 2 : Utiliser votre propre image

1. Placez votre image dans le même dossier que le script
2. Modifiez le code :

```python
# Commentez cette ligne :
# image = create_sample_image()

# Décommentez et modifiez cette ligne :
image = cv2.imread('votre_image.jpg', cv2.IMREAD_GRAYSCALE)
```

3. Exécutez le script :

```bash
python projet1_histogrammes.py
```

---

## 📊 Résultats Générés

Le script génère automatiquement :

### 1. **Figure complète** (`projet1_resultats.png`)
   - Images : Originale, Égalisée, CLAHE
   - Histogrammes des trois versions
   - Histogramme cumulé
   - Graphique de comparaison des dynamiques

### 2. **Analyse textuelle** (console)
   - Calcul de l'histogramme manuel
   - Vérification avec OpenCV
   - Calcul des dynamiques (min/max)
   - Analyse comparative des méthodes

---

## 📖 Structure du Code

```
projet1_histogrammes.py
│
├── create_sample_image()          # Création d'une image d'exemple
├── calcul_histogramme_manuel()    # Calcul avec boucles
├── Calcul histogramme OpenCV      # Vérification
├── Histogramme cumulé             # Analyse cumulative
├── Égalisation globale            # cv2.equalizeHist()
├── CLAHE                          # Égalisation adaptative
├── calculer_dynamique()           # Min, max, dynamique
└── Visualisation complète         # Matplotlib
```

---

## 🔍 Explications Techniques

### 1. **Histogramme**
L'histogramme représente la distribution des niveaux de gris dans une image (0-255). Il permet d'analyser :
- La répartition des intensités
- Le contraste global
- Les zones sous-exposées ou sur-exposées

### 2. **Histogramme Cumulé**
Somme cumulative de l'histogramme. Utilisé pour :
- Comprendre la distribution cumulative
- Base mathématique de l'égalisation

### 3. **Égalisation Globale**
```python
image_egalisee = cv2.equalizeHist(image)
```
- Redistribue uniformément les intensités
- Améliore le contraste global
- Peut sur-amplifier le bruit

### 4. **CLAHE (Contrast Limited Adaptive Histogram Equalization)**
```python
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
image_clahe = clahe.apply(image)
```
- **clipLimit** : Limite le contraste pour éviter la sur-amplification
- **tileGridSize** : Taille des tuiles pour l'égalisation locale
- Préserve mieux les détails locaux

### 5. **Dynamique**
```
Dynamique = max(image) - min(image)
```
Mesure l'étendue des intensités utilisées (0-255 = dynamique maximale)

---

## 📈 Résultats Attendus

### Image Originale
- Histogramme concentré dans certaines zones
- Contraste limité
- Dynamique variable

### Image Égalisée
- Distribution uniforme sur [0-255]
- Contraste maximal
- Dynamique = 255
- Peut créer des artefacts

### Image CLAHE
- Distribution équilibrée
- Contraste amélioré localement
- Dynamique = 255
- Aspect plus naturel

---

## 📝 Exemple de Résultats

### Valeurs typiques obtenues :

| Méthode | Min | Max | Dynamique | Qualité |
|---------|-----|-----|-----------|---------|
| Original | 0 | 243 | 243 | Faible contraste |
| Égalisée | 0 | 255 | 255 | Contraste élevé |
| CLAHE | 0 | 255 | 255 | Optimal |

---

## 🎓 Travaux Demandés (selon PDF)

- [x] Charger une image en niveaux de gris
- [x] Calculer l'histogramme manuellement (boucles)
- [x] Vérifier avec cv2.calcHist
- [x] Tracer l'histogramme cumulé et l'interpréter
- [x] Appliquer l'égalisation globale : equalizeHist
- [x] Appliquer CLAHE : expliquer son intérêt
- [x] Comparer l'image originale, égalisée et CLAHE
- [x] Calculer la dynamique (min/max) avant et après

---

## 📄 Livrables

### À rendre :

1. **Figure** : `projet1_resultats.png`
   - Image originale + versions améliorées
   - Histogrammes

2. **Analyse** : Texte de 8-10 lignes (fourni dans le code)

3. **Rapport** : Document PDF contenant :
   - Introduction
   - Méthodologie
   - Résultats (figures)
   - Analyse et interprétation
   - Conclusion

---

## 💡 Interprétation des Résultats

### Pourquoi CLAHE est meilleur pour la photographie ?

1. **Préservation des détails locaux**
   - Traitement adaptatif par régions
   - Pas de perte d'information dans les zones homogènes

2. **Contraste naturel**
   - Évite la sur-saturation
   - Rendu visuel plus agréable

3. **Limitation du bruit**
   - Le paramètre `clipLimit` contrôle l'amplification
   - Réduit les artefacts dans les zones uniformes

4. **Flexibilité**
   - Paramètres ajustables (clipLimit, tileGridSize)
   - Adaptable à différents types d'images

---

## 🔧 Personnalisation

### Modifier les paramètres CLAHE :

```python
# Augmenter le contraste
clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))

# Traitement plus fin
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(16, 16))

# Traitement plus global
clahe = cv2.createCLAHE(clipLimit=1.5, tileGridSize=(4, 4))
```

### Tester différentes images :

```python
# Portrait
image = cv2.imread('portrait.jpg', cv2.IMREAD_GRAYSCALE)

# Paysage
image = cv2.imread('paysage.jpg', cv2.IMREAD_GRAYSCALE)

# Photo de nuit
image = cv2.imread('nuit.jpg', cv2.IMREAD_GRAYSCALE)
```

---

## 🐛 Dépannage

### Problème : Image trop sombre après traitement
**Solution** : Ajustez le `clipLimit` de CLAHE (augmentez à 3.0 ou 4.0)

### Problème : Artefacts visibles
**Solution** : Augmentez `tileGridSize` à (16, 16) ou (32, 32)

### Problème : Erreur de lecture d'image
**Solution** : Vérifiez le chemin du fichier et le format (JPG, PNG supportés)

### Problème : Histogramme manuel ≠ OpenCV
**Solution** : Vérifiez les types de données (uint8) et les bornes [0, 255]

---

## 📚 Références

1. **OpenCV Documentation**
   - [Histogram Equalization](https://docs.opencv.org/4.x/d5/daf/tutorial_py_histogram_equalization.html)
   - [CLAHE](https://docs.opencv.org/4.x/d6/dc7/group__imgproc__hist.html#gad689d2607b7b3889453804f414ab1018)

2. **Articles scientifiques**
   - Zuiderveld, K. (1994). "Contrast Limited Adaptive Histogram Equalization"
   - Pizer, S. M. et al. (1987). "Adaptive histogram equalization"

3. **Cours M1 STIC**
   - Dr. HALLACI S. - Projets 2025

---

## 👨‍💻 Auteur

**Projet réalisé dans le cadre du cours :**
- **M1 STIC** - Traitement d'Images
- **Enseignant** : Dr. HALLACI S
- **Année** : 2025

---

## 📧 Contact

Pour toute question concernant ce projet :
- Email de l'enseignant : [à compléter]
- Documentation OpenCV : https://docs.opencv.org/

---

## 📜 Licence

Ce projet est réalisé dans un cadre pédagogique.

---

## ✅ Checklist du Projet

Avant de rendre votre projet, vérifiez :

- [ ] Le code s'exécute sans erreur
- [ ] La figure `projet1_resultats.png` est générée
- [ ] Les trois images (originale, égalisée, CLAHE) sont visibles
- [ ] Les trois histogrammes sont affichés
- [ ] L'histogramme cumulé est tracé
- [ ] Le graphique de dynamique est présent
- [ ] L'analyse de 8-10 lignes est rédigée
- [ ] Le rapport PDF est complet
- [ ] Les calculs de dynamique sont corrects
- [ ] Les commentaires du code sont clairs

---

## 🎯 Critères d'Évaluation

| Critère | Points | Détails |
|---------|--------|---------|
| Code fonctionnel | 30% | Exécution sans erreur |
| Histogramme manuel | 15% | Implémentation correcte |
| Visualisations | 25% | Qualité des figures |
| Analyse | 20% | Pertinence de l'interprétation |
| Rapport | 10% | Clarté et structure |

**Total : 100%**

---

## 🌟 Améliorations Possibles

Pour aller plus loin :

1. **Métriques de qualité**
   - Calculer le PSNR (Peak Signal-to-Noise Ratio)
   - Calculer le SSIM (Structural Similarity Index)

2. **Interface graphique**
   - Créer une interface avec Tkinter
   - Ajuster les paramètres en temps réel

3. **Comparaison étendue**
   - Tester sur plusieurs types d'images
   - Créer un tableau comparatif automatique

4. **Optimisation**
   - Paralléliser le calcul manuel
   - Utiliser NumPy vectorisé

---

**Bonne chance avec votre projet ! 🎓📸**

*Dernière mise à jour : Décembre 2025*