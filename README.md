# Projet_Niryo

Dépôt du projet de pilotage et d’automatisation autour de la cellule robotisée **Niryo**.

Ce dépôt regroupe plusieurs versions, sous-projets et livrables liés au développement :
- d’un **mode manuel de pilotage** via HOTAS,
- d’une **interface utilisateur avec flux caméra**,
- d’un **logiciel final intégré**,
- ainsi que d’un **mode automatique simplifié**.

---

## Objectif du dépôt

Ce GitHub permet :
- de conserver les différentes briques du projet,
- de retrouver rapidement les versions importantes,
- de tester séparément ou globalement les principaux modules du logiciel,
- de documenter le rôle de chaque fichier et archive.

---

## Structure du dépôt

### `README.md`
Fichier de présentation du dépôt.  
Il explique le rôle des fichiers présents et indique comment démarrer les différentes parties du projet.

### `Code Final Auto Nettoyé.py`
Script Python correspondant au **mode automatique simplifié**.  
Il permet de tester une logique séquentielle de fonctionnement du robot et du convoyeur, sans passer par l’interface complète.

**Usage conseillé :**
- tester la logique automatique seule,
- vérifier le cycle convoyeur + détection + prise + dépôt.

---

### `MODE MANUEL.zip`
Archive contenant la partie **mode manuel** du projet.  
Cette version est centrée sur le pilotage du robot et du convoyeur via le **HOTAS**.

On y retrouve normalement :
- la lecture des entrées HOTAS,
- la logique de pilotage temps réel,
- la gestion des états critiques,
- le feedback audio / visuel,
- les scripts de test ou de calibration.

**Usage conseillé :**
- tester le pilotage manuel seul,
- travailler sur le mapping,
- vérifier la réactivité du contrôle robot.

---

### `INTERFACE CAM.zip`
Archive contenant la partie **interface utilisateur / caméra**.  
Cette version est dédiée aux tests d’interface graphique, à l’affichage du flux vidéo et aux composants visuels.

On y retrouve normalement :
- la fenêtre principale,
- les widgets de statut,
- la gestion de la caméra,
- les états simulés ou réels selon la version.

**Usage conseillé :**
- tester l’interface indépendamment,
- vérifier l’intégration caméra,
- travailler sur l’ergonomie visuelle.

---

### `PROJET PILOTAGE NIRYO UI.zip`
Archive correspondant à la **version la plus complète / intégrée** du projet.  
Elle regroupe le pilotage, l’interface et la logique globale du logiciel final.

Cette archive est celle à privilégier si l’on veut tester la version la plus proche du logiciel final présenté dans le projet.

**Usage conseillé :**
- lancer la version la plus aboutie du logiciel,
- tester le fonctionnement global,
- retrouver l’architecture finale du projet.

---

### `interface_monofichier_yasmine.py`
Première version simplifiée de l’interface utilisateur, développée sous la forme d’un **script monofichier**.

Cette version a principalement servi :
- à valider les premiers choix d’interface,
- à tester l’affichage dynamique,
- à expérimenter le flux caméra avant modularisation.

**Usage conseillé :**
- observer la première approche de l’interface,
- comparer avec les versions plus avancées en archive.

---

## Par où commencer ?

### Cas 1 — Tester le logiciel final
Commencer par :
- **`PROJET PILOTAGE NIRYO UI.zip`**

C’est la version la plus complète du projet.

### Cas 2 — Tester uniquement le pilotage manuel
Commencer par :
- **`MODE MANUEL.zip`**

### Cas 3 — Tester uniquement l’interface / caméra
Commencer par :
- **`INTERFACE CAM.zip`**
ou
- **`interface_monofichier_yasmine.py`** pour la version simplifiée

### Cas 4 — Tester uniquement le mode automatique
Commencer par :
- **`Code Final Auto Nettoyé.py`**

---

## Pré-requis

Avant d’exécuter les scripts, il est recommandé d’utiliser :

- **Python 3.10.x**
- un **environnement virtuel (venv)**

Bibliothèques principales utilisées dans le projet :
- `pyniryo`
- `PySide6`
- `opencv-python`
- `pygame`

Selon la version testée, d’autres dépendances peuvent être nécessaires.
