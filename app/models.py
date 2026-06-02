from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import Boolean
from sqlalchemy import JSON

from app.database import Base


class Event(Base):

    __tablename__ = "events"

    event_id = Column(
        String,
        primary_key=True
    )

    store_id = Column(
        String,
        index=True
    )

    camera_id = Column(
        String
    )

    visitor_id = Column(
        String,
        index=True
    )

    event_type = Column(
        String,
        index=True
    )

    timestamp = Column(
        String,
        index=True
    )

    zone_id = Column(
        String,
        nullable=True
    )

    dwell_ms = Column(
        Integer,
        default=0
    )

    is_staff = Column(
        Boolean,
        default=False
    )

    confidence = Column(
        Float,
        default=0.0
    )

    metadata_json = Column(
        JSON,
        nullable=True
    )


class VisitorSession(Base):

    __tablename__ = "sessions"

    visitor_id = Column(
        String,
        primary_key=True
    )

    store_id = Column(
        String,
        index=True
    )

    entry_time = Column(
        String
    )

    exit_time = Column(
        String,
        nullable=True
    )

    total_dwell_ms = Column(
        Integer,
        default=0
    )

    converted = Column(
        Boolean,
        default=False
    )

    is_staff = Column(
        Boolean,
        default=False
    )

    visit_count = Column(
        Integer,
        default=1
    )


class Anomaly(Base):

    __tablename__ = "anomalies"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    store_id = Column(
        String
    )

    anomaly_type = Column(
        String
    )

    severity = Column(
        String
    )

    reason = Column(
        String
    )

    suggested_action = Column(
        String
    )

    timestamp = Column(
        String
    )