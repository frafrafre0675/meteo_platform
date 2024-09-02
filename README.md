# Plateforme Météo avec Kafka & NoSQL FRANCESCO KUHN

## Installation rapide

### Clonez le projet

        git clone https://github.com/votre-repo/meteorological-platform.git
        cd meteorological-platform

### Lancez les services

        ./scripts/start.sh

### Accédez au Dashboard

        Ouvrez http://localhost:8501 dans votre navigateur pour voir le dashboard en action.

### Exécutez les tests (optionnel)

        docker-compose exec producer python src/tests/producer_test.py
        docker-compose exec consumer python src/tests/consumer_test.py

### Arrêtez tous les services quand vous avez terminé

        ./scripts/stop.sh
