from sqlalchemy import func

from app.models import Event


class HeatmapService:

    def __init__(self, db):

        self.db = db

    def build(
        self,
        store_id
    ):

        rows = (

            self.db.query(

                Event.zone_id,

                func.count(
                    Event.event_id
                ),

                func.avg(
                    Event.dwell_ms
                )

            )

            .filter(
                Event.store_id
                ==
                store_id,

                Event.zone_id
                !=
                None
            )

            .group_by(
                Event.zone_id
            )

            .all()

        )

        output = []

        max_visits = 1

        if rows:

            max_visits = max(
                row[1]
                for row in rows
            )

        for zone, visits, dwell in rows:

            score = int(
                (
                    visits
                    /
                    max_visits
                )
                * 100
            )

            output.append({

                "zone":
                    zone,

                "visits":
                    visits,

                "avg_dwell_ms":
                    int(dwell or 0),

                "normalized_score":
                    score
            })

        return output