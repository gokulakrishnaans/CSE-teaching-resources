
def fifo(pages, capacity):
    frames = []
    next_to_replace = 0
    faults = 0

    for page in pages:
        if page not in frames:
            faults += 1
            if len(frames) < capacity:
                frames.append(page)
            else:
                frames[next_to_replace] = page
                next_to_replace = (next_to_replace + 1) % capacity

        print(f"Page {page}: {frames}")

    return faults


def lru(pages, capacity):
    frames = []
    last_used = {}
    faults = 0

    for time, page in enumerate(pages):
        if page not in frames:
            faults += 1
            if len(frames) < capacity:
                frames.append(page)
            else:
                victim = min(frames, key=lambda p: last_used[p])
                frames[frames.index(victim)] = page

        last_used[page] = time
        print(f"Page {page}: {frames}")

    return faults


def optimal(pages, capacity):
    frames = []
    faults = 0

    for i, page in enumerate(pages):
        if page not in frames:
            faults += 1
            if len(frames) < capacity:
                frames.append(page)
            else:
                future = pages[i + 1:]
                next_use = {
                    p: future.index(p) if p in future else float("inf")
                    for p in frames
                }
                victim = max(frames, key=lambda p: next_use[p])
                frames[frames.index(victim)] = page

        print(f"Page {page}: {frames}")

    return faults


if __name__ == "__main__":
    reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    frame_capacity = 3

    if frame_capacity <= 0:
        raise ValueError("Frame capacity must be positive")

    for name, algorithm in [
        ("FIFO", fifo),
        ("LRU", lru),
        ("Optimal", optimal),
    ]:
        print(f"\n{name} Page Replacement")
        faults = algorithm(reference_string, frame_capacity)
        print(f"Total page faults: {faults}")
