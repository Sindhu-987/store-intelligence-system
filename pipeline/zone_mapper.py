import json


class ZoneMapper:

    def __init__(self, layout_file):

        with open(layout_file, "r") as f:
            self.layout = json.load(f)

    def point_in_polygon(self, point, polygon):

        x, y = point

        inside = False

        n = len(polygon)

        p1x, p1y = polygon[0]

        for i in range(n + 1):

            p2x, p2y = polygon[i % n]

            if y > min(p1y, p2y):

                if y <= max(p1y, p2y):

                    if x <= max(p1x, p2x):

                        if p1y != p2y:

                            xinters = (
                                y - p1y
                            ) * (
                                p2x - p1x
                            ) / (
                                p2y - p1y
                            ) + p1x

                        if p1x == p2x or x <= xinters:
                            inside = not inside

            p1x, p1y = p2x, p2y

        return inside

    def get_zone(self, bbox):

        x1, y1, x2, y2 = bbox

        center = (
            (x1 + x2) // 2,
            (y1 + y2) // 2
        )

        for zone in self.layout["zones"]:

            if self.point_in_polygon(
                center,
                zone["polygon"]
            ):
                return zone["zone_id"]

        return None