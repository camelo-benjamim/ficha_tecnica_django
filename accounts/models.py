# accounts/models.py
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


class AccountManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, nome_empresa, celular,proprietario,cnpj,segmento_empresa, password, **extra_fields):
        values = [email, nome_empresa, celular,proprietario,cnpj,segmento_empresa]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        for field_name, value in field_value_map.items():
            if not value:
                raise ValueError('The {} value must be set'.format(field_name))

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            nome_empresa=nome_empresa,
            celular=celular,
            proprietario=proprietario,
            cnpj=cnpj,
            segmento_empresa=segmento_empresa,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, nome_empresa, celular,proprietario,cnpj,segmento_empresa, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, nome_empresa, celular,proprietario,cnpj,segmento_empresa, password, **extra_fields)

    def create_superuser(self, email, nome_empresa, celular,proprietario,cnpj,segmento_empresa=None,password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, nome_empresa, celular,proprietario,cnpj,segmento_empresa,password, **extra_fields)

class SegmentoEmpresa(models.Model):
    class Meta:
        verbose_name = "Segmento"
        verbose_name_plural = "Segmentos"
    nome_segmento = models.CharField(max_length=40,unique=True,verbose_name="segmento")

    def __str__(self):
        return self.nome_segmento
class Account(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
    email = models.EmailField(unique=True)
    logo = models.ImageField(upload_to="logo_usuarios/",null=True,blank=True,default=None)
    proprietario = models.CharField(max_length=150)
    nome_empresa = models.CharField(max_length=120,unique=True)
    segmento_empresa = models.ForeignKey(SegmentoEmpresa,on_delete=models.CASCADE,blank=True,null=True)
    cnpj = models.IntegerField(unique=True,validators=[MinValueValidator(111111111111),
                                       MaxValueValidator(99999999999999)])
    celular = models.IntegerField(unique=True,validators=[MinValueValidator(11911111111),
                                       MaxValueValidator(99999999999)])
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['celular', 'proprietario','nome_empresa','cnpj']

    def __str__(self):
        return self.nome_empresa