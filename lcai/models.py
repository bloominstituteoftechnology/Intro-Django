from django.db import models

SECTION_NAMES = (
    'home',
    'proyectos',
    'eventos',
    'miembros',
)


class Home(models.Model):
    texto_es = models.TextField(blank=True)
    texto_en = models.TextField(blank=True)
    # foto_1 = PENDING
    # foto_2 = PENDING
    # foto_3 = PENDING

    def __str__(self):
        return "Home page info."


class Project(models.Model):
    title_es = models.CharField(max_length=128, blank=False)
    title_en = models.CharField(max_length=128, blank=False)
    intro_es = models.TextField(blank=False)
    intro_en = models.TextField(blank=False)
    description_es = models.TextField(blank=True)
    description_en = models.TextField(blank=True)
    # foto1
    # foto2
    # foto3
    # foto4

    def __str__(self):
        return self.title_es


class Evento(models.Model):
    evento_es = models.CharField(max_length=256, blank=False)
    evento_en = models.CharField(max_length=256, blank=False)
    # foto = PENDING (images)
    # cartel = PENDING (images)
    # folleto_frontal = PENDING (images)
    # folleto_reverso = PENDING (images)

    def __str__(self):
        return self.evento_es


class Role(models.Model):
    ROLES = (
        ('role_dir', 'directora'),
        ('role_inv', 'investigadores'),
        ('role_doc', 'doctorandos'),
        ('role_phd', 'phpthesis'),
        ('role_col', 'colaboradores'),
    )

    role = models.CharField(
        max_length=24,
        choices=ROLES,
        default='role_inv',
    )


class Miembro(Role):
    nombre = models.CharField(max_length=128, blank=False)
    email = models.EmailField(max_length=254)
    # descrip_es
    # descrip_en
    # enlace_a_web
    # enlace_a_web_personal
    # title_en
    # title_es
    # universidad_en
    # universidad_es
    # foto

    def __str__(self):
        return self.nombre


''' SECOND ATTEMPT
class Section(models.Model):
    SECTION_NAMES = (
        ('section_h', 'home'),
        ('section_p', 'proyectos'),
        ('section_e', 'eventos'),
        ('section_m', 'miembros'),
    )

    section = models.CharField(
        max_length=24,
        choices=SECTION_NAMES,
        default='proyectos',
    )

'''
