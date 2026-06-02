class StoreAnalytics:

    @staticmethod
    def conversion_rate(
        visitors,
        purchasers
    ):

        if visitors == 0:
            return 0

        return round(
            purchasers
            /
            visitors
            *
            100,
            2
        )

    @staticmethod
    def abandonment_rate(
        queue_entries,
        purchases
    ):

        if queue_entries == 0:
            return 0

        abandoned = (
            queue_entries
            -
            purchases
        )

        return round(
            abandoned
            /
            queue_entries
            *
            100,
            2
        )