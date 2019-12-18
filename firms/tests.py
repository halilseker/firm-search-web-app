from django.test import Client, TestCase
from django.urls import reverse

from .models import Firm


class FirmTests(TestCase):

    def setUp(self):
        self.firm = Firm.objects.create(
            firm_title='KarMetal',
            firm_address='Sakarya',
            firm_phone_number='0534 555 55 55',
            firm_mobile_number='0543 444 44 44',
            firm_services='Metal Dograma',
            firm_representative='Metin Kar',
            firm_email='karmetal@gmail.com',
        )

    def test_firm_listing(self):
        self.assertEqual(f'{self.firm.firm_title}', 'KarMetal')
        self.assertEqual(f'{self.firm.firm_address}', 'Sakarya')
        self.assertEqual(f'{self.firm.firm_phone_number}', '0534 555 55 55')
        self.assertEqual(f'{self.firm.firm_mobile_number}', '0543 444 44 44')
        self.assertEqual(f'{self.firm.firm_services}', 'Metal Dograma')
        self.assertEqual(f'{self.firm.firm_representative}', 'Metin Kar')
        self.assertEqual(f'{self.firm.firm_email}', 'karmetal@gmail.com')

    def test_firm_list_view(self):
        response = self.client.get(reverse('firm_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'KarMetal')
        self.assertTemplateUsed(response, 'firms/firm_list.html')

    def test_firm_detail_view(self):
        response = self.client.get(self.firm.get_absolute_url())
        no_response = self.client.get('/firms/1234/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'KarMetal')
        self.assertTemplateUsed(response, 'firms/firm_detail.html')
