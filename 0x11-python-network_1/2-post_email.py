#!/usr/bin/python3
"""Sending a post request using urllib package"""
import urllib.parse
import urllib.request
import sys


def send_email(url, email):
    """This method sends email as a post request to input url"""
    values = {"email": email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        return response.read()


def main():
    """Main Entry - This is the main entry of the program"""
    if (len(sys.argv) == 3):
        url = sys.argv[1]
        email = sys.argv[2]
        body = send_email(url, email)
        print(body.decode('utf-8'))


if __name__ == "__main__":
    main()
