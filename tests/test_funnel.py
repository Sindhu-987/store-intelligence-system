from app.funnel import (
    FunnelService
)


def test_funnel_empty(
    db
):

    service = FunnelService(
        db
    )

    result = service.funnel(
        "ST1008"
    )

    assert (
        result[
            "entry"
        ]
        == 0
    )