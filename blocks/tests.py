from django.test import Client, TestCase
from django.urls import reverse

from .models import Block


class TestUserAction(TestCase):
    ''' !!!  Before running the tests
         you need to comment out the add_blocks() in index function  !!! '''

    def setUp(self):
        self.client = Client()
        self.block = Block.objects.create(
            height=1,
            haash='988adb159f524bdf4008f091a39a8e590316654c383cb5c8acbce3194',
            timestamp=1610706373,
            miner='BTJi34JG4dmL5GbTYgDdp8Nyb7Mhpsd1az',
            transactionCount=2
        )

    def test_block_adding(self):
        urls = (
            reverse('index'),
            reverse('block', args=[self.block.height]),
        )

        for url in urls:
            with self.subTest(url=url):
                response = self.client.get(url)
                self.assertContains(response, self.block.height)
                self.assertContains(response, self.block.haash)
                self.assertContains(response, self.block.miner)
                self.assertContains(response, self.block.transactionCount)
