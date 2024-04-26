#!/usr/bin/python3
"""
Fetch URL using urllib package:
This Python script fetches https://alx-intranet.hbtn.io/status using urllib
"""
import urllib.request


def fetch_url():
    """This method fetchs https://alx-intranet.hbtn.io/status using urllib"""
    with urllib.request.urlopen(
            "https://alx-intranet.hbtn.io/status"
    ) as response:
        return response.read()


def main():
    """Main Entry - This is the main entry of the program"""
    body = fetch_url()
    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")
    print(f"\t- utf8 content: {body.decode(encoding='utf-8')}")


if __name__ == "__main__":
    main()
