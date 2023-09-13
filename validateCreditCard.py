import re

def validate_credit_card(card_number):
    pattern = r'^[.,4-6]\d{3}(-?\d{4}){3}$'
    if re.match(pattern, card_number):
        sanitized_card_number = card_number.replace("-", "")
        for i in range(len(sanitized_card_number)-3):
            if sanitized_card_number[i] == sanitized_card_number[i+1] == sanitized_card_number[i+2] == sanitized_card_number[i+3]:
                return False
        return True
    return False

def main():
    n = int(input())
    for _ in range(n):
        card_number = input().strip()
        is_valid = validate_credit_card(card_number)
        print('Valid' if is_valid else 'Invalid')

if __name__ == "__main__":
    main()
