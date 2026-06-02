from datetime import datetime

from app.models import VisitorSession


class SessionService:

    def __init__(self, db):

        self.db = db

    def create_session(
        self,
        visitor_id,
        store_id,
        is_staff=False
    ):

        existing = (
            self.db.query(
                VisitorSession
            )
            .filter(
                VisitorSession.visitor_id
                ==
                str(visitor_id)
            )
            .first()
        )

        if existing:
            return existing

        session = VisitorSession(

            visitor_id=str(visitor_id),

            store_id=store_id,

            entry_time=datetime.utcnow().isoformat(),

            total_dwell_ms=0,

            converted=False,

            is_staff=is_staff,

            visit_count=1
        )

        self.db.add(session)

        self.db.commit()

        return session

    def mark_converted(
        self,
        visitor_id
    ):

        session = (
            self.db.query(
                VisitorSession
            )
            .filter(
                VisitorSession.visitor_id
                ==
                str(visitor_id)
            )
            .first()
        )

        if not session:
            return

        session.converted = True

        self.db.commit()

    def update_dwell(
        self,
        visitor_id,
        dwell_ms
    ):

        session = (
            self.db.query(
                VisitorSession
            )
            .filter(
                VisitorSession.visitor_id
                ==
                str(visitor_id)
            )
            .first()
        )

        if not session:
            return

        session.total_dwell_ms += dwell_ms

        self.db.commit()