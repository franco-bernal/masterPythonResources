import logging as log

log.basicConfig(level=log.DEBUG)

if __name__ == '__main__':
    log.debug('xxxxx')
    log.info('Mensaje a nivel info')
    log.warning('Mensaje a nivel de warning')
    log.error('Mensaje a nivel de error')
    log.critical('Mensaje a nivel critico')