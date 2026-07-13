files_to_fix = [
    ('frontend/src/app/auth/signup/page.tsx', "We've sent a confirmation link", "We&apos;ve sent a confirmation link"),
    ('frontend/src/app/error.tsx', "We encountered an unexpected error. Don't worry, we're working on it!", "We encountered an unexpected error. Don&apos;t worry, we&apos;re working on it!"),
    ('frontend/src/app/not-found.tsx', "Sorry, we couldn't find the page you're looking for.", "Sorry, we couldn&apos;t find the page you&apos;re looking for."),
    ('frontend/src/app/page.tsx', "Start Now — It's Free", "Start Now — It&apos;s Free")
]

for filepath, search, replace in files_to_fix:
    with open(filepath, 'r') as f:
        content = f.read()
    content = content.replace(search, replace)
    with open(filepath, 'w') as f:
        f.write(content)

rules_page = 'frontend/src/app/rules/page.tsx'
with open(rules_page, 'r') as f:
    content = f.read()
content = content.replace('  }, [visaType, category, page]); // eslint-disable-line react-hooks/exhaustive-deps', '  }, [visaType, category, page, fetchRules]); // eslint-disable-line react-hooks/exhaustive-deps')
with open(rules_page, 'w') as f:
    f.write(content)
