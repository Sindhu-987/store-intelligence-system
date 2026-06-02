import pandas as pd

from datetime import datetime
from datetime import timedelta


class PurchaseEngine:

    def __init__(
        self,
        pos_csv_path
    ):

        self.df = pd.read_csv(
            pos_csv_path
        )

    def find_converted_visitors(
        self,
        visitor_sessions
    ):

        converted = set()

        for _, row in self.df.iterrows():

            try:

                txn_time = datetime.strptime(

                    f"{row['order_date']} {row['order_time']}",

                    "%d-%m-%Y %H:%M:%S"

                )

            except:

                continue

            for visitor_id, session in visitor_sessions.items():

                billing_time = session.get(
                    "billing_time"
                )

                if not billing_time:
                    continue

                if (
                    billing_time
                    <=
                    txn_time
                    <=
                    billing_time
                    + timedelta(minutes=5)
                ):

                    converted.add(
                        visitor_id
                    )

        return converted