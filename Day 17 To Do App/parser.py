import zipfile
import pathlib

def make_archive(filepaths,dest_dir):
    dest_path = pathlib.Path(dest_dir,"compressed.zip")
    with zipfile.ZipFile(dest_dir,'w') as archive:
        #filepath = pathlib.Path(filepath)
        for filepath in filepaths:
            archive.write(filepath)
