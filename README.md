# First
OPAN 243

You must first follow the [setup instructions](https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/sendgrid.md) to create an account, verify your account, setup a single sender, and obtain an API Key.

## Setup

Create and activate a virtual environment:

```sh
conda create -n my-first-env python=3.10

conda activate my-first-env

Obtain an [API Key from Alphavantage](https://www.alphavantage.co/support/#api-key) or from the prof (`ALPHAVANTAGE_API_KEY`).

Create a ".env" file and paste in the following contents:

```sh

# this is the ".env" file...

ALPHAVANTAGE_API_KEY="_________"
```



python app/my_script.py

python -m app.my_script

## Usage

Run the example script:

```sh
python app/my_script.py


Run unemployment report


```sh
python app/unemployment.py
```

Run the stocks report:
```sh
python -m app.stocks
```

Install Packages:

```sh
pip install -r requirements.txt
```

# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app flask run




## Testing

Run tests:

'''sh
pytest
'''


