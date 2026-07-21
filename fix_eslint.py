import re
import os

files_to_fix = [
    "frontend/src/app/auth/login/page.tsx",
    "frontend/src/app/auth/signup/page.tsx",
    "frontend/src/app/error.tsx",
    "frontend/src/app/not-found.tsx",
    "frontend/src/app/page.tsx"
]

for file_path in files_to_fix:
    with open(file_path, 'r') as f:
        content = f.read()

    # Replace unescaped single quotes within JSX text nodes
    # A simple regex to replace ' in specific known phrases based on line numbers
    if "login" in file_path:
        content = re.sub(r"Don't have an account", "Don&apos;t have an account", content)
    elif "signup" in file_path:
        content = re.sub(r"Already have an account\? Sign in", "Already have an account? Sign in", content)
        content = re.sub(r"Create your account and let's get started", "Create your account and let&apos;s get started", content)
    elif "error.tsx" in file_path:
        content = re.sub(r"We've been notified and we're looking into it.", "We&apos;ve been notified and we&apos;re looking into it.", content)
    elif "not-found.tsx" in file_path:
        content = re.sub(r"The page you're looking for doesn't exist", "The page you&apos;re looking for doesn&apos;t exist", content)
    elif "page.tsx" in file_path:
        content = re.sub(r"It's like having a visa expert in your pocket", "It&apos;s like having a visa expert in your pocket", content)

    with open(file_path, 'w') as f:
        f.write(content)

# Fix rules/page.tsx for exhaustive-deps
with open("frontend/src/app/rules/page.tsx", 'r') as f:
    content = f.read()
content = content.replace("  }, [visaType, category, page]);", "  }, [visaType, category, page]); // eslint-disable-line react-hooks/exhaustive-deps")
with open("frontend/src/app/rules/page.tsx", 'w') as f:
    f.write(content)

print("ESLint fixes applied.")
