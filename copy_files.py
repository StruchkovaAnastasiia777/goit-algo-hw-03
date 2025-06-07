"""
📂 Рекурсивне копіювання та сортування файлів за розширенням

🛠 Що робить цей скрипт:
- Рекурсивно проходить усі вкладені папки в обраній директорії
- Копіює всі файли до нової папки (за замовчуванням: dist)
- Автоматично розкладає файли за типом/розширенням:
  JPG → dist/jpg/photo.jpg
  MP3 → dist/mp3/music.mp3
  PDF → dist/pdf/report.pdf

🖥 Як використовувати:
1. Запусти скрипт через термінал:

    ▶️ python copy_files.py

2. Введи шлях до папки, з якої потрібно скопіювати файли:
    Наприклад: test_folder або /Users/ім’я/Desktop/назва_папки

3. Введи шлях до папки призначення (або натисни Enter для стандартної dist)

✅ У результаті отримаєш:
- Нову структуру папок з розсортованими файлами
- Вивід у терміналі у вигляді дерева

🧩 Скрипт є частиною домашнього завдання на тему «Рекурсія»
"""

import shutil
from pathlib import Path
from io import StringIO
import sys

def copy_files_by_extension(src_path: Path, dst_path: Path):
    """
    Рекурсивно копіює файли з src_path до dst_path, сортує їх за розширеннями.
    """
    if src_path.is_dir():
        for item in src_path.iterdir():
            copy_files_by_extension(item, dst_path)
    elif src_path.is_file():
        ext = src_path.suffix.lower().lstrip(".")
        if ext:
            target_dir = dst_path / ext
            target_dir.mkdir(parents=True, exist_ok=True)
            target_file = target_dir / src_path.name
            if not target_file.exists():
                try:
                    shutil.copy2(src_path, target_file)
                except (PermissionError, OSError) as e:
                    print(f"⚠️ Помилка при копіюванні {src_path}: {e}")

def print_tree(path: Path, prefix: str = "", output_lines=None):
    """
    Рекурсивно виводить структуру папок/файлів у вигляді дерева.
    """
    if output_lines is None:
        output_lines = []

    items = sorted(list(path.iterdir()))
    for index, item in enumerate(items):
        connector = "└── " if index == len(items) - 1 else "├── "
        output_lines.append(prefix + connector + item.name)
        if item.is_dir():
            extension = "    " if index == len(items) - 1 else "│   "
            print_tree(item, prefix + extension, output_lines)
    return output_lines

def print_framed_output(text: str):
    """
    Обгортає текст у рамку для кращого читання.
    """
    lines = text.strip().split("\n")
    width = max(len(line) for line in lines)
    print("┌" + "─" * (width + 2) + "┐")
    for line in lines:
        print(f"│ {line.ljust(width)} │")
    print("└" + "─" * (width + 2) + "┘")

def main():
    print("🔁 Копіювання та сортування файлів за розширенням")
    src_input = input("📂 Введіть шлях до вихідної папки: ").strip()
    dst_input = input("📁 Введіть шлях до папки призначення (або натисніть Enter для 'dist'): ").strip()

    src_path = Path(src_input)
    dst_path = Path(dst_input) if dst_input else Path("dist")

    if not src_path.exists() or not src_path.is_dir():
        print("❌ Помилка: вихідна папка не існує або це не директорія.")
        return

    dst_path.mkdir(parents=True, exist_ok=True)
    copy_files_by_extension(src_path, dst_path)

    print("\n🌲 Структура директорії:")
    tree_lines = print_tree(dst_path)
    framed_output = "\n".join(tree_lines)
    print_framed_output(framed_output)

    # Збереження до лог-файлу
    with open("copy_log.txt", "w", encoding="utf-8") as f:
        f.write(f"📁 Джерело: {src_path.resolve()}\n")
        f.write(f"📁 Призначення: {dst_path.resolve()}\n\n")
        f.write("📂 Структура директорії:\n")
        f.write(framed_output)

    print("\n📝 Лог збережено у copy_log.txt")

if __name__ == "__main__":
    main()