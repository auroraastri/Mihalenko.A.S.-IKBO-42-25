"""Модульные тесты для проверки 1-3 этапов эмулятора."""

import unittest
from src.parser import parse_command
from src.vfs import VirtualFileSystem


class TestEmulatorCore(unittest.TestCase):

    def test_parser_empty(self) -> None:
        self.assertEqual(parse_command(""), [])
        self.assertEqual(parse_command("   "), [])

    def test_parser_spaces(self) -> None:
        self.assertEqual(parse_command("ls -la /home"), ["ls", "-la", "/home"])
        self.assertEqual(parse_command("cd   docs"), ["cd", "docs"])

    def test_default_vfs_structure(self) -> None:
        vfs = VirtualFileSystem(None)
        self.assertIn("home", vfs.root.children)
        user_node = vfs.root.children["home"].children.get("user")
        self.assertIsNotNone(user_node)
        self.assertIn("sample.txt", user_node.children)

    def test_vfs_multilevel_loading(self) -> None:
        vfs = VirtualFileSystem("vfs_samples/multilevel.xml")
        self.assertIn("root_dir", vfs.root.children)
        sub1 = vfs.root.children["root_dir"].children.get("sub1")
        self.assertIsNotNone(sub1)
        sub2 = sub1.children.get("sub2")
        self.assertIsNotNone(sub2)
        file_node = sub2.children.get("data.txt")
        self.assertIsNotNone(file_node)
        self.assertEqual(file_node.data, b"Nested content in base64")


if __name__ == "__main__":
    unittest.main()
