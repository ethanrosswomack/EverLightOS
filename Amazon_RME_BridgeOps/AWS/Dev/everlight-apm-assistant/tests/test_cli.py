import subprocess, sys, json, os, tempfile, pathlib

def run(*args):
    return subprocess.run([sys.executable, "-m", "everlight_apm_assistant.cli", *args], capture_output=True, text=True)

def test_cli_new_and_render():
    r = run("new","--date","2025-09-23","--site","TPA4")
    assert r.returncode == 0
    r2 = run("add","--equip","Drive-1","--preset","fiducial_replace")
    assert r2.returncode == 0
    r3 = run("render")
    assert "fiducial" in r3.stdout
    assert "replaced" in r3.stdout
    assert "restored" in r3.stdout
    assert "Verified alignment" in r3.stdout

def test_cli_preset_override():
    r = run("new","--date","2025-09-23","--site","TPA4")
    assert r.returncode == 0
    # Override action only
    r2 = run("add","--equip","Drive-2","--preset","fiducial_replace","--action","inspected")
    assert r2.returncode == 0
    r3 = run("render")
    out = r3.stdout
    assert "fiducial" in out
    assert "inspected" in out
    assert "restored" not in out  # action override
    assert "Verified alignment" in out