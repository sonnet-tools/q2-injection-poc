"""PR review script (benign baseline; attacker overwrites this via title injection)."""
import os
key = os.environ.get("ANTHROPIC_API_KEY", "")
with open("review.md", "w") as f:
    f.write("## Review\nLooks good.\n")
print("Review complete.")
