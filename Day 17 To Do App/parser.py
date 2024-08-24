import zipfile as zp
import pathlib

def make_archive(filepaths,dest_dir):
    dest_path = pathlib.Path(dest_dir,"compressed.zip")
    with zp.ZipFile(dest_path,'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)
