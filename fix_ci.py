with open(".github/workflows/ci.yml", "r") as f:
    c = f.read()

c = c.replace("./visasight/frontend", "./frontend")
c = c.replace("./visasight/backend", "./backend")
c = c.replace("node-version: '20.x'", "node-version: '22.x'")

with open(".github/workflows/ci.yml", "w") as f:
    f.write(c)
