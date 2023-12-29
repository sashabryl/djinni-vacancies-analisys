DJINNI_URL = "https://djinni.co/jobs/keyword-python/"

COLUMNS = [
    "pandas",
    "sql",
    "machine_learning",
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
    "excel"
]


class Vacancy:
    def __init__(self, text: str) -> None:
        for column in COLUMNS:
            self.__setattr__(column, 1 if column in text else 0)

    def __str__(self) -> str:
        return " ".join(self.__getattribute__(attr) for attr in COLUMNS)
