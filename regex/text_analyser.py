import re

def analyse_text(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+[A-Z\.|a-z]{2,}\b'
    phone_pattern = r'\+\d{1,3} \d{3} \d{3} \d{4}' # 123-456-0000

    emails = re.findall(email_pattern, text)
    phones = re.findall(phone_pattern, text)

    return {
        'emails': emails,
        'phones': phones
    }

if __name__ == '__main__':
    sample_text = """
    Hello, my email is sanjib@example.com and my phone number is +1 123 456 0000.
    """
    result = analyse_text(sample_text)
    print("Text analysis results:")
    print("-" * 20)
    print(f"Emails: {result['emails']}")
    if result['emails']:
        for email in result['emails']:
            print(f"Email: {email}")
    else:
        print("No emails found.")
    
    print("\nPhone numbers found")

    if result['phones']:
        for phone in result['phones']:
            print(f"Phone: {phone}")
    else:
        print("No phone numbers found.")
