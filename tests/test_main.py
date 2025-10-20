# tests/test_main.py

import pytest
import requests
from src.main import check_security_headers

def test_check_security_headers_http_fallback(requests_mock):
    """
    Teszteset arra, hogy a check_security_headers sikeresen visszavált http-re,
    ha a https kapcsolat nem sikerül.
    """
    domain = "test.example.com"
    https_url = f"https://{domain}"
    http_url = f"http://{domain}"

    # A https kérés hibát dob
    requests_mock.get(https_url, exc=requests.exceptions.RequestException)

    # A http kérés sikeres, de hiányoznak a fejlécek
    requests_mock.get(http_url, headers={"X-Frame-Options": "SAMEORIGIN"})

    # Az elvárt eredmény a hiányzó fejlécek listája
    expected_missing = [
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "X-Content-Type-Options"
    ]

    # Futtatjuk a függvényt
    missing_headers = check_security_headers(domain)

    # Ellenőrizzük, hogy az eredmény megegyezik-e az elvárttal
    assert sorted(missing_headers) == sorted(expected_missing)

def test_check_security_headers_connection_error(requests_mock):
    """
    Teszteset arra, hogy a check_security_headers mind https, mind http
    kapcsolódási hiba esetén a megfelelő hibaüzenetet adja vissza.
    """
    domain = "test.example.com"
    https_url = f"https://{domain}"
    http_url = f"http://{domain}"

    # Mindkét kérés hibát dob
    requests_mock.get(https_url, exc=requests.exceptions.RequestException)
    requests_mock.get(http_url, exc=requests.exceptions.RequestException)

    # Futtatjuk a függvényt
    result = check_security_headers(domain)

    # Ellenőrizzük, hogy a hibaüzenet megfelelő-e
    assert result == "Nem sikerült csatlakozni"

def test_check_security_headers_all_present_https(requests_mock):
    """
    Teszteset arra, hogy a check_security_headers helyesen ismeri fel,
    ha minden biztonsági fejléc megvan (https).
    """
    domain = "test.example.com"
    url = f"https://{domain}"

    headers = {
        "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
        "Content-Security-Policy": "default-src 'self'",
        "X-Frame-Options": "DENY",
        "X-Content-Type-Options": "nosniff"
    }

    requests_mock.get(url, headers=headers)

    # Futtatjuk a függvényt
    missing_headers = check_security_headers(domain)

    # Ellenőrizzük, hogy az eredmény üres lista
    assert missing_headers == []
