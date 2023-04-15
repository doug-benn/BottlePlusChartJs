import unittest

from boddle import boddle
from webtest import TestApp

import server


class tests(unittest.TestCase):
    def test_index(self):
        app = TestApp(server.app)
        assert app.get("/").status == "200 OK"  # fetch a page successfully

    def test_error(self):
        app = TestApp(server.app)
        assert app.get("/error", expect_errors=True).status == "404 Not Found"

    def test_data_set(self):
        app = TestApp(server.app)

        data = [
            {"Language": "Python", "Folder": "Here", "FileType": ".py", "count": 20},
            {"Language": "C++", "Folder": "There", "FileType": ".cp", "count": 20},
            {"Language": "Java", "Folder": "Here", "FileType": ".py", "count": 20},
        ]

        assert app.post_json("/demo", data).status == "200 OK"  # fetch a page successfully

    def test_data_update(self):
        app = TestApp(server.app)

        data = ({"Language": "Java", "Folder": "Here", "FileType": ".py", "endDateTime": "2023-04-15T10:45:00"},)

        assert app.post_json("/", data).status == "200 OK"  # fetch a page successfully


if __name__ == "__main__":
    unittest.main()
