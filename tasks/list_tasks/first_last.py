"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Есть список работников, отсортированный по из производительности.

Отредактировать функцию get_first_last таким образом, чтобы можно было
узнать кто лучший, а кто худший работник
"""
workers = [
    "Зебест Иван Суперович",
    "Просто Антон Работович",
    "Забил Артем Гвоздевич"
]


def get_first_last(collection: list) -> tuple:
    return collection[0], collection[-1]


if __name__ == '__main__':
    print("Результаты месяца:")
    best, worst = get_first_last(workers)
    print(f"+10% к премии: {best}")
    print(f"-10% к премии: {worst}")
