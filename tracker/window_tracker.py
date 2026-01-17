import subprocess
import shutil
import time
import sys


def get_windows():
    # Check if wmctrl is available
    if not shutil.which("wmctrl"):
        print("Error: 'wmctrl' is not installed.", file=sys.stderr)
        print("Please install it with: sudo pacman -S wmctrl", file=sys.stderr)
        sys.exit(1)

    try:
        output = subprocess.check_output(["wmctrl", "-lG"]).decode()
    except subprocess.CalledProcessError:
        return []

    windows = []

    for line in output.splitlines():
        parts = line.split(None, 7)
        if len(parts) < 8:
            continue

        win_id = parts[0]
        screen = int(parts[1])
        title = parts[7]

        windows.append({"id": win_id, "screen": screen, "title": title})

    return windows


def main():
    last_active = {}

    try:
        while True:
            for win in get_windows():
                last_active.setdefault(win["screen"], win["title"])

            print(last_active)
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nExiting...", file=sys.stderr)
        sys.exit(0)


if __name__ == "__main__":
    main()
