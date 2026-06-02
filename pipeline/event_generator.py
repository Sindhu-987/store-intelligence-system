import uuid

from datetime import datetime


class EventGenerator:

    def generate(
        self,
        store_id,
        camera_id,
        visitor_id,
        event_type,
        zone_id=None,
        dwell_ms=0,
        is_staff=False,
        confidence=1.0,
        metadata=None
    ):

        return {

            "event_id":
                str(uuid.uuid4()),

            "store_id":
                store_id,

            "camera_id":
                camera_id,

            "visitor_id":
                str(visitor_id),

            "event_type":
                event_type,

            "timestamp":
                datetime.utcnow()
                .isoformat(),

            "zone_id":
                zone_id,

            "dwell_ms":
                dwell_ms,

            "is_staff":
                is_staff,

            "confidence":
                confidence,

            "metadata":
                metadata or {}
        }

    def entry(
        self,
        store_id,
        camera_id,
        visitor_id
    ):

        return self.generate(
            store_id,
            camera_id,
            visitor_id,
            "ENTRY"
        )

    def exit(
        self,
        store_id,
        camera_id,
        visitor_id
    ):

        return self.generate(
            store_id,
            camera_id,
            visitor_id,
            "EXIT"
        )

    def reentry(
        self,
        store_id,
        camera_id,
        visitor_id
    ):

        return self.generate(
            store_id,
            camera_id,
            visitor_id,
            "REENTRY"
        )

    def zone_enter(
        self,
        store_id,
        camera_id,
        visitor_id,
        zone
    ):

        return self.generate(
            store_id,
            camera_id,
            visitor_id,
            "ZONE_ENTER",
            zone_id=zone
        )

    def zone_exit(
        self,
        store_id,
        camera_id,
        visitor_id,
        zone
    ):

        return self.generate(
            store_id,
            camera_id,
            visitor_id,
            "ZONE_EXIT",
            zone_id=zone
        )

    def zone_dwell(
        self,
        store_id,
        camera_id,
        visitor_id,
        zone,
        dwell_ms
    ):

        return self.generate(
            store_id,
            camera_id,
            visitor_id,
            "ZONE_DWELL",
            zone_id=zone,
            dwell_ms=dwell_ms
        )