import os
import xml.etree.ElementTree as ET

from scopus.utils import get_content, get_encoded_text

SCOPUS_AFFILIATION_DIR = os.path.expanduser('~/.scopus/affiliation')

if not os.path.exists(SCOPUS_AFFILIATION_DIR):
    os.makedirs(SCOPUS_AFFILIATION_DIR)


class ScopusAffiliation:
    @property
    def affiliation_id(self):
        """The Scopus ID of the affiliation."""
        return self._aff_id

    @property
    def date_created(self):
        """Date the Scopus record was created."""
        return self._date_created

    @property
    def nauthors(self):
        """Number of authors in the affiliation."""
        return self._nauthors

    @property
    def ndocuments(self):
        """Number of documents for the affiliation."""
        return self._ndocuments

    @property
    def url(self):
        """URL to the affiliation's profile page."""
        return self._url

    @property
    def api_url(self):
        """URL to the affiliation's API page."""
        return self._api_url

    @property
    def org_type(self):
        """Type of the affiliation."""
        return self._org_type

    @property
    def org_domain(self):
        """Internet domain of the affiliation."""
        return self._org_domain

    @property
    def org_url(self):
        """Website of the affiliation."""
        return self._org_url

    @property
    def name(self):
        """The name of the affiliation."""
        return self._name

    @property
    def address(self):
        """The address of the affiliation."""
        return self._address

    @property
    def city(self):
        """The city of the affiliation."""
        return self._city

    @property
    def country(self):
        """The country of the affiliation."""
        return self._country

    def __init__(self, aff_id, refresh=False):
        """Class to represent an Affiliation in Scopus.

        Parameters
        ----------
        aff_id : str or int
            The Scopus Affiliation ID.  Optionally expressed
            as an Elsevier EID (i.e., in the form 10-s2.0-nnnnnnnn).

        refresh : bool (optional, default=False)
            Whether to refresh the cached file if it exists or not.

        Notes
        -----
        The files are cached in ~/.scopus/affiliation/{aff_id}.
        """
        aff_id = str(int(str(aff_id).split('-')[-1]))

        qfile = os.path.join(SCOPUS_AFFILIATION_DIR, aff_id)
        url = ('https://api.elsevier.com/content/affiliation/'
               'affiliation_id/{}'.format(aff_id))

        xml = ET.fromstring(get_content(qfile, url=url, refresh=refresh))

        # coredata
        self._url = xml.find('coredata/link[@rel="scopus-affiliation"]')
        _aff_id = get_encoded_text(xml, 'coredata/dc:identifier')
        self._aff_id = _aff_id.split(":")[-1]
        if self._url is not None:
            self._url = self.url.get('href')
        self._api_url = get_encoded_text(xml, 'coredata/prism:url')
        self._nauthors = get_encoded_text(xml, 'coredata/author-count')
        self._ndocuments = get_encoded_text(xml, 'coredata/document-count')

        self._name = get_encoded_text(xml, 'affiliation-name')
        self._address = get_encoded_text(xml, 'address')
        self._city = get_encoded_text(xml, 'city')
        self._country = get_encoded_text(xml, 'country')

        # institution-profile
        date_created = xml.find('institution-profile/date-created')
        if date_created is not None:
            self._date_created = (int(date_created.attrib['year']),
                                  int(date_created.attrib['month']),
                                  int(date_created.attrib['day']))
        else:
            self._date_created = (None, None, None)
        self._org_type = get_encoded_text(xml, 'institution-profile/org-type')
        self._org_domain = get_encoded_text(xml, 'institution-profile/org-domain')
        self._org_url = get_encoded_text(xml, 'institution-profile/org-URL')

    def __str__(self):
        s = '''{self.name} ({self.nauthors} authors, {self.ndocuments} documents)
    {self.address}
    {self.city}, {self.country}
    {self.url}'''.format(self=self)
        return s
