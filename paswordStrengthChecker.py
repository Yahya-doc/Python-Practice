password = input("Enter a password to check: ")

is_long = len(password) >= 8
has_upper = any(char.isupper() for char in password)
has_number = any(char.isdigit() for char in password)
has_special = any(not char.isalnum() for char in password)

if is_long and has_upper and has_number and has_special:
    print("It is a strong password.")

elif is_long and (has_upper or has_number or has_special):
    
    missing = []
    if not has_upper:
        missing.append("an upper case letter")
    if not has_number:
        missing.append("a number")
    if not has_special:
        missing.append("a special character")
    print(f"Missing: {','.join(missing)}.")  

else:
    print("It is a very weak password.")      