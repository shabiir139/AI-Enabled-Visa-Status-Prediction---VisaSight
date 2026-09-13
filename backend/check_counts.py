from app.api.cases import list_visa_cases
from app.api.rules import list_visa_rules

print("Cases lines:")
with open("backend/app/api/cases.py") as f:
    lines = f.readlines()
    for i, l in enumerate(lines[120:150]):
        print(f"{120+i}: {l.rstrip()}")
print("\nRules lines:")
with open("backend/app/api/rules.py") as f:
    lines = f.readlines()
    for i, l in enumerate(lines[50:80]):
        print(f"{50+i}: {l.rstrip()}")
