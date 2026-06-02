from sqlalchemy.orm import Session

from app.models import Event
from app.session_service import (
    SessionService
)


class EventIngestionService:

    def __init__(
        self,
        db: Session
    ):

        self.db = db

        self.session_service = (
            SessionService(db)
        )

    def ingest_events(
        self,
        events
    ):

        inserted = 0

        duplicates = 0

        for event in events:

            existing = (
                self.db.query(Event)
                .filter(
                    Event.event_id
                    ==
                    event.event_id
                )
                .first()
            )

            if existing:

                duplicates += 1

                continue

            db_event = Event(

                event_id=event.event_id,

                store_id=event.store_id,

                camera_id=event.camera_id,

                visitor_id=event.visitor_id,

                event_type=event.event_type,

                timestamp=event.timestamp,

                zone_id=event.zone_id,

                dwell_ms=event.dwell_ms,

                is_staff=event.is_staff,

                confidence=event.confidence,

                metadata_json=event.metadata
            )

            self.db.add(
                db_event
            )

            if (
                event.event_type
                ==
                "ENTRY"
            ):

                self.session_service.create_session(

                    visitor_id=
                    event.visitor_id,

                    store_id=
                    event.store_id,

                    is_staff=
                    event.is_staff
                )

            inserted += 1

        self.db.commit()

        return {

            "inserted":
                inserted,

            "duplicates":
                duplicates
        }