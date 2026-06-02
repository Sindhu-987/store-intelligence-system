from typing import Dict
from typing import Any
from typing import Optional

from pydantic import BaseModel


class EventSchema(BaseModel):

    event_id: str

    store_id: str

    camera_id: str

    visitor_id: str

    event_type: str

    timestamp: str

    zone_id: Optional[str] = None

    dwell_ms: int = 0

    is_staff: bool = False

    confidence: float

    metadata: Dict[str, Any] = {}


class EventIngestRequest(BaseModel):

    events: list[EventSchema]