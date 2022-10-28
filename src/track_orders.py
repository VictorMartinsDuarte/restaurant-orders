from collections import Counter


class TrackOrders:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def add_new_order(self, customer, order, day):
        self._data.append({customer, order, day})

    def get_most_ordered_dish_per_customer(self, customer):
        customer_orders = []
        for customer, order, _ in self._data:
            if (customer == customer):
                customer_orders.append(order)
        return Counter(customer_orders).most_common(1)[0][0]

    def get_never_ordered_per_customer(self, customer):
        all_orders_set = set()
        orders_by_customer = set()
        for customers, order, _ in self._data:
            all_orders_set.add(order)
            if customers == customer:
                orders_by_customer.add(order)
        return all_orders_set - orders_by_customer

    def get_days_never_visited_per_customer(self, customer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass

    def all_orders_set(self):
        return set(order["order"] for order in self._data)

    def orders_by_customer(self, customer):
        return set(o["order"] for o in self._data if o["customer"] == customer)
