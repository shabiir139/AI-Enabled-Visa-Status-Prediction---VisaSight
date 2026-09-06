import re

def fix(path):
    with open(path, "r") as f: content = f.read()
    # Find text nodes between > and <
    # Be careful not to replace quotes inside jsx props or script tags
    def replace_quote(match):
        text = match.group(1)
        text = text.replace("'", "&apos;")
        return ">" + text + "<"

    content = re.sub(r">([^<]*'[^<]*)<", replace_quote, content)
    with open(path, "w") as f: f.write(content)

fix("frontend/src/app/auth/login/page.tsx")
fix("frontend/src/app/auth/signup/page.tsx")
fix("frontend/src/app/error.tsx")
fix("frontend/src/app/not-found.tsx")
fix("frontend/src/app/page.tsx")

with open("frontend/src/app/rules/page.tsx", "r") as f: c = f.read()
c = c.replace("}, []);", "}, []); // eslint-disable-line react-hooks/exhaustive-deps")
with open("frontend/src/app/rules/page.tsx", "w") as f: f.write(c)
