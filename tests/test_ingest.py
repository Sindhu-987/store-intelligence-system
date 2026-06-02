from app.ingestion import (
    EventIngestionService
)

from app.models import Event


class MockEvent:

    event_id = "1"

    store_id = "ST1008"

    camera_id = "CAM1"

    visitor_id = "101"

    event_type = "ENTRY"

    timestamp = "2026-01-01"

    zone_id = None

    dwell_ms = 0

    is_staff = False

    confidence = 0.9

    metadata = {}


def test_event_ingestion(
    db
):

    service = EventIngestionService(
        db
    )

    result = service.ingest_events(
        [MockEvent()]
    )

    assert result[
        "inserted"
    ] == 1

    count = (
        db.query(Event)
        .count()
    )

    assert count == 1