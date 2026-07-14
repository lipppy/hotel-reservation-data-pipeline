# Glossary for Hotel Reservation Data Pipeline

Short term-by-term definitions. For longer "why does this project do X"
explanations, see [FAQ.md](FAQ.md) instead.

- **Apaleo**: The hotel property management system this project pulls
  reservation data from. `integrations/apaleo/client.py` is the ready-made
  client used to call it; you don't write the API calls yourself, only use
  the client.
- **backend developer**: someone who builds the server-side part of an app —
  the code that reads/writes data and answers requests. That's what you're
  doing this week: the `/api/reservations` endpoint and the database code
  behind it.
- **cursor**: An object used to send SQL to a database and read back the
  results. In this project, created from a MySQL connection with
  `connection.cursor()`, then used to `execute()` `INSERT`/`UPDATE`/`SELECT`
  statements.
- **CSV**: Comma-Separated Values, a file format used to store tabular data in plain text. Each line represents a row, and each value is separated by a comma. Example: `name,age,city\nJohn,30,New York\nJane,25,Los Angeles`.
- **dictionary**: A collection of key-value pairs, where each key is unique. In Python, dictionaries are defined using curly braces `{}`. Example: `my_dict = {'key1': 'value1', 'key2': 'value2'}`.
- **endpoint**: A specific URL path exposed by a web API. This project's
  single endpoint is `/api/reservations`, served by `api.py`.
- **environment variable**: A configuration value (API keys, database
  credentials, etc.) kept outside the source code, typically in a `.env`
  file, and read at runtime — in this project with the `python-dotenv`
  package — instead of being hard-coded.
- **frontend developer**: someone who builds what the user sees and clicks.
  `index.html` is this project's frontend — it's already built, you don't
  need to touch it.
- **full-stack developer**: someone comfortable working on both frontend and
  backend. Not required for this project, but a natural next step once
  you're comfortable with the backend side.
- **JSON**: JavaScript Object Notation, a lightweight data interchange format that is easy for humans to read and write, and easy for machines to parse and generate. JSON is often used for transmitting data in web applications. Example: `{"name": "John", "age": 30, "city": "New York"}`.
- **list**: A collection of items in a specific order, which can be modified. In Python, lists are defined using square brackets `[]`. Example: `my_list = [1, 2, 3]`.
- **query parameter**: Extra input passed to a web API as part of the URL, after a `?`. This project's endpoint reads `hotelCode`, `from`, and `to` this way, e.g. `/api/reservations?hotelCode=BER&from=2026-07-01&to=2026-07-07`.
- **REST API**: Representational State Transfer Application Programming Interface, a set of rules and conventions for building and interacting with web services. REST APIs use HTTP requests to perform operations such as GET, POST, PUT, and DELETE on resources represented in JSON or XML format.
- **software architect**: the person who decides how a system is structured
  and how its pieces fit together. For this project those decisions were
  already made for you (see [PROJECT.md](PROJECT.md)) — not your job this
  week.
- **upsert**: A database write that inserts a row if it doesn't exist yet, or
  updates it if it does. Used when saving reservations to MySQL so
  re-running the pipeline for the same hotel/date range doesn't create
  duplicate rows.
