"""
Docstring для storage
"""
from typing import List
import json
import os

from orders import Order

ORDERS_FILE = "orders.json"


def load() -> List[Order]:
    """Загрузить заказы из файла."""
    if not os.path.exists(ORDERS_FILE):
        print("Файл заказов не найден, создана пустая коллекция.")
        return []

    try:
        with open(ORDERS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data

            print("Некорректный формат файла заказов (ожидался список).")
            return []
    except json.JSONDecodeError as e:
        print(
            f"Файл заказов повреждён (ошибка JSON: {e})")
        return []
    except Exception as e:
        print(f"Ошибка при загрузке заказов: {e}. Возвращён пустой список.")
        return []


def save(items: List[Order]):
    """Сохранить заказы в файл."""
    try:
        with open(ORDERS_FILE, "w", encoding="utf-8") as f:
            json.dump(items, f, ensure_ascii=False, indent=2)
        print("Заказы успешно сохранены.")
    except Exception as e:
        print(f"Ошибка при сохранении заказов: {e}")
