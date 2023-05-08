import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    version="1.0.0",
    name="rouge_score",
    author="Google LLC",
    description="Multilingual ROUGE score based on Google rouge_score and xl-sum",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['rouge_score'],
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
        "pythainlp",
#         "pyonmttok",
        "jieba",
#         "fugashi[unidic]"
    ],
    python_requires='>=3.6',
)
