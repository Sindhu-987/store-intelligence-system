class EntryExitDetector:

    def __init__(self, line_x=500):

        self.line_x = line_x
        self.last_positions = {}

    def update(self, visitor_id, bbox):

        x1, y1, x2, y2 = bbox

        center_x = (x1 + x2) // 2

        if visitor_id not in self.last_positions:
            self.last_positions[visitor_id] = center_x
            return None

        previous_x = self.last_positions[visitor_id]

        self.last_positions[visitor_id] = center_x

        if previous_x < self.line_x and center_x >= self.line_x:
            return "ENTRY"

        if previous_x > self.line_x and center_x <= self.line_x:
            return "EXIT"

        return None