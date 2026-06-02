import cv2
import json

from pipeline.detect import PersonDetector
from pipeline.tracker import VisitorTracker

from pipeline.staff_classifier import (
    StaffClassifier
)

from pipeline.entry_exit_detector import (
    EntryExitDetector
)

from pipeline.event_generator import (
    EventGenerator
)

from pipeline.session_manager import (
    SessionManager
)

from pipeline.reentry_detector import (
    ReentryDetector
)

from pipeline.config import *


def process_video(
    video_path,
    camera_id
):

    detector = PersonDetector()

    tracker = VisitorTracker()

    event_generator = EventGenerator()

    session_manager = (
        SessionManager()
    )

    reentry_detector = (
        ReentryDetector()
    )

    entry_detector = (
        EntryExitDetector()
    )

    staff_classifier = (
        StaffClassifier()
    )

    cap = cv2.VideoCapture(
        video_path
    )

    generated_events = []

    frame_count = 0

    processed_frames = 0

    while True:

        success, frame = cap.read()

        if not success:
            break

        frame_count += 1

        if frame_count % 30 != 0:
            continue

        processed_frames += 1

        if processed_frames % 100 == 0:

            print(
                f"{camera_id}: processed {processed_frames}"
            )

        detections = detector.detect(
            frame
        )

        tracked_people = tracker.update(
            detections
        )

        for person in tracked_people:

            visitor_id = str(
                person["track_id"]
            )

            bbox = person["bbox"]

            staff_classifier.update(
                visitor_id,
                camera_id
            )

            is_staff = (
                staff_classifier.is_staff(
                    visitor_id
                )
            )

            # ENTRY CAMERA
            if camera_id == ENTRY_CAMERA:

                movement = (
                    entry_detector.update(
                        visitor_id,
                        bbox
                    )
                )

                if movement == "ENTRY":

                    if (
                        reentry_detector
                        .check_reentry(
                            visitor_id
                        )
                    ):

                        generated_events.append(

                            event_generator.reentry(

                                STORE_ID,

                                camera_id,

                                visitor_id
                            )
                        )

                    else:

                        generated_events.append(

                            event_generator.entry(

                                STORE_ID,

                                camera_id,

                                visitor_id
                            )
                        )

                    if not session_manager.exists(
                        visitor_id
                    ):

                        session_manager.start_session(
                            visitor_id
                        )

                elif movement == "EXIT":

                    generated_events.append(

                        event_generator.exit(

                            STORE_ID,

                            camera_id,

                            visitor_id
                        )
                    )

                    reentry_detector.register_exit(
                        visitor_id
                    )

                    session_manager.end_session(
                        visitor_id
                    )

            # CAM1 = SKINCARE

            if camera_id == "CAM1":

                generated_events.append(

                    event_generator.zone_enter(

                        STORE_ID,

                        camera_id,

                        visitor_id,

                        "SKINCARE"
                    )
                )

                generated_events.append(

                    event_generator.zone_dwell(

                        STORE_ID,

                        camera_id,

                        visitor_id,

                        "SKINCARE",

                        1000
                    )
                )

            # CAM2 = MAKEUP

            if camera_id == "CAM2":

                generated_events.append(

                    event_generator.zone_enter(

                        STORE_ID,

                        camera_id,

                        visitor_id,

                        "MAKEUP"
                    )
                )

                generated_events.append(

                    event_generator.zone_dwell(

                        STORE_ID,

                        camera_id,

                        visitor_id,

                        "MAKEUP",

                        1000
                    )
                )

            session_manager.touch(
                visitor_id
            )

    cap.release()

    print(
        f"{camera_id}: completed"
    )

    return generated_events


if __name__ == "__main__":

    videos = {

        "CAM1":
            "data/videos/CAM1.mp4",

        "CAM2":
            "data/videos/CAM2.mp4",

        "CAM3":
            "data/videos/CAM3.mp4",

        "CAM4":
            "data/videos/CAM4.mp4",

        "CAM5":
            "data/videos/CAM5.mp4"
    }

    all_events = []

    for camera_id, path in videos.items():

        print(
            f"Processing {camera_id}"
        )

        events = process_video(
            path,
            camera_id
        )

        all_events.extend(
            events
        )

    with open(
        OUTPUT_EVENTS_FILE,
        "w"
    ) as f:

        for event in all_events:

            f.write(
                json.dumps(event)
                + "\n"
            )

    print(
        f"Generated {len(all_events)} events"
    )