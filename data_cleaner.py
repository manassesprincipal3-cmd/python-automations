import json

# Simulação de dados brutos e bagunçados (com duplicatas)
raw_contacts = [
    {"name": "Alice Smith", "email": "ALICE@EXAMPLE.COM"},
    {"name": "Bob Jones", "email": "bob@example.com"},
    {"name": "Alice S.", "email": "alice@example.com"},  # E-mail duplicado
    {"name": "Charlie Brown", "email": "charlie@domain.org"}
]

def clean_and_deduplicate(contacts):
    seen_emails = set()
    cleaned_list = []
    
    for contact in contacts:
        email_clean = contact["email"].strip().lower()
        
        # Garante que não haverá e-mails repetidos na lista final
        if email_clean not in seen_emails:
            seen_emails.add(email_clean)
            cleaned_list.append({
                "name": contact["name"].strip().title(),
                "email": email_clean
            })
            
    return cleaned_list

if __name__ == "__main__":
    cleaned_data = clean_and_deduplicate(raw_contacts)
    print("--- Dados Limpos e Organizados ---")
    print(json.dumps(cleaned_data, indent=4))
