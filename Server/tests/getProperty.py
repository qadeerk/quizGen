import json

# Load the API key from property.json
def load_api_key():
    with open('./property.json') as f:
        config = json.load(f)
    return config.get('key')
