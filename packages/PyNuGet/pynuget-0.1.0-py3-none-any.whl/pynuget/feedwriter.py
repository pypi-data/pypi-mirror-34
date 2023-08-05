# -*- coding: utf-8 -*-
"""
"""

import datetime as dt
import json
import re

from lxml import etree as et

from pynuget import logger

BASE = b"""<?xml version="1.0" encoding="utf-8" ?>
<feed
  xml:base="https://www.nuget.org/api/v2/"
  xmlns="http://www.w3.org/2005/Atom"
  xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices"
  xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata"
>
</feed>
"""
NS_D = "{http://schemas.microsoft.com/ado/2007/08/dataservices}"
NS_M = "{http://schemas.microsoft.com/ado/2007/08/dataservices/metadata}"
NS_DEFAULT = "{http://www.w3.org/2005/Atom}"
NSMAP = {
    None: NS_DEFAULT.strip("{}"),
    'd': NS_D.strip("{}"),
    'm': NS_M.strip("{}"),
}

ADO_BASE_URL = "http://schemas.microsoft.com/ado/2007/08/dataservices"
ADO_SCHEMA_URL = ADO_BASE_URL + "/scheme"
ADO_METADATA_URL = ADO_BASE_URL + "/metadata"


class FeedWriter(object):

    def __init__(self, feed_name, base_url='http://localhost:5000/'):
        logger.debug("Initializing FeedWriter")
        self.feed_name = feed_name
        self.base_url = base_url

    def write(self, results):
        self.begin_feed()
        try:
            for result in results:
                self.add_entry(result)
        except TypeError:
            pass
        return et.tostring(self.feed)

    def write_to_output(self, results):
        """
        results : list of dicts, I think.
        """
        logger.debug("FeedWriter.write_to_output(%d)" % len(results))
        # TODO: header line
        return self.write(results)

    def begin_feed(self):
        logger.debug("FeedWriter.begin_feed()")
        self.feed = et.fromstring(BASE)
        node = et.Element('id')
        node.text = self.base_url + str(self.feed_name)
        self.feed.append(node)
        self.add_with_attributes(
            self.feed,
            'title',
            self.feed_name,
            {'type': 'text'},
        )
        node = et.Element('updated')
        node.text = self.format_date(dt.datetime.utcnow())
        self.feed.append(node)
        self.add_with_attributes(
            self.feed,
            'link',
            None,
            {'rel': 'self', 'title': self.feed_name, 'href': self.feed_name},
        )

    def add_entry(self, row):
        """
        Parameters
        ----------
        row :
            SQLAlchemy result set object
        """
        logger.debug("FeedWriter.add_entry(%s)" % row)
        entry_id = 'Packages(Id="{}",Version="{}")'.format(row.package_id,
                                                           row.version)
        entry = et.Element('entry')
        self.feed.append(entry)
        node = et.Element('id')
        node.text = self.base_url + entry_id
        entry.append(node)
        self.add_with_attributes(
            entry,
            'category',
            None,
            {'term': 'NuGetGallery.V2FeedPackage', 'scheme': ADO_SCHEMA_URL},
        )
        self.add_with_attributes(
            entry,
            'link',
            None,
            {'rel': 'edit', 'title': 'V2FeedPackage', 'href': entry_id},
        )

        # Yes, this "title" is actually the package ID. Actual title is in
        # the metadata.
        self.add_with_attributes(entry, 'title', str(row.package_id),
                                 {'type': 'text'})
        self.add_with_attributes(entry, 'summary', None, {'type': 'text'})
        node = et.Element('updated')
        node.text = self.format_date(row.created)
        entry.append(node)

        authors_node = et.Element('author')
        entry.append(authors_node)
        node = et.Element('name')
        node.text = row.authors
        authors_node.append(node)

        self.add_with_attributes(
            entry,
            'link',
            None,
            {'rel': 'edit-media',
             'title': 'V2FeedPackage',
             'href': entry_id + '/$value',
             },
        )
        url = "{}download/{}/{}".format(self.base_url, row.package_id,
                                        row.version)
        self.add_with_attributes(
            entry,
            'content',
            None,
            {'type': 'application/zip', 'src': url},
        )
        self.add_entry_meta(entry, row)

    def add_entry_meta(self, entry, row):
        """
        Parameters
        ----------
        row :
            SQLAlchemy result set object
        """
        logger.debug("FeedWriter.add_entry_meta(%s, %s)" % (entry, row))
        properties = et.Element(NS_M + 'properties', nsmap=NSMAP)
        entry.append(properties)

        gallery_details_url = "{}details/{}/{}".format(self.base_url,
                                                       row.package_id,
                                                       row.version)

        meta = {
            'Id': row.title,
            'Version': row.version,
            'NormalizedVersion': row.version,
            'Copyright': row.copyright_,
            'Created': self.render_meta_date(row.created),
            'Dependencies': self.render_dependencies(row.dependencies),
            'Description': row.description,  # TODO: htmlspecialchars
            'DownloadCount': {'value': str(row.package.download_count), 'type': 'Edm.Int32'},
            'GalleryDetailsUrl': gallery_details_url,
            'IconUrl': row.icon_url,  #TODO: htmlspecialchars
            'IsLatestVersion': self.render_meta_boolean(row.package.latest_version == row.version),
            'IsAbsoluteLatestVersion': self.render_meta_boolean(row.package.latest_version == row.version),
            'IsPrerelease': self.render_meta_boolean(row.is_prerelease),
            'Language': None,
            'Published': self.render_meta_date(row.created),
            'PackageHash': row.package_hash,
            'PackageHashAlgorithm': row.package_hash_algorithm,
            'PackageSize': {'value': str(row.package_size), 'type': 'Edm.Int64'},
            'ProjectUrl': row.project_url,
            'ReportAbuseUrl': '',
            'ReleaseNotes': row.release_notes,  # TODO: htmlspecialchars
            'RequireLicenseAcceptance': self.render_meta_boolean(row.require_license_acceptance),
            'Summary': None,
            'Tags': row.tags,
            'Title': row.title,
            'VersionDownloadCount': {'value': str(row.version_download_count), 'type': 'Edm.Int32'},
            'MinClientVersion': '',
            'LastEdited': {'value': None, 'type': 'Edm.DateTime'},
            'LicenseUrl': row.license_url,
            'LicenseNames': '',
            'LicenseReportUrl': '',
        }

        for name, data in sorted(meta.items()):
            if isinstance(data, dict):
                value = data['value']
                type_ = data['type']
            else:
                value = data
                type_ = None

            self.add_meta(properties, name, value, type_)

    def render_meta_date(self, date):
        return {'value': self.format_date(date) + "Z", 'type': 'Edm.DateTime'}

    def render_meta_boolean(self, value):
        return {'value': str(value), 'type': 'Edm.Boolean'}

    def format_date(self, value):
        logger.debug("{}: {}".format(value, type(value)))
        if isinstance(value, dt.datetime):
            #  return value.isoformat(timespec='seconds')      # Py3.6+
            return value.isoformat()
        return value

    def render_dependencies(self, raw):
        logger.debug("FeedWriter.render_dependencies(%s)" % raw)
        if not raw:
            return ''

        try:
            data = json.loads(raw)
        except json.decoder.JSONDecodeError:
            return ''

        output = []

        for dependency in data:
            formatted_dependency = "{}:{}:".format(dependency['id'],
                                                   dependency['version'])
            if 'framework' in dependency.keys():
                formatted_dependency += self.format_target_framework(
                    dependency['framework'],
                )
            output.append(formatted_dependency)

        return "|".join(output)

    def format_target_framework(self, framework):
        """Format a raw target framework from a NuSpec into the format
        used in the packages feed.

        Eg:
        DNX4.5.1 -> dnx451
        DNXCore5.0 -> dnxcore50
        """
        return re.sub('[^A-Z0-9]', '', framework, flags=re.IGNORECASE).lower()

    def add_with_attributes(self, entry, name, value, attributes):
        """

        Parameters
        ----------
        entry :
            Looks to be a SimpleXMLElement node object
        attributes :
            Dict, I think.
        """
        child = et.Element(name)
        child.text = str(value)
        entry.append(child)
        for attr_name, attr_value in sorted(attributes.items()):
            child.set(attr_name, str(attr_value))

    def add_meta(self, entry, name, value, type_=None):

        child = et.Element(NS_D + name, nsmap=NSMAP)
        child.text = value
        entry.append(child)

        if type_:
            child.set('type', type_)

        if value is None:
            child.set('null', 'true')
