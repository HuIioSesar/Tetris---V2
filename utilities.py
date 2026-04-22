import json
import os
from datetime import datetime

class Blinker:
    def __init__(self, fps, period_seconds=0.5):
        self.fps = fps
        self.period_frames = max(1, int(fps * period_seconds))
        self.timer = 0
        self.state = True

    def update(self):
        self.timer += 1
        if self.timer >= self.period_frames:
            self.state = not self.state
            self.timer = 0
        return self.state


class ScoreManager:
    SCORES_FILE = os.path.join(os.path.dirname(__file__), "scores.json")

    @classmethod
    def _load_raw_scores(cls):
        if os.path.exists(cls.SCORES_FILE):
            try:
                with open(cls.SCORES_FILE, "r", encoding="utf-8") as f:
                    data = json.load(f)
            except (json.JSONDecodeError, OSError):
                data = []
        else:
            data = []

        if not isinstance(data, list):
            data = []

        return data

    @classmethod
    def _save_raw_scores(cls, scores_list):
        with open(cls.SCORES_FILE, "w", encoding="utf-8") as f:
            json.dump(scores_list, f, indent=2)

    @classmethod
    def save_score(cls, score: int, name: str, mode: str) -> int | None:
        scores = cls._load_raw_scores()

        date_string = datetime.now().strftime("%d-%m-%Y")

        new_entry = {
            "score": int(score),
            "name": name,
            "mode": mode,
            "date": date_string,
        }

        scores.append(new_entry)
        scores.sort(key=lambda entry: entry.get("score", 0), reverse=True)
        top_three = scores[:3]
        cls._save_raw_scores(top_three)

        rank: int | None = None
        for idx, entry in enumerate(top_three):
            if (entry.get("score") == new_entry["score"]
                and entry.get("name") == new_entry["name"]
                and entry.get("mode") == new_entry["mode"]
                and entry.get("date") == new_entry["date"]  ):
                rank = idx
                break

        return rank

    @classmethod
    def update_name(cls, rank: int, name: str) -> None:
        scores = cls._load_raw_scores()

        if 0 <= rank < len(scores):
            scores[rank]["name"] = name

            cls._save_raw_scores(scores)

    @classmethod
    def load_top_scores(cls, mode: str | None = None, limit: int = 3):
        data = cls._load_raw_scores()

        if not data:
            return [("", None)] * limit

        # Filter by mode if requested
        if mode is not None:
            filtered = [entry for entry in data if entry.get("mode") == mode]
            entries = filtered if filtered else data
        else:
            entries = data

        highscores = []
        for entry in entries[:limit]:
            name = str(entry.get("name")) if entry.get("name") is not None else ""
            raw_score = entry.get("score")

            if raw_score in (None, ""):
                highscores.append((name, None))
            else:
                highscores.append((name, int(raw_score)))

        # Make sure we always return exactly `limit` entries
        while len(highscores) < limit:
            highscores.append(("", None))

        return highscores