# Practice

Warm-up exercises for the Python basics used in this project, one file per
topic from the [PROJECT.md](../PROJECT.md) appendix. These are independent
of the real project pipeline in [`tasks/`](../tasks/) - no Apaleo credentials
needed, and the database ones use their own scratch table so they won't
touch real data.

Each file has a short example followed by 2-3 exercises marked `TODO`. Work
through them in order:

```bash
make run FILE=practice/01_getting_started.py
make run FILE=practice/02_variables_and_data_types.py
make run FILE=practice/03_lists_and_dictionaries.py
make run FILE=practice/04_conditions_and_loops.py
make run FILE=practice/05_functions.py
make run FILE=practice/06_modules_and_packages.py
make run FILE=practice/07_file_handling.py
make run FILE=practice/08_json.py
make run FILE=practice/09_dates.py
make run FILE=practice/10_error_handling.py
make run FILE=practice/11_string_formatting.py
make run FILE=practice/12_http_requests.py
make run FILE=practice/13_database_work.py
```

[`14_testing.py`](14_testing.py) is the exception - it's not a script to run
top to bottom, it's a set of pytest test functions, so it's run differently:

```bash
make test
```

Once you're comfortable with a topic, move on to the matching step in
[`tasks/`](../tasks/), where you apply it to the real reservation pipeline.
