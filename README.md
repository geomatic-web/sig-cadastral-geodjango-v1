# SIG Web Cadastral avec Django & GeoDjango

Projet de **SIG Web cadastral** développé avec **Django, GeoDjango, PostGIS et Leaflet**.  
Il permet la **visualisation des parcelles**, la **recherche**, le **filtrage** et la **gestion via l’admin Django**.

---

## Fonctionnalités
- Cartographie des parcelles (polygones)
- API GeoJSON avec Django REST Framework
- Recherche de parcelle (numéro / propriétaire)
- Filtrage par usage
- Interface cartographique Leaflet
- Interface d’administration Django
- Authentification (connexion)

---

## Prérequis

Avant de lancer le projet, assurez-vous d’avoir :

1️⃣ Python
- Python **3.11 ou 3.12**
```bash
python --version

 2️⃣ PostgreSQL + PostGIS

PostgreSQL 14+

Extension PostGIS activée

CREATE DATABASE sig_db;
\c django
CREATE EXTENSION postgis;

3️⃣ Librairies SIG (obligatoire pour GeoDjango)

Sous Windows :

Installer OSGeo4W

##Cocher :
GDAL,GEOS,PROJ
## Installation du projet
Étape 1 — Cloner le dépôt
git clone https://github.com/geomatic-web/Sig-Django.git
cd Sig-Django
Étape 2 — Créer et activer l’environnement virtuel
python -m venv env
env\Scripts\activate | Vous devez voir :(env) en vert
Étape 3 — Installer les dépendances
pip install -r requirements.txt
