entry = input().split()

unique_codes = []

for cod in entry:
    if cod not in unique_codes:
        unique_codes.append(cod)

print(" ".join(unique_codes))