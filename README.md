# Personal Website

A personal website built with Django web framework featuring a blog, portfolio, and more.

## Features

- Responsive design using Bootstrap 5
- Blog with tagging system
- Pages with rich content
- Contact form
- User authentication
- Admin dashboard

## Prerequisites

- Python 3.8+
- pip (Python package manager)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/personal.git
   cd personal
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:

   ```bash
   python manage.py runserver
   ```

7. Access the site at <http://127.0.0.1:8000/>

## Environment Variables

For production deployment, set these environment variables:

- `DJANGO_SECRET_KEY`: Secret key for the Django application
- `DJANGO_DEBUG`: Set to "False" in production
- `DJANGO_ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `SITE_NAME`: Your website name
- `SITE_DESCRIPTION`: Your website description

## Customization

- Modify templates in the `templates` directory of each app
- Add CSS styles in `pages/static/css/style.css`
- Add JavaScript in `pages/static/js/main.js`

## Deployment

For production deployment:

1. Set environment variables as described above
2. Collect static files: `python manage.py collectstatic`
3. Set up a production database (PostgreSQL recommended)
4. Configure a web server (Nginx, Apache) with WSGI
5. Set up SSL certificate for HTTPS

## License

This project is licensed under the terms specified in the LICENSE file.
