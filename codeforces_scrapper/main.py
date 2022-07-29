#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import sys, os


def get_header(url: str) -> str:
    return f"# codeforces problem scrapped from [{url}]({url})"


def get_problem(url: str) -> str:
    webpage = requests.get(url)
    soup = BeautifulSoup(webpage.text, "html.parser")
    problem = soup.find("div", {"class": "problem-statement"})
    return str(problem)


def get_style() -> str:
    style_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                              "style.css")
    # copy the style from style.css
    with open(style_path, "r") as f:
        style = f.read()
    return str(f"<style>\n{style}\n</style>")


def write_to_file(content: str, path: str) -> None:
    path_to_file = os.path.join(path, "README.md")

    # check if a README.md already exists in the given path
    need_overwrite = os.path.exists(path_to_file)

    if need_overwrite:
        print("README.md already exists in the given path, overwrite? (y/n):",
              end="")
        overwrite_prompt = input()
        if overwrite_prompt != "y":
            sys.exit(1)

    with open(path_to_file, "w") as f:
        f.write(str(content))


def main():
    if len(sys.argv) not in [2, 3]:
        print("Usage: python3 main.py <url> [directory]")
        sys.exit(1)
    header = get_header(sys.argv[1])
    problem = get_problem(sys.argv[1])
    style = get_style()
    path = os.getcwd() if len(sys.argv) == 2 else sys.argv[2]
    write_to_file(f"{header}\n\n{problem}\n\n{style}", path)


if __name__ == "__main__":
    main()