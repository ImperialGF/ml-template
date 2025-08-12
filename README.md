# ml-template

Шаблон ML-проекта: форматирование, линт, тесты, CI.

## Быстрый старт
```bash
python -m venv .venv && source .venv/bin/activate
pip install --upgrade pip
pip install pytest pre-commit black ruff
pre-commit install
pytest
