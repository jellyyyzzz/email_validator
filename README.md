# email_validator
# email reputation validator

# Project Overview

**Email Reputation Validator** is a Python tool that validates and analyzes the **reputation, deliverability, and security risk** of an email address using the ['AbstractAPI Email Reputation API'] (https://www.abstractapi.com/email-reputaion-api).

It checks for issues like invalid format, disposable domains, risky TLDs, and potential breaches - making it ideal for **cybersecurity, email filtering, or signup verification systems**.

---

## Features
- Validate Email format and SMTP configuration
- Detect **disposable**, **role-based**, and **catch-all** email addresses
- Retrieve domain and registrar information
- Assess domain age and TLD risk
- Check for data breaches related to the email
- Display overall reputation and risk assessment

---

## Installation
Install the dependencies using
'''bash
pip install requests python-dotenv

## Setup/API Instructions
- Visit https://app.abstractapi.com/api/email-reputation/tester
- Sign up/Log in to get your API key.
