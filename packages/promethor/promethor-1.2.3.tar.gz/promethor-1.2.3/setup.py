import setuptools

setuptools.setup(
    setup_requires=["pbr>=1.9", "setuptools>=17.1"],
    data_files=[('/etc/promethor',
        ['etc/sentry.yml', 'etc/sql.yml', 'etc/mongo.yml'])],
    pbr=True
)
