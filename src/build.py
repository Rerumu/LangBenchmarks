from shlex import quote
from subprocess import DEVNULL, PIPE, Popen


def exec_bp(step, name, tmpd):
    args = [step.replace("{name}", quote(name))]
    proc = Popen(args, stderr=PIPE, stdout=DEVNULL, shell=True, cwd=tmpd)
    _, stderr = proc.communicate()

    return len(stderr) == 0, stderr.decode()


def build(setup, name, tmpd):
    ok = True

    if setup["build"]:
        ok, err = exec_bp(setup["build"], name, tmpd)

    return ok, err
