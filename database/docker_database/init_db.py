import psycopg2
import csv

# Connexion à la base de données PostgreSQL
conn = psycopg2.connect(
    dbname='mydatabase',
    user='myuser',
    password='mypassword',
    host='db',  # Nom du service Docker Compose pour le service PostgreSQL
    port='5432'
)

# Création d'un curseur
cur = conn.cursor()

# Création de la table dans la base de données
cur.execute('''
    CREATE TABLE IF NOT EXISTS nfl_stats (
        Year INT,
        Week INT,
        displayName VARCHAR(255),
        firstName VARCHAR(255),
        nickName VARCHAR(255),
        lastName VARCHAR(255),
        Team VARCHAR(255),
        Position VARCHAR(255),
        playerId INT,
        defensiveAssists INT,
        defensiveInterceptions INT,
        defensiveInterceptionsYards INT,
        defensiveForcedFumble INT,
        defensivePasses_Defensed INT,
        defensiveSacks INT,
        defensiveSafeties INT,
        defensiveSoloTackles INT,
        defensiveTotalTackles INT,
        defensiveTacklesForALoss INT,
        touchdownsDefense INT,
        fumblesLost INT,
        fumblesTotal INT,
        kickoffReturnsTouchdowns INT,
        kickoffReturnsYards INT,
        kickReturns INT,
        kickReturnsAverageYards FLOAT,
        kickReturnsLong INT,
        kickReturnsTouchdowns INT,
        kickReturnsYards INT,
        kickingFgAtt INT,
        kickingFgLong INT,
        kickingFgMade INT,
        kickingXkAtt INT,
        kickingXkMade INT,
        opponentFumbleRecovery INT,
        passingAttempts INT,
        passingCompletions INT,
        passingInterceptions INT,
        passingTouchdowns INT,
        passingYards INT,
        puntReturns INT,
        puntReturnsAverage_Yards FLOAT,
        puntReturnsLong INT,
        puntReturnsTouchdowns INT,
        puntingAverageYards FLOAT,
        puntingLong INT,
        puntingPunts INT,
        puntingPuntsInside20 INT,
        receivingReceptions INT,
        receivingTarget INT,
        receivingTouchdowns INT,
        receivingYards INT,
        rushingAttempts INT,
        rushingAverageYards FLOAT,
        rushingTouchdowns INT,
        rushingYards INT,
        totalPointsScored INT
    );
''')

# Lecture du fichier CSV et insertion des données dans la table
with open('/docker-entrypoint-initdb.d/statsNFL.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for row in reader:
        cur.execute('''
            INSERT INTO nfl_stats VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            );
        ''', tuple(row))

# Fermeture de la connexion
conn.commit()
cur.close()
conn.close()
