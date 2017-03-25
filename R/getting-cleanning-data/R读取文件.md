R语言读取文件
================
newbiejasper
2017/3/25

读取excel文件
-------------

读取excel文件文件其实有很多的包可以做到，最常用的就是xlsx和readxl, 首先，安装并载入读取excel文件所用的包：

``` r
install.packages("xlsx")
library(xlsx)
```

或者，

``` r
install.packages("readxl")
library(readxl)
```

### 两个包的基本介绍

-   xlsx是用R把excel文件中的工作表以data.frame的格式读入R语言，他有两个常用函数，其中read.xlsx2通常会比read.xlsx读取的速度更快一些，因为它的好多工作是利用Java完成的，所以速度有所提升，但是在读取子数据集的时候没有read.xlsx稳定性好。

read.xlsx(file, sheetIndex, sheetName=NULL, rowIndex=NULL, startRow=NULL, endRow=NULL, colIndex=NULL, as.data.frame=TRUE, header=TRUE, colClasses=NA, keepFormulas=FALSE, encoding="unknown", ...)

read.xlsx2(file, sheetIndex, sheetName=NULL, startRow=1, colIndex=NULL, endRow=NULL, as.data.frame=TRUE, header=TRUE, colClasses="character", ...)

注：
1. sheetIndex:工作表单号
2. rowIndex:行号，就是你想读取那些行
3. header:表头，就是有没有列名。比如姓名，年龄，学号等
4. startRow:比如你想从第五行开始读取，就设置startRow = 5

-   readxl包可以用来读取xls和xlsx格式的文件

read\_excel(path, sheet = 1, col\_names = TRUE, col\_types = NULL, na = "", skip = 0)

注：
1. sheet：读取的工作表
2. col\_names: 如果是FALSE的话，就表示第一行不是列名，R会自动给你取成x1,x2...
3. colt\_types: blank,numeric,date,text
4. na: 缺失值，默认空着的单元是缺失值，你也可以自己指定，比如认为999是缺失值

读取XML文件
-----------

### XML文件简介

在计算机领域，XML(extensible markup language)指的是可扩展标记语言，类似于HTML，它设计的宗旨是传输数据，而不是显示数据，所以这也是它和HTML的一个明显的差别。另外一个差别是XML的标签没有被预定义，我们可以根据自己的需要自行设计标签名字，所以具有自我描述性。

### 一个具体的例子

``` html
<?xml version="1.0" encoding="UTF-8"?>   
<message>   
<to>房，姜\</to>    
<from>高\</from>   
<heading>午餐\</heading>   
<content time="noon">中午怎么吃？点外卖？小白房？还是食堂？\</content>   
</message>  
```

以上就是一个XML的例子，它拥有发送者和接受者，标题，内容等信息，所以自我描述非常清晰。但是这个文档实际上只是包装了一些数据信息，而并没有做任何传输、接收和显示文档的信息，也就说你可以把他当成一个纯文本。纯文本的特点会让你在不同的操作系统进行数据共享的门槛大大降低。

### XML结构

-   XML文档是一种树结构，从根部开始扩展到枝叶。第1行是XML声明，它定义版本和编码。第2行是根元素，和第7行相对应，&lt;message&gt;叫做起始标签，&lt;/message&gt;叫做结束标签，结束标签有一个"/"符号。

-   XML文档必须包含根元素，所有元素都可以拥有子元素。

-   XML文档均可拥有文本内容和属性。例如content元素下，属性time为noon，属性值要加引号。

-   XML文档元素必须要有结束标签，标签对大小写敏感，而且必须正确嵌套，也就是说一个标签必须完整地嵌套在另一个标签里。

### 开始读取文件，首先加载XML和RCurl包。

``` r
library(XML)
library(RCurl)
```

    ## Loading required package: bitops

``` r
url <- "https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Frestaurants.xml"
file_url <- getURL(url)
doc <- xmlTreeParse(file_url,useInternal=TRUE)
rootNode <- xmlRoot(doc)
```

注意：这里，url是https传输的，xmlTreeParse不支持，会报出不是一个XMl文档的错误，所以我们需要先用getURL处理一下，然后用xmlTreeParse函数读取，如果是http的话，就可以直接把url传入xmlTreeParse函数。现在你可以把doc想象成一棵大树，也就是XML文档的树结构，xmlRoot就是获取文档节点的函数。

``` r
xmlName(rootNode)
```

    ## [1] "response"

``` r
names(rootNode)
```

    ##   row 
    ## "row"

这里，我们通过xmlName函数获取根节点的名称是response,根节点下面包括叫做row的子节点。下面，我们分析一下如下的操作：

``` r
rootNode[[1]][[1]][[1]]
```

    ## <name>410</name>

我们在选择xml文档的节点时可以采用如上的类似于R语言中列表元素的索引。其中rootNode\[\[1\]\]我们选择的进入根节点response下面的第一个子节点，就是"row"节点，rootNode\[\[1\]\]\[\[1\]\]进入的就是row节点下的第一个子节点，也叫做row,rootNode\[\[1\]\]\[\[1\]\]\[\[1\]\],进入的是这个row节点下的第一个子节点就是name节点。所以我们获得了如上的name元素。
