import os
from zipfile import Path
import time
from ner.logger import logging


class GCloud:
    def sync_folder_to_gcloud(self, gcp_bucket_url, filepath, filename):

        command = f"gsutil cp {filepath}/{filename} gs://{gcp_bucket_url}/"
        os.system(command)



    def sync_folder_from_gcloud(
        self, gcp_bucket_url: str, filename: str, destination: Path
    ):
        destination = os.path.join(os.getcwd(), destination)
        # Save current umask
        old_umask = os.umask(0)
        os.makedirs(destination, exist_ok=True)
        command = f"gsutil cp gs://{gcp_bucket_url}/{filename} {destination}"
        logging.info(destination)
        # Restore old umask
        os.system(command)



