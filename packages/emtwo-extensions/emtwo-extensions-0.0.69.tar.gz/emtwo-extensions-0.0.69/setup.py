from setuptools import setup, find_packages

setup(
    name='emtwo-extensions',
    version='0.0.69',
    install_requires=[
        'dockerflow>=2018.4.0',
        'requests',
    ],
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    package_data={'redash_stmo': ['js/*/*.js', 'js/*/*.html']},
    description="Extensions to Redash by Mozilla",
    author='Mozilla Foundation',
    author_email='dev-webdev@lists.mozilla.org',
    url='https://github.com/mozilla/redash-stmo',
    license='MPL 2.0',
    entry_points={
        'redash.extensions': [
            'dockerflow = redash_stmo.dockerflow:dockerflow',
        ],
        'webpack_bundles': [
            'datasource_link = redash_stmo.js_extensions:datasource_link',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment :: Mozilla',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
    ],
    zip_safe=False,
)
