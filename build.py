from pybuilder.core import use_plugin, init, Author

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
#use_plugin("python.flake8")
#use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin("python.pydev")
use_plugin("copy_resources")
#use_plugin('filter_resources')

name = "lldecaf"
version = "0.1.0"
summary = "Decaf compiler using llvm"
description = "Decaf compiler over llvm"
authors = [Author("Sergio Pino", "spino327@gmail.com")]
url = "https://github.com/spino327/lldecaf"
license = "..."

default_task = "publish"

@init
def initialize(project):
    # dependencies
    project.build_depends_on('mockito')
    project.build_depends_on(name = 'ply', version = '3.8')
    
    # project properties
    project.set_property("copy_resources_target", "$dir_dist")
    list_res = []
#     res_path = "resources/*/"
    res_path = "resources/samples/"
    list_res.append(res_path + "*.decaf")
    list_res.append(res_path + "*.out")
#     list_res.append("*.md")
    list_res.append("README.md")
    project.set_property("copy_resources_glob", list_res)
