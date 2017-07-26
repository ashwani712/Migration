#!/usr/bin/python
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='example.log')
logging.debug('A debug message')
logging.info('Some information')
logging.warning('A shot across the bows')
