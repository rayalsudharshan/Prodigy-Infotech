import string

def assess_password_strength(password):
    score = 0
    if len(password) < 8:
        score += 1
    if len(password) >= 16:
        score += 2
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score == 0:
        feedback = "Very weak. The password is too short and lacks any variation."
    elif score == 1:
        feedback = "Weak. The password is short and lacks variation."
    elif score == 2:
        feedback = "Moderate. The password is of reasonable length but lacks some variation."
    elif score == 3:
        feedback = "Strong. The password is long and has some variation."
    else:
        feedback = "Very strong. The password is very long and has excellent variation."

    print(feedback)

def main():
    password = input("Enter a password to assess its strength: ")
    assess_password_strength(password)

if __name__ == "__main__":
    main()