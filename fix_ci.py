with open(".github/workflows/ci.yml", "r") as f:
    content = f.read()

content = content.replace("working-directory: ./visasight/frontend", "working-directory: ./frontend")
content = content.replace("cache-dependency-path: ./visasight/frontend/package-lock.json", "cache-dependency-path: ./frontend/package-lock.json")
content = content.replace("working-directory: ./visasight/backend", "working-directory: ./backend")
content = content.replace("node-version: '20.x'", "node-version: '22.x'")

with open(".github/workflows/ci.yml", "w") as f:
    f.write(content)
