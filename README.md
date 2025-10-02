# NokshiBox

A basic Django e-commerce platform for buyers and sellers.

## Features
- Buyer & seller roles
- Product listing & category-wise organization
- Seller can add/edit products
- Product details page with seller info
- Session-based login/signup

## Requirements
- Python 3.11+ (tested on 3.13)
- Django 4.2+
- SQLite (default)
- Other dependencies listed in `requirements.txt`

## Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/osama-bq/nokshibox.git
cd nokshibox
````

2. **Create & activate virtual environment**

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Apply migrations**

```bash
python manage.py makemigrations api
python manage.py migrate
```

5. **Create superuser (optional)**

```bash
python manage.py createsuperuser
```

6. **Run server**

```bash
python manage.py runserver
```

7. **Access the site**

* Buyer home: `http://127.0.0.1:8000/`
* Seller home: `http://127.0.0.1:8000/seller/`
* Admin: `http://127.0.0.1:8000/admin/`

## Notes

* Media files are stored in `media/`.
* `venv/` and `media/` are excluded from git.
* For testing, add some categories via admin or shell.
