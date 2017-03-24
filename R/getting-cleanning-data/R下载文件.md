用R语言进行文件下载
================
newbiejasper
2017年3月24日

1. 检查文件路径是否存在
-----------------------

-   在开始下载文件之前，你首先应该知道自己工作目录，可以通过下面的代码打印出自己的working directory.

``` r
getwd()
```

-   为了从网上下载文件，我们一般都会将文件保存在我们的工作目录下，或者在工作目录下新建一个文件夹，用于存放下载的数据文件，所以我们需要先确保你要给数据文件的命名不能和其他文件重复。

``` r
file.exists("data")
```

    ## [1] FALSE

-   **FALSE**意味着没有叫做data的文件，所以我们可以很放心的新建叫做data的文件夹。

``` r
dir.create("data")
```

2. 开始下载文件
---------------

下载文件，我们需要用到的是downlaod.file()命令，它的主要参数如下：
\* url:文件下载链接的字符串。
\* destfile:目标文件，决定存放你下载的文件的位置。
\* method:下载文件的方法，注意在mac上遇到以https开头的链接要采用curl的method

3. 具体例子
-----------

这里我们以[Baltimore网站](https://data.baltimorecity.gov/Transportation/Baltimore-Fixed-Speed-Cameras/dz54-2aru)为例，在Export下有很多可供选择的下载格式CSV，Json,Xml等，右击复制下载链接，复制给url。

``` r
url = "https://data.baltimorecity.gov/api/views/dz54-2aru/rows.csv?accessType=DOWNLOAD"
download.file(url,destfile = "./data/camera.csv",method='curl')
list.files("./data")
```

    ## [1] "camera.csv"

这里出现camera.csv表示data文件夹下已经成功下载了文件。
