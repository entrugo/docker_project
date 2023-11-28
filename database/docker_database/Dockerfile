# Utilisez l'image PostgreSQL officielle en tant que base
FROM postgres:latest

# Installez les dépendances PostgreSQL
RUN apt-get update && apt-get install -y libpq-dev

# Définissez les variables d'environnement pour la connexion à la base de données
ENV POSTGRES_DB mydatabase
ENV POSTGRES_USER myuser
ENV POSTGRES_PASSWORD mypassword

# Copiez le script Python et le fichier CSV dans le conteneur
COPY init_db.sql /docker-entrypoint-initdb.d/
COPY statsNFL.csv /docker-entrypoint-initdb.d/