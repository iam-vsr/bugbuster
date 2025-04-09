import subprocess
import re
import json

def run_pylint(file_path):
    result = subprocess.run(["pylint", file_path], capture_output=True, text=True)
    output = result.stdout

    issues = []

    # Extract lines like:
    # examples\examples.py:1:0: C0114: Missing module docstring (missing-module-docstring)
    pattern = r"^(.*?):(\d+):(\d+): ([A-Z]\d+): (.*) \((.*)\)$"
    for line in output.splitlines():
        match = re.match(pattern, line.strip())
        if match:
            filepath, line_num, col_num, code, message, symbol = match.groups()
            issues.append({
                "file": filepath,
                "line": int(line_num),
                "column": int(col_num),
                "code": code,
                "message": message,
                "symbol": symbol
            })

    print(json.dumps(issues, indent=2))
    return issues

if __name__ == "__main__":
    run_pylint("examples/examples.py")
