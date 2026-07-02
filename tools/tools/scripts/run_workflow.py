#!/usr/bin/env python3
import sys
import subprocess

print("WARNING: This script is deprecated. Please use 'promptops workflow' instead.", file=sys.stderr)

cmd = ["promptops", "workflow"] + sys.argv[1:]
try:
    # Use subprocess to run the new command through uv if needed, or directly if installed
    subprocess.run(["uv", "run"] + cmd, check=True)
except subprocess.CalledProcessError as e:
    sys.exit(e.returncode)
except FileNotFoundError:
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        sys.exit(e.returncode)
