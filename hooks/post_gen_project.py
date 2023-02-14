import os
import shutil


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


def remove_folder(folder_path):
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, folder_path))


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


def delete_spidermon_specific_files():
    """Deletes files and folders exclusively used by Spidermon"""
    remove_file("{{cookiecutter.__project_slug}}/monitors.py")
    remove_folder("{{cookiecutter.__project_slug}}/templates")


if "{{ cookiecutter.deploy_to_scrapy_cloud }}".lower() == "y":
    set_scrapy_cloud_project_id()
else:
    delete_scrapy_cloud_specific_files()


if "{{ cookiecutter.use_spidermon }}".lower() != "y":
    delete_spidermon_specific_files()
