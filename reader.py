"""
Reader of the Nibelungenlied in Referenzkorpus  Mittelhochdeutsch

Source: https://www.linguistics.rub.de/rem/access/index.html
"""


import os
from lxml import etree

__author__ = ["Clément Besnier <clemsciences@aol.com>", ]

nibelungenlied_filename = "M321-G1.xml"


def get_root(filename):
    parser = etree.XMLParser(load_dtd=True, no_network=False)
    tree = etree.parse(os.path.join(filename), parser=parser)
    return tree.getroot()


def extract_annotations(entry):
    return {child.tag: child.get("tag") for child in entry.getchildren()}


def extract_by_tag(tag, tokens):
    return [token[tag] for token in tokens if tag in token]


def extract_normalized_text(root):
    return [token.get("utf") for token in root.findall(".//tok_anno")]


def extract_token_ranges(token_range: str):
    pass


def extract_line_ranges(line_ranges):
    pass


def reconstitute_text(root):
    pages_ranges = {page.get("id")[1:]: page.get("range")[1:] for page in root.findall(".//page")}
    columns_ranges = {line.get("id")[1:]: line.get("range") for line in root.findall(".//column")}
    lines_ranges = {line.get("id"): line.get("range") for line in root.findall(".//line")}
    lines = [[[lines_ranges[line] for line in lines_ranges] for column in columns_ranges
              if pages_ranges[page] == column] for page in pages_ranges]
    # TODO extract from each column, a range of line
    # TODO extract from each line, a range of tokens


if __name__ == "__main__":
    root = get_root(nibelungenlied_filename)
    tokens = [extract_annotations(entry) for entry in root.findall(".//tok_anno")]
    complete_text = [token.get("utf") for token in root.findall(".//tok_anno")]
    normalized_text = extract_by_tag("norm", tokens)
    # lemmata = extract_by_tag("lemma", tokens)
    # pos_tags = extract_by_tag("pos", tokens)
    # inflections = extract_by_tag("infl", tokens)
    print(complete_text[:100])
    reconstitute_text(root)

