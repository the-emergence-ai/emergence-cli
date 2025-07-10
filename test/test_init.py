import subprocess, sys, pathlib, shutil, json, os

def test_init_succeeds(tmp_path):
    agent_dir = tmp_path / "myagent"
    subprocess.run(
        [sys.executable, "-m", "emergence_cli", "init", str(agent_dir)],
        check=True,
    )
    assert (agent_dir / "agent.py").exists()

    # quick functional sanity: pipe a HELP msg and expect DONE
    help_msg = {
        "id": "1",
        "from": "tester",
        "to": "myagent",
        "verb": "HELP",
        "data": {"prompt": "ping"}
    }
    result = subprocess.run(
        [sys.executable, str(agent_dir / "agent.py")],
        input=json.dumps(help_msg),
        text=True,
        capture_output=True,
        check=True,
    )
    assert '"verb": "DONE"' in result.stdout
