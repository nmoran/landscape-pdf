import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="landscape_pdf", # Replace with your own username
    version="0.0.2",
    author="Niall Moran",
    author_email="niall@niallmoran.net",
    description="Utility to convert a pdf for viewing in landscape mode",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nmoran/landscape-pdf",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    scripts=['bin/landscape-pdf'],
    python_requires='>=3.6',
    install_requires=[
          'PyPDF2',
      ],
)