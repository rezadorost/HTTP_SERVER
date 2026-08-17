# Python HTTP Server

A simple HTTP server built from scratch using Python's built-in `socket` module.

The goal of this project is to understand how HTTP servers work internally before moving to frameworks such as Django and FastAPI.

This project is intentionally built without external web frameworks.

---

## 🚀 Current Features

- TCP socket server using Python `socket`
- HTTP request receiving
- HTTP request parsing
- HTTP method parsing
- HTTP path parsing
- HTTP version parsing
- Basic routing
- File-based HTML pages
- `GET` method handling
- `404 Not Found` handling
- `405 Method Not Allowed` handling
- `SO_REUSEADDR` for easier server restarts

### Current Routes

| Method | Route | Response |
|---|---|---|
| GET | `/` | Home page |
| GET | `/about` | About page |
| GET | `/contact` | Contact page |
| GET | Unknown route | 404 page |
| Other methods | Existing route | 405 page |

---

## 📁 Project Structure

```text
http_server/
│
├── server.py
├── index.html
├── about.html
├── contact.html
├── 404.html
├── 405.html
└── README.md
```

---

## ⚙️ How It Works

The server follows a simplified HTTP request/response cycle:

```text
Client
   │
   │ HTTP Request
   ▼
Python Socket Server
   │
   ├── Receive request
   ├── Parse method, path and version
   ├── Check HTTP method
   ├── Find route
   ├── Read HTML file
   └── Build HTTP response
   │
   ▼
Client
```

For example:

```text
GET /about HTTP/1.1
```

is parsed into:

```text
Method  → GET
Path    → /about
Version → HTTP/1.1
```

The router then maps:

```text
/about → about.html
```

and the server reads the HTML file and sends it back to the client.

---

## 🧪 Testing

Start the server:

```bash
python3 server.py
```

The server runs on:

```text
http://127.0.0.1:8000
```

### Test GET

```bash
curl -i http://127.0.0.1:8000/about
```

Expected response:

```text
HTTP/1.1 200 OK
```

### Test 404

```bash
curl -i http://127.0.0.1:8000/hello
```

Expected response:

```text
HTTP/1.1 404 Not Found
```

### Test 405

```bash
curl -i -X POST http://127.0.0.1:8000/about
```

Expected response:

```text
HTTP/1.1 405 Method Not Allowed
```

---

## 🗺️ Roadmap

This project will be continuously improved as I learn more about backend development and HTTP.

### HTTP Fundamentals

- [x] TCP socket server
- [x] Accept client connections
- [x] Receive HTTP requests
- [x] Parse HTTP request line
- [x] Parse HTTP method
- [x] Parse HTTP path
- [x] Parse HTTP version
- [x] Build HTTP responses
- [x] HTTP status codes
- [x] Basic routing
- [x] File-based HTML responses
- [x] 404 handling
- [x] 405 handling
- [x] HTTP headers
- [ ] Request body
- [ ] Content-Length
- [ ] Query parameters
- [ ] Multiple HTTP methods
- [ ] POST requests
- [ ] PUT requests
- [ ] PATCH requests
- [ ] DELETE requests

### Server Improvements

- [ ] Better error handling
- [ ] Static file serving
- [ ] MIME type detection
- [ ] Improved router
- [ ] Separate HTTP request parser
- [ ] Separate HTTP response builder
- [ ] Separate router module
- [ ] Better project structure
- [ ] Configuration management
- [ ] Logging

### Testing

- [x] Unit tests
- [x] HTTP request tests
- [x] Router tests
- [x] Error response tests
- [x] Integration tests

### Advanced Topics

- [ ] Query string parsing
- [ ] Cookies
- [ ] Sessions
- [ ] JSON responses
- [ ] JSON request bodies
- [ ] REST API
- [ ] Concurrent connections
- [ ] Threading
- [ ] HTTPS concepts
- [ ] Performance improvements

---

## 🎯 Project Goal

The main purpose of this project is **learning**, not creating a production-ready web server.

I am building the server from the ground up to understand what happens underneath Python web frameworks.

The long-term goal is to understand concepts such as:

```text
TCP
 ↓
HTTP
 ↓
Request
 ↓
Router
 ↓
Handler
 ↓
Response
 ↓
Client
```

before implementing the same concepts using professional backend frameworks.

---

## 📚 Learning Path

This project is part of my Python Backend learning journey.

The planned progression is:

```text
Python
   ↓
OOP
   ↓
Git & GitHub
   ↓
Sockets
   ↓
HTTP
   ↓
This HTTP Server
   ↓
REST API
   ↓
FastAPI / Django
   ↓
Databases
   ↓
Production Backend Development
```

---

## ⚠️ Disclaimer

This server is an educational implementation of HTTP.

It is **not intended for production use** and does not implement the complete HTTP specification.

The project is intentionally developed incrementally to understand backend and HTTP fundamentals.

---

## 📌 Development Philosophy

New features are added incrementally.

Each major feature should:

1. Be implemented and tested.
2. Be committed to Git.
3. Be documented in this README.
4. Be added to the roadmap when appropriate.

The README will be updated as the project evolves.
