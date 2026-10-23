# Operating Systems Resources

Educational materials, practical programs, and algorithm demonstrations for the Operating Systems course.

## 1. Page Replacement Algorithms

The `page_replacement.py` program implements three page replacement algorithms used in virtual memory management.

| Algorithm | Description |
|---|---|
| FIFO | Replaces the page that entered memory first |
| LRU | Replaces the page that has not been used for the longest time |
| Optimal | Replaces the page whose next use is farthest in the future |

## 2. Requirements

- Python 3.8 or later
- No external libraries required

## 3. How to Run

Clone or download this repository, open a terminal in the project folder, and run:

```bash
python Operating-Systems/page_replacement.py
```

On some systems, use `python3` instead of `python`.

## 4. Sample Input

The program uses the following reference string:

```text
7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2
```

Number of available frames: `3`

## 5. Expected Results

For the reference string and frame capacity above:

| Algorithm | Total page faults |
|---|---:|
| FIFO | 10 |
| LRU | 9 |
| Optimal | 7 |

The Optimal algorithm produces the fewest page faults for this particular reference string because it uses knowledge of future page references.

## 6. Learning Outcomes

After running this program, students should be able to:

- Explain how page replacement works
- Trace the contents of memory frames
- Count page faults
- Compare FIFO, LRU, and Optimal
- Understand why reference patterns affect performance

## 7. Further Exercises

1. Change the number of frames and compare the results.
2. Enter a different page reference string.
3. Create a comparison table for multiple inputs.
4. Investigate Belady's anomaly using FIFO.
5. Extend the program with a graphical visualization.

## Author

Dr. Gokulakrishnan S  
Computer Science and Engineering

*For educational use.*
