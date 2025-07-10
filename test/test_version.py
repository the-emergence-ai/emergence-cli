import subprocess, sys

def test_version():
    result = subprocess.run(
        [sys.executable, "-m", "emergence_cli", "--version"],
        capture_output=True,
        text=True,
    )
    assert "0.1.0" in result.stdout