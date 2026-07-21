import re

# Not Found
with open("frontend/src/app/not-found.tsx", 'r') as f:
    content = f.read()
content = content.replace("Sorry, we couldn't find the page", "Sorry, we couldn&apos;t find the page")
with open("frontend/src/app/not-found.tsx", 'w') as f:
    f.write(content)

# Page
with open("frontend/src/app/page.tsx", 'r') as f:
    content = f.read()
content = content.replace("Start Now — It's Free", "Start Now — It&apos;s Free")
with open("frontend/src/app/page.tsx", 'w') as f:
    f.write(content)
