#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import os
import shutil
import argparse

"""
for i in `find .   -maxdepth 1  | awk -F '/' '{ print $2 }' | grep -v "\ "`; do  
    echo "-----------------------------------------$i---------------------------------"; 
    python gen_dao.py  --dir=$i ; done

可自动生成dao文件，并移动到public目录下[cdb_mtnc/public/db_access/xxx]：
   1.通过sql文件生成model及mappers，并生成dao文件 【较少用】
        python gen_dao.py  --dir=test --sql=yes
   2.根据models及mappers生成dao文件  【常用】
        python gen_dao.py  --dir=test
"""

step = 0

def red_print(msg):
    global step
    step += 1
    print("\033[0;33;40m\t" + str(step) + msg + "\033[0m")  
def yellow_print(msg):
    print("\033[0;31;40m\tError: " + msg + "\033[0m")  

def copy_files(src_dir, dest_dir):  
     for file in os.listdir(src_dir): 
         if file == "daos.h":
            continue
         src_file = os.path.join(src_dir, file) 
         dest_file = os.path.join(dest_dir, file) 
         if os.path.isfile(src_file): 
             if not os.path.exists(dest_dir): 
                 os.makedirs(dest_dir) 
             if not os.path.exists(dest_file) or(os.path.exists(dest_file) and (os.path.getsize(dest_file) != os.path.getsize(src_file))): 
                     open(dest_file, "wb").write(open(src_file, "rb").read()) 
         if os.path.isdir(src_file): 
             copyFiles(src_file, dest_file) 

def gen_dao():
    path = os.getcwd() + "/" + args.dir
    os.chdir(path)
    flag = False
    if not os.path.exists('cowboy'):
        red_print(".create cowboy link.")
        os.symlink("../../cowboy", "cowboy")
    if args.sql:
        red_print(".update models and mappers by sql ")
        flag = os.system("./cowboy -u -o -x -m")
    else:
        red_print(".gen dao.cpp from mappers and models ")
        flag = os.system("./cowboy -o -x -m")
    if not flag:
        red_print(".gen dao files done")
        move_dao_files()
    else:
        yellow_print("gen dao files err ")
        exit(-1)

def move_dao_files():
    cur_path = os.getcwd()
    #yellow_print(path)
    path = cur_path.split("tools")[0]
    #yellow_print(path)
    global dest_dir
    dest_dir = path + "public/db_access/" + args.dir
    red_print(".move dao files to: " + dest_dir )
    os.popen("rm -rf " + dest_dir) 
    os.system("mkdir " + dest_dir)
    copy_files("dao",    dest_dir)
    copy_files("model",  dest_dir)
    copy_files("mapper", dest_dir)


def parse_options():
    global args
    info = """1.python gen_dao.py --dir=xxxx  --sql=yes 
       2.python gen_dao.py --dir=xxxx  """    
    parser = argparse.ArgumentParser(usage=info, description="")
    parser.add_argument("--dir",  required=True, help="\tgen dao.cpp from which dir.", dest="dir")
    parser.add_argument("-sql", "--sql", default=False, dest="sql", help="\tupdate models and mappers by sql.")
    args = parser.parse_args()
    if not os.path.exists(args.dir):
        yellow_print("dir "  + args.dir + " not exits!")
        exit()


if __name__ == '__main__':
    parse_options()
    gen_dao()
    red_print(".all done ")
    print("new files:__________________________")
    os.system("ls -l --full-time " + dest_dir)
