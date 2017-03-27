R语言读取文件（一）
================
newbiejasper
2017/3/25

1.读取excel文件
---------------

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

2.读取XML文件
-------------

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

开始读取文件，首先加载XML和RCurl包。

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

### XPATH语言介绍

XPATH是一门在XML文档中查找特定信息的语言，XPATH通过路径表达式，搜寻特定的元素和属性找到节点，这些路径表达式和我们电脑文件系统的路径表达式很相似。

#### XPATH的节点(Node)

XML文档是被作为节点树来对待的。我们通过XPATH语言查找特定的元素、属性和文本。树的根被称为文档节点或者根节点。

请看下面这个 XML 文档：

``` html
<?xml version="1.0" encoding="UTF-8"?>
<bookstore>
<book>
  <title lang="zhong">金融时间序列分析</title>
  <author>房小姜</author> 
  <year>2017</year>
  <price>30￥</price>
  <publisher>PKU</publisher>
</book>
</bookstore>
```

上面的XML文档中的节点例子中&lt;bookstore&gt;是根节点，&lt;publisher&gt;PKU&lt;/publisher&gt;是元素节点 lang="zhong"是属性节点， 基本值通常是在起始标签和结束标签之间的部分，像房小严，2017等都是基本值。

-   节点关系

    -   每个元素以及属性都有一个父节点，在上面的例子中，book元素是title、author、year、price以及publisher元素的父。title、author、year以及publisher元素都是book元素的子元素。子元素节点可有零个、一个或多个子元素。

    -   在上面的例子中，title、author、year、price以及publisher都是同胞，属于同一等级。

    -   某节点的父节点、父节点的父节点等叫做先辈。在上面的例子中，title元素的先辈是book元素和bookstore元素。
    -   bookstore的后代是book、title、author、year,publisher以及price元素。

#### XPATH语法

下面我们来介绍一下XPath的路径表达式。

##### XML实例文档

``` html
<?xml version="1.0" encoding="UTF-8"?>
<bookstore>
<book>
  <title lang="en">随机过程论</title>
  <price>30</price>
</book>
<book>
  <title lang="zh">应用随机分析</title>
  <price>35</price>
</book>
</bookstore>
```

##### 选取节点

XPath使用路径表达式在XML文档中选取节点。

下面列出了一些常见的路径表达式：

| 表达式   | 描述                     |
|----------|--------------------------|
| nodename | 选取此节点的所有子节点。 |
| /        | 从根节点选取。           |
| //       | 选取所有的指定节点。     |
| .        | 选取当前节点。           |
| ..       | 选取当前节点的父节点。   |
| @        | 选取属性。               |

例如，在下面的表格中，我们已列出了一些路径表达式以及相应的表达式的结果：

| 路径表达式      | 结果                                        |
|-----------------|---------------------------------------------|
| bookstore       | 选取bookstore元素的所有子节点。             |
| /bookstore      | 选取根元素 bookstore。                      |
| bookstore/book  | 选取属于bookstore的子元素中所有的book元素。 |
| //book          | 选取所有book元素。                          |
| bookstore//book | 选择属于bookstore元素的后代中所有book元素。 |
| <//@lang>       | 选取带有lang属性的所有元素。                |

##### 谓语（Predicates）

谓语用来查找某个特定的节点或者包含某个指定的值的节点。谓语被嵌在方括号中。在下面的表格中，我们列出了带有谓语的一些路径表达式，以及表达式的结果：

