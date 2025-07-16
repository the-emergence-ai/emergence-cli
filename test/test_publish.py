import subprocess, sys, shutil, json, os, pytest, pathlib

docker = shutil.which("docker")
skip = docker is None or not subprocess.run(["docker", "ps"], capture_output=True).returncode == 0

@pytest.mark.skipif(skip, reason="Docker/daemon missing in CI")
def test_publish_local(tmp_path):
    proj = tmp_path / "pusher"
    subprocess.run([sys.executable, "-m", "emergence_cli", "init", str(proj)], check=True)
    subprocess.run([sys.executable, "-m", "emergence_cli", "build", str(proj)], check=True)
    # ensure local registry up (fire and forget)
    subprocess.run(
        ["docker", "run", "-d", "-p", "5000:5000", "--name", "test-reg", "registry:2"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    try:
        subprocess.run([sys.executable, "-m", "emergence_cli", "publish", "--local", str(proj)], check=True)
    finally:
        subprocess.run(["docker", "rm", "-f", "test-reg"], stdout=subprocess.DEVNULL)
