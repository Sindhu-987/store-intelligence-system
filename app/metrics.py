from sqlalchemy import func

from app.models import Event
from app.models import VisitorSession


class MetricsService:

    def __init__(self, db):

        self.db = db

    def store_metrics(
        self,
        store_id
    ):

        visitors = (

            self.db.query(
                VisitorSession
            )

            .filter(
                VisitorSession.store_id
                ==
                store_id,

                VisitorSession.is_staff
                ==
                False
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

        # FIXED
        avg_dwell = (

            self.db.query(

                func.avg(
                    Event.dwell_ms
                )

            )

            .filter(
                Event.store_id
                ==
                store_id,

                Event.event_type
                ==
                "ZONE_DWELL"
            )

            .scalar()

        )

        queue_depth = (

            self.db.query(Event)

            .filter(
                Event.event_type
                ==
                "BILLING_QUEUE_JOIN"
            )

            .count()

        )

        abandonment = (

            self.db.query(Event)

            .filter(
                Event.event_type
                ==
                "BILLING_QUEUE_ABANDON"
            )

            .count()

        )

        conversion_rate = 0

        if visitors:

            conversion_rate = round(
                converted
                /
                visitors
                *
                100,
                2
            )

        return {

            "store_id":
                store_id,

            "unique_visitors":
                visitors,

            "purchase_count":
                converted,

            "conversion_rate":
                conversion_rate,

            "average_dwell_ms":
                int(avg_dwell or 0),

            "queue_depth":
                queue_depth,

            "abandonment_rate":
                abandonment
        }