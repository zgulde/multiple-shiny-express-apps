# Shiny Express Multi-App Demo

`server.py` is a starlette app that dynamically generates routes and converts to shiny express apps based on the `.py` files present in the `adhoc` folder. Each `.py` file in `adhoc/` is assumed to have code for a shiny express app.

The files in `adhoc/` are a hodge-pogde of demo shiny express apps and components.

## Running

```
uvicorn server:app
```

Dev

```
uvicorn --reload server:app
```

## TODO

- package in venv
- `server.py` - what if we want other apps / routes?