    #!/usr/bin/env python3
    """Fail if staged code changes lack a prompt reference or a new prompt file."""
import subprocess, sys

res = subprocess.run(["git","diff","--cached","--name-only"], capture_output=True, text=True)
staged = [p.strip() for p in res.stdout.splitlines() if p.strip()]
code_changed = any(p.startswith(("app/","src/","tests/")) for p in staged)
prompt_added = any(p.startswith("docs/prompts/") and p.endswith(".prompt.md") for p in staged)
if code_changed and not prompt_added:
    print("\n[PHR] Staged code changes detected but no prompt file added.")
    print("Add a prompt via: make prompt-new SLUG=<slug> STAGE=<stage>\n")
    sys.exit(1)
sys.exit(0)
