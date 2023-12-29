DJINNI_URL = "https://djinni.co/jobs/keyword-python/"
DJINNI_URL_JUNIOR = "https://djinni.co/jobs/?primary_keyword=Python&exp_rank=junior"
DJINNI_URL_MIDDLE = "https://djinni.co/jobs/?primary_keyword=Python&exp_rank=middle"
DJINNI_URL_SENIOR = "https://djinni.co/jobs/?primary_keyword=Python&exp_rank=senior"
DJINNI_URL_TEAM_LEAD = "https://djinni.co/jobs/?primary_keyword=Python&exp_rank=team_lead"



COLUMNS = [
    "pandas",
    "sql",
    "machine_learning",
    "artificial_intelligence",
    "django",
    "fastapi",
    "flask",
    "rest",
    "html",
    "css",
    "javascript",
    "docker",
    "postgres",
    "linux",
    "tableau",
    "react",
    "excel",
]


class Vacancy:
    def __init__(self, text: str) -> None:
        for column in COLUMNS:
            self.__setattr__(column, 1 if column.replace("_", " ") in text else 0)

    def __str__(self) -> str:
        return " ".join(self.__getattribute__(attr) for attr in COLUMNS)
