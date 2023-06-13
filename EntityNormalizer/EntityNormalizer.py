import mojimoji
import pandas as pd
from rapidfuzz import fuzz, process


class EntityDictionary:

    def __init__(self, path, source_column, target_column, index: bool = False):
        self.df = pd.read_csv(path)

        source_column = self.__parse_column(source_column, index)
        target_column = self.__parse_column(target_column, index)

        self.source_column = self.df.iloc[:, source_column].to_list()
        self.target_column = self.df.iloc[:, target_column].to_list()

    def __parse_column(self, column: str, index: bool) -> int:
        if index:
            return int(column)
        return self.df.columns.to_list().index(column)

    def get_candidates_list(self):
        return self.source_column

    def get_normalization_list(self):
        return self.target_column

    def get_normalized_term(self, term):
        return self.df[self.df.iloc[:, 0] == term].iloc[:, 2].item()


class EntityNormalizer:

    def __init__(self, database: EntityDictionary, matching_method=fuzz.ratio, matching_threshold=0):
        self.database = database
        self.matching_method = matching_method
        self.matching_threshold = matching_threshold
        self.candidates = [mojimoji.han_to_zen(x) for x in self.database.get_candidates_list()]

    def normalize(self, term):
        term = mojimoji.han_to_zen(term)
        preferred_candidate = process.extractOne(term, self.candidates, scorer=self.matching_method)
        score = preferred_candidate[1]

        if score > self.matching_threshold:
            ret = self.database.get_normalized_term(preferred_candidate[0])
            return ('[NO_NORM_FOUND]' if pd.isna(ret) else ret), score
        else:
            return '[NO_MATCH]', score


def normalize(entities: list, dictionary: EntityDictionary, matching_method=fuzz.ratio, matching_threshold=0):
    normalizer = EntityNormalizer(dictionary, matching_method, matching_threshold)
    normalized = []
    for entity in entities:
        normalization, score = normalizer.normalize(entity)
        normalized.append(str(normalization))
    return normalized
