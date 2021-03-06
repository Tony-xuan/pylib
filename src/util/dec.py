#encoding=utf-8
import logging
import time
def print_calling(fn):
    def wrapper(*args1, ** args2):
        s = "calling function %s"%(fn.__name__)
        logging.info(s)
        start = time.time()
        ret = fn(*args1, **args2)
        end = time.time()
#         s = "%s. time used = %f seconds"%(s, (end - start))
        s = "function [%s] has been called, taking %f seconds"%(fn.__name__, (end - start))
        logging.debug(s)
        return ret
    return wrapper


def print_test(fn):
    def wrapper(*args1, ** args2):
        s = "running test: %s..."%(fn.__name__)
        logging.info(s)
        ret = fn(*args1, **args2)
        s = "running test: %s...succeed"%(fn.__name__)
        logging.debug(s)
        return ret
    return wrapper
    
def print_calling_in_short(fn):
    def wrapper(*args1, ** args2):
        start = time.time()
        ret = fn(*args1, **args2)
        end = time.time()
        s = "function [%s] has been called, taking %f seconds"%(fn.__name__, (end - start))
        logging.debug(s)
        return ret
    return wrapper


