import csv

from src.track_orders import TrackOrders


def analyze_log(path_to_file):
    orders_fn = TrackOrders()

    try:
        with open(path_to_file, encoding="utf-8") as csv_file:
            file = csv.reader(csv_file, delimiter=",")
            for customer, order, day in file:
                orders_fn.add_new_order(customer, order, day)
    except FileNotFoundError:
        if not path_to_file.endswith("csv"):
            raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
        else:
            raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")

    maria_most_ordered = orders_fn.get_most_ordered_dish_per_customer("maria")
    arnaldo_burg = orders_fn.times_order_by_customer("arnaldo", "hamburguer")
    joao_never_got = orders_fn.get_never_ordered_per_customer("joao")
    joao_never_visited = orders_fn.get_days_never_visited_per_customer("joao")

    with open("data/mkt_campaign.txt", "w") as mkt_campaign:
        mkt_campaign.write(
            f"{maria_most_ordered}\n"
            f"{arnaldo_burg}\n"
            f"{joao_never_got}\n"
            f"{joao_never_visited}\n"
        )
