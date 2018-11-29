#!/bin/bash
#1. 创建一个用于存放编译结果的目录，例如build。
#2. 进入到上一部创建的build目录中，运行cmake ..来创建Makefile文件，可以通过传入`-DCMAKE_INSTALL_PREFIX=<install_dir>`来指定安装目录。
#3. 如果要全量构建，则调用make来进行整体的构建；如果要只构建某个cgi，则可以使用命令"make help | grep 该cgi去掉后缀之后的名称"获取构建对象的名称，然后运行"make 构建对象的名称"来构建。

#**可选参数**
#1. `CMAKE_INSTALL_PREFIX`，该参数表示执行`make install`时的安装目录，默认值为`/usr/local`
#2. `CMAKE_STATIC_LINK`, 该参数如果设置，则表示对依赖的外部库执行静态链接；否则执行动态链接

#usage
#  sh auto_make.sh all
#  sh auto_make.sh add_dev 

#set -x
if [ $# -lt 1 ]; then
    echo "default build all"
    cgi="all"
else
    cgi=$1
fi

work_path=$(dirname $(readlink -f $0))
cgi=${cgi//_cgi.cpp/}
cgi=${cgi//_cgi.h/}
cgi=${cgi//_cgi/}

cd ${work_path}
make clean
rm ${work_path}/CMakeCache*
rm ${work_path}/CMakeFiles -rf

#make symbol link for dependency
ln -s  /data/src/cdb2.0/cdb_mtnc/dependencies  /usr/local/cdb5/dependencies 

#全量构建：
if [ $cgi == "all" ] ; then 
    rm ${work_path}/build -rf
    mkdir -p ${work_path}/build
    cd ${work_path}/build
    install_dir="/usr/local/cdb_mtnc"
    cmake -DCMAKE_INSTALL_PREFIX=${install_dir} -DCMAKE_STATIC_LINK=1 ..
    make -j8
    make install
else
    #单独构建(暂时还没有实现单独install的功能)：
    #rm ${work_path}/build -rf
    #mkdir -p ${work_path}/build
    cd ${work_path}/build
    install_dir="/usr/local/cdb_mtnc"
    cmake -DCMAKE_INSTALL_PREFIX=${install_dir} -DCMAKE_STATIC_LINK=1 ..
    built_cgi=`make help | grep $cgi` #self_built_trsf_inst 查看到需要构建的对象名称为task_exec_self_built_trsf_inst
    var=${built_cgi//.../ }
    for item in $var
    do 
        echo "$item"
        make -j8 $item 
        #make install
    done
fi
