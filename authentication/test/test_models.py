from rest_framework.test import APITestCase
from authentication.models import User




class TestModel(APITestCase):

    def test_create_user(self):
        user = User.objects.create_user('phant', 'phant@gmail.com', 'phantom12345')  # User.objects
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, 'phant@gmail.com')


    def test_create_super_user(self):
        user = User.objects.create_superuser('phant', 'phant@gmail.com', 'phantom12345')  # User.objects
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, 'phant@gmail.com')


    def test_raises_error_when_no_username_is_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user, username="", email="phant@gmail.com", password="phantom12345")

    def test_raises_error_when_no_email_is_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user, username="username", email="", password="phantom12345'")

    def test_cant_create_super_user_with_no_staff_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_staff=True.'):
            User.objects.create_superuser('phant', 'phant@gmail.com', 'phantom12345', is_staff=False)

    def test_cant_create_super_user_with_no_supuser_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_superuser=True.'):
            User.objects.create_superuser('phant', 'phant@gmail.com', 'phantom12345', is_superuser=False)