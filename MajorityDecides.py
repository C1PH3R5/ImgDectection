import numpy as np
from collections import Counter
class MajorityDecides:
    def mostCommon(self, top_left_array):
      counts = Counter(map(tuple, top_left_array))
      return counts.most_common(1)[0][0]
