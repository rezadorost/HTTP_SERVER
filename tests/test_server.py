from unittest import TestCase

from server import parse_request_line
class TestParseRequestLine(TestCase):

    def test_parse_request_line(self):
        method, path, version = parse_request_line("GET /about HTTP/1.1")

        self.assertEqual(method, "GET")
        self.assertEqual(path, "/about")
        self.assertEqual(version, "HTTP/1.1")

    def test_invalid_request_line(self):
        with self.assertRaises(ValueError):
            parse_request_line("INVALID REQUEST")

from server import parse_headers
class TestParseHeaders(TestCase):
    def test_parse_headers(self):

        lines = [
            'GET /about HTTP/1.1',
            'Host: 127.0.0.1:8000',
            'Connection: keep-alive',
            'Cache-Control: max-age=0'
        ]
        
        headers = parse_headers(lines)

        self.assertIsInstance(headers, dict)
        self.assertEqual(len(headers) , 3)
        self.assertEqual(headers["Host"], "127.0.0.1:8000")
        self.assertEqual(headers["Connection"], "keep-alive")
        self.assertEqual(headers["Cache-Control"], "max-age=0")

    def test_invalid_headers(self):
        with self.assertRaises(ValueError):
            parse_headers([
                "GET /about HTTP/1.1",
                "INVALID REQUEST"
                ])