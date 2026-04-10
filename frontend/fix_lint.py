import re
import os

files_to_fix = [
    ("src/app/auth/signup/page.tsx", "We've sent a confirmation", "We&apos;ve sent a confirmation"),
    ("src/app/error.tsx", "we couldn't find the exact page", "we couldn&apos;t find the exact page"),
    ("src/app/error.tsx", "that couldn't be found", "that couldn&apos;t be found"),
    ("src/app/error.tsx", "what you're looking for", "what you&apos;re looking for"),
    ("src/app/not-found.tsx", "we can't find the page you're looking for.", "we can&apos;t find the page you&apos;re looking for."),
    ("src/app/page.tsx", "whether you're preparing", "whether you&apos;re preparing"),
    ("src/app/page.tsx", "you'll find", "you&apos;ll find"),
]

for filepath, search, replace in files_to_fix:
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        content = content.replace(search, replace)
        with open(filepath, 'w') as f:
            f.write(content)
    except Exception as e:
        print(f"Failed on {filepath}: {e}")

# Fix rules/page.tsx useEffect dependency
rules_file = "src/app/rules/page.tsx"
with open(rules_file, 'r') as f:
    content = f.read()

if "// eslint-disable-next-line react-hooks/exhaustive-deps" not in content:
    content = content.replace("    }, []);", "    // eslint-disable-next-line react-hooks/exhaustive-deps\n    }, []);")
    with open(rules_file, 'w') as f:
        f.write(content)
