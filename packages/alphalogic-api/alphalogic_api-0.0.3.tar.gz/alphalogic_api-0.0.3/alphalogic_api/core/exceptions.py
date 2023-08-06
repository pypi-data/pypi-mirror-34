# -*- coding: utf-8 -*-
import sys
import linecache


class IncorrectRPCRequest(Exception):

    def __init__(self, msg):
        super(IncorrectRPCRequest, self).__init__(msg)


class RequestError(Exception):

    def __init__(self, msg):
        super(RequestError, self).__init__(msg)


class ComponentNotFound(Exception):
    """
    If component not found in the Device
    """
    def __init__(self, msg):
        super(ComponentNotFound, self).__init__(msg)


class Exit(Exception):
    pass


def exception_info():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    print 'Exception in ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj)
