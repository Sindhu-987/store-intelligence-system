import supervision as sv
import numpy as np


class VisitorTracker:

    def __init__(self):

        self.tracker = sv.ByteTrack()

    def update(self, detections):

        if len(detections) == 0:
            return []

        xyxy = np.array([
            d["bbox"]
            for d in detections
        ])

        confidence = np.array([
            d["confidence"]
            for d in detections
        ])

        class_id = np.zeros(len(detections))

        supervision_detections = sv.Detections(
            xyxy=xyxy,
            confidence=confidence,
            class_id=class_id
        )

        tracked = self.tracker.update_with_detections(
            supervision_detections
        )

        tracked_objects = []

        for i in range(len(tracked.xyxy)):

            tracked_objects.append({
                "track_id": int(tracked.tracker_id[i]),
                "bbox": tracked.xyxy[i].tolist(),
                "confidence": float(tracked.confidence[i])
            })

        return tracked_objects