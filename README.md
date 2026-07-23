````markdown
# Dockersmart

**Automated Docker configuration generator for Django projects**

Dockersmart est un outil en ligne de commande qui permet de générer automatiquement une configuration Docker pour un projet Django existant.

L'objectif est de simplifier la conteneurisation des applications Django en analysant le projet, en identifiant ses composants techniques, puis en générant les fichiers Docker nécessaires.

Dockersmart analyse notamment :

- la structure du projet Django
- les dépendances Python
- la version de Python utilisée
- le système de base de données
- les services additionnels (Redis, Celery, Flower...)
- le serveur d'application (Gunicorn, Uvicorn...)

Les fichiers suivants peuvent être générés automatiquement :

```
Dockerfile
docker-compose.yml
.dockerignore
.env.example
```

---

# Installation

## Depuis PyPI

```bash
pip install dockersmart
```

Vérifier l'installation :

```bash
dockersmart version
```

---

## Installation depuis les sources

Cloner le dépôt :

```bash
git clone https://github.com/GNGHE/dockersmart.git
cd dockersmart
```

Créer un environnement virtuel :

```bash
python -m venv venv
```

Activation :

Linux :

```bash
source venv/bin/activate
```

Windows :

```bash
venv\Scripts\activate
```

Installation en mode développement :

```bash
pip install -e .
```

---

# Utilisation

Placez-vous dans un projet Django existant :

```
my_project/

├── manage.py
├── requirements.txt
├── app/
└── settings.py
```

Puis exécutez :

```bash
dockersmart init dev
```

ou pour une configuration de production :

```bash
dockersmart init prod
```

Dockersmart va analyser le projet et générer les fichiers nécessaires.

---

# Commandes disponibles

## init

Génération de la configuration Docker.

### Mode développement

```bash
dockersmart init dev
```

Génère une configuration adaptée au développement avec :

- montage du projet en volume
- serveur Django intégré
- services nécessaires détectés automatiquement


Exemple :

```yaml
command: python manage.py runserver 0.0.0.0:8000
```

---

### Mode production

```bash
dockersmart init prod
```

Génère une configuration orientée déploiement :

- image Python optimisée
- serveur Gunicorn
- collecte des fichiers statiques
- configuration sans volumes locaux


Exemple :

```bash
gunicorn project.wsgi:application --bind 0.0.0.0:8000
```

---

# doctor

Analyse un projet Django et fournit un diagnostic.

Commande :

```bash
dockersmart doctor
```

Exemple :

```
Dockersmart Doctor

Check              Status       Details

manage.py          ✔            Found
settings.py        ✔            config/settings.py
Python             ✔            3.12
Database           ✔            PostgreSQL
Server             ✔            Gunicorn
Services           ✔            Redis, Celery
Dockerfile         -            Not found


Project is ready to be dockerized.
```

Cette commande permet de vérifier rapidement si un projet peut être dockerisé.

---

# validate

Vérifie les fichiers Docker existants.

Commande :

```bash
dockersmart validate
```

Contrôles effectués :

- présence du Dockerfile
- présence du fichier docker-compose
- validation de la syntaxe YAML
- présence des fichiers d'environnement

---

# clean

Supprime les fichiers générés par Dockersmart.

Commande :

```bash
dockersmart clean
```

Fichiers concernés :

```
Dockerfile
docker-compose.yml
docker-compose.yaml
.dockerignore
.env.example
```

---

# version

Affiche la version installée :

```bash
dockersmart version
```

Exemple :

```
Dockersmart version 0.1.0
```

---

# help

Affiche la liste des commandes disponibles :

```bash
dockersmart help
```

---

# Options

Certaines commandes acceptent des options supplémentaires.

## verbose

Affiche les différentes étapes d'exécution :

```bash
dockersmart init dev --verbose
```

Exemple :

```
Inspecting project...
Detecting services...
Building configuration...
Generating Docker files...
```

---

## debug

Affiche les informations internes détectées :

```bash
dockersmart init dev --debug
```

Exemple :

```python
{
    database: "postgresql",
    server: "gunicorn",
    services: [
        "redis",
        "celery",
        "flower"
    ]
}
```

---

## dry-run

Simule une génération sans créer de fichiers :

```bash
dockersmart init dev --dry-run
```

Utile pour vérifier la configuration détectée.

---

# Architecture interne

Dockersmart est organisé autour de plusieurs étapes :

```
Project
   |
   v
Inspectors
   |
   v
Detectors
   |
   v
Configurators
   |
   v
Generators
   |
   v
Docker files
```

Structure principale :

```
dockersmart/

├── cli/
│   └── commands.py

├── inspectors/
│   ├── structure_inspector.py
│   ├── dependency_inspector.py
│   ├── runtime_inspector.py
│   └── service_inspector.py

├── detectors/
│   ├── database_detector.py
│   ├── server_detector.py
│   └── system_dependency_detector.py

├── configurators/
│   ├── dev_configurator.py
│   └── prod_configurator.py

├── generators/
│   ├── dockerfile_generator.py
│   ├── compose_generator.py
│   └── env_generator.py

├── templates/
│   ├── dockerfile/
│   ├── compose/
│   └── dockerignore/
```

---

# Services supportés

Dockersmart détecte automatiquement plusieurs composants :

| Service | Support |
|---|---|
| PostgreSQL | Oui |
| MySQL | Oui |
| Redis | Oui |
| Celery | Oui |
| Flower | Oui |
| Django Channels | Oui |
| Prometheus | Oui |

---

# Exemple

Projet Django :

```
portfolio/

├── manage.py
├── requirements.txt
└── portfolio/

    ├── settings.py
    └── wsgi.py
```

Dépendances :

```
Django
psycopg2
redis
celery
flower
gunicorn
```

Commande :

```bash
dockersmart init prod
```

Résultat :

```
portfolio/

├── Dockerfile
├── docker-compose.yml
├── .dockerignore
└── .env.example
```

Services générés :

```
web
postgres
redis
celery_worker
flower
```

---

# Roadmap

## Version 1.0

- commande `inspect`
- commande `detect`
- personnalisation des templates
- support FastAPI
- support Flask

---

# Auteur

Ephraim Gode
