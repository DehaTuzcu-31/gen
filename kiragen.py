import random

def generate_visa_card():
    # Kart numarası: 16 haneli, 4 ile başlıyor
    card_number = '4' + ''.join(str(random.randint(0, 9)) for _ in range(15))

    # Son kullanma tarihi: Ay (01-12) ve gelecek yıllar (2025-2030 arası)
    exp_month = f"{random.randint(1, 12):02}"
    exp_year = str(random.randint(2025, 2030))

    # CVV: 3 haneli
    cvv = ''.join(str(random.randint(0, 9)) for _ in range(3))

    return f"{card_number}|{exp_month}|{exp_year}|{cvv}"

# Örnek olarak 5 sahte kart üretelim
for _ in range(5):
    print(generate_visa_card())
input()
