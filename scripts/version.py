import argparse
from pathlib import Path
import re
import subprocess


VERSION = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")
MANIFEST = Path("plugins/codex-devcraft/.codex-plugin/plugin.json")


def parse_version(value):
    match = VERSION.fullmatch(value)
    if not match:
        raise ValueError(f"invalid version: {value}")
    return tuple(int(part) for part in match.groups())


def manifest_metadata(source):
    name = re.search(r'(?m)^\s*"name"\s*:\s*"([^"]+)"\s*,?$', source)
    version = re.search(r'(?m)^\s*"version"\s*:\s*"([^"]+)"\s*,?$', source)
    if not name or not version:
        raise ValueError("plugin.json requires name and version")
    parse_version(version.group(1))
    return name.group(1), version.group(1)


def read_version(root):
    return manifest_metadata((root / MANIFEST).read_text(encoding="utf-8"))[1]


def next_version(current, selector):
    major, minor, patch = parse_version(current)
    if selector == "patch":
        target = (major, minor, patch + 1)
    elif selector == "minor":
        target = (major, minor + 1, 0)
    elif selector == "major":
        target = (major + 1, 0, 0)
    else:
        target = parse_version(selector)
    if target <= (major, minor, patch):
        raise ValueError("new version must be greater than current version")
    return ".".join(str(part) for part in target)


def changelog_section(changelog, heading):
    match = re.search(
        rf"(?ms)^## \[{re.escape(heading)}\]\s*$\n(.*?)(?=^## |\Z)",
        changelog,
    )
    if not match or not match.group(1).strip():
        raise ValueError(f"CHANGELOG.md has no nonempty [{heading}] section")
    return match, match.group(1).strip()


def replace_manifest_version(source, target):
    updated, count = re.subn(
        r'(?m)^(\s*"version"\s*:\s*")[^"]+("\s*,?\s*)$',
        rf"\g<1>{target}\g<2>",
        source,
        count=1,
    )
    if count != 1:
        raise ValueError("plugin.json requires one version field")
    return updated


def rotate_changelog(changelog, target):
    match, body = changelog_section(changelog, "Unreleased")
    replacement = f"## [Unreleased]\n\n## [{target}]\n\n{body}\n\n"
    return changelog[: match.start()] + replacement + changelog[match.end() :]


def verify(root):
    name, version = manifest_metadata((root / MANIFEST).read_text(encoding="utf-8"))
    if name != "codex-devcraft":
        raise ValueError(f"unexpected plugin name: {name}")
    changelog = (root / "CHANGELOG.md").read_text(encoding="utf-8")
    if not re.search(r"(?m)^## \[Unreleased\]\s*$", changelog):
        raise ValueError("CHANGELOG.md has no [Unreleased] section")
    changelog_section(changelog, version)


def bump(root, selector):
    manifest_path = root / MANIFEST
    changelog_path = root / "CHANGELOG.md"
    manifest = manifest_path.read_text(encoding="utf-8")
    changelog = changelog_path.read_text(encoding="utf-8")
    target = next_version(manifest_metadata(manifest)[1], selector)
    updated_manifest = replace_manifest_version(manifest, target)
    updated_changelog = rotate_changelog(changelog, target)
    manifest_path.write_text(updated_manifest, encoding="utf-8")
    changelog_path.write_text(updated_changelog, encoding="utf-8")
    verify(root)
    return target


def notes(root, version):
    parse_version(version)
    _, body = changelog_section(
        (root / "CHANGELOG.md").read_text(encoding="utf-8"), version
    )
    return body + "\n"


def tagged(root, version):
    result = subprocess.run(
        ["git", "tag", "--list", f"v{version}", version],
        cwd=root,
        text=True,
        capture_output=True,
        check=False,
    )
    return result.returncode == 0 and bool(result.stdout.strip())


def changed(root, _before):
    version = read_version(root)
    return version != "0.0.0" and not tagged(root, version)


def main():
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest="command", required=True)
    bump_parser = commands.add_parser("bump")
    bump_parser.add_argument("selector", help="patch, minor, major, or an exact X.Y.Z")
    commands.add_parser("current")
    notes_parser = commands.add_parser("notes")
    notes_parser.add_argument("version")
    changed_parser = commands.add_parser("changed")
    changed_parser.add_argument("--before", required=True)
    commands.add_parser("verify")
    arguments = parser.parse_args()
    root = Path.cwd()
    try:
        if arguments.command == "bump":
            print(bump(root, arguments.selector))
        elif arguments.command == "current":
            print(read_version(root))
        elif arguments.command == "notes":
            print(notes(root, arguments.version), end="")
        elif arguments.command == "changed":
            print(str(changed(root, arguments.before)).lower())
        else:
            verify(root)
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
