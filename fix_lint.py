import re

files = [
    'frontend/src/app/auth/signup/page.tsx',
    'frontend/src/app/error.tsx',
    'frontend/src/app/not-found.tsx'
]

for f in files:
    with open(f, 'r') as file:
        content = file.read()
    content = re.sub(r"(?<!=)'(?!s\b|re\b|t\b|m\b|ve\b|ll\b|d\b)", "&apos;", content) # Too complex, let's just do targeted replacements based on line nums
