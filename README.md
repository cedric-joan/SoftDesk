# SOFTDESK

Créer une API sécurisée RESTful en utilisant ``Django REST``.


Cette application permettra à une communauté d'utilisateurs de remonter et suivre des problèmes techniques (issue tracking system).

# Fonctionnalités
L'application présente les cas d'utilisations suivantes :

1 - Une application de suivi des problèmes pour les trois plateformes (site web, application Android et iOS).

2 - L'application permettra esentiellement aux utilisateurs de créer divers projets, d'ajouter des uttilisateurs à des projets spécifiques, de créer des problèmes au sein des projets et d'attribuer des libellés à ces problèmes en fonction de leurs priorités.

3 - Les trois plateformes exploiteront les points de terminaison d'API qui serviront les données


# Tester le projet

Lancer votre terminal et clonez le projet:

    git clone https://github.com/cedric-joan/SoftDesk.git


# Installation

Pour faire fonctionner ce site web, suiver les instructions suivantes:
``Python version : 3.9``

Créer un environnement virtuel en utilisant la commande: ``python -m venv env``.

Pour l'activer exécutez la commande: env/bin/activate ou source env/Scripts/activate (sous Windows)

Les dépendances sont listés dans le fichier `requirements.txt`.

Lancer la commande: 
```
pip install -r requirements.txt
```

# Lancer le programme

Allez dans le dossier src/ Lancer la commande:
```
python manage.py runserver
```

Une fois l'API lancée:
```
vous devriez voir dans le terminal Starting development server at http://127.0.0.1:8000/
```
Adresse administrateur:
```
http://127.0.0.1:8000/admin
```
Vous pouvez à présent continuer de suivre les instructions de la documentation sur [POSTMAN](https://documenter.getpostman.com/view/21257311/2s93z58PWL)


