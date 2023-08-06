# -*- coding: utf-8 -*-
"""
One thing to note: in the NuSpec XML file, 'id' is the project name
which must be unique across the NuGet server and 'title' is the
human-friendly title of the package.
"""

import datetime as dt
import json

from sqlalchemy import Column, Integer, String, Text, Boolean
from sqlalchemy import ForeignKey
from sqlalchemy import func
from sqlalchemy import desc
from sqlalchemy import or_
from sqlalchemy import cast
from sqlalchemy.dialects import sqlite
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship

from pynuget import logger


Base = declarative_base()


class Package(Base):
    """
    """

    __tablename__ = "package"

    package_id = Column(Integer, primary_key=True)
    name = Column(String(256), index=True, unique=True, nullable=False)
    title = Column(String(256))
    download_count = Column(Integer, index=True, nullable=False, default=0)
    latest_version = Column(Text())

    def __repr__(self):
        return "<Package({}, {})>".format(self.package_id, self.name)


class Version(Base):
    """
    """

    __tablename__ = "version"

    version_id = Column(Integer, primary_key=True)
    package_id = Column(Integer, ForeignKey("package.package_id"),
                        nullable=False)
    title = Column(Text())
    description = Column(Text())
    created = Column(Integer)
    version = Column(String(32), index=True)
    package_hash = Column(Text())
    package_hash_algorithm = Column(Text())
    dependencies = Column(Text())
    package_size = Column(Integer)
    release_notes = Column(Text())
    version_download_count = Column(Integer, nullable=False, default=0)
    tags = Column(Text())
    license_url = Column(Text())
    project_url = Column(Text())
    icon_url = Column(Text())
    authors = Column(Text())
    owners = Column(Text())
    require_license_acceptance = Column(Boolean())
    copyright_ = Column(Text())
    is_prerelease = Column(Boolean())

    package = relationship("Package", backref="versions")

    def __repr__(self):
        return "<Version({}, {}, {})>".format(self.version_id, self.package.name, self.version)

    @hybrid_property
    def thing(self):
        return "{}~~{}".format(self.package_id, self.version)

    @thing.expression
    def thing(cls):
        name = cast(cls.package_id, String)
        version = cast(cls.version, String)
        return name + "~~" + version


def count_packages(session):
    """
    Count the number of packages on the server.

    Parameters
    ----------
    session : :class:`sqlalchemy.orm.session.Session`

    Returns
    -------
    int
    """
    logger.debug("db.count_packages()")
    return session.query(func.count(Package.package_id)).scalar()


def search_packages(session,
                    include_prerelease=False,
                    order_by=desc(Version.version_download_count),
                    filter_=None,
                    search_query=None):
    """
    Parameters
    ----------
    session : :class:`sqlalchemy.orm.session.Session`
    include_prerelease : bool
    order_by : :class:`sqlalchemy.sql.operators.ColumnOperators`
    filder_ : str
        One of ('is_absolute_latest_version', 'is_latest_version').
    search_query : str
    """
    logger.debug("db.search_packages(...)")
    query = session.query(Version).join(Package)

    if search_query is not None:
        search_query = "%" + search_query + "%"
        query = query.filter(
            or_(Package.name.like(search_query),
                Package.title.like(search_query)
                )
        )

    if not include_prerelease:
        query = query.filter(Version.is_prerelease.isnot(True))

    known_filters = ('is_absolute_latest_version', 'IsLatestVersion')
    if filter_ is None:
        pass
    elif filter_ in known_filters:
        query = query.filter(Version.version == Package.latest_version)
    else:
        raise ValueError("Unknown filter '{}'".format(filter_))

    if order_by is not None:
        query = query.order_by(order_by)

    results = query.all()
    logger.debug("Found %d results." % len(results))

    return results


def package_updates(session, packages_dict, include_prerelease=False):
    """
    I *think* this returns a list of packages that need updating...

    Seems like the route for this fuction expects args from a url that look
    like:
        /updates?packageids='pkg1'|'pkg2'&versions='vers1'|'vers2'
    where "|" might be encoded as %7C

    Parameters
    ----------
    session : :class:`sqlalchemy.orm.session.Session`
    packages_dict : dict
        Dict of {package.name, version}.
    include_prerelease : bool
    """
    logger.debug("db.package_updates(...)")
    package_versions = ["{}~~{}".format(pkg, vers)
                        for pkg, vers
                        in packages_dict.items()]

    query = (session.query(Version)
             .filter(Version.version == Package.latest_version)
             .filter(Version.package_id.in_(packages_dict.keys()))
             .filter(~Version.thing.in_(package_versions))
             )

    return query.order_by(Version.package_id).all()


