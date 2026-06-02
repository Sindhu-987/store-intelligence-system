from datetime import datetime

from app.models import Event
from app.models import VisitorSession


class AnomalyService:

    def __init__(self, db):

        self.db = db

    def detect(
        self,
        store_id
    ):

        anomalies = []

        queue_size = (

            self.db.query(Event)

            .filter(

                Event.store_id
                ==
                store_id,

                Event.event_type
                ==
                "BILLING_QUEUE_JOIN"

            )

            .count()

        )

        if queue_size > 10:

            anomalies.append({

                "type":
                    "QUEUE_SPIKE",

                "severity":
                    "WARN",

                "reason":
                    f"{queue_size} queue joins detected",

                "suggested_action":
                    "Open another billing counter",

                "timestamp":
                    datetime.utcnow().isoformat()
            })

        visitors = (

            self.db.query(
                VisitorSession
            )

            .filter(
                VisitorSession.store_id
                ==
                store_id
            )

            .count()

        )

        converted = (

            self.db.query(
                VisitorSession
            )

            .filter(
                VisitorSession.store_id
                ==
                store_id,

                VisitorSession.converted
                ==
                True
            )

            .count()

        )

        if visitors > 10:

            rate = (
                converted
                /
                visitors
            ) * 100

            if rate < 10:

                anomalies.append({

                    "type":
                        "CONVERSION_DROP",

                    "severity":
                        "CRITICAL",

                    "reason":
                        f"Conversion only {rate:.2f}%",

                    "suggested_action":
                        "Check staffing and inventory",

                    "timestamp":
                        datetime.utcnow().isoformat()
                })

        return anomalies