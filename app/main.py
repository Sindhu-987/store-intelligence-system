from fastapi import FastAPI
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import (
    Base,
    engine,
    get_db
)

from app.schemas import (
    EventIngestRequest
)

from app.ingestion import (
    EventIngestionService
)

from app.metrics import (
    MetricsService
)

from app.funnel import (
    FunnelService
)

from app.heatmap import (
    HeatmapService
)

from app.anomalies import (
    AnomalyService
)

from app.health import (
    HealthService
)

Base.metadata.create_all(
    bind=engine
)

app = FastAPI(
    title="Store Intelligence API",
    version="1.0.0"
)


@app.get("/")
def root():

    return {
        "message":
        "Store Intelligence API"
    }


@app.post("/events/ingest")
def ingest_events(
    request: EventIngestRequest,
    db: Session = Depends(get_db)
):

    service = EventIngestionService(
        db
    )

    result = service.ingest_events(
        request.events
    )

    return result


@app.get(
    "/stores/{store_id}/metrics"
)
def metrics(
    store_id: str,
    db: Session = Depends(get_db)
):

    service = MetricsService(
        db
    )

    return service.store_metrics(
        store_id
    )


@app.get(
    "/stores/{store_id}/funnel"
)
def funnel(
    store_id: str,
    db: Session = Depends(get_db)
):

    service = FunnelService(
        db
    )

    return service.funnel(
        store_id
    )


@app.get(
    "/stores/{store_id}/heatmap"
)
def heatmap(
    store_id: str,
    db: Session = Depends(get_db)
):

    service = HeatmapService(
        db
    )

    return service.build(
        store_id
    )


@app.get(
    "/stores/{store_id}/anomalies"
)
def anomalies(
    store_id: str,
    db: Session = Depends(get_db)
):

    service = AnomalyService(
        db
    )

    return service.detect(
        store_id
    )


@app.get("/health")
def health(
    db: Session = Depends(get_db)
):

    service = HealthService(
        db
    )

    return service.health()