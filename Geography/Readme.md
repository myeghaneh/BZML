---

title: "Database of  publication abstracts on exoplanets  from NASA archive"

date: July 2019

author: "Gerd Graßhoff", "Sabrina Bier"

---
# Content

Collection of abstracts in publications on exoplanets, as collected by NASA. The dataframes are stored  JSON prepared for importing as Pandas dataframes.

# Files

  - dfExoplanetsNASA.json: publication data with abstracts
  - dfExoplanetsNASAabs.json: processed abstracts
  - dfExoplanetsNASAabsSentences.json: sentences as extracted with Spacy.
  - dfConfirmedExoplanetsNASA.json: list of confirmed Exoplanets from NASA database.

## Fields of dfExoplanetsNASA_v3.json

* ID: `numpy.int64` consecutive ID of papers.
* bibcode: `str` identifier of the paper from NASA ADS. It is taken from NASA ADS without chances.
* doi: `str` Digital Object Indentifier of the actual published paper.  It is taken from NASA ADS without chances. If the paper has no DOI, this is marked with 'None'.
* authors: `list of str` authors of the paper. If the paper has no authors, this is marked with ['None']. The number of the authors is adjusted to the reference of affiliations.
* affiliation:	`list of lists of str` affiliations of the authors contributing to the paper. Unknown affiliations are marked with ['None'].
* acknowledgement: `str` acknowledgements given by the authors of the paper. If the paper has no acknowledgements, this is marked with 'None'. The word "acknowledgement" in all possible variations is strip off.
* grant:	`list of str` grants, supporting the work on the paper. If the paper gives no grants, this is marked with an empty list [].
* published:	`str` month and year of publication of the paper, the day of publication is not stated and therefore always 00. The column 'published' has the following format: YYYY-MM-DD. It is taken from NASA ADS without any chances.
* year: `numpy.int64` year in which the paper was published. It is taken from NASA ADS without chances.
* title: `str` title of the paper. If the paper has no title or NASA ADS does not provide any title, this is marked with 'None'. It is taken from NASA ADS without chances.
* abstract: `str` abstract of the paper. If the paper has no abstract, this is marked with 'None'. It is taken from NASA ADS without chances.
* keywords: `list of str` keywords choosen by the authors to describe the paper. If the paper contains no keywords, this is marked with an empty list []. It is taken from NASA ADS without chances.
* citation_count: `numpy.int64` number of citations of the paper known to NASA ADS. It is taken from NASA ADS without chances.

This database is primary for the oder files of prepocessed abstracts (dfExoplanetsNASAabsClear_v1.json) and extracted sentences (dfExoplanetsNASAabsSentences_v1.json).

# References

  - Covered publication time: 1943 to Dec 2019

  - link to source (as July 2019):
[NASA ADS](https://ui.adsabs.harvard.edu/)

  - information:
[NASA ADS info](https://ui.adsabs.harvard.edu/about/)

  - documentation:
[NASA ADS help](https://adsabs.github.io/help/)

    - https://github.com/adsabs/adsabs-dev-api,
    - http://adsabs.github.io/help/api/, https://groups.google.com/forum/#!forum/adsabs-dev-api
    - https://ads.readthedocs.io/en/latest/

# Supported by:
  - Max Planck Institute for History of Science
  - Humboldt University Berlin
  - Berlin Center of Machine Learning
  - grant *FKZ: 01 IS 18037* A of Federal Ministry of Education and Research
