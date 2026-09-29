from collections import deque
from typing import List


def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
    def is_one_char_diff(s1: str, s2: str) -> bool:
        diff = 0
        for i in range(len(s1)):
            diff += 1 if s1[i] != s2[i] else 0
        return diff == 1

    # bfs to get min #mutations to get end gene
    q = deque([startGene])
    visited = set([startGene])
    steps = 0
    while q:
        for _ in range(len(q)):
            cur_gene = q.popleft()
            if cur_gene == endGene:
                return steps
            for gene in bank:
                if gene in visited:
                    continue
                if is_one_char_diff(cur_gene, gene):
                    q.append(gene)
                    visited.add(gene)
        steps += 1
    return -1
