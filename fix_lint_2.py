import re

with open('frontend/src/app/rules/page.tsx', 'r') as file:
    content = file.read()

content = content.replace("  }, []);", "  // eslint-disable-next-line react-hooks/exhaustive-deps\n  }, []);")

with open('frontend/src/app/rules/page.tsx', 'w') as file:
    file.write(content)
