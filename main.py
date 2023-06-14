import argparse

from EntityNormalizer import EntityDictionary, normalize

"""
Command line tool for normalizing entities based on a dictionary.

The input file must contain one entity per line. The output file will contain the normalized entities, again, one per line.
If the entity does not produce any match in the dictionary, it will be normalized to [NO_MATCH]. If the entity is found 
in the dictionary but the normalization is empty, it will be normalized to [NO_NORM_FOUND].

Command line arguments:
    input: Input file path
    output: Output file path
    dictionary: Normalization dictionary file path
    source: Surface form column from dictionary
    target: Normalization column from dictionary
    matching_threshold: Threshold of string similarity for the normalization to be accepted (default: 50) (Optional)
    index: Use column indexes instead of names (Optional)

Example usage (with column names):
    python main.py data/input.txt data/output.txt data/dictionary.csv surface_form_col normalization_col --matching_threshold 50

Example usage (with integer column indexes):
    python main.py data/input.txt data/output.txt data/dictionary.csv --index source 0 target 2 --matching_threshold 80
        
"""

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""Command line tool for normalizing entities based on a dictionary.

The input file must contain one entity per line. The output file will contain the normalized entities, again, one per line.
If the entity does not produce any match in the dictionary, it will be normalized to [NO_MATCH]. If the entity is found in the dictionary but the normalization is empty, it will be normalized to [NO_NORM_FOUND].""",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("input", type=str, help="Input file path")
    parser.add_argument("output", type=str, help="Output file path")
    parser.add_argument(
        "dictionary", type=str, help="Normalization dictionary file path"
    )
    parser.add_argument("source", type=str, help="Surface form column from dictionary")
    parser.add_argument("target", type=str, help="Normalization column from dictionary")
    parser.add_argument(
        "--matching_threshold",
        type=int,
        help="Threshold of string similarity for the normalization to be accepted (default: 50)",
        default=50,
    )
    parser.add_argument(
        "--index", action="store_true", help="Use column indexes instead of names"
    )
    args = parser.parse_args()

    ## Parse input file
    with open(args.input, "r") as f:
        text_entities = f.readlines()

    ## Normalize entities
    normalization_dictionary = EntityDictionary(
        args.dictionary, args.source, args.target, index=args.index
    )
    normalized = normalize(
        text_entities,
        normalization_dictionary,
        matching_threshold=args.matching_threshold,
    )

    ## Write output file
    with open(args.output, "w") as f:
        f.write("\n".join(normalized))
