from subprocess import DEVNULL, PIPE, Popen, TimeoutExpired

heap_key = "mem_heap_B="  # Match these for heap memory usage


def memory_usage(ms_out):
    memory = 0

    for line in ms_out.splitlines():
        if line.startswith(heap_key):
            memory = max(memory, int(line[len(heap_key):]))

    return memory


def bench(setup, tmpd):
    total = None
    proc = Popen(["valgrind --tool=massif --massif-out-file=memory " + setup["run"]],
                 stderr=PIPE, stdout=DEVNULL, cwd=tmpd, shell=True)

    try:
        proc.communicate(timeout=120)
        proc = Popen(["cat", "memory"],
                     stderr=DEVNULL, stdout=PIPE, cwd=tmpd)

        total = memory_usage(proc.communicate()[0].decode())
    except TimeoutExpired:
        pass

    return total
