"""
Сніжинка Коха ❄️ — рекурсивне малювання фракталу

🔍 Що робить ця програма:
- Будує фрактал «сніжинка Коха» за допомогою рекурсивної функції
- Малює три сторони сніжинки шляхом заміни кожної лінії на ламану фігуру
- Візуалізація відбувається у графічному вікні turtle

📥 Вхідні дані:
- Рівень рекурсії (ціле число >= 0), вводиться вручну через `input()`

📤 Результат:
- Побудова сніжинки у вікні turtle
- Повідомлення про успішне завершення
- Вікно закривається після кліку мишкою

▶️ Приклад запуску:
    python koch_snowflake.py
    Введіть рівень рекурсії (0 або більше): 3

💡 Чим більший рівень — тим складніший фрактал і довший час побудови

🧩 Скрипт є частиною обов’язкового завдання до теми «Рекурсія»
"""

import turtle
import argparse
import sys

def koch_curve(t: turtle.Turtle, order: int, size: float):
    """Рекурсивна функція для побудови кривої Коха."""
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_snowflake(order: int):
    """Малює сніжинку Коха заданого рівня."""
    screen = turtle.Screen()
    screen.title(f"Koch Snowflake (order {order})")
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-150, 90)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, 300)
        t.right(120)

    screen.mainloop()

def main():
    parser = argparse.ArgumentParser(description="Побудова сніжинки Коха.")
    parser.add_argument("order", type=int, nargs="?", help="Рівень рекурсії (0 або більше)")
    args = parser.parse_args()

    # Якщо не передали через аргументи — запитати через input()
    if args.order is None:
        try:
            order = int(input("Введіть рівень рекурсії (0 або більше): "))
        except ValueError:
            print("❌ Помилка: введіть ціле число.")
            sys.exit(1)
    else:
        order = args.order

    if order < 0:
        print("❌ Рівень рекурсії не може бути від’ємним.")
        sys.exit(1)

    draw_koch_snowflake(order)

if __name__ == "__main__":
    main()
