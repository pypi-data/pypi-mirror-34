# Flask-Perf

[![PyPI version](https://badge.fury.io/py/Flask-Perf.svg)](https://badge.fury.io/py/Flask-Perf)
[![Build Status](https://travis-ci.org/abetlen/Flask-Perf.svg?branch=master)](https://travis-ci.org/abetlen/Flask-Perf)

A Flask extension for code and database query profiling.

This profiler is an implementation of the methods described in this post [post](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xvi-debugging-testing-and-profiling) however the extension allows you to also control profiling through the application config.

## Installation

```bash
$ pip install flask_perf
```

## Example

```python
from flask import Flask, jsonify
from flask_perf import Profiler

app = Flask(__name__)
app.config["PROFILER_ENABLED"] = True
profiler = Profiler(app) # or profiler.init_app(app)

@app.route("/")
def index():
    return jsonfiy({
        "message": "Hello World!"
    })
```

## Configuration

| Config Name | Description | `default` |
| :---------- |:------------| -------:|
| `PROFILER_ENABLED` | Enable the profiler. | `False`  |
| `PROFILER_RESTRICTIONS` | List of profiler restrictions, described in depth in the [Official Python  Docs](https://docs.python.org/dev/library/profile.html#pstats.Stats.print_stats) | `[]`   |
| `PROFILER_SQLALCHEMY_ENABLED` | Enable SQLAlchemy query logging. **Note**: This option requires that the `flask_sqlalchemy` package is installed and the `SQLALCHEMY_RECORD_QUERIES` config option is set to `True`. | `False` |
| `PROFILER_SQLALCHEMY_THRESHOLD` | Minimum query duration in seconds to log.  | `0` |
| `PROFILER_SQLALCHEMY_FORMAT` | Logged SQLAlchemy query format.  | `"statement: {query}\nparameters: {parameters}\nduration: {duration}s\ncontext: {context}\n"` |
