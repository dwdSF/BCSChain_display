from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from django.views.decorators.cache import cache_page

from .models import Block
from .utils import add_blocks


@cache_page(30, key_prefix='index_page')
def index(request):
    ''' The function implements the download of the blocks from the blockchain.
        Displaying blocks with custom pagination. '''

    add_blocks()
    blocks = Block.objects.all()

    paginator = Paginator(blocks, 50)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
        'page': page,
        'paginator': paginator,
    }

    return render(request, 'index.html', context)


def block_view(request, block_height):
    ''' Displaying information about a single block. '''

    block = get_object_or_404(Block, height=block_height)
    context = {
        'single_block': block,
    }

    return render(request, 'block.html', context)
