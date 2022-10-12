#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, re, time, datetime, json, socket, threading, webbrowser


def load_config(filename):
    with open(filename) as f:
        config = json.load(f)
        return config

def open_static(filename, mode='rb'):
    try:
        with open(filename, mode) as f:
            data = f.read()
            ts = os.stat(filename).st_mtime
            last_modified = datetime.datetime \
                .utcfromtimestamp(ts) \
                .strftime('%a, %d %b %Y %H:%M:%S GMT')
            return data, last_modified
    except:
        return b'', 0

def build_header(status, file_type, last_modified):

    last_modified = f'Last-Modified: {last_modified}'.encode()
    return http_status[status].encode() + sep \
        + content_type[file_type].encode() + sep \
        + last_modified + sep + sep

def parse_request(request):
    headers = request.decode().split('\r\n')
    method, request, protocol = headers[0].split(' ')
    if request == '/': request = '/index.html'
    path = re.findall('[/a-z.]+', request)[0]
    try:
        file_type = path.split('.')[1]
    except IndexError:
        file_type = request.split('.')[-1]
    return method, path, file_type
    

def prepare_response(method, path, file_type):

    if routes.get(file_type):
        path = routes[file_type] + path
    else:
        path = '.' + path
    # Open file
    body, last_modified = open_static(path, 'rb')
    # Add different status codes for the retrival
    if body:
        header = build_header('200', file_type, last_modified)
    elif not body:
        header = build_header('404', file_type, last_modified)
    elif IndexError:
        header = build_header('400', file_type, last_modified)
    elif PermissionError:
        header = build_header('403', file_type, last_modified)
    return header + body

def process_request(msg, client):
    method, path, file_type = parse_request(msg)
    response = prepare_response(method, path, file_type)
    client.send(response)
    client.close()
    print(f'({time.ctime()}) - {method} - {path}')

def run():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Host (0.0.0.0 means for any ip address)
        host = '0.0.0.0'
        # Take port from command line
        try:
            port = int(sys.argv[1])
        except:
            port = config['default_port']
            print(f'Missing or Invalid port. Setting to default port {port}')
        # Bind socket to the desired address
        s.bind((host, port))
        # Listen for incoming messages
        s.listen()
        # Shows introduction to the terminal
        webbrowser.open(f'http://localhost:{port}')
        # Server is going to run until something breaks
        while True:
            # Client connected
            client, addr = s.accept()
            # Read clients message (suppose to be HTTP GET request)
            msg = client.recv(8092)
            # if the server got an appropriate request -> create response
            if msg:
                threading.Thread(target=process_request, args=(msg, client)).start()
        s.close() # close the connection after every request


# Load server configuration
config       = load_config('config.json')
http_status  = config['http_status']
content_type = config['content_type']
routes       = config['routes']
sep          = config['sep'].encode()

if __name__ == '__main__':
    run()
