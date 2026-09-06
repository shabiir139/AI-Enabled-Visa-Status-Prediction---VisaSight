def replace_line(path, line_num, search, replace):
    with open(path, "r") as f:
        lines = f.readlines()
    if search in lines[line_num - 1]:
        lines[line_num - 1] = lines[line_num - 1].replace(search, replace)
    with open(path, "w") as f:
        f.writelines(lines)

replace_line("frontend/src/app/auth/signup/page.tsx", 81, "We've", "We&apos;ve")
replace_line("frontend/src/app/error.tsx", 59, "Don't", "Don&apos;t")
replace_line("frontend/src/app/error.tsx", 59, "we're", "we&apos;re")
replace_line("frontend/src/app/not-found.tsx", 55, "couldn't", "couldn&apos;t")
replace_line("frontend/src/app/page.tsx", 183, "It's", "It&apos;s")
