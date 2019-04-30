from subprocess import DEVNULL, PIPE, Popen, TimeoutExpired


def bench(setup, tmpd):
    total = None
    proc = Popen(["/usr/bin/time -f s%U " + setup["run"]],
                 stderr=PIPE, stdout=DEVNULL, cwd=tmpd, shell=True)

    try:
        _, stderr = proc.communicate(timeout=120)
        index = stderr.rindex(b"s")  # Ugly but works
        total = float(stderr.decode()[index + 1:-1])
    except TimeoutExpired:
        pass

    return total
