import numpy as np
from itertools import combinations

class Apriori:
    def __init__(self, min_support: float = 0, min_confidence: float = 0):
        # parameters
        self.min_supprot = min_support
        self.min_confidence = min_confidence

        # interim structure
        self.k_frequent_sets_list = []  # {Items_n: Times}
        self.one_frequent_sets = {}
        self.current_data = None

        # data
        self.orig_data = None
        self.data_lens = None

    def train(self, data: np.ndarray):
        self.orig_data = data
        self.data_lens = data.shape[0]
        initialization_dict = {(x,): None for x in range(data.shape[1])}
        self.k_frequent_sets_list.append(initialization_dict)
        self._get_k_frequent_set(1)

    def _get_k_frequent_set(self, k: int)->None:
        if k == self.orig_data.shape[1]:
            return
        self.k_frequent_sets_list.append(dict())
        if k == 1:
            tuples_set = self.k_frequent_sets_list[k-1]
        else:
            tuples_set = self._get_k_tuples_set(k)

        for each_tuple in tuples_set:
            n = self._search_tuples_nums_in_matrix(each_tuple)
            if n / self.data_lens >= self.min_supprot:
                self.k_frequent_sets_list[k][each_tuple] = n

        if len(self.k_frequent_sets_list[k]) > 1:
            self._get_k_frequent_set(k+1)

    def _get_k_tuples_set(self, k: int)->set:
        tuples = list(self.k_frequent_sets_list[k-1].keys())
        combination_tuples_list = []

        for i1 in range(len(tuples)):   # combination
            for i2 in range(i1+1, len(tuples)):
                if len(set(tuples[i1] + tuples[i2])) == k:
                    combination_tuples_list.append(tuple(set(tuples[i1] + tuples[i2])))

        for each_tuple in combination_tuples_list:  # filtering
            for each_prior_tuple in [self.k_frequent_sets_list[k-1].keys()]:
                if len(set(each_prior_tuple) - set(each_tuple)) != 0:
                    combination_tuples_list.remove(each_tuple)

        return set(combination_tuples_list)

    def _search_tuples_nums_in_matrix(self, indexs: tuple)->int:
        q = np.zeros(self.orig_data.shape[1])

        for i in indexs:
            q[i] = 1

        a = np.sum(self.orig_data * q)

        return len(np.where(a == 3)[0])





