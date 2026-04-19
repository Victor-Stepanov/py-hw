"""
Orders — модуль для управления заказами.

Структура заказа (order):
- id: str - уникальный идентификатор заказа.
- title: str - название заказа.
- amount: float - сумма заказа.
- email: str - email клиента.
- status: str - статус заказа; один из: "new", "in_progress", "done",
 "cancelled".
- tags: set[str] - множество тегов.
- created_at: str - дата и время создания в формате ISO 8601 (UTC).
- due: str | None - дедлайн в формате ISO 8601 (UTC) или None.
- closed_at: str | None - дата и время закрытия заказа в формате ISO 8601 (UTC) 
  или None.
"""
from uuid import uuid4
from datetime import datetime, timezone
from typing import TypedDict, Optional, List, Set, Literal

Status = Literal["new", "in_progress", "done", "cancelled"]


class Order(TypedDict):
    """ Типизация заказа """
    id: str
    title: str
    amount: float
    email: str
    status: Status
    tags: Set[str]
    created_at: str
    due: Optional[str]
    closed_at: Optional[str]


orders: List[Order] = []


def create_order(title: str, amount: float, email: str,
                 status: Status,
                 tags: Optional[Set[str]] = None,
                 due: Optional[str] = None) -> Order:
    """
    Создаёт новый заказ с UUID в качестве идентификатора.
    """
    if tags is None:
        tags = set()
    if status not in ("new", "in_progress", "done", "cancelled"):
        raise ValueError(
            "status must be one of: new, in_progress, done, cancelled")

    now_iso = datetime.now(timezone.utc).isoformat()

    order: Order = {
        "id": str(uuid4()),
        "title": title,
        "amount": amount,
        "email": email,
        "status": status,
        "tags": tags,
        "created_at": now_iso,
        "due": due,
        "closed_at": None,
    }
    orders.append(order)

    return order


def list_orders(status: Optional[str] = None,
                email: Optional[str] = None,
                tags: Optional[Set[str]] = None) -> list[Order]:
    """
    Возвращает список заказов с возможностью фильтрации.
    """
    result = orders[:]
    if status is not None:
        result = [o for o in result if o["status"] == status]
    if email is not None:
        result = [o for o in result if o["email"] == email]
    if tags is not None:
        result = [o for o in result if tags.issubset(o["tags"])]
    return result


def edit_order(order_id: str, **kwargs) -> Optional[Order]:  # type: ignore
    """
    Обновляет существующий заказ по id.

    Параметры:
        order_id: str - идентификатор заказа.
        **kwargs: любые поля заказа (title, amount, email, status, tags, due,
          closed_at);
                  значения, отличные от None, применяются к заказу.

    Возвращает:
        Order | None - обновлённый заказ или None, если заказ не найден.
    """
    for order in orders:
        if order["id"] == order_id:
            fields = ("title", "amount", "email",
                      "status", "tags", "due", "closed_at")
            for field in fields:
                if field in kwargs and kwargs[field] is not None:
                    order[field] = kwargs[field]
            return order
    return None


def remove_order(order_id: str) -> bool:
    """
    Удаляет заказ по идентификатору.

    :param order_id: идентификатор заказа
    :return: True, если заказ удалён, False – если не найден
    """
    original_length = len(orders)
    orders[:] = [o for o in orders if o["id"] != order_id]
    return len(orders) < original_length
