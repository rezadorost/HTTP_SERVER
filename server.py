import socket


HOST = "127.0.0.1"
PORT = 8000


def parse_request_line(line):
    method, path, version = line.split()
    return method, path, version


def parse_headers(lines):
    headers = {}

    for line in lines[1:]:
        key, value = line.split(": ", 1)
        headers[key] = value

    return headers


def main():
    socket_server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    socket_server.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_REUSEADDR,
        1
    )

    socket_server.bind((HOST, PORT))
    socket_server.listen()

    print(f"server running on http://{HOST}:{PORT}")

    routes = {
        "/": "index.html",
        "/about": "about.html",
        "/contact": "contact.html"
    }

    while True:
        client_socket, client_address = socket_server.accept()

        print(f"client connected: {client_address}")

        request = client_socket.recv(4096)
        request = request.decode()

        headers_part, body = request.split("\r\n\r\n", 1)

        header_lines = headers_part.splitlines()

        headers = parse_headers(header_lines)

        print("HEADERS:")
        for key, value in headers.items():
            print(f"{key}: {value}")

        print("BODY:")
        print(body)

        first_line = header_lines[0]

        method, path, version = parse_request_line(first_line)

        print("method:", method)
        print("path:", path)
        print("version:", version)

        if method == "GET":
            filename = routes.get(path)

            if filename:
                status = "200 OK"
            else:
                filename = "404.html"
                status = "404 Not Found"

        else:
            status = "405 Method Not Allowed"
            filename = "405.html"

        with open(filename, "r") as file:
            response_body = file.read()

        response = (
            f"HTTP/1.1 {status}\r\n"
            "Content-Type: text/html\r\n"
            "\r\n"
            + response_body
        )

        client_socket.sendall(response.encode())

        client_socket.close()

if __name__ == "__main__":
    main()