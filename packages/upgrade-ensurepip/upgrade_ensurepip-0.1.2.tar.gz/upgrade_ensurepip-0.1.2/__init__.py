# coding: utf-8

_package_data = dict(
    full_package_name=u"upgrade_ensurepip",
    version_info=(0, 1, 2),
    __version__="0.1.2",
    author=u"Anthon van der Neut",
    author_email=u"a.van.der.neut@ruamel.eu",
    description=u"upgrade pip and setuptools versions used by venv",
    keywords=u"pip ensurepip upgrade",
    license=u"MIT",
    since=2018,
    python_requires=u">=3.3",
    status=u"α",
    universal=True,
    install_requires=[],
    classifiers=[
        u"Environment :: Console",
        u"Operating System :: OS Independent",
        u"Programming Language :: Python",
        u"Programming Language :: Python :: 3.4",
        u"Programming Language :: Python :: 3.5",
        u"Programming Language :: Python :: 3.6",
        u"Programming Language :: Python :: 3.7",
        u"Programming Language :: Python :: 3 :: Only",
        u"Topic :: Software Development :: Libraries :: Python Modules",
        u"Topic :: Software Development :: Quality Assurance",
    ],
    oitnb=dict(multi_line_unwrap=True),
)


version_info = _package_data["version_info"]
__version__ = _package_data["__version__"]
