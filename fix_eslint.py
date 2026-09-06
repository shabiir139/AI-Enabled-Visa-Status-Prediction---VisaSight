import re
files = [
    "frontend/src/app/auth/login/page.tsx",
    "frontend/src/app/auth/signup/page.tsx",
    "frontend/src/app/error.tsx",
    "frontend/src/app/page.tsx",
    "frontend/src/app/not-found.tsx"
]
for fpath in files:
    with open(fpath, "r") as f: content = f.read()
    content = content.replace("setError(&apos;');", "setError('');")
    content = content.replace("setError(&apos;Something went wrong&apos;);", "setError('Something went wrong');")
    content = content.replace("console.error(&apos;Login error:&apos;, err);", "console.error('Login error:', err);")
    content = content.replace("console.error(&apos;Signup error:&apos;, err);", "console.error('Signup error:', err);")
    content = content.replace("console.error(&apos;Search error:&apos;, err);", "console.error('Search error:', err);")
    content = content.replace("const [error, setError] = useState(&apos;');", "const [error, setError] = useState('');")
    with open(fpath, "w") as f: f.write(content)
