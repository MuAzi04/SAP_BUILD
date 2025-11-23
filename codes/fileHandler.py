import requests
import zipfile
import shutil
import os

def folder_to_zip(folder_path, zip_path):

    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"Folder '{folder_path}' does not exist.")

    # Create zip file
    shutil.make_archive(zip_path, 'zip', folder_path)

def unzip_file(zip_path, extract_to):
    if not os.path.exists(zip_path):
        raise FileNotFoundError(f"Zip file '{zip_path}' does not exist.")
    
    # Ensure the extraction folder exists
    os.makedirs(extract_to, exist_ok=True)
    
    # Extract the zip file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    
    print(f"Zip file '{zip_path}' extracted to '{extract_to}'")

def remove_path(path):
    if not os.path.exists(path):
        print(f"Path '{path}' does not exist.")
        return

    if os.path.isfile(path):
        os.remove(path)
        print(f"File '{path}' has been removed.")
    elif os.path.isdir(path):
        shutil.rmtree(path)
        print(f"Folder '{path}' and all its contents have been removed.")
    else:
        print(f"Path '{path}' is not a file or folder and cannot be removed.")

def uzip_and_remove(zip_path, extract_to):
    unzip_file(zip_path, extract_to)
    remove_path(zip_path)

def zip_and_remove(folder_path, zip_path):
    folder_to_zip(folder_path, zip_path)
    remove_path(folder_path)

def get_file(url, save_path):
    # Ensure the folder exists
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"File downloaded successfully to '{save_path}'")
    else:
        raise Exception(f"Failed to download file. Status code: {response.status_code}")

def download_mtar(url, save_path):
    
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f".mtar file downloaded to '{save_path}'")
    else:
        raise Exception(f"Failed to download file. Status code: {response.status_code}")