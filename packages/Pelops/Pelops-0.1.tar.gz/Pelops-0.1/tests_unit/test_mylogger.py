import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import logging
import pelops.mylogger


class TestMyLogger(unittest.TestCase):
    def test_0getloglevel(self):
        input_values = [
            (logging.CRITICAL, "critical"),
            (logging.CRITICAL, "CRITICAL"),
            (logging.CRITICAL, "Critical"),
            (logging.ERROR, "error"),
            (logging.ERROR, "ERROR"),
            (logging.ERROR, "Error"),
            (logging.WARNING, "warning"),
            (logging.WARNING, "WARNING"),
            (logging.WARNING, "Warning"),
            (logging.INFO, "info"),
            (logging.INFO, "INFO"),
            (logging.INFO, "Info"),
            (logging.DEBUG, "debug"),
            (logging.DEBUG, "DEBUG"),
            (logging.DEBUG, "Debug"),
        ]
        for level, name in input_values:
            self.assertEqual(pelops.mylogger._get_log_level(name), level)

        with self.assertRaises(ValueError):
            pelops.mylogger._get_log_level("fefsvbk")

    def test_1create_logger(self):
        config = {
            "log-level": "INFO",
            "log-file": "test.log"
        }
        l = pelops.mylogger.create_logger(config, "test")
        self.assertIsNotNone(l)
        self.assertEqual(l.getEffectiveLevel(), logging.INFO)
        self.assertEqual(1, len(l.handlers))
        for handler in l.handlers:
            self.assertEqual(type(handler), logging.FileHandler)

    def test_2get_child(self):
        config = {
            "log-level": "INFO",
            "log-file": "test.log"
        }
        config_child = {
            "log-level": "DEBUG"
        }
        l = pelops.mylogger.create_logger(config, "test")
        self.assertIsNotNone(l)
        c = pelops.mylogger.get_child(l, "child", config_child)
        self.assertIsNotNone(c)
        self.assertEqual(l.getEffectiveLevel(), logging.INFO)
        self.assertEqual(c.getEffectiveLevel(), logging.DEBUG)


if __name__ == '__main__':
    unittest.main()

