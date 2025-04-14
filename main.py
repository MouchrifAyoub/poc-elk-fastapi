from fastapi import FastAPI
import logging

# Configuration du logger
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
def read_root():
    logger.info("Page d'accueil appelée")
    return {"message": "Bienvenue sur l'API"}

@app.get("/ping")
def ping():
    logger.info("Ping reçu")
    return {"pong": True}

@app.get("/fail")
def fail():
    logger.error("Une erreur simulée est survenue")
    return {"error": "Erreur simulée"}
