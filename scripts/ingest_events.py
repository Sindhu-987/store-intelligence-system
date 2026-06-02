import json
import requests

API_URL = "http://127.0.0.1:8000/events/ingest"

EVENT_FILE = "events.jsonl"


def main():

    events = []

    with open(
        EVENT_FILE,
        "r"
    ) as f:

        for line in f:

            line = line.strip()

            if not line:
                continue

            events.append(
                json.loads(line)
            )

    print(
        f"Loaded {len(events)} events"
    )

    payload = {
        "events": events
    }

    response = requests.post(
        API_URL,
        json=payload
    )

    print(
        response.status_code
    )

    print(
        response.text
    )


if __name__ == "__main__":

    main()