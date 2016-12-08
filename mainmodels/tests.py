from django.test import TestCase
from .models import Category

class CategoryTestCase(TestCase):
    def setUp(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Database [ Category ]")
        Category.objects.create(categoryID=1,categoryName="Development")
        print("Insert [ Category : Development ]")
        Category.objects.create(categoryID=11,categoryName="Business")
        print("Insert [ Category : Business ]")
        Category.objects.create(categoryID=21,categoryName="IT & Software")
        print("Insert [ Category : IT & Software]")
        Category.objects.create(categoryID=31,categoryName="Office Productivity")
        print("Insert [ Category : Office Productivity ]")
        Category.objects.create(categoryID=41,categoryName="Personal Development")
        print("Insert [ Category : Personal Development ]")
        Category.objects.create(categoryID=51,categoryName="Design")
        print("Insert [ Category : Design ]")
        Category.objects.create(categoryID=61,categoryName="Photography")
        print("Insert [ Category : Photography ]")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    def test_Development_Element(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Category --> Devlopement Element")
        temp = Category.objects.get(categoryID=1)
        self.assertEqual(temp.categoryName, "Development")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    def test_Development_ID(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Category --> Devlopement ID")
        temp = Category.objects.get(categoryName="Development")
        self.assertEqual(temp.categoryID, 1)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    
    def test_Business_Element(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Category --> Business Element")
        temp = Category.objects.get(categoryID=11)
        self.assertEqual(temp.categoryName, "Business")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    def test_Business_ID(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Category --> Business ID")
        temp = Category.objects.get(categoryName="Business")
        self.assertEqual(temp.categoryID, 11)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    
    def test_IT(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Category --> IT & Software Element")
        temp = Category.objects.get(categoryID=21)
        self.assertEqual(temp.categoryName, "IT & Software")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    def test_IT(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Category --> IT & Software ID")
        temp = Category.objects.get(categoryName="IT & Software")
        self.assertEqual(temp.categoryID, 21)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    
    def test_Productivity_Element(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Category --> Office Productivity Element")
        temp = Category.objects.get(categoryID=31)
        self.assertEqual(temp.categoryName, "Office Productivity")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    def test_Productivity_ID(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Category --> Office Productivity ID")
        temp = Category.objects.get(categoryName="Office Productivity")
        self.assertEqual(temp.categoryID, 31)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    
    def test_Personal(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Category --> Personal Development Element")
        temp = Category.objects.get(categoryID=41)
        self.assertEqual(temp.categoryName, "Personal Development")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    def test_Personal(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Category --> Personal Development ID")
        temp = Category.objects.get(categoryName="Personal Development")
        self.assertEqual(temp.categoryID, 41)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    
    def test_Design_Element(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Category --> Design Element")
        temp = Category.objects.get(categoryID=51)
        self.assertEqual(temp.categoryName, "Design")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    def test_Design_ID(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Category --> Design ID")
        temp = Category.objects.get(categoryName="Design")
        self.assertEqual(temp.categoryID, 51)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    def test_Photography_Element(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Category --> Photography Element")
        temp = Category.objects.get(categoryID=61)
        self.assertEqual(temp.categoryName, "Photography")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    def test_Photography_ID(self):
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Category --> Photography ID")
        temp = Category.objects.get(categoryName="Photography")
        self.assertEqual(temp.categoryID, 61)
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
