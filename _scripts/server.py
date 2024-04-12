#!/usr/bin/env python3

import argparse
import json
from pathlib import Path
from http.server import BaseHTTPRequestHandler, HTTPServer


parser = argparse.ArgumentParser(description='Serve all block-based programs for conversion by Blockly.')
parser.add_argument('--all', action='store_true',
                    help='Redo all programs when given, else only missing programs.')

# Parse the arguments
args = parser.parse_args()
redo_all = args.all

programs = {}

# Get the directory of the current script
script_dir = Path(__file__).parent.resolve()
programs_dir = (script_dir / '../_includes/programs').resolve()

# Iterate over all .py files in the directory
for file_path in programs_dir.glob('*.py'):
    if redo_all or not file_path.with_suffix('.png').exists():
        print(f'Including: {file_path}')
        with open(file_path, 'r') as f:
            json_blob = f.read().splitlines()[0][len('# pybricks blocks file:'):]
            programs[file_path.stem] = json.loads(json_blob)

class CORSHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/manifest.txt':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(programs).encode())
        else:
            self.send_response(404)

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        BaseHTTPRequestHandler.end_headers(self)

httpd = HTTPServer(('localhost', 4001), CORSHTTPRequestHandler)
httpd.serve_forever()
