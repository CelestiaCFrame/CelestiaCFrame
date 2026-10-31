from datetime import date
from pathlib import Path

START_DATES = {
    "python": date(2019, 1, 1),
    "lua": date(2021, 1, 1),
    "web": date(2025, 1, 1),
}

def years_of_experience(start_date):
    today = date.today()

    years = today.year - start_date.year

    if (today.month, today.day) < (
        start_date.month, start_date.day
    ):
        years -= 1

    return max(0, years)


readme = Path("README.md")
content = readme.read_text(encoding="utf-8")

content = content.replace(
    "{{PYTHON_YEARS}}",
    str(years_of_experience(START_DATES["python"]))
)

content = content.replace(
    "{{LUA_YEARS}}",
    str(years_of_experience(START_DATES["lua"]))
)

content = content.replace(
    "{{WEB_YEARS}}",
    str(years_of_experience(START_DATES["web"]))
)

readme.write_text(content, encoding="utf-8")
