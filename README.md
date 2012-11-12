Fake SYSUJWXT
=============

Python wrapper for SYSUJWXT API

声明：使用本API造成的一切后果自负。

原理
----

使用python的pycurl库模拟http登录教务系统，其中大部分功能都是通过json通信的，但是json是非标准的，只有javascript可以解析。

你可以用这个库实现任何和python相关的服务，比如用python web框架搭建一个自用教务系统的网站或搭建一个云服务提供api给手机app调用。

功能
----

- 查询分数
- 查询课表
- 查询学分与绩点
- 可选课程与选课
- 选课结果与退课
- 修改密码

TODO
----

- 评教

Change log
----------

2012 10 16 - 0.1

- Initial Commit

2012 10 31 - 0.2

- 添加计算GPA和学分的功能


License
-------

[MIT License](http://www.opensource.org/licenses/mit-license.php)

&copy; 2011-2012 Maple Valley &lt;maplevalley8@gmail.com&gt;

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


没有找到文档？Learn to Read the Source, Luke
