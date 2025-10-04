# main.py - Ethical Hacker AI Agent Tool
# This is the main entry point for our subdomain enumeration and vulnerability scanning tool.

import requests
import json
import argparse
import warnings
from urllib3.exceptions import InsecureRequestWarning

# Suppress only the single InsecureRequestWarning from urllib3
warnings.simplefilter('ignore', InsecureRequestWarning)

def find_subdomains(domain):
    """
    Finds subdomains for a given domain using the crt.sh certificate transparency log.
    Returns a list of subdomains, or None if an error occurs.
    """
    subdomains = set()
    url = f"https://crt.sh/?q=%.{domain}&output=json"

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        if not response.text.strip():
            return []

        certificates = json.loads(response.text)

        for cert in certificates:
            names = cert.get('name_value', '').split('\n')
            for name in names:
                if name.endswith(f".{domain}") and '*' not in name:
                    subdomains.add(name.lower())

    except requests.RequestException as e:
        print(f"Hiba a crt.sh API hívása közben: {e}")
        return None
    except json.JSONDecodeError:
        print("Hiba a JSON válasz feldolgozása közben a crt.sh-tól.")
        return None

    return sorted(list(subdomains))

def check_security_headers(url):
    """
    Checks for the presence of important security headers for a given URL.
    Returns a list of missing headers.
    """
    missing_headers = []
    required_headers = [
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options"
    ]

    try:
        response = requests.get(f"https://{url}", timeout=10, verify=False)
        headers = response.headers

        for header in required_headers:
            if header not in headers:
                missing_headers.append(header)

    except requests.RequestException:
        return "Nem sikerült csatlakozni"

    return missing_headers

def main():
    """
    Main function to parse arguments and run the scanner.
    """
    parser = argparse.ArgumentParser(description="Al-domain kereső és biztonsági fejléc ellenőrző eszköz.")
    parser.add_argument("domain", help="A cél domain, amit vizsgálni kell (pl. example.com).")
    args = parser.parse_args()

    target_domain = args.domain

    print(f"Al-domainek keresése a(z) '{target_domain}' domainhez...")

    found_subdomains = find_subdomains(target_domain)

    if found_subdomains is None:
        print("A lekérdezés hiba miatt nem sikerült.")
    elif not found_subdomains:
        print("Nem található al-domain.")
    else:
        print(f"Talált al-domainek ({len(found_subdomains)} db). Biztonsági fejlécek ellenőrzése...")
        for sub in found_subdomains:
            print(f"\n--- Ellenőrzés: {sub} ---")
            missing = check_security_headers(sub)
            if isinstance(missing, str):
                print(f"Hiba: {missing}")
            elif not missing:
                print("Minden fontos biztonsági fejléc megtalálható. ✅")
            else:
                print("Hiányzó biztonsági fejlécek: ❌")
                for header in missing:
                    print(f"- {header}")

if __name__ == "__main__":
    main()