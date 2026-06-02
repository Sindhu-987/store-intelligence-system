from datetime import datetime


class SessionManager:

    def __init__(self):

        self.sessions = {}

    def start_session(
        self,
        visitor_id
    ):

        self.sessions[
            visitor_id
        ] = {

            "entry_time":
                datetime.utcnow(),

            "zones": set(),

            "last_seen":
                datetime.utcnow(),

            "total_dwell_ms":
                0,

            "converted":
                False
        }

    def exists(
        self,
        visitor_id
    ):

        return (
            visitor_id
            in
            self.sessions
        )

    def touch(
        self,
        visitor_id
    ):

        if visitor_id not in self.sessions:
            return

        self.sessions[
            visitor_id
        ]["last_seen"] = (
            datetime.utcnow()
        )

    def add_zone(
        self,
        visitor_id,
        zone
    ):

        if visitor_id not in self.sessions:
            return

        self.sessions[
            visitor_id
        ]["zones"].add(
            zone
        )

    def add_dwell(
        self,
        visitor_id,
        dwell_ms
    ):

        if visitor_id not in self.sessions:
            return

        self.sessions[
            visitor_id
        ]["total_dwell_ms"] += (
            dwell_ms
        )

    def convert(
        self,
        visitor_id
    ):

        if visitor_id not in self.sessions:
            return

        self.sessions[
            visitor_id
        ]["converted"] = True

    def end_session(
        self,
        visitor_id
    ):

        if visitor_id not in self.sessions:
            return None

        session = self.sessions[
            visitor_id
        ]

        session[
            "exit_time"
        ] = datetime.utcnow()

        return session