# ApiMeter
[![pipeline status](https://git.umlife.net/qa/YmApiMeter/badges/master/pipeline.svg)](https://git.umlife.net/qa/YmApiMeter/commits/master)
[![coverage report](https://git.umlife.net/qa/YmApiMeter/badges/master/coverage.svg)](https://git.umlife.net/qa/YmApiMeter/commits/master)

ApiMeter 是一款面向 HTTP(S) 协议的通用测试框架，只需编写维护一份 YAML/JSON 脚本，即可实现自动化测试、性能测试、线上监控、持续集成等多种测试需求。基于 Python 开发，支持 Python 2.7和3.3以上版本，可运行于 macOS、Linux、Windows平台。 

### 一、安装方式
```
pip install ApiMeter
```

### 二、版本升级
```
pip install -U ApiMeter
```

### 三、使用方式
在 ApiMeter 安裝成功后，可以使用 apimeter、ymapi、ymapimeter 命令进行调用，如：
```
$ apimeter -V
1.0.0

$ ymapi -V
1.0.0

$ ymapimeter -V
1.0.0

$ apimeter -h
usage: main.py [-h] [-V] [--no-html-report]
               [--html-report-name HTML_REPORT_NAME]
               [--html-report-template HTML_REPORT_TEMPLATE]
               [--log-level LOG_LEVEL] [--log-file LOG_FILE]
               [--dot-env-path DOT_ENV_PATH] [--failfast]
               [--startproject STARTPROJECT]
               [--validate [VALIDATE [VALIDATE ...]]]
               [--prettify [PRETTIFY [PRETTIFY ...]]]
               [testset_paths [testset_paths ...]]

One-stop solution for HTTP(S) testing.

positional arguments:
  testset_paths         testset file path

optional arguments:
  -h, --help            show this help message and exit
  -V, --version         show version
  --no-html-report      do not generate html report.
  --html-report-name HTML_REPORT_NAME
                        specify html report name, only effective when
                        generating html report.
  --html-report-template HTML_REPORT_TEMPLATE
                        specify html report template path.
  --log-level LOG_LEVEL
                        Specify logging level, default is INFO.
  --log-file LOG_FILE   Write logs to specified file path.
  --dot-env-path DOT_ENV_PATH
                        Specify .env file path, which is useful for keeping
                        production credentials.
  --failfast            Stop the test run on the first error or failure.
  --startproject STARTPROJECT
                        Specify new project name.
  --validate [VALIDATE [VALIDATE ...]]
                        Validate JSON testset format.
  --prettify [PRETTIFY [PRETTIFY ...]]
                        Prettify JSON testset format.

$ ymapimeter test_file.yml or test_file.ymal or test_file.json or test_dir/
test result and report ...
```     

### 四、开发者模式
1、ApiMeter使用 pipenv 对依赖包进行管理，如果你没有安装，安装命令如下：
```
pip install pipenv
```
2、拉取 ApiMeter 源代码：
```
git clone git@git.umlife.net:qa/YmApiMeter.git
```
3、进入仓库目录，安装依赖：
```
cd YmApiMeter/
pipenv install --dev
```
4、进入测试目录，运行单元测试：
```
export PYTHONPATH=`pwd`
cd tests/
# 直接命令行输出测试结果
pipenv run python -m unittest discover

或

# 当前目录输出测试报告unit_test_report.html
pipenv run python all_test.py   

或

# 计算单元测试覆盖率，在当前目录下生成.coverage统计结果文件
pipenv run coverage run --source=../apimeter -m unittest discover  
# 命令行中输出直观的文字报告
pipenv run coverage report -m  
# 将统计结果转化为HTML报告，在当前目录下生成htmlcov报告目录，查看里面的index.html文件即可
pipenv run coverage html  
```
5、进入仓库目录，进行代码规范检测：
```
# 直接命令行中输出结果
pipenv run python -m flake8  

或

# 通过flake8chart插件将结果转化为csv表格和svg图片
pipenv run python -m flake8 --statistics | flake8chart --chart-type=PIE --chart-output=flake8_pie_report.svg --csv-output=flake8_data.csv

或

# 通过flake8_formatter_junit_xml插件将结果转化为junit格式报告
pipenv run python -m flake8 --format junit-xml --output-file flake8_junit_report.xml

或

# 通过falke8-junit-report插件将结果转化为junit格式报告
pipenv run python -m flake8 --output-file flake8.txt
pipenv run python -m flake8_junit flake8.txt flake8_junit_report.xml 
```
6、开发调试，运行方式：
```
pipenv run python main.py apimeter -h
```


### 五、一键上传 PYPI 并打 TAG
每次在 __about__.py 更新版本号后，运行以下命令，实现自动化打包上传 PYPI ，同时根据版本号自动打 TAG 并推送到仓库：
```
pipenv run python setup.py upload
```