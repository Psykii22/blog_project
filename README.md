# Blog Project

A simple blog application built with Django and SQLite.

## Features

- [x] Create, Read, Update, Delete (CRUD) blog posts
- [x] Category management (Create & List)
- [x] Search posts by title or content
- [x] Filter posts by category and status
- [x] Pagination (5 posts per page)
- [x] Related posts suggestion
- [x] Draft / Published status for posts
- [x] Class-Based Views (CBV)

## Tech Stack

- Python
- Django
- SQLite
- HTML/CSS

## Run Locally

```bash
# Clone the repo
git clone https://github.com/Psykii22/blog_project.git
cd blog_project

# Create virtual environment
python -m venv venv
venv\Scripts\activate       # Windows
# source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.
