import json
import logging
import time

import requests

from blocks.models import Block

bcsblocks_url = 'https://bcschain.info/api/recent-blocks?count='
bcsinfo_url = 'https://bcschain.info/api/info/'


def get_height():
    try:
        response = requests.get(bcsinfo_url)
        response.raise_for_status()
    except requests.exceptions.ConnectionError:
        logging.error('Ошибка соединения.')
    except requests.exceptions.HTTPError:
        logging.error(f'Ошибка HTTP, код: {response.status_code}')

    try:
        height = response.json().get('height')
    except (json.JSONDecodeError, ValueError, TypeError, IndexError):
        logging.error('Невозможно декодировать JSON.')

    return height


def get_blocks(height):
    try:
        response = requests.get(bcsblocks_url + str(height))
        response.raise_for_status()
    except requests.exceptions.ConnectionError:
        logging.error('Ошибка соединения.')
    except requests.exceptions.HTTPError:
        logging.error(f'Ошибка HTTP, код: {response.status_code}')

    try:
        return response.json()
    except json.JSONDecodeError:
        logging.error('Невозможно декодировать JSON.')


def add_blocks():
    ''' The function works with the bcschain API.
        On the first call, it will unload all blocks from the blockchain. '''

    height = get_height()

    try:
        lastdb_block = Block.objects.all()[:1]
        maxdb_height = lastdb_block[0].height
        if maxdb_height == height:
            return None
        if maxdb_height != height:
            height -= maxdb_height
    except IndexError:
        pass

    blocks = get_blocks(height)

    for block in blocks:
        Block.objects.create(
            height=block.get('height'),
            haash=block.get('hash'),
            timestamp=block.get('timestamp'),
            miner=block.get('miner'),
            transactionCount=block.get('transactionCount')
        )

    time.sleep(10)
