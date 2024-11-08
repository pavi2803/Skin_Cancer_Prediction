import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()



__version__ = "0.0.0"

REPO_NAME = "Skin_Cancer_Prediction"
AUTHOR_USER_NAME = "pavi2803"
SRC_REPO = "skindisease"
AUTHOR_EMAIL = "pavi2468kuk@gmail.com"



setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="skin cancer identification using images",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)