<table style="width:99%;">
<colgroup>
<col width="47%" />
<col width="51%" />
</colgroup>
<thead>
<tr class="header">
<th>路径表达式</th>
<th>结果</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>/bookstore/book[2]</td>
<td>选取属于bookstore子元素的第二个book 元素。</td>
</tr>
<tr class="even">
<td>/bookstore/book[last()]</td>
<td>选取属于bookstore子元素的最后一个book元素。</td>
</tr>
<tr class="odd">
<td>/bookstore/book[last()-1]</td>
<td>选取属于bookstore子元素的倒数第二个book元素。</td>
</tr>
<tr class="even">
<td>/bookstore/book[position()&lt;3]</td>
<td>选取最前面的两个属于bookstore元素的子元素的 book 元素。</td>
</tr>
<tr class="odd">
<td>//title<span class="citation">[@lang]</span></td>
<td>选取所有拥有名为lang的属性的title元素。</td>
</tr>
<tr class="even">
<td>//title<span class="citation">[@lang='eng']</span></td>
<td>选取所有title元素，且这些元素拥有值为eng的lang属性。</td>
</tr>
<tr class="odd">
<td>/bookstore/book[price&gt;35.00]</td>
<td>选取bookstore元素的所有book元素，且其中的price 元素的值须大于 35.00。</td>
</tr>
<tr class="even">
<td>/bookstore/book[price&gt;35.00]/title</td>
<td>选取 bookstore 元素中的 book 元素的所有 title 元素，且其中的price 元素的值须大于 35.00。</td>
</tr>
</tbody>
</table>

##### XPath的轴

轴可定义相对于当前节点的节点集。

| 轴名称             | 结果                                                     |
|--------------------|----------------------------------------------------------|
| ancestor           | 选取当前节点的所有先辈（父、祖父等）。                   |
| ancestor-or-self   | 选取当前节点的所有先辈（父、祖父等）以及当前节点本身。   |
| attribute          | 选取当前节点的所有属性。                                 |
| child              | 选取当前节点的所有子元素。                               |
| descendant         | 选取当前节点的所有后代元素（子、孙等）。                 |
| descendant-or-self | 选取当前节点的所有后代元素（子、孙等）以及当前节点本身。 |
| following          | 选取文档中当前节点的结束标签之后的所有节点。             |
| namespace          | 选取当前节点的所有命名空间节点。                         |
| parent             | 选取当前节点的父节点。                                   |
| preceding          | 选取文档中当前节点的开始标签之前的所有节点。             |
| preceding-sibling  | 选取当前节点之前的所有同级节点。                         |
| self               | 选取当前节点。                                           |

实例如下：

| 例子                   | 结果                                                               |
|------------------------|--------------------------------------------------------------------|
| child::book            | 选取所有属于当前节点的子元素的book节点。                           |
| attribute::lang        | 选取当前节点的lang属性。                                           |
| child::\*              | 选取当前节点的所有子元素。                                         |
| attribute::\*          | 选取当前节点的所有属性。                                           |
| child::text()          | 选取当前节点的所有文本子节点。                                     |
| child::node()          | 选取当前节点的所有子节点。                                         |
| descendant::book       | 选取当前节点的所有 book 后代。                                     |
| ancestor::book         | 选择当前节点的所有 book 先辈。                                     |
| ancestor-or-self::book | 选取当前节点的所有 book 先辈以及当前节点（如果此节点是 book 节点） |
| child::\*/child::price | 选取当前节点的所有 price 孙节点。                                  |

#### 用XPATH语言读取XML和html文档具体实例

``` r
zipcode <- xpathSApply(rootNode,"//zipcode",xmlValue)
head(zipcode)
```

    ## [1] "21206" "21231" "21224" "21211" "21223" "21218"

分析：这里采用的是xpathSApply函数，和R语言自带的apply函数很接近，这个语句的功能是遍历这个XML文档的所有节点，找到所有zipcode的节点，然后用xmlValue把值取出来，以向量的形式返回。我们可以通过head验证，发现结果确实是提取出了邮编zipcode。

``` r
xpathSApply(rootNode,'//row[@_id="1"]',xmlValue)
```

    ## [1] "41021206Frankford2NORTHEASTERN"

分析：这条语句是遍历rootNode，寻找属性值\_id="1"的row元素，并返回个子节点的值，你可以看到他返回的name，zipcode,neighborhood元素都同时返回到一条字符串里了。
