# Markdown转pdf文档配置
## 安装依赖包
* pip install markdown2pdf
* 注意：安装过程中可能报如下错误：

	Collecting cairocffi>=0.5 (from weasyprint->markdown2pdf)
  Using cached cairocffi-0.7.2.tar.gz
    Complete output from command python setup.py egg_info:
    Package libffi was not found in the pkg-config search path.
    Perhaps you should add the directory containing `libffi.pc'
    to the PKG_CONFIG_PATH environment variable
    No package 'libffi' found
    Package libffi was not found in the pkg-config search path.
    Perhaps you should add the directory containing `libffi.pc'
    to the PKG_CONFIG_PATH environment variable
    No package 'libffi' found
    Package libffi was not found in the pkg-config search path.
    Perhaps you should add the directory containing `libffi.pc'
    to the PKG_CONFIG_PATH environment variable
    No package 'libffi' found
    Package libffi was not found in the pkg-config search path.
    Perhaps you should add the directory containing `libffi.pc'
    to the PKG_CONFIG_PATH environment variable
    No package 'libffi' found
    Package libffi was not found in the pkg-config search path.
    Perhaps you should add the directory containing `libffi.pc'
    to the PKG_CONFIG_PATH environment variable
    No package 'libffi' found
    c/_cffi_backend.c:15:17: 致命错误：ffi.h：没有那个文件或目录
     #include <ffi.h>
                     ^
    编译中断。
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
      File "/tmp/pip-build-0DPWM5/cairocffi/setup.py", line 65, in <module>
        **cffi_args
      File "/usr/lib64/python2.7/distutils/core.py", line 112, in setup
        _setup_distribution = dist = klass(attrs)
      File "/usr/lib/python2.7/site-packages/setuptools/dist.py", line 269, in __init__
        self.fetch_build_eggs(attrs['setup_requires'])
      File "/usr/lib/python2.7/site-packages/setuptools/dist.py", line 313, in fetch_build_eggs
        replace_conflicting=True,
      File "/usr/lib/python2.7/site-packages/pkg_resources/__init__.py", line 826, in resolve
        dist = best[req.key] = env.best_match(req, ws, installer)
      File "/usr/lib/python2.7/site-packages/pkg_resources/__init__.py", line 1092, in best_match
        return self.obtain(req, installer)
      File "/usr/lib/python2.7/site-packages/pkg_resources/__init__.py", line 1104, in obtain
        return installer(requirement)
      File "/usr/lib/python2.7/site-packages/setuptools/dist.py", line 380, in fetch_build_egg
        return cmd.easy_install(req)
      File "/usr/lib/python2.7/site-packages/setuptools/command/easy_install.py", line 640, in easy_install
        return self.install_item(spec, dist.location, tmpdir, deps)
      File "/usr/lib/python2.7/site-packages/setuptools/command/easy_install.py", line 670, in install_item
        dists = self.install_eggs(spec, download, tmpdir)
      File "/usr/lib/python2.7/site-packages/setuptools/command/easy_install.py", line 850, in install_eggs
        return self.build_and_install(setup_script, setup_base)
      File "/usr/lib/python2.7/site-packages/setuptools/command/easy_install.py", line 1078, in build_and_install
        self.run_setup(setup_script, setup_base, args)
      File "/usr/lib/python2.7/site-packages/setuptools/command/easy_install.py", line 1066, in run_setup
        raise DistutilsError("Setup script exited with %s" % (v.args[0],))
    distutils.errors.DistutilsError: Setup script exited with error: command 'gcc' failed with exit status 1
    
    ----------------------------------------
	Command "python setup.py egg_info" failed with error code 1 in /tmp/pip-build-0DPWM5/cairocffi/

* 这是因为安装过程中会编译一些东西，如果依赖没解决则可能编译失败，这种情况下可百度一下该安装哪些依赖包，我安装时还另外安装了python开发包`yum insatll python-devel`和`yum install libffi-devel`。

## 由md文件转pdf文件
* 一般转换

	`md2pdf resume.md`
* 指定样式转换

	`md2pdf resume.md --theme=github`
* 自定义样式转换

	`md2pdf resume.md --theme=path_to_style.css`

![test_pic](test.jpg)
