import os
from django_productline.context import PRODUCT_CONTEXT

DATA_DIR = os.path.join(PRODUCT_CONTEXT.CONTAINER_DIR, '__data__/')

if not os.path.exists(DATA_DIR):
    os.mkdir(DATA_DIR)

refine_MEDIA_ROOT = os.path.join(DATA_DIR, 'uploads/')
refine_STATIC_ROOT = os.path.join(DATA_DIR, 'generated_static/')
