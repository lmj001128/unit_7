
import logging

class Tools():

    def Log(self):
        log = logging.basicConfig(level=logging.DEBUG,
                                  format='%(levelname)s %(message)s %(asctime)s %(filename)s')
        return log

