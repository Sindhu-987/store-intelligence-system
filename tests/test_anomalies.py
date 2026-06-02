from app.anomalies import (
    AnomalyService
)


def test_anomalies(
    db
):

    service = AnomalyService(
        db
    )

    result = service.detect(
        "ST1008"
    )

    assert isinstance(
        result,
        list
    )