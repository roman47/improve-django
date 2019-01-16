from django.urls import reverse
from django.test import TestCase

from .models import Menu, Item


class MenuViewsTests(TestCase):
    def setUp(self):
        self.Menu = Menu.objects.create(
            season="Fall",
            created_date="2018-1-1",
            expiration_date="2020-1-1"
        )
        self.Menu2 = Menu.objects.create(
            season="Summer",
            created_date="2018-1-1",
            expiration_date="2020-1-1"
        )

        self.Item = Item.objects.create(
            name="Pizza",
            description="not good for you",
            chef_id=1,
        )
        self.Item2 = Item.objects.create(
            name="Advocado Toast",
            description="So Hot right now",
            chef_id=1,
        )

    def test_menu_list_view(self):
        resp = self.client.get(reverse('menu_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.Menu, resp.context['menus'])
        self.assertIn(self.Menu2, resp.context['menus'])
        self.assertTemplateUsed(resp, 'menu/list_all_current_menus.html')
        self.assertContains(resp, self.Menu.season)

    def test_menu_detail_view(self):
        resp = self.client.get(reverse('menu_detail',
                                       kwargs={'pk': self.Menu.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.Menu, resp.context['menu'])

