from contextlib import contextmanager
import time
@contextmanager
def trace_span(name, **attributes):
    started=time.perf_counter()
    try: yield
    finally: print(f"[trace] {name}: {time.perf_counter()-started:.3f}s")
