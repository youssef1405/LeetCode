# Solution 1
#--------------

def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
    sums = []
    for i,row in enumerate(mat):
        sums.append((sum(row), i))

    sorted_sums = sorted(sums)
    k_rows = sorted_sums[:k]
    k_weakest_rows = []
    for val in k_rows:
        k_weakest_rows.append(val[1])

    return k_weakest_rows


# Solution 2
#--------------