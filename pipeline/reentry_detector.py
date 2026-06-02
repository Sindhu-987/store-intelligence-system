from datetime import datetime
from datetime import timedelta


class ReentryDetector:

    def __init__(
        self,
        minutes=10
    ):

        self.window = timedelta(
            minutes=minutes
        )

        self.exits = {}

    def register_exit(
        self,
        visitor_id
    ):

        self.exits[
            visitor_id
        ] = datetime.utcnow()

    def check_reentry(
        self,
        visitor_id
    ):

        if visitor_id not in self.exits:
            return False

        diff = (
            datetime.utcnow()
            -
            self.exits[
                visitor_id
            ]
        )

        return diff <= self.window