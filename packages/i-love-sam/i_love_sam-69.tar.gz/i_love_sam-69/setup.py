import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='i_love_sam',
    version='69',
    #packages=['antibody_ngs_pipeline',],
    description='I love sam',
    author="nilloc",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    license='MIT License',
    scripts=['bin/i_love_sam'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
