#!/usr/bin/env python3
# encoding: utf-8

import unittest
from . import jlv
from pathlib import Path
from shutil import rmtree


class Testjlv(unittest.TestCase):
    test_root_dir = Path("/tmp/test")
    if test_root_dir.is_dir():
        rmtree(test_root_dir)
    test_root_dir.mkdir()

    test_log_file = test_root_dir / ".jlv"
    test_log_lines = ["test2.txt\n", "txt1.txt\n"]
    with open(test_log_file, "w+") as f:
        f.writelines(test_log_lines)
        f.close()

    test_journal_dir = test_root_dir / "journal"
    test_journal_dir.mkdir()
    test_entry_titles = [
        "test1.txt",
        "test2.txt"
    ]
    test_entry_paths = []
    for i in range(len(test_entry_titles)):
        test_entry_paths.append(test_journal_dir / test_entry_titles[i])
    for entry_path in test_entry_paths:
        entry_path.touch()

    test_archive_dir = test_journal_dir / "2017"
    test_archive_dir.mkdir()
    test_archive_titles = [
        "archive1.txt"
    ]
    test_archive_paths = []
    for i in range(len(test_archive_titles)):
        test_archive_paths.append(test_archive_dir / test_archive_titles[i])
    for entry_path in test_archive_paths:
        entry_path.touch()

    def test_get_entries(self):
        result = jlv.get_entries(self.test_journal_dir)
        print("\nresult: " + str(result))
        self.assertCountEqual(result, self.test_entry_paths)

    def test_get_entries_recursive(self):
        result = jlv.get_entries(self.test_journal_dir, recursive=True)
        print("\nresult: " + str(result))
        self.assertCountEqual(
            result,
            self.test_entry_paths +
            self.test_archive_paths)

    def test_get_path_from_first_line_of_log(self):
        result = jlv.get_path_from_first_line_of_log(self.test_log_file)
        print("\nresult: " + str(result))
        self.assertEqual(result, Path("test2.txt"))

    def test_is_entry_path_existing(self):
        result = jlv.is_entry_path_existing("test1.txt", self.test_journal_dir)
        print("\nresult of actual entry argument: " + str(result))
        self.assertEqual(result, True)
        result = jlv.is_entry_path_existing(
            "not_real.txt", self.test_journal_dir)
        print("\nresult of fake entry argument: " + str(result))
        self.assertEqual(result, False)

    def test_get_list_of_entries_with_name_containing(self):
        result = jlv.get_list_of_entries_with_name_containing(
            self.test_journal_dir, "1")
        result = list(result)
        print("\nresult of existing entry: " + str(result))
        self.assertEqual(result, [Path(self.test_journal_dir / "test1.txt")])
        result = jlv.get_list_of_entries_with_name_containing(
            self.test_journal_dir, "archive")
        print("\nresult of directory search string: " + str(result))
        self.assertEqual(len(result), 0)


if __name__ == '__main__':
    unittest.main()
