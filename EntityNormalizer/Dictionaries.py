import os

from EntityNormalizer import EntityDictionary


class MedDicCancerADE(EntityDictionary):

    def __init__(self, source_column='出現形', target_column='[細分類]', index: bool = False):
        super().__init__(
            path=os.path.join(os.path.dirname(__file__), "resources/MedDic-CANCER-ADE-JA_202306.csv"),
            source_column=source_column,
            target_column=target_column,
            index=index,
        )


class MedDicCancerDrug(EntityDictionary):

    def __init__(self, source_column='出現形', target_column='[細分類]', index: bool = False):
        super().__init__(
            path=os.path.join(os.path.dirname(__file__), "resources/MedDic-CANCER-DRUG-JA_202306.csv"),
            source_column=source_column,
            target_column=target_column,
            index=index,
        )