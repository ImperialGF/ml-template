import json
import os
import subprocess
import sys
import tempfile


def test_cli_summarize():
    content = "x,y\n1,2\n"
    with tempfile.NamedTemporaryFile("w+", suffix=".csv", delete=False, encoding="utf-8") as tmp:
        tmp.write(content)
        tmp.flush()
        result = subprocess.run(
            [sys.executable, "-m", "src.mltemplate.cli", tmp.name],
            capture_output=True,
            text=True,
            check=True,
        )
        data = json.loads(result.stdout)
        assert data["cols"] == 2 and data["rows"] == 2
        os.unlink(tmp.name)
