# librerias
import logging as log

# Configuracion del log
log.basicConfig(level=log.INFO,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[log.FileHandler('logger.log'), log.StreamHandler()]
                )

# test
if __name__ == '__main__':
    log.debug('Debug level')
    log.info('Info level')
    log.warning('Warning level')
    log.error('Error level')
    log.critical('Critical level')
    