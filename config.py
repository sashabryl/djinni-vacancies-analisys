class Vacancy:
    def __init__(self, text: str) -> None:
        self.pandas = "pandas" in text
        self.sql = "sql" in text
        self.machine_learning = "machine_learning" in text
        self.django = "django" in text
        self.fastapi = "fastapi" in text
        self.flask = "flask" in text
        self.rest = "rest" in text
        self.html = "html" in text
        self.css = "css" in text
        self.javascript = "javascript" in text
        self.docker = "docker" in text
        self.postgres = "postgres" in text
