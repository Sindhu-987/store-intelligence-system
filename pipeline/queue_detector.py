class QueueDetector:

    def __init__(
        self,
        threshold=2
    ):

        self.threshold = threshold

    def queue_depth(
        self,
        billing_visitors
    ):

        return len(
            billing_visitors
        )

    def queue_exists(
        self,
        billing_visitors
    ):

        return (
            len(
                billing_visitors
            )
            >=
            self.threshold
        )