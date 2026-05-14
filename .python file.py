import re

def check_password_strength(password):
    score = 0

    # Length check
    if len(password) >= 8:
        score += 1

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1

    # Lowercase check
    if re.search(r"[a-z]",password):
        score += 1

    # Number check
    if re.search(r"\d", password):
        score += 1

    # Special character check
    if re.search(r"[!@#$^&*()..?\":{}|<>]",password):
        score += 1

    # Strength result
    if score <= 2:
        return "Weak Password ❌"
    elif score == 3 or score == 4:
        return "Medium Password ⚠"
    else:
        return "Strong Password ✅"

passsword = input("Gauu@123")
result = check_password_strength(passsword)

print("Password Strength:", result)
 

