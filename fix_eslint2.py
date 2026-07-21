import re

# Signup
with open("frontend/src/app/auth/signup/page.tsx", 'r') as f:
    content = f.read()
content = content.replace("We've sent a confirmation link to", "We&apos;ve sent a confirmation link to")
with open("frontend/src/app/auth/signup/page.tsx", 'w') as f:
    f.write(content)

# Error
with open("frontend/src/app/error.tsx", 'r') as f:
    content = f.read()
content = content.replace("Don't worry, we're working on it!", "Don&apos;t worry, we&apos;re working on it!")
with open("frontend/src/app/error.tsx", 'w') as f:
    f.write(content)

# Not Found
with open("frontend/src/app/not-found.tsx", 'r') as f:
    content = f.read()
content = content.replace("The page you're looking for doesn't exist", "The page you&apos;re looking for doesn&apos;t exist")
content = content.replace("doesn't", "doesn&apos;t")
content = content.replace("you're", "you&apos;re")
with open("frontend/src/app/not-found.tsx", 'w') as f:
    f.write(content)

# Page
with open("frontend/src/app/page.tsx", 'r') as f:
    content = f.read()
content = content.replace("It's like having", "It&apos;s like having")
with open("frontend/src/app/page.tsx", 'w') as f:
    f.write(content)

# Rules page
with open("frontend/src/app/rules/page.tsx", 'r') as f:
    content = f.read()
content = content.replace("  }, [visaType, category, page]); // eslint-disable-line react-hooks/exhaustive-deps", "")
content = content.replace("  }, [visaType, category, page]);", "  }, [visaType, category, page]); // eslint-disable-line react-hooks/exhaustive-deps")
with open("frontend/src/app/rules/page.tsx", 'w') as f:
    f.write(content)
