from app.models import Event


class FunnelService:

    def __init__(self, db):

        self.db = db

    def funnel(
        self,
        store_id
    ):

        entry_visitors = set()

        zone_visitors = set()

        billing_visitors = set()

        purchase_visitors = set()

        events = (
            self.db.query(Event)
            .filter(
                Event.store_id
                ==
                store_id
            )
            .all()
        )

        for event in events:

            visitor = event.visitor_id

            if event.event_type == "ENTRY":
                entry_visitors.add(visitor)

            if event.event_type == "ZONE_ENTER":
                zone_visitors.add(visitor)

            if event.event_type == "BILLING_QUEUE_JOIN":
                billing_visitors.add(visitor)

            if event.event_type == "PURCHASE":
                purchase_visitors.add(visitor)

        entry_count = len(
            entry_visitors
        )

        zone_count = len(
            zone_visitors
        )

        billing_count = len(
            billing_visitors
        )

        purchase_count = len(
            purchase_visitors
        )

        return {

            "entry": entry_count,

            "zone_visit": zone_count,

            "billing_queue": billing_count,

            "purchase": purchase_count,

            "dropoff_after_entry":
                entry_count
                -
                zone_count,

            "dropoff_after_zone":
                zone_count
                -
                billing_count,

            "dropoff_after_billing":
                billing_count
                -
                purchase_count
        }