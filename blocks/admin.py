from django.contrib import admin

from .models import Block


class BlockAdmin(admin.ModelAdmin):
    ''' Admin panel with the ability to search by block height and hash.
        Filtering by the address of the miner and the number of transactions'''

    list_display = ('height', 'haash', 'timestamp',
                    'miner', 'transactionCount')
    search_fields = ('height', 'haash')
    list_filter = ('miner', 'transactionCount')


admin.site.register(Block, BlockAdmin)
