import os


PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def replace_string_in_file(filepath, to_replace, replacement):
    full_path = os.path.join(PROJECT_DIRECTORY, filepath)
    with open(full_path, "r") as f:
        text = f.read()
    text = text.replace(to_replace, replacement)
    with open(full_path, "w") as f:
        f.write(text)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def set_scrapy_cloud_project_id():
    """Obtain Scrapy Cloud project ID from user and write it to scrapinghub.yml"""
    scrapy_cloud_project_id = input("Scrapy Cloud Project ID: ")
    replace_string_in_file(
        "scrapinghub.yml", 
        "__scrapy_cloud_project_id__", 
        scrapy_cloud_project_id,
    )


def delete_scrapy_cloud_specific_files():
    """Deletes files exclusively used by Scrapy Cloud"""
    remove_file("scrapinghub.yml")
    remove_file("requirements_scrapinghub.txt")


def set_kaggle_urls():
    """Obtain Kaggle URLs for Dataset and Notebook from user and write to README.md"""
    kaggle_dataset_url = input("Kaggle Dataset URL: ")
    replace_string_in_file(
        "README.md", 
        "__kaggle_dataset_url__", 
        kaggle_dataset_url,
    )
    kaggle_notebook_url = input("Kaggle Notebook URL: ")
    replace_string_in_file(
        "README.md", 
        "__kaggle_notebook_url__", 
        kaggle_notebook_url,
    )


if "{{ cookiecutter.deploy_to_scrapy_cloud }}".lower() == "y":
    set_scrapy_cloud_project_id()
else:
    delete_scrapy_cloud_specific_files()


if "{{ cookiecutter.host_on_kaggle }}".lower() == "y":
    set_kaggle_urls()
