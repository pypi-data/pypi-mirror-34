import os
import shutil

# third party
import requests
import pandas as pd

# internal
from deep_teaching_commons import config


class Iris:
    def __init__(self, base_data_dir=None, auto_download=True, verbose=True):
        self.base_data_dir = base_data_dir if base_data_dir else config.BASE_DATA_DIR
        self.data_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

        self.verbose = verbose

        self.data_dir = os.path.join(self.base_data_dir, 'Iris')
        self.data_path = os.path.join(self.data_dir, 'iris.data')

        if auto_download:
            if self.verbose:
                print('auto download is active, attempting download')
            self.download()

    def download(self):
        # download data if directory does not yet exist
        if os.path.exists(self.data_dir):
            if self.verbose:
                print('data directory already exists, no download required')
        else:
            if self.verbose:
                print('data directory does not exist, starting download')

            # create directory
            os.makedirs(self.data_dir)

            try:
                # stream download
                r = requests.get(self.data_url, stream=True)
                r.raise_for_status()
                with open(self.data_path, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=4096):
                        if chunk:
                            f.write(chunk)
                r.raise_for_status()
            except:
                shutil.rmtree(self.data_dir)
                raise

            if self.verbose:
                print('data successfully downloaded')

    def dataframe(self):
        iris = pd.read_csv(self.data_path, header=None)
        header = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
        iris.columns = header
        return iris
