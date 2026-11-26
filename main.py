"""Funniest Sign on a Haunted Server Room Door.

Writes one funny sign line (1-120 chars) to entry.txt in the output
directory make.fun provides (MAKEFUN_OUTPUT_DIR), falling back to a local
./output directory when run outside the grader.

The sign: the previous sysadmin died in 2011, but his login session never
timed out -- so the door warns you he is still logged in.
"""

import os
import sys

SIGN = "NOTICE: The previous admin is still logged in. He died in 2011. His session never timed out."


def main():
    try:
        out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "output"
        )
        os.makedirs(out_dir, exist_ok=True)
        # The gate allows 1-120 characters of UTF-8 text; refuse to emit
        # anything outside it rather than hand in an invalid entry.
        text = SIGN.strip()
        if not (1 <= len(text) <= 120):
            raise ValueError("sign is %d chars, must be 1-120" % len(text))
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        os.chmod(path, 0o644)
    except Exception as exc:  # noqa: BLE001 - never fail the run
        print("error: %s" % exc, file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
