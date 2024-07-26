import re

def password_strength_checker(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'[0-9]', password) is not None
    special_criteria = re.search(r'[@$!%*?&]', password) is not None
    uniqueness_criteria = len(set(password)) / len(password) > 0.7 if len(password) > 0 else False
    
    strength = 0
    feedback = []

    if length_criteria:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    if uppercase_criteria:
        strength += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")
    
    if lowercase_criteria:
        strength += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")
    
    if digit_criteria:
        strength += 1
    else:
        feedback.append("Password should include at least one digit.")
    
    if special_criteria:
        strength += 1
    else:
        feedback.append("Password should include at least one special character (@$!%*?&).")
    
    if uniqueness_criteria:
        strength += 1
    else:
        feedback.append("Password should have a higher ratio of unique characters.")

    if strength == 6:
        feedback.append("Your password is strong.")
    elif strength >= 4:
        feedback.append("Your password is good, but can be improved.")
    else:
        feedback.append("Your password is weak.")

    return strength, feedback

# Example usage
password = "Passw0rd!"
strength, feedback = password_strength_checker(password)
print(f"Password Strength: {strength}/6")
for line in feedback:
    print(line)
