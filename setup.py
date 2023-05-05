import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mrouge",
    author="Google LLC",
    description="Multilingual ROUGE score based on Google rouge_score and xl-sum",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['mrouge'],
    package_dir = {'rouge_score':''},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License"
    ],
    install_requires=[
        "absl-py",
        "nltk",
        "numpy",
        "six>=1.14.0",
        "git+https://github.com/otuncelli/turkish-stemmer-python",
        "git+https://github.com/abhik1505040/bengali-stemmer",
        "pythainlp",
        "pyonmttok",
        "jieba",
        "fugashi[unidic]"
    ],
    python_requires='>=3.6',
)