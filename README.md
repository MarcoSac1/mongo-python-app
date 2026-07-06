# Mongo-Python-App

## Descrizione

Mongo-Python-App è un'API REST sviluppata in Python utilizzando FastAPI e MongoDB Atlas. Il progetto è stato realizzato con un'architettura modulare per mostrare come sviluppare un backend mantenendo separate le responsabilità delle diverse componenti.

L'applicazione permette di gestire due risorse principali:

- Users
- Courses

Per entrambe sono disponibili le principali operazioni CRUD (Create, Read, Update e Delete).

Il progetto utilizza inoltre il Repository Pattern, così da evitare duplicazioni di codice e rendere facilmente estendibile l'applicazione.

---

# Architettura del progetto

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

Ogni cartella ha una responsabilità ben precisa.

- **models** contiene i modelli Pydantic utilizzati per validare i dati ricevuti dalle API.
- **routes** definisce gli endpoint REST e riceve le richieste HTTP provenienti dal client.
- **repositories** contiene tutta la logica di accesso al database MongoDB. Il `BaseRepository` implementa le operazioni CRUD generiche, mentre `UserRepository` e `CourseRepository` estendono tali funzionalità per le rispettive collezioni.
- **database.py** gestisce la connessione con MongoDB Atlas.
- **config.py** legge le variabili d'ambiente dal file `.env`.
- **main.py** rappresenta il punto di ingresso dell'applicazione e registra tutti i router.

---

# Requisiti

- Python 3.12+
- MongoDB Atlas
- pip

---

# Installazione

Clonare il repository:

```bash
git clone <repository-url>
cd mongo-python-app
```

Creare l'ambiente virtuale:

```bash
python3 -m venv .venv
```

Attivarlo:

Linux/macOS

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Installare le dipendenze:

```bash
pip install -r requirements.txt
```

---

# Configurazione

Creare un file `.env` nella cartella principale del progetto inserendo:

```env
MONGO_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/
MONGO_DB_NAME=nome_database
```

Le credenziali devono essere quelle del proprio cluster MongoDB Atlas.

---

# Avvio del server

Avviare l'applicazione con:

```bash
uvicorn app.main:app --reload
```

Il server sarà disponibile all'indirizzo:

```
http://127.0.0.1:8000
```

La documentazione Swagger sarà disponibile su:

```
http://127.0.0.1:8000/docs
```

---

# Esempi di richieste HTTP

## Ottenere tutti gli utenti

```http
GET /users
```

---

## Creare un utente

```http
POST /users
```

Payload JSON

```json
{
  "name": "Mario Rossi",
  "email": "mario.rossi@email.it",
  "city": "Roma"
}
```

---

## Ottenere tutti i corsi

```http
GET /courses
```

---

## Creare un corso

```http
POST /courses
```

Payload JSON

```json
{
  "title": "Python Base",
  "category": "Programming",
  "description": "Corso introduttivo a Python",
  "active": true
}
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

L'applicazione utilizza il Repository Pattern per separare la logica di accesso al database dalla logica delle API.

Il `BaseRepository` implementa tutte le operazioni CRUD comuni. Le classi `UserRepository` e `CourseRepository` ereditano tali funzionalità, aggiungendo esclusivamente la logica specifica delle rispettive collezioni.

Questa struttura rende il progetto più modulare, facilmente estendibile e riduce la duplicazione del codice.
