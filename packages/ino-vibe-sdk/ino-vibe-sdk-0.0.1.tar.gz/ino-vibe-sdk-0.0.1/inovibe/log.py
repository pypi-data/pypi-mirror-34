import logging

import google.cloud.logging
from google.cloud.logging.resource import Resource


class Singleton(type):
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '__instance'):
            cls.__instance = super(Singleton, cls).__call__(*args, **kwargs)

        return cls.__instance


class GCloudInstances(metaclass=Singleton):
    def __init__(self):
        self._log_client = google.cloud.logging.Client()
        self._log_client.setup_logging(log_level=logging.INFO)

    def logger(self, name):
        return self._log_client.logger(name)


def info(label, data):
    """Write log to StackDriver.

    data should be dictionary type.
    """
    logger = GCloudInstances().logger(name=label)

    LOG_RESOURCE = Resource(type='container', labels={})
    try:
        logger.log_struct(info=data,
                          severity='INFO',
                          resource=LOG_RESOURCE)
    except Exception as e:
        logger.log_text(text=data.__str__(),
                        severity='ERROR',
                        resource=LOG_RESOURCE)


def warn():
    pass


def report():
    pass
