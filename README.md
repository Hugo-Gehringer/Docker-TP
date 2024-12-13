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

2. Générez les secrets :
   ```sh
   echo "user" | docker secret create db_user -
   echo "password" | docker secret create db_password -
   echo "flaskdb" | docker secret create db_name -
   echo "db" | docker secret create db_host -

3. Démarer le docker compose :
   ```sh
   docker-compose up -d

## Initialiser Swarm

1. Initialiser le swarm
   ```sh
   docker swarm init

2. Déployer la stack
   ```sh
   docker stack deploy -c docker-stack.yml swarm-stack

## Utilisation de l'application

- Application : [http://localhost/webapp/home](http://localhost/webapp/home)
- Check db : [http://localhost/webapp/check-db](http://localhost/webapp/check-db)
- Portainer : [http://localhost:9000](http://localhost:9000)