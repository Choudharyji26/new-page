#!/usr/bin/env python3
import os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from http.server import HTTPServer, SimpleHTTPRequestHandler
port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
HTTPServer(("127.0.0.1", port), SimpleHTTPRequestHandler).serve_forever()
