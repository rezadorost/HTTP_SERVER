import socket

HOST = '127.0.0.1'
PORT = 8000

socket_server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

socket_server.setsockopt(
    socket.SOL_SOCKET,
    socket.SO_REUSEADDR,
    1
)

socket_server.bind((HOST , PORT))
socket_server.listen()

print(f'server runing on http://{HOST}:{PORT}')

routes ={
    "/": "index.html",
    "/about": "about.html",
    "/contact": "contact.html"
}
while True:
    client_socket, client_address = socket_server.accept()

    print(f'client connected : {client_address}')

    request = client_socket.recv(4096)

    request = request.decode()

    headers_part, body = request.split("\r\n\r\n", 1)

    header_lines = headers_part.splitlines()

    print("HEADERS :")

    headers = {}

    for line in header_lines[1:]:
        key, value = line.split(": ", 1)
        headers[key]= value

    for key, value in headers.items():
        print(f"{key}: {value}")

    print('BODY :')
    print(body)

    first_line = header_lines[0]
    method , path , version = first_line.split()

    print('method :', method)
    print('path :', path)
    print('version :', version)

#permission methods
    if method == "GET":
        filename = routes.get(path)
        #handle paths
        if filename:
            status = "200 OK"
        else:
            filename = "404.html"
            status = "404 Not Found"
    else:
        status = "405 Method Not Allowed"
        filename = "405.html"


    
    with open(filename , "r")as file:
        body = file.read()

    response = (
        f"HTTP/1.1 {status}\r\n"
        "Content-Type: text/html\r\n"
        "\r\n"
        +body
    )
    client_socket.sendall(response.encode())

    client_socket.close()
