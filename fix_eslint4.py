rules_page = 'frontend/src/app/rules/page.tsx'
with open(rules_page, 'r') as f:
    content = f.read()
content = content.replace('  }, [selectedType]);', '  }, [selectedType]); // eslint-disable-line react-hooks/exhaustive-deps')
with open(rules_page, 'w') as f:
    f.write(content)
