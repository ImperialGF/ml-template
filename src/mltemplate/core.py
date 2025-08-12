import csv
from pathlib import Path


def summarize_csv(path: str) -> dict:
    """
    Читает CSV и возвращает сводку:
    - количество строк (включая заголовок)
    - количество столбцов
    - имена столбцов
    """
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {p}")

    with p.open("r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

    if not rows:
        return {"rows": 0, "cols": 0, "columns": []}

    header = rows[0]
    return {"rows": len(rows), "cols": len(header), "columns": header}
