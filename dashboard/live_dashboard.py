from rich.live import Live
from rich.table import Table

import requests
import time

STORE_ID = "ST1008"

API_URL = (
    "http://localhost:8000"
)


def build_table():

    metrics = requests.get(
        f"{API_URL}/stores/{STORE_ID}/metrics"
    ).json()

    anomalies = requests.get(
        f"{API_URL}/stores/{STORE_ID}/anomalies"
    ).json()

    table = Table(
        title="Store Intelligence Dashboard"
    )

    table.add_column("Metric")
    table.add_column("Value")

    table.add_row(
        "Visitors",
        str(
            metrics[
                "unique_visitors"
            ]
        )
    )

    table.add_row(
        "Avg Dwell",
        str(
            metrics[
                "average_dwell_ms"
            ]
        )
    )

    table.add_row(
        "Queue Depth",
        str(
            metrics[
                "queue_depth"
            ]
        )
    )

    table.add_row(
        "Conversion",
        str(
            metrics[
                "conversion_rate"
            ]
        )
    )

    table.add_row(
        "Anomalies",
        str(len(anomalies))
    )

    return table


with Live(
    build_table(),
    refresh_per_second=1
) as live:

    while True:

        live.update(
            build_table()
        )

        time.sleep(1)