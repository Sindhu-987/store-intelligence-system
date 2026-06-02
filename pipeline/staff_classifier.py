from collections import defaultdict


class StaffClassifier:

    def __init__(self):

        self.staff_scores = defaultdict(int)

    def update(
        self,
        visitor_id,
        camera_id
    ):

        if camera_id in [
            "CAM4",
            "CAM5"
        ]:

            self.staff_scores[
                visitor_id
            ] += 1

    def is_staff(
        self,
        visitor_id
    ):

        return (
            self.staff_scores[
                visitor_id
            ] >= 5
        )