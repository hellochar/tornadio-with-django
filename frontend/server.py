#! /usr/bin/env python

import os
import tornado.httpserver
import tornado.ioloop
import tornado.wsgi
import sys
import django.core.handlers.wsgi

def main():
    # Starting Django
    sys.path.append('/home/felix/Projects/trnserver/frontend')
    os.environ['DJANGO_SETTINGS_MODULE'] = 'frontend.settings'
    application = django.core.handlers.wsgi.WSGIHandler()
    container = tornado.wsgi.WSGIContainer(application)
    http_server = tornado.httpserver.HTTPServer(container)
    http_server.listen(8000)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
