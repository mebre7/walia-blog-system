# [Walia Blog System](https://walia-blog-system.onrender.com/)

A community-driven blog platform built with Django for publishing technology stories, country guides, field-specific insights, and more.

## Features

- **Blog posts** with draft/published status, featured image, slug auto-generation, and featured flag
- **Categories** with short code auto-generation, description, tagline, and image
- **Blog detail** page with related posts and category sidebar
- **Search** across title, content, category, and author with filter support
- **Posts by category** listing page
- **Trending post** section on the homepage (latest published post)
- **Featured posts** section (up to 5 flagged posts)
- **Newsletter subscribe** form with category interest selection
- **User accounts** via the `accounts` app (login required to read full posts)
- Custom dropdown UI for category selection (vanilla JS, no dependencies)

## Tech stack

- Python - Python programming language
- Django - Django web framework
- PostgreSQL / Supabase - PostgreSQL / Supabase database
- Cloudinary - Cloudinary media storage and CDN
- Gunicorn - Gunicorn WSGI server
- WhiteNoise - WhiteNoise static file management
- Bootstrap 5 - CSS framework
- Django Crispy Forms - Form rendering
- Render - Deployment platform


## Local setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd Walia-blog-system
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

Create a `.env` file in the project root:

```env
SECRET_KEY=replace-with-a-long-random-secret
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DATABASE_URL=postgresql://USER:PASSWORD@HOST:PORT/DATABASE?sslmode=require

CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret
CLOUDINARY_PREFIX=walia-blog/
```

For a simple local test, you may omit `DATABASE_URL`; Django will use `db.sqlite3`.

> Never commit `.env` files or Cloudinary/Supabase credentials.

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Create an administrator account

```bash
python manage.py createsuperuser
```

### 7. Start the development server

```bash
python manage.py runserver
```

Open:

- Website: `http://127.0.0.1:8000/`
- Admin panel: `http://127.0.0.1:8000/admin/`

Use the admin panel to create categories and publish blog posts.