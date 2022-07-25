import zipfile
import tempfile
import os
import shutil
from shutil import copy


# folder compression
def zipDir(dirpath='source_dir', outFullName='targetzip'):
    """
    folder compression
    :param dirpath: target path
    :param outFullName: path to save +xxxx.zip
    :return:
    """
    with zipfile.ZipFile(outFullName, "w", zipfile.ZIP_DEFLATED) as zf:
        for path, dirnames, filenames in os.walk(dirpath):
            # remove the target and path, only compress the subfolders and files in this folder
            fpath = path.replace(dirpath, '')
            for filename in filenames:
                zf.write(os.path.join(path, filename), os.path.join(fpath, filename))
    zf.close()
    print(r"folder\"{0}\" was zipped into\"{1}\".".format(dirpath, outFullName))

if __name__ == "__main__":
    project_folder = os.path.split(os.path.realpath(__file__))[0]  # checkpoints(including long name folders)
    # Use temporary dir
    # compress checkpoints folders under temp folders, and then add the .py scripts
    for each_folder in os.listdir(project_folder + r'/sample/checkpoints/'):
        with tempfile.TemporaryDirectory() as tmp_dir:
            source_path = os.path.abspath(project_folder + r'/sample/checkpoints/' + each_folder)
            target_path = os.path.abspath(tmp_dir + r'/checkpoints/' + each_folder)
            # print(source_path)
            # print(target_path)
            if not os.path.exists(target_path):
                os.makedirs(target_path)
            if os.path.exists(source_path):
                shutil.rmtree(target_path)
            shutil.copytree(source_path, target_path)
            zipDir(dirpath=tmp_dir, outFullName=project_folder + r'/paddle_' + each_folder + '.zip')
    # To this step, all checkpoints are compressed. Following append .py files

    zip_list = []
    for file in os.listdir(project_folder):
        if os.path.splitext(file)[1] == '.zip':
            zip_list.append(file)
    prepare_file = project_folder + r'/sample/prepare.py'
    for zips in zip_list:
        z = zipfile.ZipFile(zips, 'a')  # a(append) files into zip
        z.write(prepare_file, arcname='prepare.py', compress_type=zipfile.ZIP_DEFLATED)
        z.write(r'predict.py', arcname='predict.py', compress_type=zipfile.ZIP_DEFLATED)
        z.write(r'model.py', arcname='model.py', compress_type=zipfile.ZIP_DEFLATED)
        z.write(r'common.py', arcname='common.py', compress_type=zipfile.ZIP_DEFLATED)
        z.write(r'wind_turbine_data.py', arcname='wind_turbine_data.py', compress_type=zipfile.ZIP_DEFLATED)
        z.close()
        print('Submission formatted .zip finished! ({})'.format(zips))
        
    # run eval(unable for some reason)
    # zip_list = []
    # score_list = []
    # for file in os.listdir():
    #     if file.endswith(".zip"):
    #         zip_list.append(file)
    #         score_list.append(evaluation.eval(file)['score'])
    # print(score_list)
