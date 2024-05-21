from modeltranslation.translator import translator, TranslationOptions
from .models import *


class ProductTranslation(TranslationOptions):
    fields = ('title', 'description')


translator.register(Product, ProductTranslation)
