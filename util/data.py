from pathlib import Path
from urllib.request import Request, urlopen

def _get_input_file_path(y, d):
    path = Path("input", f"{y}", f"{d}")
    if path.is_file():
        return path

    if path.exists():
        raise RuntimeError(f"{path} exists, but is not a file.")

    path.parent.mkdir(parents = True, exist_ok = True)

    if not Path("session").is_file():
        raise RuntimeError("Put your AOC session cookie value in the file called session")

    with open("session") as f:
        session = f.read()

    request = Request(
        f"https://adventofcode.com/{y}/day/{d}/input",
        headers = dict(Cookie = f"session={session}"))

    with urlopen(request) as src, path.open("xb") as dst:
        dst.write(src.read())

    return path

def get_input(y, d):
    path = _get_input_file_path(y, d)
    with path.open() as f:
        return f.read()
