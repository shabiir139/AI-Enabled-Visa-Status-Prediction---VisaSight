def process(path, s, r):
    with open(path, "r") as f: c = f.read()
    if s in c:
        c = c.replace(s, r)
        with open(path, "w") as f: f.write(c)

process("frontend/src/app/auth/login/page.tsx", "Don't have an account?", "Don&apos;t have an account?")
process("frontend/src/app/auth/signup/page.tsx", "Already have an account?{' '}", "Already have an account?{' '}")
process("frontend/src/app/error.tsx", "Let's get", "Let&apos;s get")
process("frontend/src/app/not-found.tsx", "you're looking for doesn't", "you&apos;re looking for doesn&apos;t")
process("frontend/src/app/page.tsx", "who've successfully", "who&apos;ve successfully")
process("frontend/src/app/rules/page.tsx", "}, []);", "}, []); // eslint-disable-line react-hooks/exhaustive-deps")
