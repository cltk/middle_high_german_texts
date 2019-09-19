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


if __name__ == "__main__":
    root = get_root(nibelungenlied_filename)
    tokens = [extract_annotations(entry) for entry in root.findall(".//tok_anno")]
    normalized_text = extract_by_tag("norm", tokens)
    lemmata = extract_by_tag("lemma", tokens)
    pos_tags = extract_by_tag("pos", tokens)
    inflections = extract_by_tag("infl", tokens)
