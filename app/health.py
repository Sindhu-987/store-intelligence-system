from datetime import datetime

from sqlalchemy import func

from app.models import Event


class HealthService:

    def __init__(self, db):

        self.db = db

    def health(self):

        last_event = (

            self.db.query(
                func.max(
                    Event.timestamp
                )
            )

            .scalar()

        )

        stale_feed = False

        if last_event is None:
            stale_feed = True

        return {

            "status":
                "healthy",

            "last_event_timestamp":
                last_event,

            "stale_feed":
                stale_feed,

            "timestamp":
                datetime.utcnow()
                .isoformat()
        }