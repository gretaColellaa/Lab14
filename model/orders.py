from dataclasses import dataclass
from datetime import datetime

@dataclass
class Order:
    order_id: int
    customer_id: int
    order_status: int
    order_date: datetime
    required_date: datetime
    shipped_date: datetime
    store_id: int
    staff_id: int

    def __hash__(self):
        return hash((self.order_id, self.order_date))

    def __eq__(self, other):
        if not isinstance(other, Order):
            return NotImplemented
        return (self.order_id == other.order_id and
                self.customer_id == other.customer_id and
                self.order_status == other.order_status and
                self.order_date == other.order_date and
                self.required_date == other.required_date and
                self.shipped_date == other.shipped_date and
                self.store_id == other.store_id and
                self.staff_id == other.staff_id)

    def __str__(self):
        return (f"Order(ID: {self.order_id}, Customer: {self.customer_id}, Status: {self.order_status}, "
                f"Order Date: {self.order_date}, Required: {self.required_date}, Shipped: {self.shipped_date}, "
                f"Store: {self.store_id}, Staff: {self.staff_id})")