from app.health import (
    HealthService
)


def test_health(
    db
):

    service = HealthService(
        db
    )

    result = service.health()

    assert (
        result["status"]
        ==
        "healthy"
    )