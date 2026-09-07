import unittest
from app import AppHandler


class TestApplication(unittest.TestCase):

    def test_application_handler_exists(self):
        self.assertTrue(callable(AppHandler))


if __name__ == "__main__":
    unittest.main()
