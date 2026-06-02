from app.models import VisitorSession


class EventProcessor:

    def __init__(self, db):

        self.db = db

    def process_event(
        self,
        event
    ):

        session = (

            self.db.query(
                VisitorSession
            )

            .filter(
                VisitorSession.visitor_id
                ==
                event.visitor_id
            )

            .first()

        )

        if not session:
            return

        if event.event_type == "ZONE_DWELL":

            session.total_dwell_ms += (
                event.dwell_ms
            )

        self.db.commit()