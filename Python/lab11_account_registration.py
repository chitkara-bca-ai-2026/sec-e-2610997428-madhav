print("Input:")
username = input("  Username: ")
password = input("  Password: ")

print("\n========================================")
print("PASSWORD VALIDATION REPORT")
print("========================================")

print("Username:", username)
print("Password:", "*" * len(password))

length_valid = len(password) >= 8
digit_valid = any(char.isdigit() for char in password)
uppercase_valid = any(char.isupper() for char in password)

print("\n--- Validation Rules ---")

if length_valid:
    print(f"[PASS] Minimum 8 characters ({len(password)} characters)")
else:
    print(f"[FAIL] Minimum 8 characters ({len(password)} characters)")

if digit_valid:
    print("[PASS] At least one digit")
else:
    print("[FAIL] At least one digit")

if uppercase_valid:
    print("[PASS] At least one uppercase letter")
else:
    print("[FAIL] At least one uppercase letter")

print("\n--- Result ---")

if length_valid and digit_valid and uppercase_valid:
    print("Password is VALID!")
    print(f"Account created successfully for {username}!")
else:
    print("Password is INVALID.")

print("========================================")
