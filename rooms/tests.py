from django.test import TestCase
from django.urls import resolve
from .views import rooms_view


class RoomsTest(TestCase):
    # def test_스모크(self):
    #     assert 1 is not 1, "당연히 1 = 1 ..."

    def test_연결테스트(self):
        found = resolve("/api/v1/rooms/list/")
        self.assertEqual(found.func, rooms_view)
