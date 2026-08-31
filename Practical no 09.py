print("S113 Dhani Singh")

def fifo_page_replacement(pages, frames):
    memory = []
    hits = 0
    misses = 0
    pointer = 0

    for page in pages:
        if page in memory:
            hits += 1
        else:
            misses += 1

            if len(memory) < frames:
                memory.append(page)
            else:
                memory[pointer] = page
                pointer = (pointer + 1) % frames

    hit_ratio = hits / len(pages)
    miss_ratio = misses / len(pages)

    return hits, misses, hit_ratio, miss_ratio


def lru_page_replacement(pages, frames):
    memory = []
    recent = []
    hits = 0
    misses = 0

    for page in pages:
        if page in memory:
            hits += 1
            recent.remove(page)
            recent.append(page)
        else:
            misses += 1

            if len(memory) < frames:
                memory.append(page)
            else:
                lru_page = recent.pop(0)
                memory[memory.index(lru_page)] = page

            recent.append(page)

    hit_ratio = hits / len(pages)
    miss_ratio = misses / len(pages)

    return hits, misses, hit_ratio, miss_ratio


pages = list(map(int, input("Enter page reference string: ").split()))
frames = int(input("Enter number of frames: "))

fifo_hits, fifo_misses, fifo_hit_ratio, fifo_miss_ratio = fifo_page_replacement(
    pages, frames
)

lru_hits, lru_misses, lru_hit_ratio, lru_miss_ratio = lru_page_replacement(
    pages, frames
)

print("\nFIFO Page Replacement")
print("Hits:", fifo_hits)
print("Misses:", fifo_misses)
print("Hit Ratio:", round(fifo_hit_ratio, 2))
print("Miss Ratio:", round(fifo_miss_ratio, 2))

print("\nLRU Page Replacement")
print("Hits:", lru_hits)
print("Misses:", lru_misses)
print("Hit Ratio:", round(lru_hit_ratio, 2))
print("Miss Ratio:", round(lru_miss_ratio, 2))
