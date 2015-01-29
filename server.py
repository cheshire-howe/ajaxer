import os

import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
            (r"/ajax/(\w+)/?(\w+)?/?(\w+)?/?(\w+)?/?(\w+)?", AjaxHandler),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
        )
        tornado.web.Application.__init__(self, handlers, **settings)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class AjaxHandler(tornado.web.RequestHandler):
    def get(self, controller, action=None, *params):
        if (action is not None):
            c = __import__(controller)
            result = getattr(c, action)(*params)
            self.render("modules/%s.html" % action, result=result)
        else:
            self.render("modules/%s.html" % controller)


def main():
    tornado.options.parse_command_line()
    app = Application()
    app.listen(options.port)
    print "server up and running on port %d" % options.port
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
