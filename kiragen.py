import random

def generate_visa_credit_card(num_cards, pause_each=False):
    cards = []
    for i in range(1, num_cards + 1):
        card_number = "4" + "".join([str(random.randint(0, 9)) for _ in range(15)])
        expiration_year = random.randint(2025, 2031)
        expiration_month = str(random.randint(1, 12)).zfill(2)
        expiration_date = f"{expiration_month}/{expiration_year}"
        cvv = str(random.randint(100, 999))
        card = f"[ID{i}]|{card_number}|{expiration_date}|{cvv}"
        cards.append(card)
        print(card)
        if pause_each:
            input("Devam etmek için Enter'a basın...")
            print()
    return cards

# Kullanıcıdan kart sayısını alın
num_cards = int(input("Kaç tane Visa kredi kartı oluşturmak istiyorsunuz? "))

# Kartları oluşturun
cards = generate_visa_credit_card(num_cards, pause_each=False)

# Kartları yazdırın
print("\n--- Oluşturulan Kartlar ---")
for card in cards:
    print(card)

input("\nÇıkmak için Enter'a basın.")
