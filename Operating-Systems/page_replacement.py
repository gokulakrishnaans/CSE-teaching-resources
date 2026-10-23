
def fifo(pages, capacity):
    frames = []
    next_to_replace = 0
    faults = 0
    history = []

    for page in pages:
        if page in frames:
            result = "HIT"
        else:
            faults += 1
            result = "FAULT"

            if len(frames) < capacity:
                frames.append(page)
            else:
                frames[next_to_replace] = page
                next_to_replace = (next_to_replace + 1) % capacity

        history.append((page, frames.copy(), result))

    return faults, history


def lru(pages, capacity):
    frames = []
    last_used = {}
    faults = 0
    history = []

    for time, page in enumerate(pages):
        if page in frames:
            result = "HIT"
        else:
            faults += 1
            result = "FAULT"

            if len(frames) < capacity:
                frames.append(page)
            else:
                victim = min(frames, key=lambda p: last_used[p])
                frames[frames.index(victim)] = page

        last_used[page] = time
        history.append((page, frames.copy(), result))

    return faults, history


def optimal(pages, capacity):
    frames = []
    faults = 0
    history = []

    for i, page in enumerate(pages):
        if page in frames:
            result = "HIT"
        else:
            faults += 1
            result = "FAULT"

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

        history.append((page, frames.copy(), result))

    return faults, history


def display_results(name, pages, capacity, algorithm):
    faults, history = algorithm(pages, capacity)
    hits = len(pages) - faults

    print(f"\n{'=' * 55}")
    print(f"{name} PAGE REPLACEMENT")
    print(f"{'=' * 55}")
    print(f"{'Page':<8}{'Frames':<25}{'Result':<10}")
    print("-" * 45)

    for page, frames, result in history:
        frame_display = str(frames)
        print(f"{page:<8}{frame_display:<25}{result:<10}")

    print("-" * 45)
    print(f"Total references : {len(pages)}")
    print(f"Page faults      : {faults}")
    print(f"Page hits        : {hits}")
    print(f"Frame capacity   : {capacity}")

    return faults, hits


def main():
    reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    frame_capacity = 3

    if not reference_string:
        raise ValueError("Reference string cannot be empty.")

    if frame_capacity <= 0:
        raise ValueError("Frame capacity must be positive.")

    if any(not isinstance(p, int) or isinstance(p, bool)
           for p in reference_string):
        raise ValueError("Page references must be integers.")

    algorithms = [
        ("FIFO", fifo),
        ("LRU", lru),
        ("Optimal", optimal),
    ]

    summary = []

    for name, algorithm in algorithms:
        faults, hits = display_results(
            name, reference_string, frame_capacity, algorithm
        )
        summary.append((name, faults, hits))

    print(f"\n{'=' * 45}")
    print("FINAL COMPARISON")
    print(f"{'=' * 45}")
    print(f"{'Algorithm':<15}{'Faults':<10}{'Hits':<10}")
    print("-" * 35)

    for name, faults, hits in summary:
        print(f"{name:<15}{faults:<10}{hits:<10}")

    best = min(summary, key=lambda item: item[1])
    print(f"\nFewest page faults: {best[0]} ({best[1]} faults)")


if __name__ == "__main__":
    main()
