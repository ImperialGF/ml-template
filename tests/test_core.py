import tempfile
from src.mltemplate.core import summarize_csv

def test_summarize_csv_basic():
    content = "a,b,c\n1,2,3\n4,5,6\n"
    with tempfile.NamedTemporaryFile("w+", suffix=".csv", delete=False, encoding="utf-8") as tmp:
        tmp.write(content)
        tmp.flush()
        summary = summarize_csv(tmp.name)
        assert summary["rows"] == 3
        assert summary["cols"] == 3
        assert summary["columns"] == ["a", "b", "c"]
