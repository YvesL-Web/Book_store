from django.test import TestCase
from django.urls import reverse

from .models import Book

# Create your tests here.

class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="Dance With The Fire",
            author = "Marcus Dark",
            price="25.00",
        )

    def test_book_listing(self):
        self.assertEqual(f"{self.book.title}","Dance With The Fire")
        self.assertEqual(f"{self.book.author}","Marcus Dark")
        self.assertEqual(f"{self.book.price}","25.00")

    def test_book_list_view(self):
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Dance With The Fire")
        self.assertTemplateUsed(response, "books/book_list.html")

    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get("/books/12345/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Dance With The Fire")
        self.assertTemplateUsed(response, "books/book_detail.html")