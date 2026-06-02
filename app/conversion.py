from datetime import datetime
from datetime import timedelta


class ConversionEngine:

    def __init__(self):

        pass

    def correlate_purchase(
        self,
        transaction_time,
        visitor_sessions
    ):

        converted_visitors = []

        for visitor_id, session in visitor_sessions.items():

            if "billing_time" not in session:
                continue

            billing_time = session[
                "billing_time"
            ]

            if (
                billing_time
                <=
                transaction_time
                <=
                billing_time
                + timedelta(minutes=5)
            ):

                converted_visitors.append(
                    visitor_id
                )

        return converted_visitors