import sys

VALID_MODES = ["LOAD", "EXPORT"]
# load or export
mode = sys.argv[1]

if not mode.upper() in VALID_MODES:
    raise ValueError(f"{str(mode).upper()} is not a valid mode, valid modes are: {(', '.join(VALID_MODES))}")

pw = input("ENV PASS: ")

def load(password: str):
    