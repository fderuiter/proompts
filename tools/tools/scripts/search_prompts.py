#!/usr/bin/env python3
import sys
import subprocess

print("WARNING: This script is deprecated. Please use 'promptops search' instead.", file=sys.stderr)

cmd = ["promptops", "search"] + sys.argv[1:]
try:
    subprocess.run(["uv", "run"] + cmd, check=True)
except subprocess.CalledProcessError as e:
    sys.exit(e.returncode)
except FileNotFoundError:
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        sys.exit(e.returncode)
