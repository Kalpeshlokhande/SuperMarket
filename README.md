
# Online Supermarket

A basic e-commerce supermarket site built with Django.

## Features

- Customer registration/login/logout
- Browse products by category
- Add to cart, remove from cart
- Checkout with address (Cash on Delivery only)
- View order history
- Admin: manage products, categories, and orders

## Setup

1. Clone the repo and enter directory:
   ```
   git clone <your-github-url>
   cd supermarket
   ```

2. Create and activate virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install django pillow
   ```

4. Migrate and create superuser:
   ```
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ```

5. Run server:
   ```
   python manage.py runserver
   ```

6. Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

