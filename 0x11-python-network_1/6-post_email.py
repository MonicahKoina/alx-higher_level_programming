#!/usr/bin/python3
"""
Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response
"""
import sys
import requests


def main():
    url = sys.argv[1]
    payload = {"email": sys.argv[2]}
    res = requests.post(url, data=payload)
    print(res.text)


if __name__ == "__main__":
    main()
