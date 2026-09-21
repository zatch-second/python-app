import requests

def fetch_data():
    # Fetches a dummy JSON object from a public API
    response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
    return response.json()['id']

if __name__ == '__main__':
    print(f"Fetched ID: {fetch_data()}")