from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, email, username=None, password=None, **extra_fields):
            extra_fields.setdefault("is_staff", True)
            extra_fields.setdefault("is_superuser", True)

            if extra_fields.get("is_staff") is not True:
                raise ValueError("Superuser must have is_staff=True.")
            if extra_fields.get("is_superuser") is not True:
                raise ValueError("Superuser must have is_superuser=True.")

            return self._create_user(username, email, password, **extra_fields)
