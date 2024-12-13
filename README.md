# Projet TP Ddocker Flask avec Nginx et PostgreSQL

#### Hugo Gehringer et Maxime Palleja

Ce projet configure une application Flask avec Nginx et PostgreSQL comme base de données en utilisant Docker.

## Services :

- Flask : Application web
- Nginx : Serveur web
- PostgreSQL : Base de données
- Portainer : Interface de gestion de Docker

## Prérequis

- Docker
- Docker Compose

## Installation

1. Clonez le dépôt :
   ```sh
   git clone https://github.com/Hugo-Gehringer/Docker-TP.git
   cd Docker-TP
   
2. Créer l'image docker pour l'application Flask :
   ```sh
   docker build -t flask-app:latest .

## Lancez l'application avec Docker Compose
1. Il suffit de lancer la commande suivante dans le dossier du docker-compose.yml :
   ```sh
   docker-compose up -d

## Initialiser Swarm

1. Initialiser le swarm
   ```sh
   docker swarm init
   
2. Générez les secrets :
   ```sh
   echo "user" | docker secret create db_user -
   echo "password" | docker secret create db_password -
   echo "flaskdb" | docker secret create db_name -
   echo "db" | docker secret create db_host -
3. Déployer la stack en utilisant le fichier docker-stack.yml en étant dans le dossier du fichier :
   ```sh
   docker stack deploy -c docker-stack.yml swarm-stack

## Utilisation de l'application

- Application : [http://localhost/webapp/home](http://localhost/webapp/home)
- Check db : [http://localhost/webapp/check-db](http://localhost/webapp/check-db)
- Portainer : [http://localhost:9000](http://localhost:9000)