text = input().split()

unique_texts = []

for part in text:
    if part not in unique_texts:
        unique_texts.append(part)

total = len(unique_texts)

print(" ".join(unique_texts))
print(total)