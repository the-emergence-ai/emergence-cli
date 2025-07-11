import os, sys, subprocess, shutil, json, pathlib, pytest

docker_available = shutil.which("docker") is not None

@pytest.mark.skipif(not docker_available, reason="Docker not available in test env")
def test_build(tmp_path):
    # 1) scaffold an agent
    proj = tmp_path / "buildme"
    subprocess.run(
        [sys.executable, "-m", "emergence_cli", "init", str(proj)],
        check=True,
    )
    # 2) build the image
    result = subprocess.run(
        [sys.executable, "-m", "emergence_cli", "build", str(proj)],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "Image built" in result.stdout
