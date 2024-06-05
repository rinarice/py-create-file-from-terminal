import sys
import os

from datetime import datetime


def main() -> None:
    args = sys.argv[1:]
    dir_path = None
    file_path = None

    if "-d" in args:
        d_index = args.index("-d")
        dir_path = os.path.join(*args[d_index + 1:])
        os.makedirs(dir_path, exist_ok=True)

    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]
        file_path = file_name

        if dir_path is not None:
            file_path = os.path.join(dir_path, file_name)

    lines = []

    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
    content = timestamp

    content += "\n".join(f"{i + 1} {line}" for i, line in enumerate(lines))

    if file_path is not None:
        if os.path.exists(file_path):
            with open(file_path, "a") as file:
                file.write("\n" + content)
        else:
            with open(file_path, "w") as file:
                file.write(content)


if __name__ == "__main__":
    main()
