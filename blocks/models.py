from django.db import models
from django.utils.translation import gettext_lazy as _

from unixtimestampfield.fields import UnixTimeStampField


class Block(models.Model):
    ''' Model of a single block of the blockchain.
    A special field for Unix time is used. '''

    height = models.PositiveIntegerField(
        verbose_name='высота блока', unique=True
    )
    haash = models.CharField(
        verbose_name='хэш блока', max_length=64, unique=True
    )
    timestamp = UnixTimeStampField(verbose_name='время блока')
    miner = models.CharField(verbose_name='адрес майнера', max_length=50)
    transactionCount = models.PositiveSmallIntegerField(
        verbose_name='кол-во транзакций')

    def __str__(self):
        return self.haash

    class Meta:
        ordering = ('-height',)
        verbose_name_plural = _('блоки')
