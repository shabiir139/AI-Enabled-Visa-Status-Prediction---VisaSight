from pathlib import Path

def replace_unescaped(filepath, start_line, end_line, replace_what, replace_with):
    lines = Path(filepath).read_text().splitlines()
    for i in range(start_line - 1, end_line):
        lines[i] = lines[i].replace(replace_what, replace_with)
    Path(filepath).write_text("\n".join(lines) + "\n")

replace_unescaped('frontend/src/app/error.tsx', 59, 59, "Don't worry, we're", "Don&apos;t worry, we&apos;re")
replace_unescaped('frontend/src/app/not-found.tsx', 55, 55, "couldn't find the page you're", "couldn&apos;t find the page you&apos;re")
replace_unescaped('frontend/src/app/page.tsx', 183, 183, "It's Free", "It&apos;s Free")
