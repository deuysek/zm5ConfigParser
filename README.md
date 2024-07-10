# zm5ConfigParser
>analyse and split config files of zm5  
分析并导出造梦西游5配置数据

## Usage:
> Open configParser.py via python script editor,change the input_file to your config path like "cg1_20240701_2.swf",run the script and all config will be export to folder under the working directory.


## 使用方法：
>通过 python 脚本编辑器打开 configParser.py，将 input_file 变量改为配置文件路径，如 "cg1_20240701_2.swf"，运行脚本后，所有配置将导出到工作目录下的文件夹中。

## Environment:  

```console
$ python -m pip install -r requirements.txt
```

## 环境配置：
```console
$ python -m pip install -r requirements.txt
```

## ConfigFileCapture：
> Use fiddler to capture network traffic data is the best way. Find the cg****.swf file and save data to local. And also you can search the cache file on you computer. The cache file is usually in directory:
C:\Users\%username%\AppData\Local\Microsoft\Windows\INetCache\IE

## 造梦西游5配置文件获取
> 使用 fiddler 捕捉网络流量数据是最好的方法。找到 cg****.swf 文件并将数据保存到本地。也可以在电脑上搜索缓存文件。缓存文件通常位于：C:\Users\%username%\AppData\Local\Microsoft\Windows\INetCache\IE
