import json
from os import walk
from pathlib import Path
from sys import argv
from tempfile import TemporaryDirectory

import memory
import speed
from build import build

data = []
tmpd = TemporaryDirectory()
substr = ""

prgd = Path(".").absolute()  # Make sure the paths stay absolute
langd = prgd.joinpath("lang")
config = prgd.joinpath("config")

if len(argv) == 2:
    substr = argv[1]


def run_bench(fpath, setup):  # Run a benchmark with a path and setup, over all language implementations
    setname = setup["name"]
    values = []

    for file in sorted(fpath.iterdir()):
        ok, err = build(setup, str(file), tmpd.name)

        if ok:
            print(f"Running sample `{file.name}` ({setname})")

            values.append({
                "name": file.stem,
                "speed": speed.bench(setup, tmpd.name),
                "memory": memory.bench(setup, tmpd.name)
            })
        else:
            print(f"Failed to build `{file.name}` ({setname})\n{err}")

    data.append({
        "name": setname,
        "values": values
    })


for lang in config.iterdir():  # Iterate over all implementation configurations
    configs = json.load(lang.open("r"))

    for lconf in configs:
        setname = lconf["name"]

        if substr in setname:
            run_bench(langd.joinpath(lconf["folder"]), lconf)

# Generate the JSON data file
fp = open(prgd.joinpath("site", "data.json"), "w")
fp.write(json.dumps(data))
fp.close()
