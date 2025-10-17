import requests

def is_online(url="https://www.google.com"):
    try:
        response = requests.get(url, timeout=3)
        return True if response.status_code == 200 else False
    except requests.RequestException:
        return False

def connection_message(offline_count):
    if offline_count >= 7:
        return "You cannot use internet-based features until your connection is restored. You can still use offline features like tell me a joke or check the date."
    elif offline_count >= 5:
        return "It seems your internet connection is still not available. Some features may not work properly."
    elif offline_count >= 3:
        return "You might need to connect your system to the internet."
    else:
        return ""
    
# Example usage:
# if is_online():
#     print("Internet is available!")
# else:
#     print("No internet connection!")
