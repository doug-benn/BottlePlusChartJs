import unittest

from boddle import boddle
from webtest import TestApp

import server


class tests(unittest.TestCase):
    def index(self):
        with boddle(params={"name": "Derek"}):
            assert server.index() == "Hi Derek!"

    def test_index(self):
        app = TestApp(server.app)
        assert app.get("/").status == "200 OK"  # fetch a page successfully

    def test_error(self):
        app = TestApp(server.app)
        assert app.get("/error", expect_errors=True).status == "404 Not Found"

    def test_post_data(self):
        app = TestApp(server.app)
        assert app.post("/", dict(id=1, value="value")).status == "200 OK"  # fetch a page successfully

    # def test_functional_login_logout(self):
    #     app = TestApp(server.app)

    #     app.post("/login", {"user": "foo", "pass": "bar"})  # log in and get a cookie

    #     assert app.get("/admin").status == "200 OK"  # fetch a page successfully

    #     assert app.get("/logout").status_code == 200  # log out
    #     app.reset()  # drop the cookie

    #     # fetch the same page, unsuccessfully
    #     assert app.get("/admin", expect_errors=True).status == "401 Unauthorized"


if __name__ == "__main__":
    unittest.main()
