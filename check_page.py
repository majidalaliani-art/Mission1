import urllib.request

try:
    with urllib.request.urlopen('http://127.0.0.1:8000/') as response:
        content = response.read().decode('utf-8')
        print(f"Status Code: {response.getcode()}")
        if response.getcode() == 200:
            print("Page loaded successfully!")
            if "للدخول" in content or "login" in content.lower():
                print("Login page detected!")
except Exception as e:
    print(f"Error: {e}")
