from collections import Counter


class TrackOrders:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def add_new_order(self, customer, order, day):
        self._data.append((customer, order, day))

    def get_most_ordered_dish_per_customer(self, customer):
        customer_orders = []
        for customers, order, _ in self._data:
            if customers.lower() == customer.lower():
                customer_orders.append(order)
        return Counter(customer_orders).most_common(1)[0][0]

    def get_never_ordered_per_customer(self, customer):
        all_orders_set = set()
        orders_by_customer = set()
        for customers, order, _ in self._data:
            all_orders_set.add(order)
            if customers.lower() == customer.lower():
                orders_by_customer.add(order)
        return all_orders_set.difference(orders_by_customer)

    def get_days_never_visited_per_customer(self, customer):
        all_days = set(day for _, _, day in self._data)
        day_by_customer = set()
        for customers, _, day in self._data:
            if customers.lower() == customer.lower():
                day_by_customer.add(day)
        return all_days.difference(day_by_customer)

    def get_busiest_day(self):
        days_with_orders = Counter(day for _, _, day in self._data)
        return days_with_orders.most_common(1)[0][0]

    def get_least_busy_day(self):
        days_with_orders = Counter(day for _, _, day in self._data)
        return days_with_orders.most_common()[-1][0]

    def times_order_by_customer(self, customer, order):
        times_order = ([
            ord
            for customers, ord, _ in self._data
            if customers == customer.lower() and ord == order.lower()
        ])
        return len(times_order)
