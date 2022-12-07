import os
import gzip
import urllib.request

data_warehouse = os.path.join(os.getcwd(), 'data_warehouse')

# Download datasets from Kaggle and Make separate folders for each dataset:
# Large_Set: https://www.kaggle.com/datasets/saurabhbagchi/books-dataset/code
# Goodbooks-10k: https://www.kaggle.com/datasets/zygmunt/goodbooks-10k
# Define function to downlad datasets from kaggle, unzip them and create directories for them:

def download_dataset(url, file_name, dataset_name):
    # Create directory for the dataset:
    dataset_dir = os.path.join(data_warehouse, dataset_name)
    if not os.path.exists(dataset_dir):
        os.makedirs(dataset_dir)
    # Download dataset from kaggle:
    urllib.request.urlretrieve(url, os.path.join(dataset_dir, file_name))
    # Unzip the dataset:
    with gzip.open(os.path.join(dataset_dir, file_name), 'rb') as f_in:
        with open(os.path.join(dataset_dir, file_name[:-3]), 'wb') as f_out:
            f_out.write(f_in.read())


#Define main function to download datasets and place them in data_warehouse directory on Windows:

def main():
    # Create warehouse directory if it doesn't exist, and empty it if it does:
    if not os.path.exists(data_warehouse):
        os.makedirs(data_warehouse)

    # Download Large_Set dataset:
    download_dataset('https://www.kaggle.com/datasets/saurabhbagchi/books-dataset/code/files/Books%20Dataset.zip?download=true',
                     'Books Dataset.zip', 'Large_Set')
    # Download Goodbooks-10k dataset:
    download_dataset('https://www.kaggle.com/datasets/zygmunt/goodbooks-10k/code/files/goodbooks-10k.zip?download=true',
                     'goodbooks-10k.zip', 'Goodbooks-10k')

if __name__ == '__main__':
    main()