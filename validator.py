import os
import requests
from dotenv import load_dotenv

#Load API key from .env
load_dotenv()
API_KEY = os.getenv("ABSTRACT_API_KEY")
print(f"Loaded API key {API_KEY}")

def validate_email(email:str):
    """Validate an email using AbstractAPI"""
    url = "https://emailreputation.abstractapi.com/v1/"
    params = {"api_key": API_KEY, "email": email}
    response = requests.get(url, params=params)

    if response.status_code != 200:
        print(f"API Error: {response.status_code}")
        print(f"Response: {response.text}")
        return

    data = response.json()
    #print("\nFull API Response:\n", data)

    #--- Extract key sections ---
    deliverability = data.get("email_deliverability", {})
    quality = data.get("email_quality", {})
    sender = data.get("email_sender", {})
    domain = data.get("email_domain", {})
    risk = data.get("email_risk", {})
    breaches = data.get("email_breaches", {})

    print("\n---Email Reputation Results---")
    print(f"Email Address: {data.get('email_address', 'N/A')}")
    print(f"Deliverability Status: {deliverability.get('status', 'N/A')}")
    print(f"Format Valid: {deliverability.get('is_format_valid', 'N/A')}")
    print(f"SMTP Valid: {deliverability.get('is_smtp_valid', 'N/A')}")
    print(f"MX Valid: {deliverability.get('is_mx_valid', 'N/A')}")
    print(f"MX Records: {', '.join(deliverability.get('mx_records', []))}")

    print(f"\nQuality Score: {quality.get('score', 'N/A')}")
    print(f"Free Email: {quality.get('is_free_email', 'N/A')}")
    print(f"Disposable: {quality.get('is_disposable', 'N/A')}")
    print(f"Role-based Email: {quality.get('is_role', 'N/A')}")
    print(f"Catch-all Domain: {quality.get('is_catchall', 'N/A')}")

    print(f"\nProvider: {sender.get('email_provider_name', 'N/A')}")
    print(f"Organization: {sender.get('organization_name', 'N/A')}")

    print(f"\nDomain: {domain.get('domain', 'N/A')}")
    print(f"Domain Age (Days): {domain.get('domain_age', 'N/A')}")
    print(f"Registrar: {domain.get('registrar', 'N/A')}")
    print(f"Risky TLD: {domain.get('is_risky_tld', 'N/A')}")

    print(f"\nRisk Status (Address): {risk.get('address_risk_status', 'N/A')}")
    print(f"Risk Status (Domain): {risk.get('domain_risk_status', 'N/A')}")

    print(f"\nTotal Breaches: {breaches.get('total_breaches', 0)}")

if __name__=="__main__":
    email = input("Enter the email to validate: ").strip()
    validate_email(email)
