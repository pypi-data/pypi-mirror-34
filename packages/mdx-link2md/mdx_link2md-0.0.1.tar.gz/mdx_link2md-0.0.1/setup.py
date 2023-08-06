import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='mdx_link2md',
    version='0.0.1',
    author='scyu16',
    author_email='devmaily@yandex.com',
    url='https://github.com/scyu16/mdx_link2md',
    license='MIT',
    description='A markdown link preprocessor for Python Markdown',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='markdown, html',
    install_requires=[
        'markdown>=2.6.11'
    ],
    packages=setuptools.find_packages(),
    classifiers=(
                  'Topic :: Text Processing :: Markup',
                  'Topic :: Utilities',
                  'Programming Language :: Python :: 3.6',
                  'Programming Language :: Python :: Implementation :: PyPy',
                  'License :: OSI Approved :: MIT License',
    ),
)
