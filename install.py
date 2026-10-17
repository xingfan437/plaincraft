"""Install the bundled local skills; no config edits, hooks or network calls."""

import argparse
import hashlib
import os
from pathlib import Path
import shutil
import sys
import tempfile


def fingerprint(directory: Path) -> dict:
    return {path.relative_to(directory).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest() for path in directory.rglob("*") if path.is_file() and "__pycache__" not in path.parts and path.suffix not in {".pyc", ".pyo"}}


def install(source: Path, destination: Path, names: list[str]) -> list[str]:
    # Preflight every target before making the first change.
    selected = []
    result = []
    for name in names:
        origin, target = source / name, destination / name
        if not (origin / "SKILL.md").is_file():
            raise ValueError("Missing skill source: " + name)
        if target.is_symlink():
            raise ValueError("Existing skill target is a link; inspect it manually: " + str(target))
        if target.exists():
            if not target.is_dir() or fingerprint(target) != fingerprint(origin):
                raise ValueError("Existing skill differs; no files overwritten: " + str(target))
            result.append(name + ": already installed (identical)")
        else:
            selected.append((name, origin, target))
    destination.mkdir(parents=True, exist_ok=True)
    for name, origin, target in selected:
        # Stage on the same filesystem and rename only after a complete copy.
        with tempfile.TemporaryDirectory(prefix=".clearwork-", dir=destination) as temporary:
            staged = Path(temporary) / name
            shutil.copytree(origin, staged, ignore=shutil.ignore_patterns("__pycache__", "*.pyc", "*.pyo"))
            staged.rename(target)
        result.append(name + ": installed")
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--destination", type=Path, help="Skill folder. Default: CODEX_HOME/skills, or ~/.codex/skills.")
    parser.add_argument("--only", choices=("worktrace", "plaincraft"))
    args = parser.parse_args(argv)
    root = Path(__file__).resolve().parent
    destination = args.destination or Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))) / "skills"
    try:
        names = [args.only] if args.only else [name for name in ("worktrace", "plaincraft") if (root / "skills" / name / "SKILL.md").is_file()]
        if not names:
            raise ValueError("No bundled skills found")
        for message in install(root / "skills", destination, names):
            print(message)
        print("Start a new chat, or reload skills if available. Invocation: " + " / ".join("$" + name for name in names))
        return 0
    except (OSError, ValueError) as exc:
        print("Clearwork: " + str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
