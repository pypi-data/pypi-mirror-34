import time
from datetime import datetime

from google.cloud import logging
from google.cloud.logging import DESCENDING

from inovibe import log


def test_log_info():
    client = logging.Client(project='ino-vibe-dev')
    FILTER = 'logName:projects/ino-vibe-dev/logs/unittest'

    rand_value = datetime.now().timestamp()
    log.info(label='unittest',
             data={'type': 'random_log', 'msg': rand_value})

    time.sleep(10.0)

    iterator = client.list_entries(filter_=FILTER,
                                   order_by=DESCENDING)
    pages = iterator.pages
    page1 = next(pages)

    first_entry = next(page1)

    assert first_entry.payload['type'] == 'random_log'
    assert first_entry.payload['msg'] == rand_value
    assert first_entry.severity == 'INFO'


def test_log_wrong_format():
    client = logging.Client(project='ino-vibe-dev')
    FILTER = 'logName:projects/ino-vibe-dev/logs/unittest'

    log.info(label='unittest', data='hello world')

    time.sleep(10.0)

    iterator = client.list_entries(filter_=FILTER,
                                   order_by=DESCENDING)
    pages = iterator.pages
    page1 = next(pages)

    first_entry = next(page1)

    assert first_entry.payload == 'hello world'
    assert first_entry.severity == 'ERROR'
