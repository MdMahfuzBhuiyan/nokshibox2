from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Custom user manager
class UserManager(BaseUserManager):
    def create_user(self, email, full_name, mobile_no, role, password=None, **extra_fields):
        if not email:
            raise ValueError('Email must be set')
        if role not in ['buyer', 'seller']:
            raise ValueError('Role must be either buyer or seller')
        email = self.normalize_email(email)
        user = self.model(email=email, full_name=full_name, mobile_no=mobile_no, role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, mobile_no, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, full_name, mobile_no, role='admin', password=password, **extra_fields)

# Custom user model
class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
    ]

    full_name = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='user_photos/', blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)

    profile_completed = models.BooleanField(default=False)

    security_question_1 = models.CharField(max_length=255, blank=True, null=True)
    security_answer_1 = models.CharField(max_length=255, blank=True, null=True)

    security_question_2 = models.CharField(max_length=255, blank=True, null=True)
    security_answer_2 = models.CharField(max_length=255, blank=True, null=True)


    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # avoid clash
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set_permissions',  # avoid clash
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'mobile_no']

    def __str__(self):
        return f"{self.full_name} ({self.role})"

# Category model
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Product model
class Product(models.Model):
    title = models.CharField(max_length=255)
    details = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='media/product_images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    seller = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'seller'})
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title