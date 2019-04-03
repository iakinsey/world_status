from logging import getLogger, DEBUG, StreamHandler, Formatter
from sys import stdout


handler = StreamHandler(stdout)
log = getLogger("world_status")

handler.setFormatter(Formatter('[%(asctime)s] %(message)s'))
log.addHandler(handler)
log.setLevel(DEBUG)
