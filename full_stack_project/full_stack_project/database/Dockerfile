# Use the official PostgreSQL image as the base image
FROM postgres

# Copy the SQL file into the container
COPY init_db.sql /docker-entrypoint-initdb.d/
COPY statsNFL.csv /docker-entrypoint-initdb.d/

# Environment variables for initializing the database
ENV POSTGRES_DB=mydatabase
ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword
