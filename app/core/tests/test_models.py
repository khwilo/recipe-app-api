"""
Tests for models
"""

from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase

from core import models


def create_user(email="john@example.com", password="john@1234"):
    """Create and return a new user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    """Test models"""

    def test_create_user_with_email_success(self):
        """Test creating a user with email is successful"""
        email = "test@example.com"
        password = "password123"
        user = get_user_model().objects.create_user(
            email=email, password=password
        )  # noqa

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users"""
        sample_emails = [
            ["test1@EXAMPLE.com", "test1@example.com"],
            ["Test2@Example.com", "Test2@example.com"],
            ["TEST3@EXAMPLE.COM", "TEST3@example.com"],
            ["test4@example.com", "test4@example.com"],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(
                email=email, password="sample123"
            )
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test that creating a user without an email raises an exception"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user("", "pass123")

    def test_create_super_user(self):
        """Test creation of a superuser"""
        user = get_user_model().objects.create_superuser(
            "test@example.com", "pass1234"
        )  # no qa

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_recipe(self):
        """Test create recipe is successful"""
        user = get_user_model().objects.create_user(
            "test@example.com", "pass1234"
        )  # noqa
        recipe = models.Recipe.objects.create(
            user=user,
            title="Recipe One",
            time_minutes=5,
            price=Decimal("5.50"),
            description="About Recipe One",
        )

        self.assertEqual(str(recipe), recipe.title)

    def test_create_tag(self):
        """Test creating tags is successful"""
        user = create_user()
        tag = models.Tag.objects.create(user=user, name="Tag1")

        self.assertEqual(str(tag), tag.name)

    def test_create_ingredient(self):
        """Test creating ingredients is successful"""
        user = create_user()
        ingredient = models.Ingredient.objects.create(
            user=user, name="Ingredient1"
        )  # noqa

        self.assertEqual(str(ingredient), ingredient.name)
