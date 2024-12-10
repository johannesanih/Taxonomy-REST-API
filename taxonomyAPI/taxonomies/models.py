from django.db import models

# Create your models here.
class Taxonomy(models.Model):
    REPRODUCTIVE_STRATEGY_CHOICES = [ ('HERMAPHRODITIC', 'Hermaphroditic'),
        ('DIOECIOUS', 'Dioecious'),
        ('SEQUENTIAL_HERMAPHRODITISM', 'Sequential Hermaphroditism'),
        ('SIMULTANEOUS_HERMAPHRODITISM', 'Simultaneous Hermaphroditism'),
        ('PARTHENOGENESIS', 'Parthenogenesis'),
        ('GYNOGENESIS', 'Gynogenesis'),
        ('HYBRIDOGENESIS', 'Hybridogenesis'),
    ]

    SEX_DETERMINATION_CHOICES = [
        ('GENETIC', 'Genetic'),
        ('ENVIRONMENTAL', 'Environmental'),
        ('HAPLO_DIPLOID', 'Haplo-diploid'),
        ('POLYGENIC', 'Polygenic'),
        ('EPIGENETIC', 'Epigenetic'),
    ]
    
    name = models.CharField(max_length=200, blank=False)
    male_name = models.CharField(max_length=200, blank=True)
    female_name = models.CharField(max_length=200, blank=True)
    
    reproductive_strategy = models.CharField(max_length=50, choices=REPRODUCTIVE_STRATEGY_CHOICES)
    sex_determination = models.CharField(max_length=50, choices=SEX_DETERMINATION_CHOICES)
    
    domain = models.CharField(max_length=255)
    kingdom = models.CharField(max_length=255)
    phylum = models.CharField(max_length=255)
    class_name = models.CharField(max_length=255)
    order = models.CharField(max_length=255)
    family = models.CharField(max_length=255)
    genus = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    
    description = models.TextField(blank=False)
    added_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['name']