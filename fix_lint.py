import re

files_to_fix = [
    "frontend/src/app/auth/signup/page.tsx",
    "frontend/src/app/error.tsx",
    "frontend/src/app/not-found.tsx"
]

for filepath in files_to_fix:
    try:
        with open(filepath, 'r') as f:
            content = f.read()

        if "We've sent a confirmation link" in content:
            content = content.replace("We've sent a confirmation link", "We&apos;ve sent a confirmation link")

        if "Don&apos;t worry, we're working on it!" in content:
            content = content.replace("Don&apos;t worry, we're working on it!", "Don&apos;t worry, we&apos;re working on it!")

        if "Sorry, we couldn't find the page you're looking for." in content:
            content = content.replace("Sorry, we couldn't find the page you're looking for.", "Sorry, we couldn&apos;t find the page you&apos;re looking for.")

        with open(filepath, 'w') as f:
            f.write(content)

    except Exception as e:
        print(f"Error fixing {filepath}: {e}")

print("Done")
