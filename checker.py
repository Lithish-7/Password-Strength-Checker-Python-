import re

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Too short (min 8 characters)")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("No uppercase letters")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("No lowercase letters")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("No numbers")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("No special characters")

    return score, feedback

# Run it
password = input("Enter your password: ")
score, feedback = check_password_strength(password)

print(f"\nPassword Strength Score: {score}/5")
if score == 5:
    print("✅ Strong password!")
else:
    print("⚠️ Weak areas:")
    for issue in feedback:
        print(f"- {issue}")
