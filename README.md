# Tracking my mood without sharing my private information.
I built this streamlit app with form input for tracking daily mood changes and showing analytics over time. I wanted to:

1. Create an app that was locally hosted without much effort and accessible from my phone
2. Using DuckDB for fast, local, structured data storage
3. Using streamlit for interactive visualization and form input

## Setup
- Install python 3.13
- Clone this repository
- Initialize `venv`

```shell
python -m venv .venv
```

- Install packages from `requirements.txt`

```shell
pip install -r requirements.txt
```

- Run `app.py`

```shell
streamlit run app.py
```
