import re

def check_password(password):
    """
    Checks the strength of a password based on various criteria and provides feedback.

    Args:
        password (str): The password to be checked.

    Returns:
        str: A message indicating the password's strength and suggestions for improvement.
    """

    min_length = 8
    min_uppercase = 1
    min_lowercase = 1
    min_digit = 1
    min_special = 1
    
    uppercase_count = sum(1 for char in password if char.isupper())
    lowercase_count = sum(1 for char in password if char.islower())
    digit_count = sum(1 for char in password if char.isdigit())
    special_count = len(re.findall(r'[!@#$%^&*()\-+=/?{|}<>,.;:`~"]', password))

    
    if len(password) < min_length:
        return f"Password is too short. Minimum length is {min_length} characters."
    elif uppercase_count < min_uppercase:
        return f"Password needs at least {min_uppercase} uppercase letter(s)."
    elif lowercase_count < min_lowercase:
        return f"Password needs at least {min_lowercase} lowercase letter(s)."
    elif digit_count < min_digit:
        return f"Password needs at least {min_digit} digit(s)."
    elif special_count < min_special:
        return f"Password needs at least {min_special} special character(s)."

    
    strength = "Weak"
    if uppercase_count + lowercase_count >= 2:
        strength = "Medium"
    if digit_count > 0:
        strength = "Strong"
    if special_count > 0:
        strength = "Very Strong"

    return f"Password strength: {strength}. Consider using a longer password and a mix of uppercase, lowercase, digits, and special characters for higher security."

while True:
    password = input("Enter your password (or 'q' to quit): ")
    if password.lower() == 'q':
        break
    feedback = check_password(password)
    print(feedback)