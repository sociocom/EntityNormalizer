# Entity Normalizer

Python tool for normalizing entities based on a dictionary.

## Usage
This tool can be used as:
-  a *command line tool*, by cloning this repository and running `main.py` with the required parameters.
- a *Python package* , by installing the package using `pip install git+https://github.com/gabrielandrade2/EntityNormalizer.git`

### Input and output
  
The input file must contain one entity per line. 
The output file will contain the normalized entities, again, one per line.  
The dicitory file must be an *Excel-like* table file, such as `xls`, `csv` and such.

If the entity does not produce any match in the dictionary, it will be normalized to [NO_MATCH]. 
If the entity is found in the dictionary but the normalization is empty, it will be normalized to [NO_NORM_FOUND].  
  
----
  
### Command line usage
`python main.py input output dictionary source target [--matching_threshold MATCHING_THRESHOLD] [--index]`

#### Parameters
`input`: Input file path [Required]
`output`: Output file path [Required]
`dictionary`: Normalization dictionary file path [Required]
`source`: Surface form column from dictionary [Required]
`target`: Normalization column from dictionary [Required]
`matching_threshold`: Threshold of string similarity for the normalization to be accepted (default: 50) [Optional]
`index`: Use column indexes instead of names [Optional]
  
#### Example
- With column names:  
`python main.py data/input.txt data/output.txt data/dictionary.csv surface_form_col normalization_col --matching_threshold 50`
  
- With integer column indexes: 
`python main.py data/input.txt data/output.txt data/dictionary.csv --index source 0 target 2 --matching_threshold 80`

---

 ### Python package usage
After instalation,  the `normalized` function can be invoked with the dicitonary and a `list` of entities to produce a `list` of normalized entities.

#### Example
```python
from EntityNormalizer import EntityDictionary, normalize

entities  =  [entity1, entity2, entity3]

normalization_dictionary  = EntityDictionary('data/dictionary.csv',  'surface_forms',  'normalizations')
normalized  = normalize(entities,  normalization_dictionary,  matching_threshold=70)

print(normalized)
```
