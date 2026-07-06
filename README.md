# Mongo-Python-App

## Descrizione

![CI/CD](https://github.com/MarcoSac1/mongo-python-app/actions/workflows/ci.yml/badge.svg)


Mongo-Python-App è un'API REST sviluppata in Python utilizzando FastAPI e MongoDB Atlas.

L'obiettivo del progetto è mostrare come realizzare un backend moderno seguendo un'architettura modulare, mantenendo separate le diverse responsabilità dell'applicazione e rendendo il codice facilmente estendibile e riutilizzabile.

L'API permette di gestire due risorse principali:

- Users
- Courses

Per entrambe sono disponibili le principali operazioni CRUD (Create, Read, Update e Delete).

Il progetto utilizza inoltre il Repository Pattern per centralizzare tutta la logica di accesso al database ed evitare duplicazioni di codice.

---

# Architettura

L'applicazione è organizzata in moduli, in modo che ogni componente abbia un compito ben preciso.

```
app/
│
├── main.py
├── config.py
├── database.py
│
├── models/
│   ├── user_model.py
│   └── course_model.py
│
├── repositories/
│   ├── base_repository.py
│   ├── user_repository.py
│   └── course_repository.py
│
├── routes/
│   ├── user_routes.py
│   └── course_routes.py
│
└── utils/
    └── mongo_helpers.py
```

Le responsabilità dei vari moduli sono le seguenti:

- **main.py** rappresenta il punto di ingresso dell'applicazione. Qui viene creata l'istanza di FastAPI e vengono registrati tutti i router.

- **config.py** legge le variabili d'ambiente presenti nel file `.env`, come l'URI di MongoDB e il nome del database.

- **database.py** gestisce la connessione a MongoDB Atlas e fornisce un'unica istanza del database a tutta l'applicazione.

- **models/** contiene i modelli Pydantic utilizzati per validare automaticamente i dati ricevuti dalle richieste HTTP.

- **routes/** definisce gli endpoint REST. Ogni route riceve una richiesta HTTP e la inoltra al repository appropriato.

- **repositories/** contiene la logica di accesso al database. Il `BaseRepository` implementa tutte le operazioni CRUD comuni, mentre `UserRepository` e `CourseRepository` ereditano queste funzionalità aggiungendo solamente la logica specifica della propria collezione.

- **utils/** contiene funzioni di supporto utilizzate in più parti del progetto, come la conversione dei documenti MongoDB in oggetti facilmente serializzabili.

---

# Requisiti

Prima di eseguire il progetto è necessario avere installato:

- Python 3.12 o superiore
- pip
- Git
- Un database MongoDB Atlas

---

# Installazione

Clonare il repository:

```bash
git clone <repository-url>
cd mongo-python-app
```

Creare un ambiente virtuale:

```bash
python3 -m venv .venv
```

Attivarlo.

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

Installare tutte le dipendenze del progetto:

```bash
pip install -r requirements.txt
```

---

# Configurazione del file .env

Creare un file `.env` nella cartella principale del progetto.

Inserire al suo interno le variabili d'ambiente necessarie alla connessione con MongoDB Atlas:

```env
MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/
MONGO_DB_NAME=nome_database
```

Dove:

- **MONGO_URI** è la stringa di connessione al cluster MongoDB Atlas.
- **MONGO_DB_NAME** è il nome del database utilizzato dall'applicazione.

Il file `.env` non viene caricato su GitHub poiché contiene informazioni riservate.

---

# Avvio del server

Per avviare il server FastAPI eseguire:

```bash
uvicorn app.main:app --reload
```

Una volta avviato, l'applicazione sarà disponibile all'indirizzo:

```
http://127.0.0.1:8000
```

La documentazione interattiva Swagger sarà disponibile su:

```
http://127.0.0.1:8000/docs
```

Da questa pagina è possibile visualizzare e testare tutti gli endpoint dell'API.

---

# Esempi di richieste HTTP

## Ottenere tutti gli utenti

```http
GET /users
```

oppure

```bash
curl http://127.0.0.1:8000/users
```

---

## Creare un nuovo utente

```http
POST /users
```

Payload JSON:

```json
{
  "name": "Mario",
  "surname": "Rossi",
  "email": "mario@email.it",
  "city": "Roma",
  "active": true
}
```

Con `curl`:

```bash
curl -X POST http://127.0.0.1:8000/users \
-H "Content-Type: application/json" \
-d '{
  "name":"Mario",
  "surname":"Rossi",
  "email":"mario@email.it",
  "city":"Roma",
  "active":true
}'
```

---

## Ottenere tutti i corsi

```http
GET /courses
```

oppure

```bash
curl http://127.0.0.1:8000/courses
```

---

## Creare un nuovo corso

```http
POST /courses
```

Payload JSON:

```json
{
  "title": "Python Base",
  "category": "Programming",
  "description": "Corso introduttivo a Python",
  "active": true
}
```

Con `curl`:

```bash
curl -X POST http://127.0.0.1:8000/courses \
-H "Content-Type: application/json" \
-d '{
  "title":"Python Base",
  "category":"Programming",
  "description":"Corso introduttivo a Python",
  "active":true
}'
```

---

# Tecnologie utilizzate

- Python
- FastAPI
- MongoDB Atlas
- PyMongo
- Pydantic
- Uvicorn

---

# Repository Pattern

Per evitare di riscrivere le stesse operazioni CRUD per ogni collezione del database, il progetto utilizza il Repository Pattern.

Il `BaseRepository` implementa tutte le operazioni generiche come creazione, lettura, modifica ed eliminazione dei documenti. I repository specifici, come `UserRepository` e `CourseRepository`, ereditano questi metodi e aggiungono soltanto le funzionalità dedicate alle rispettive collezioni.

Questa soluzione rende il codice più pulito, facilmente manutenibile ed estendibile nel tempo.

---

# Conclusione

Questo progetto rappresenta un esempio di backend sviluppato seguendo buone pratiche di progettazione software. L'utilizzo di FastAPI, MongoDB Atlas e del Repository Pattern permette di mantenere il codice organizzato, modulare e facilmente estendibile, favorendo anche il lavoro collaborativo tra più sviluppatori.
