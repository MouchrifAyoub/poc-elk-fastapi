# POC – Centralisation des logs avec ELK (FastAPI + Logstash + Elasticsearch + Kibana)

## 🎯 Objectif

Mettre en place une preuve de concept (POC) démontrant la faisabilité de la **centralisation des logs applicatifs** à l'aide de la stack **ELK** :
- Logs générés par une **API FastAPI**
- Collectés et analysés via **Logstash**
- Stockés dans **Elasticsearch**
- Visualisés et monitorés dans **Kibana**

---

## 🏗 Architecture

```plaintext
FastAPI → app.log → Logstash → Elasticsearch → Kibana
```

---

## 📂 Structure du projet

```
POC_ELK_LOGS/
├── env/                    # Environnement virtuel Python
├── app.log                 # Fichier de logs généré par l'API
├── main.py                 # API FastAPI (génère les logs)
├── docker-compose.yml      # Stack ELK (Elasticsearch, Logstash, Kibana)
├── logstash.conf           # Configuration Logstash
└── README.md               # Ce fichier
```

---

## 🚀 Étapes de mise en route

### 1. Lancer la stack ELK

```bash
docker-compose up -d
```

### 2. Lancer l'API FastAPI

```bash
uvicorn main:app --reload
```

### 3. Générer des logs

Accéder à l’API :

- http://localhost:8000/
- http://localhost:8000/ping
- http://localhost:8000/fail (génère une erreur)

### 4. Accéder à Kibana

> http://localhost:5601

- Créer un index pattern : `logs-fastapi*`
- Sélectionner le champ `@timestamp`

---

## 📊 Visualisations Kibana

Visualisations créées dans le Dashboard :
- Histogramme : fréquence des logs par niveau
- Camembert : répartition des logs (INFO, ERROR…)
- (à venir) Table des derniers logs, alertes

---

## ✅ Résultat

- ✔ Centralisation fonctionnelle des logs
- ✔ Stack ELK opérationnelle
- ✔ Visualisation dynamique dans Kibana

---

## 📌 Auteurs
- Réalisé par Ayoub (POC DevOps & Observabilité)