def find_by_pkg_name(session, package_name, version=None):
    """
    Find a package by name. If version is `None`, returns all versions.

    Parameters
    ----------
    session : :class:`sqlalchemy.orm.session.Session`
    package_name : str
        The NuGet name of the package - the "id" tag in the NuSpec file.
    version : str
        The version of the package to download. If `None`, then return all
        versions.

    Returns
    -------
    results : list of :class:`Version`
    """
    logger.debug("db.find_by_pkg_name('%s', version='%s')" % (package_name,
                                                              version))
    query = (session.query(Version)
             .join(Package)
             .filter(Package.name == package_name)
             )

    stmt = query.statement.compile(dialect=sqlite.dialect(),
                                   compile_kwargs={"literal_binds": True})
    logger.debug(stmt)

    if version:
        query = query.filter(Version.version == version)
    query.order_by(desc(Version.version))

    results = query.all()
    logger.info("Found %d results." % len(results))
    logger.debug(results)

    return results


def find_pkg_by_id(session, package_id):
    query = (session.query(Package)
             .filter(Package.package_id == package_id)
             )

    # TODO: Error handling
    result = query.one()
    logger.debug(result)

    return result


def validate_id_and_version(session, package_name, version):
    """
    Not exactly sure what this is supposed to do, but I *think* it simply
    makes sure that the given pacakge_id and version exist... So that's
    what I've decided to make it do.

    Parameters
    ----------
    session : :class:`sqlalchemy.orm.session.Session`
    package_name : str
        The NuGet name of the package - the "id" tag in the NuSpec file.
    version : str
    """
    logger.debug("db.validate_id_and_version(...)")
    query = (session.query(Version)
             .filter(Package.name == package_name)
             .filter(Version.version == version)
             )
    return session.query(query.exists()).scalar()


def increment_download_count(session, package_name, version):
    """
    Increment the download count for a given package version.

    Parameters
    ----------
    session : :class:`sqlalchemy.orm.session.Session`
    package_name : str
        The NuGet name of the package - the "id" tag in the NuSpec file.
    version : str
    """
    msg = "db.increment_download_count(%s, %s)"
    logger.debug(msg % (package_name, version))
    obj = (session.query(Version)
           .filter(Package.name == package_name)
           .filter(Version.version == version)
           ).one()
    obj.version_download_count += 1
    obj.package.download_count += 1
    session.commit()


def insert_or_update_package(session, package_name, title, latest_version):
    """

    Parameters
    ----------
    session : :class:`sqlalchemy.orm.session.Session`
    package_name : str
        The NuGet name of the package - the "id" tag in the NuSpec file.
    title : str
    latest_version : str
    """
    logger.debug("db.insert_or_update_package(...)")
    sql = session.query(Package).filter(Package.name == package_name)
    obj = sql.one_or_none()
    if obj is None:
        pkg = Package(name=package_name, title=title,
                      latest_version=latest_version)
        session.add(pkg)
    else:
        sql.update({Package.name: package_name,
                    Package.title: title,
                    Package.latest_version: latest_version})
    session.commit()


def insert_version(session, **kwargs):
    """Insert a new version of an existing package."""
    logger.debug("db.insert_version(...)")
    kwargs['created'] = dt.datetime.utcnow()
    if 'dependencies' in kwargs:
        kwargs['dependencies'] = json.dumps(kwargs['dependencies'])
    if 'is_prerelease' not in kwargs:
        kwargs['is_prerelease'] = 0
    if 'require_license_acceptance' not in kwargs:
        kwargs['require_license_acceptance'] = 0

    version = Version(**kwargs)
    session.add(version)
    session.commit()
    logger.debug(version)


def delete_version(session, package_name, version):
    """

    Parameters
    ----------
    session : :class:`sqlalchemy.orm.session.Session`
    package_name : str
        The NuGet name of the package - the "id" tag in the NuSpec file.
    version : str
    """
    msg = "db.delete_version({}, {})"
    logger.debug(msg.format(package_name, version))
    sql = (session.query(Version).join(Package)
           .filter(Package.name == package_name)
           .filter(Version.version == version)
           )
    version = sql.one()
    pkg = version.package

    session.delete(version)

    # update the Package.latest_version value, or delete the Package
    versions = (session.query(Version)
                .join(Package)
                .filter(Package.name == package_name)
                ).all()
    if len(versions) > 0:
        pkg.latest_version = max(v.version for v in versions)
    else:
        logger.info("No more versions exist. Deleting package %s" % pkg)
        session.delete(pkg)
    session.commit()
