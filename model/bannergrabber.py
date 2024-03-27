import requests

def grab_banner(server_url):
    try:
        response = requests.get(server_url)
        server_header = response.headers.get('Server')
        return server_header
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return 'Error'
