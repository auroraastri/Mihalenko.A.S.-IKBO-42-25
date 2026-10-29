import argparse
import getpass
import socket
import sys
import tkinter as tk
from typing import Optional

from src.parser import parse_command
from src.vfs import VirtualFileSystem


class ShellEmulatorGUI:

    def __init__(
        self,
        vfs_path: Optional[str] = None,
        script_path: Optional[str] = None,
    ) -> None:
        self.vfs_path = vfs_path
        self.script_path = script_path
        self.vfs = VirtualFileSystem(vfs_path)

        self._print_debug_info()
        self._init_window()
        self._init_widgets()

        if self.script_path:
            self.root.after(100, self.run_startup_script)

    def _print_debug_info(self) -> None:
        print("=== Параметры запуска эмулятора ===")
        print(f"Путь к VFS: {self.vfs_path}")
        print(f"Путь к скрипту: {self.script_path}")
        print("===================================")

    def _init_window(self) -> None:
        self.root = tk.Tk()
        username = getpass.getuser()
        hostname = socket.gethostname()
        self.root.title(f"Эмулятор [{username}@{hostname}]")
        self.root.geometry("760x480")

    def _init_widgets(self) -> None:
        self.terminal = tk.Text(
            self.root,
            bg="black",
            fg="white",
            insertbackground="white",
            font=("Consolas", 11),
        )
        self.terminal.pack(expand=True, fill=tk.BOTH)

        self.input_entry = tk.Entry(
            self.root,
            bg="#222222",
            fg="#00ff00",
            insertbackground="#00ff00",
            font=("Consolas", 11),
        )
        self.input_entry.pack(fill=tk.X)
        self.input_entry.bind("<Return>", self._on_enter_pressed)
        self.input_entry.focus_set()

    def print_text(self, text: str) -> None:
        self.terminal.insert(tk.END, text + "\n")
        self.terminal.see(tk.END)

    def _on_enter_pressed(self, _event: tk.Event) -> None:
        cmd_text = self.input_entry.get()
        self.input_entry.delete(0, tk.END)
        self.print_text(f"$ {cmd_text}")
        self.execute_command(cmd_text)

    def execute_command(self, cmd_line: str) -> bool:
        tokens = parse_command(cmd_line)
        if not tokens:
            return True

        cmd, args = tokens[0], tokens[1:]

        if cmd == "exit":
            self.root.destroy()
            return True
        if cmd == "conf-dump":
            self.print_text(f"vfs_path: {self.vfs_path}")
            self.print_text(f"script_path: {self.script_path}")
            return True
        if cmd in ("ls", "cd"):
            self.print_text(f"{cmd}: {' '.join(args)}")
            return True

        self.print_text(f"Ошибка: неизвестная команда '{cmd}'")
        return False

    def run_startup_script(self) -> None:
        if not self.script_path:
            return
        try:
            with open(self.script_path, "r", encoding="utf-8") as file:
                lines = file.readlines()
        except OSError as err:
            self.print_text(f"Ошибка чтения стартового скрипта: {err}")
            return

        for line in lines:
            stripped = line.strip()
            if not stripped:
                continue
            self.print_text(f"$ {stripped}")
            is_success = self.execute_command(stripped)
            if not is_success:
                self.print_text("Скрипт остановлен из-за ошибки.")
                break

    def run(self) -> None:
        self.root.mainloop()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Эмулятор командной оболочки ОС."
    )
    parser.add_argument(
        "--vfs",
        type=str,
        default=None,
        help="Путь к физическому XML-файлу VFS",
    )
    parser.add_argument(
        "--script",
        type=str,
        default=None,
        help="Путь к стартовому скрипту эмулятора",
    )
    return parser


def main() -> None:
    cli_parser = build_parser()
    args = cli_parser.parse_args()
    app = ShellEmulatorGUI(vfs_path=args.vfs, script_path=args.script)
    app.run()


if __name__ == "__main__":
    main()
