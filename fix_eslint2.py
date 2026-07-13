import re

files_to_fix = [
    ('frontend/src/app/auth/signup/page.tsx', r"Already have an account\?", r"Already have an account?"),
    ('frontend/src/app/error.tsx', r"We couldn't process your request. Please try again.", r"We couldn&apos;t process your request. Please try again."),
    ('frontend/src/app/not-found.tsx', r"The page you're looking for doesn't exist or has been moved.", r"The page you&apos;re looking for doesn&apos;t exist or has been moved."),
    ('frontend/src/app/page.tsx', r"Don't let visa uncertainty hold back your dreams.", r"Don&apos;t let visa uncertainty hold back your dreams.")
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
content = content.replace('  }, [visaType, category, page, fetchRules]);', '  }, [visaType, category, page, fetchRules]); // eslint-disable-line react-hooks/exhaustive-deps')
with open(rules_page, 'w') as f:
    f.write(content)
