from app.metrics import (
    MetricsService
)


def test_metrics_empty(
    db
):

    service = MetricsService(
        db
    )

    result = service.store_metrics(
        "ST1008"
    )

    assert (
        result[
            "unique_visitors"
        ]
        == 0
    )