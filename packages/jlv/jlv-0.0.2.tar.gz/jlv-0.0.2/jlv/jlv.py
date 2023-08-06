#!/usr/bin/env python3
# encoding: utf-8

import os
from sys import argv
import logging
from datetime import datetime
from pathlib import Path
from typing import List


def prepend_filename_to_log(filename: Path or str, log_file: Path):
    if not log_file.exists():
        log_file.touch()
    with open(log_file, "r+") as f:
        lines = f.readlines()
        lines.insert(0, str(filename) + "\n")
        f.writelines(lines)
        f.close()


def get_path_from_first_line_of_log(log_path) -> Path:
    if not log_path.exists():
        raise ValueError("log path '" + str(log_path) + "' doesn't exist")
    with open(log_path, "r") as f:
        first_entry_string = f.read().splitlines()[0]
    return Path(first_entry_string)


def is_entry_path_existing(entry_path: Path or str, journal_dir: Path) -> bool:
    full_entry_path = Path(journal_dir / entry_path)
    return full_entry_path.exists()


def get_title_taken_message(title):
    return "Sorry! The title \"" + title + "\" is already taken. :c"


def get_vim_launch_command(journal_file):
    return 'vim + "' + str(journal_file) + '"'


def get_unique_title(journal_dir):
    title = input("Please provide a title or just say \"no\": ")
    if title == "no":
        return "untitled"
    new_entry = journal_dir / (title + ".txt")
    if new_entry.exists():
        print(get_title_taken_message(title))
        return get_unique_title(journal_dir)
    if title == "":
        return get_unique_title(journal_dir)
    else:
        return title


def get_entries(journal_dir: Path, recursive: bool = False) -> List[Path]:
    if recursive:
        all_files: List[Path] = journal_dir.rglob("*")
        hidden_files: List[Path] = journal_dir.rglob(".*")
    else:
        all_files: List[Path] = journal_dir.glob("*")
        hidden_files: List[Path] = journal_dir.glob(".*")
    return [file for file in all_files if not any(
        file == hfile for hfile in hidden_files) and not file.is_dir()]


def get_entries_with_phrase_in_body(
        journal_dir: Path,
        phrase: str,
        recursive: bool = False) -> list:
    print("Printing journal files containing the phrase \"" + phrase + "\"")
    if recursive:
        journal_entries = get_entries(journal_dir, recursive=True)
    else:
        journal_entries = get_entries(journal_dir)
    return [entry for entry in journal_entries if entry.read_text().find(phrase) != -1]


def get_list_of_entries_with_name_containing(
        journal_dir: Path,
        search_str: str,
        search_archives=False):
    if search_archives:
        matched_paths = journal_dir.rglob("*" + search_str + "*")
    else:
        matched_paths = journal_dir.glob("*" + search_str + "*")
    return [path for path in matched_paths if not path.is_dir()]


def main(
    journal_dir=Path.home() /
    "Documents/journal",
    log_file=Path.home() /
        ".jlv"):

    no_flags_given = True
    title = "untitled"

    for index, arg in enumerate(argv):
        if arg[0:6] == "--log=":
            log_level = arg[6:]
            level_num = getattr(logging, log_level.upper())
            if not isinstance(level_num, int):
                raise ValueError('Invalid log level: %s' % log_level)
            logging.basicConfig(
                format='%(levelname)s:%(message)s',
                level=level_num)
            logging.info("custom logging level given: " + log_level)
            if log_level.upper() == "INFO":
                journal_dir = Path("/tmp")
                log_file = Path("/tmp/.jlv")
                logging.info("argv = " + str(argv))
            no_flags_given = False
        if arg == "-t":
            title = argv[index + 1]
            no_flags_given = False
        if arg == "-p":
            entry_location = get_path_from_first_line_of_log(log_file)
            entry_path = journal_dir / entry_location
            command = get_vim_launch_command(entry_path)
            os.system(command)
            exit(0)
        if arg == "-s":
            logging.info("index = " + str(index) + "\nargv = " + str(argv))
            matched_entries = get_entries_with_phrase_in_body(
                journal_dir, argv[index + 1])
            print("\n".join(str(entry) for entry in matched_entries))
            exit(0)
        if arg == "-l":
            entries = get_entries(journal_dir)
            print("\n".join(str(entry) for entry in entries))
            exit(0)
        if arg == "-o":
            search_string = argv[index + 1]
            possible_entry_paths = get_list_of_entries_with_name_containing(
                journal_dir, search_string)
            for entry_path in possible_entry_paths:
                response = ""
                while response != "y" and response != "n":
                    print("Open " + str(entry_path) + "? (y/n)")
                    response = input()
                if response == "y":
                    command = get_vim_launch_command(entry_path)
                    os.system(command)
                    break
            exit(0)

    logging.info("jlv starting...")

    d = datetime.now().isoformat(sep='_', timespec='seconds')

    if no_flags_given and len(argv) > 1:
        title = argv[1]

    logging.info("title = " + title)
    logging.info("journal directory: " + str(journal_dir))

    if not journal_dir.is_dir():
        journal_dir.mkdir()
        logging.info(str(journal_dir) + " directory was created")
    else:
        logging.info(str(journal_dir) + " directory was found")

    if title != "untitled":
        # can't have forward slashes in the filename
        journal_file = journal_dir / (title.replace("/", "-") + ".txt")
    else:
        journal_file = journal_dir / ("untitled_" + d)

    if journal_file.is_file():
        print(get_title_taken_message(title))
        title = get_unique_title(journal_dir)
        if title != "untitled":
            journal_file = journal_dir / (title + ".txt")
        else:
            journal_file = journal_dir / ("untitled_" + d)

    logging.info("creating new journal file: " + str(journal_file))
    journal_file.touch()
    with open(journal_file, "w+") as f:
        f.write(title + "\n\ncreated " + d + "\n\n\n")

    command = get_vim_launch_command(journal_file)
    os.system(command)

    if title == "untitled":
        title = get_unique_title(journal_dir)
        if title != "untitled":
            new_journal_file = journal_dir / (title + ".txt")
            journal_file.rename(new_journal_file)
            journal_file = new_journal_file
            with open(journal_file) as f:
                lines = f.readlines()
            lines[0] = title + "\n"
            with open(journal_file, "w") as f:
                f.writelines(lines)

    prepend_filename_to_log(journal_file.relative_to(journal_dir), log_file)


# TODO add -r (recent) functionality for printing out last 10 journal entries in format "title.txt, date-stamp"
# TODO add -l (list) functionality for listing out all journal entries in
# format "title.txt, date-stamp"

if __name__ == '__main__':
    main()
