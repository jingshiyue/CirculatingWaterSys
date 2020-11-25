from django.test import TestCase
from pathlib import Path
# Create your tests here.
BASE_DIR = Path(__file__).resolve().parent.parent
print(type(BASE_DIR))
print(str(BASE_DIR))