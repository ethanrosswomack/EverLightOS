import subprocess, sys, json, os, tempfile, pathlib

def run(*args):
    return subprocess.run([sys.executable, "-m", "everlight_apm_assistant.cli", *args], capture_output=True, text=True)

def test_cli_new_and_render():
    r = run("new","--date","2025-09-23","--site","TPA4")
    assert r.returncode == 0
    r2 = run("add","--equip","Drive-1","--comp","fiducial","--action","replaced","--result","restored")
    assert r2.returncode == 0
    r3 = run("render")
    assert "Drive-1" in r3.stdout
