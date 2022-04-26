import os.path
import shutil

prj_name = 'my_project'
tmpl_name = 'templates'
root_dir = os.path.join(os.path.curdir, prj_name)
tmpl_dir = os.path.join(root_dir, tmpl_name)

if not os.path.exists(tmpl_dir):
    os.makedirs(tmpl_dir)

for root, dirs, files in os.walk(root_dir):
    if tmpl_name in root:
        for file in files:
            src_file = os.path.join(root, file)
            dst_dir = os.path.join(tmpl_dir, os.path.basename(root))
            dst_file = os.path.join(dst_dir, file)
            if not os.path.exists(dst_dir):
                os.makedirs(dst_dir)
                print(f'mkdir {dst_dir}')
            if not src_file == dst_file and not os.path.exists(dst_file):
                shutil.copy(src_file,dst_file)
                print('Copy', src_file,'>',dst_file)
