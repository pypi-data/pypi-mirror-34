#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import base64
import functools
import os
from typing import Any, Callable

from tornado import web
from tornado.log import access_log


BASE_HTML = '''
<html>
<head><title>main</title></head>
<body>
<h1 id="hello">Hello</h1>
<a id="link1" href="./1">link1</a>
<a id="link2" href="./2">link2</a>
</body>
</html>
'''


class MainHandler(web.RequestHandler):
    def get(self) -> None:
        self.write(BASE_HTML)


class EmptyHandler(web.RequestHandler):
    def get(self) -> None:
        self.write('')


class LongHandler(web.RequestHandler):
    async def get(self) -> None:
        await asyncio.sleep(0.1)
        self.write('')


class LinkHandler1(web.RequestHandler):
    def get(self) -> None:
        self.set_status(200)
        self.write('''
<head><title>link1</title></head>
<h1 id="link1">Link1</h1>
<a id="back1" href="./">back1</a>
        ''')


class RedirectHandler1(web.RequestHandler):
    def get(self) -> None:
        self.redirect('/redirect2')


class RedirectHandler2(web.RequestHandler):
    def get(self) -> None:
        self.write('<h1 id="red2">redirect2</h1>')


def auth_api(username: str, password: str) -> bool:
    if username == 'user' and password == 'pass':
        return True
    else:
        return False


def basic_auth(auth: Callable[[str, str], bool]) -> Callable:
    def decore(f: Callable) -> Callable:
        def _request_auth(handler: Any) -> None:
            handler.set_header('WWW-Authenticate', 'Basic realm=JSL')
            handler.set_status(401)
            handler.finish()

        @functools.wraps(f)
        def new_f(*args: Any) -> None:
            handler = args[0]

            auth_header = handler.request.headers.get('Authorization')
            if auth_header is None:
                return _request_auth(handler)
            if not auth_header.startswith('Basic '):
                return _request_auth(handler)

            auth_decoded = base64.b64decode(auth_header[6:])
            username, password = auth_decoded.decode('utf-8').split(':', 2)

            if (auth(username, password)):
                f(*args)
            else:
                _request_auth(handler)

        return new_f
    return decore


class AuthHandler(web.RequestHandler):
    @basic_auth(auth_api)
    def get(self) -> None:
        self.write('ok')


def log_handler(handler: Any) -> None:
    """Override tornado's logging."""
    # log only errors (status >= 500)
    if handler.get_status() >= 500:
        access_log.error(
            '{} {}'.format(handler.get_status(), handler._request_summary())
        )


def get_application() -> web.Application:
    static_path = os.path.join(os.path.dirname(__file__), 'static')
    handlers = [
        ('/', MainHandler),
        ('/1', LinkHandler1),
        ('/redirect1', RedirectHandler1),
        ('/redirect2', RedirectHandler2),
        ('/auth', AuthHandler),
        ('/empty', EmptyHandler),
        ('/long', LongHandler),
        ('/static', web.StaticFileHandler, dict(path=static_path)),
    ]
    return web.Application(
        handlers,
        log_function=log_handler,
        static_path=static_path,
    )


if __name__ == '__main__':
    app = get_application()
    app.listen(9000)
    asyncio.get_event_loop().run_forever()
