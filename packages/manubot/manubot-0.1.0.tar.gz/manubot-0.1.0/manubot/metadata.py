import json
import logging
import re
import urllib.request

import requests

from manubot.arxiv import get_arxiv_citeproc
from manubot.pubmed import get_pubmed_citeproc


def get_short_doi_url(doi):
    """
    Get the shortDOI URL for a DOI.
    """
    quoted_doi = urllib.request.quote(doi)
    url = 'http://shortdoi.org/{}?format=json'.format(quoted_doi)
    try:
        response = requests.get(url).json()
        short_doi = response['ShortDOI']
        short_doi = short_doi[3:]  # Remove "10/" prefix
        short_url = 'https://doi.org/' + short_doi
        return short_url
    except Exception:
        logging.exception(f'shortDOI lookup failed for {doi}')
        return None


def get_doi_citeproc(doi):
    """
    Use Content Negotioation (http://citation.crosscite.org/docs.html) to
    retrieve the citeproc JSON citation for a DOI.
    """
    url = 'https://doi.org/' + urllib.request.quote(doi)
    header = {
        'Accept': 'application/vnd.citationstyles.csl+json',
    }
    response = requests.get(url, headers=header)
    try:
        citeproc = response.json()
    except Exception as error:
        logging.error(f'Error fetching metadata for doi:{doi}.\n'
                      f'Invalid response from {response.url}:\n{response.text}')
        raise error
    citeproc['URL'] = f'https://doi.org/{doi}'
    short_doi_url = get_short_doi_url(doi)
    if short_doi_url:
        citeproc['short_url'] = short_doi_url
    return citeproc


def get_pmc_citeproc(identifier):
    """
    Get the citeproc JSON for a PubMed Central record by its PMID, PMCID, or
    DOI, using the NCBI Citation Exporter API.

    https://github.com/ncbi/citation-exporter
    https://www.ncbi.nlm.nih.gov/pmc/tools/ctxp/
    https://www.ncbi.nlm.nih.gov/pmc/utils/ctxp/samples
    https://github.com/greenelab/manubot/issues/21
    """
    params = {
        'ids': identifier,
        'report': 'citeproc',
    }
    url = 'https://www.ncbi.nlm.nih.gov/pmc/utils/ctxp'
    response = requests.get(url, params)
    try:
        citeproc = response.json()
    except Exception as error:
        logging.error(f'Error fetching PMC metadata for {identifier}.\n'
                      f'Invalid response from {response.url}:\n{response.text}')
        raise error
    citeproc['URL'] = f"https://www.ncbi.nlm.nih.gov/pmc/articles/{citeproc['PMCID']}/"
    return citeproc


def get_url_citeproc_greycite(url):
    """
    Uses Greycite which has experiened uptime problems in the past.
    API calls seem to take at least 15 seconds. Browser requests are much
    faster. Setting header did not have an effect. Consider mimicking browser
    using selenium.

    More information on Greycite at:
    http://greycite.knowledgeblog.org/
    http://knowledgeblog.org/greycite
    https://arxiv.org/abs/1304.7151
    https://git.io/v9N2C

    Uses urllib.request.urlopen rather than requests.get due to
    https://github.com/kennethreitz/requests/issues/4023
    """
    response = requests.get(
        'http://greycite.knowledgeblog.org/json',
        params={'uri': url},
        headers={'Connection': 'close'},
    )
    # Some Greycite responses were valid JSON besides for an error appended
    # like "<p>*** Date set from uri<p>" or "<p>*** fetch error : 404<p>".
    pattern = re.compile(r"<p>\*\*\*.*<p>")
    text = pattern.sub('', response.text)
    csl_item = json.loads(text)
    csl_item['type'] = 'webpage'
    return csl_item


def get_url_citeproc_manual(url):
    """
    Manually create citeproc for a URL.
    """
    return {
        'URL': url,
        'type': 'webpage',
    }


def get_url_citeproc(url):
    """
    Get citeproc for a URL trying a sequence of strategies.
    """
    try:
        return get_url_citeproc_greycite(url)
    except Exception as e:
        logging.warning(f'Error getting {url} from Greycite: {e}')
        # Fallback strategy
        return get_url_citeproc_manual(url)


citeproc_retrievers = {
    'doi': get_doi_citeproc,
    'pmid': get_pubmed_citeproc,
    'pmcid': get_pmc_citeproc,
    'arxiv': get_arxiv_citeproc,
    'url': get_url_citeproc,
}
