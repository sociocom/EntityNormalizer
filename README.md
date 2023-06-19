# Entity Normalizer

Python tool for normalizing entities based on a dictionary.

## Usage

This tool can be used as:
- a *command line tool*, by cloning this repository and running `pip install .` under the root of this source; 
then you can run`main.py` with the required parameters to process your entity-listed file.
- a *Python package* , by installing the package using `pip install EntityNormalizer`

### Input and output
  
The input file must contain one entity per line. 
The output file will contain the normalized entities, again, one per line.  
The dictionary file must be a comma-separated table file, i.e., `csv`.

If the entity does not produce any match in the dictionary, it will be normalized to `[NO_MATCH]`. 
If the entity is found in the dictionary but the normalization is empty, it will be normalized to `[NO_NORM_FOUND]`.  
  
----
  
### Command line usage

`python main.py input output dictionary source target [--matching_threshold MATCHING_THRESHOLD] [--index]`

#### Parameters

- `input`: Input file path [Required]
- `output`: Output file path [Required]
- `dictionary`: Normalization dictionary file path [Required]
- `source`: Surface form column from dictionary [Required]
- `target`: Normalization column from dictionary [Required]
- `matching_threshold`: Threshold of string similarity for the normalization to be accepted (default: 50) [Optional]
- `index`: Use column indexes instead of names [Optional]
  
#### Example

- With column names:  

    `python main.py data/input.txt data/output.txt data/dictionary.csv surface_form_col normalization_col --matching_threshold 50`
- With integer column indexes:

    `python main.py data/input.txt data/output.txt data/dictionary.csv --index source 0 target 2 --matching_threshold 80`

---

 ### Python package usage
After installation,  the `normalized` function can be invoked with the dicitonary and a `list` of entities to produce a `list` of normalized entities.

#### Example
```python
from EntityNormalizer import EntityDictionary, normalize

entities = ['entity1', 'entity2', 'entity3']

normalization_dictionary = EntityDictionary('data/dictionary.csv', 'surface_forms', 'normalizations')
normalized = normalize(entities, normalization_dictionary, matching_threshold=70)

print(normalized)
```

## Bundled dictionaries

This library comes with a set of bundled dictionaries, which can be found under the `resources` folder:

- MedDic-CANCER-ADE-JA
- MedDic-CANCER-DRUG-JA

These are a set of Japanese medical dictionaries developed with normalization of concepts normally found during the
analysis of adverse events caused by anticancer drugs. Please refer to 
[this page](https://sociocom.naist.jp/meddic-cancer-ja/) for mor information.

There are convenience classes for loading these dictionaries, which can be accessed with the `Dictionaries` module:

```python
from EntityNormalizer import Dictionaries

# Load the dictionaries
cancer_ade = Dictionaries.MedDicCancerADE()
cancer_drug = Dictionaries.MedDicCancerDrug()
```

Both dictionaries use the columns `出現形` (Surface form) and `[細分類]` (Sub-classification) as source and target
columns, respectively. 

This can be altered by passing the referring parameter when creating the dictionary:

```python
from EntityNormalizer import Dictionaries

cancer_ade = Dictionaries.MedDicCancerADE(source_column='customColumn', target_column='customColumn2')
```
