# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
	title 		= models.CharField(max_length=120) 
	description = models.TextField(blank=True,null=True)
	price 		= models.DecimalField(decimal_places=2,max_digits=1000) 
	summary	 	= models.TextField(default='Just to understand!!') 
