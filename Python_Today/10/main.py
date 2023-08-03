import requests
from bs4 import BeautifulSoup


def test_reqest(url, retry=5):
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"
    }

    try:
        response = requests.get(url=url, headers=headers)
        print(f"[+] {url} {response.status_code}")
    except Exception as ex:
        if retry:
            print(f"[INFO] retry={retry} > {url}")
            return test_reqest(url, retry=(retry - 1))
        else:
            raise
    else:
        return response

def main():
    pass

if __name__ == "__main__":
    main()
