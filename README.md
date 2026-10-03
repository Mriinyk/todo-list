# Todo List

A Django task manager with deadlines, reusable tags, task completion controls, and tag management.

## Requirements

- Python 3.10 or newer
- pip

## Run locally

```bash
python -m venv .venv
```

Activate the virtual environment, then install dependencies and initialize the database:

```bash
python -m pip install -r requirements.txt
```

Copy `.env.example` to `.env` and replace `SECRET_KEY` with a private random value. Keep `.env` out of version control.

Then initialize the database and start the development server:

```bash
python manage.py migrate
python manage.py runserver
```

Open <http://127.0.0.1:8000/> for tasks or <http://127.0.0.1:8000/tags/> to manage tags.

## Features

- Create, edit, delete, complete, and reopen tasks.
- Set an optional deadline and assign multiple tags to a task.
- Create, edit, and delete tags.
- Tasks are sorted with open tasks first, then by newest creation time.
- Responsive Bootstrap interface with shared navigation on every page.

## Tests

```bash
python manage.py test
```
