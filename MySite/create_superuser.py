import os
from django.contrib.auth import get_user_model

User = get_user_model()

def create_admin():
    username = os.environ.get("ADMIN_USERNAME", "admin")
    email = os.environ.get("ADMIN_EMAIL", "admin@email.com")
    password = os.environ.get("ADMIN_PASSWORD", "admin123")

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print("Superusuário criado com sucesso!")
    else:
        print("Superusuário já existe.")

if __name__ == "__main__":
    create_admin()