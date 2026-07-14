# FAQ for Hotel Reservation Data Pipeline

Answers to specific questions that tend to come up while working through this
project. For short term definitions (e.g. what a `dictionary` or `REST API`
is), see [GLOSSARY.md](GLOSSARY.md) instead.


## What is my role in this project?

Build the `/api/reservations` endpoint end to end, following the
task-by-task plan in [PROJECT.md](PROJECT.md): call the Apaleo API, save and
reload the data as JSON and CSV, load it into MySQL, then query it back out
and return it as JSON.


## What is not my role in this project?

Deciding how the pieces fit together — that part's already decided for you
(see PROJECT.md's "Context" section). You also don't need to write the
Apaleo API client (it's provided) or touch `index.html` (the frontend is
already built). Your job is the backend logic in between.

Curious what "backend developer" and similar job titles actually mean? See
the one-line definitions in [GLOSSARY.md](GLOSSARY.md) — the distinctions
don't matter much for this project, so that's all the detail you need.


## How should I use git while working through this project?

Work in your own feature branch, not `main`, and commit as you finish each
practice file or task file. Once a practice chapter or task is done and
working, push your branch and ask your mentor to review it before moving
on to the next one. See PROJECT.md's "Git workflow" section for the exact
commands.


## Is it okay to ask for help if I get stuck?

Yes — always. Getting stuck, or finding a task overwhelming, is a normal
part of learning this stuff for the first time, not a sign you're doing
something wrong. Ask early rather than guessing for a long time — the goal
of this week is for the practice to be digestible and useful, and hopefully
fun, not stressful.


## What are these `.md` files?

`.md` files are Markdown files, which are plain text files that use a simple syntax to format text. They are commonly used for documentation, README files, and other text-based content. Markdown allows you to create headings, lists, links, code blocks, and other formatting elements in a way that is easy to read and write. In this project, `.md` files are used for documentation purposes, such as providing explanations and instructions for the project.


## What is `.gitignore`?

`.gitignore` is a file used by Git to determine which files and directories to ignore in a project. This is useful for excluding temporary files, build artifacts, and sensitive information from being committed to the repository.


## Why some files are highlighted with grey in the VS Code editor?

In Visual Studio Code, files highlighted in grey typically indicate that they are ignored by Git, as specified in the `.gitignore` file. This means that these files will not be tracked by Git and will not be included in commits. Common examples of ignored files include temporary files, build artifacts, and sensitive configuration files like `.env`. The grey highlighting helps developers quickly identify which files are not part of the version control system, allowing them to focus on the files that are actively being tracked and managed by Git.


## What is `.env` and `.env.example`?

`.env.example` is a template file that contains example environment variables for a project. It serves as a reference for developers to create their own `.env` file with the necessary configuration settings.

`.env` is a file used to store environment variables for a project. It typically contains configuration settings, such as API keys, database credentials, and other sensitive information that should not be hard-coded into the source code. The `.env` file is usually included in `.gitignore` to prevent it from being tracked by Git and shared publicly.


## What is `Makefile` and how to use it?

A `Makefile` is a file that contains a set of directives used by the `make` build automation tool. It defines tasks and dependencies for building, testing, and managing a project. In this project, the `Makefile` provides convenient commands to manage the development environment, run scripts, and perform other tasks.


## Why I can see `__init__.py` files in the project?

`__init__.py` files are used to mark directories as Python packages. They allow Python to recognize the directory as a package and enable the import of modules from that package. In this project, `__init__.py` files are included in directories that contain Python modules, allowing for proper organization and import of code. Without `__init__.py`, Python would not treat the directory as a package, and you would not be able to import modules from it.


## What is `requirements.txt`?

`requirements.txt` is a file used to list the Python dependencies required for a project. It allows developers to specify the packages and their versions needed to run the application. This file can be used with package managers like `pip` to install the required dependencies in a virtual environment or on a server.


## What is a virtual environment?

A virtual environment is an isolated Python environment that allows you to manage dependencies for a specific project without affecting the global Python installation. It enables you to install packages and libraries specific to your project, preventing conflicts with other projects that may require different versions of the same packages. Virtual environments are commonly created using tools like `venv` or `virtualenv`.


## What is this .venv directory?

The `.venv` directory is a common name for the directory that contains the virtual environment for a Python project. It is created when you set up a virtual environment using tools like `venv` or `virtualenv`. The `.venv` directory contains the Python interpreter, libraries, and scripts specific to the virtual environment, allowing you to manage dependencies and run your project in isolation from the global Python installation.


## What is the difference in terms of isolation between a virtual environment and Docker?

A virtual environment provides isolation at the Python package level, allowing you to manage dependencies for a specific project without interfering with other projects. However, it still relies on the underlying operating system and Python installation.

Docker, on the other hand, provides isolation at the operating system level. It allows you to package an application along with its dependencies, libraries, and configuration files into a container that can run consistently across different environments. Docker containers are lightweight and provide a higher level of isolation compared to virtual environments, making them suitable for deploying applications in a consistent and reproducible manner.


## What is the difference between `docker-compose` and `docker`?

`docker` is a command-line tool that allows you to manage individual Docker containers. It provides commands to build, run, stop, and manage containers.

`docker-compose` is a tool that allows you to define and manage multi-container Docker applications. It uses a YAML file (`docker-compose.yml`) to configure the services, networks, and volumes for the application. With `docker-compose`, you can start, stop, and manage all the containers defined in the configuration file with a single command, making it easier to work with complex applications consisting of multiple interconnected services.


## What is the difference between `JSON` and `CSV`?

See [GLOSSARY.md](GLOSSARY.md) for what each format is on its own. The
practical difference for this project: `JSON` supports nested structures
(an object inside an object), while `CSV` is flat, one row per reservation.
That's why task 2 saves the raw Apaleo response as JSON, but task 3 has to
flatten it down to a handful of fields before it can be written as CSV.


## `JSON` and `Python dictionaries` are so similar, are they the same?

While `JSON` and Python dictionaries are similar in structure, they are not the same. `JSON` is a text-based format used for data interchange, whereas Python dictionaries are a data structure used within the Python programming language. You can convert between the two using the `json` module in Python: `json.loads()` to convert a JSON string to a Python dictionary, and `json.dumps()` to convert a Python dictionary to a JSON string.


## What is `isort` and `black`?
`isort` is a Python utility that automatically sorts and organizes import statements in your code according to a specified style. It helps maintain a consistent import order and improves code readability.

`black` is a Python code formatter that enforces a consistent code style by automatically formatting your code. It helps improve code readability and reduces debates over code style in team projects.


## What is this `if __name__ == "__main__":` block?

In Python, the `if __name__ == "__main__":` block is used to check whether a script is being run directly or being imported as a module in another script. Code inside this block will only execute if the script is run directly. This is commonly used to call a `main()` function or execute code that should not run when the script is imported as a module.

Example:
```python
def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()
```


## What is this `localhost` thing especially combined with `:8080` in the URL?

`localhost` refers to your own computer, also known as the loopback address. When you see `localhost` in a URL, it means that the web browser is trying to connect to a web server running on your own machine. The `:8080` part specifies the port number that the server is listening on. In this project, the Nginx web server is configured to serve the dashboard on port 8080, so you would open `http://localhost:8080` in your browser to view it. The API endpoint is served on port 5000, so you would open `http://localhost:5000/api/reservations` to access it directly. The database is served on port 3306, so you would connect to it with a MySQL client using `localhost:3306`.
