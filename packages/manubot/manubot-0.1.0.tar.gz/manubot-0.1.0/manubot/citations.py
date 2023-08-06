import hashlib
import logging
import re

import base62

from manubot.metadata import citeproc_retrievers

"""
Regex to extract citations.

Same rules as pandoc, except more permissive in the following ways:

1. the final character can be a slash because many URLs end in a slash.
2. underscores are allowed in internal characters because URLs, DOIs, and
   citation tags often contain underscores.

If a citation string does not match this regex, it can be substituted for a
tag that does, as defined in citation-tags.tsv.

https://github.com/greenelab/manubot-rootstock/issues/2#issuecomment-312153192

Prototyped at https://regex101.com/r/s3Asz3/2
"""
citation_pattern = re.compile(
    r'(?<!\w)@[a-zA-Z0-9][\w:.#$%&\-+?<>~/]*[a-zA-Z0-9/]')


def standardize_citation(citation):
    """
    Standardize citation idenfiers based on their source
    """
    source, identifier = citation.split(':', 1)
    if source == 'doi':
        identifier = identifier.lower()
    return f'{source}:{identifier}'


def is_valid_citation_string(string):
    """
    Return True if the citation string is a properly formatted citation.
    Return False if improperly formatted or a non-citation.
    """
    if not string.startswith('@'):
        logging.error(f'{string} → does not start with @')
        return False

    try:
        source, identifier = string.lstrip('@').split(':', 1)
    except ValueError as e:
        logging.error(f'Citation not splittable: {string}')
        return False

    if not source or not identifier:
        msg = f'{string} → blank source or identifier'
        logging.error(msg)
        return False

    # Exempted non-citation sources used for pandoc-fignos, pandoc-tablenos,
    # and pandoc-eqnos
    if source in {'fig', 'tbl', 'eq'}:
        return False

    # Check supported source type
    if source != 'tag' and source not in citeproc_retrievers:
        logging.error(f'{string} → source "{source}" is not valid')
        return False

    return True


def get_citation_id(standard_citation):
    """
    Get the citation_id for a standard_citation.
    """
    assert '@' not in standard_citation
    as_bytes = standard_citation.encode()
    blake_hash = hashlib.blake2b(as_bytes, digest_size=6)
    digest = blake_hash.digest()
    citation_id = base62.encodebytes(digest)
    return citation_id


def citation_to_citeproc(citation):
    """
    Return a dictionary with citation metadata
    """
    assert citation == standardize_citation(citation)
    source, identifier = citation.split(':', 1)

    if source in citeproc_retrievers:
        citeproc = citeproc_retrievers[source](identifier)
    else:
        msg = f'Unsupported citation  source {source} in {citation}'
        raise ValueError(msg)

    citation_id = get_citation_id(citation)
    citeproc = citeproc_passthrough(citeproc, set_id=citation_id)

    return citeproc


# Valid CSL (citeproc JSON) types as per
# https://github.com/citation-style-language/schema/blob/4846e02f0a775a8272819204379a4f8d7f45c16c/csl-types.rnc#L5-L39
citeproc_types = {
    "article",
    "article-journal",
    "article-magazine",
    "article-newspaper",
    "bill",
    "book",
    "broadcast",
    "chapter",
    "dataset",
    "entry",
    "entry-dictionary",
    "entry-encyclopedia",
    "figure",
    "graphic",
    "interview",
    "legal_case",
    "legislation",
    "manuscript",
    "map",
    "motion_picture",
    "musical_score",
    "pamphlet",
    "paper-conference",
    "patent",
    "personal_communication",
    "post",
    "post-weblog",
    "report",
    "review",
    "review-book",
    "song",
    "speech",
    "thesis",
    "treaty",
    "webpage",
}

citeproc_type_fixer = {
    'journal-article': 'article-journal',
    'book-chapter': 'chapter',
    'posted-content': 'manuscript',
    'proceedings-article': 'paper-conference',
    'standard': 'entry',
    'reference-entry': 'entry',
}

# Remove citeproc keys to fix pandoc-citeproc errors
citeproc_remove_keys = [
    # Error in $[0].ISSN[0]: failed to parse field ISSN: mempty
    'ISSN',
    # Error in $[2].ISBN[0]: failed to parse field ISBN: mempty
    'ISBN',
    # pandoc-citeproc expected Object not array for archive
    'archive',
    # failed to parse field event: Could not read as string
    'event',
    # remove the references of cited papers. Not neccessary and unwieldy.
    'reference',
    # Error in $[26].categories[0][0]: failed to parse field categories: mempty
    'categories',
]


def citeproc_passthrough(csl_item, set_id=None):
    """
    Fix errors in a CSL item and optionally change its id.
    http://citeproc-js.readthedocs.io/en/latest/csl-json/markup.html
    https://github.com/citation-style-language/schema/blob/master/csl-data.json
    """
    if set_id is not None:
        csl_item['id'] = set_id

    # Correct invalid CSL item types
    # See https://github.com/CrossRef/rest-api-doc/issues/187
    old_type = csl_item['type']
    csl_type = citeproc_type_fixer.get(old_type, old_type)
    if csl_type not in citeproc_types:
        csl_type = 'entry'
    csl_item['type'] = csl_type

    # Remove problematic objects
    for key in citeproc_remove_keys:
        csl_item.pop(key, None)

    # pandoc-citeproc error
    # failed to parse field issued: Could not read as string: Null
    try:
        value = csl_item['issued']['date-parts'][0][0]
        if value is None:
            del csl_item['issued']
    except KeyError:
        pass

    return csl_item
