import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="converse",
    version="0.1a4",
    author="Hrishi Olickel",
    author_email="hrishioa@gmail.com",
    description="Conversational Analytics and Plotting Library",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/hrishioa/converse",
    packages=setuptools.find_packages(),
    install_requires=[
        'plotly',
        'textblob',
        'fuzzywuzzy[speedup]',
        'tqdm',
        'pandas'
    ],
    keywords=["sentiment","messenger","chatbot","sentiment-analysis"],
    license="GNU General Public License v3",
    classifiers=[
        "Programming Language :: Python :: 2",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
