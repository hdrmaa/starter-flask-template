
# Flask Starter Template

A simple basic Flask application for anyone to use as base.

## Run Locally

* Before continuing, please make sure you have **Python 3** and **PIP** installed.
* This guide uses **Linux** command. Please adapt the instruction for another OS.

Clone the project

```bash
  git clone https://github.com/hdrmaa/starter-flask-template
```

Go to the project directory

```bash
  cd starter-flask-template
```

**[Optional]** Use `virtualenv`

```bash
  pip3 install virtualenv
  virtualenv venv

  source venv/bin/activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python main.py
  # OR
  # FLASK_DEBUG=1 python main.py -> to enable debugging mode
```
