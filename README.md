# Sticky Notes App

## Overview
Sticky Notes App is a Django-based web application that allows users to create, view, update, and delete notes. It demonstrates CRUD functionality, unit testing, and the Model-View-Template (MVT) architecture.

## Features
- Create sticky notes with a title and content.
- View a list of all notes.
- Update existing notes.
- Delete notes.
- Includes unit tests for all core functionality.
- Styled HTML templates with CSS.
- Proper handling of static files and database migrations.

## Project Structure
StickyNotes/
├── manage.py
├── sticky_notes/            # Project settings
├── notes/                   # App folder with models, views, forms, urls, tests
  ├── templates/             # HTML templates
  ├── static/                # CSS files
  └── migrations/            # Migration files

## Installation
1. Clone the repository:
```bash
git clone https://github.com/mmchunu/sticky-notes-app.git
cd sticky-notes-app

2. Create a virtual environment:
python -m venv venv

3. Activate the virtual environment:
Git Bash: source venv/Scripts/activate

4. Install Django:
pip install django

5. Run migrations:
python manage.py migrate

6. Start the development server:
python manage.py runserver

7. Open your browser and visit: http://127.0.0.1:8000/

## Run Tests
python manage.py test notes

## Notes
- The venv/ folder is excluded.
- Make sure all CRUD operations work properly.
- The project demonstrates Django skills including models, views, forms,
  templates, static files, migrations, and testing.

## GitHub Repository
[https://github.com/mmchunu/sticky-notes-app]
