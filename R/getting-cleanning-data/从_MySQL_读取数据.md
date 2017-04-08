从 mysql 读取数据
================
newbiejasper
2017/4/9

MySQL是什么东西？
=================

1.  免费的且广泛使用的开源数据库软件
2.  广泛应用于基于网络的应用
3.  数据被存储在数据库(data.table)中，数据库中存在着很多的表(table)，表包含列(column)和行(row)，列也叫做字段(fields)，行也叫做记录(record),列一般都是作为变量名的，例如姓名，性别，id等。

需要的R语言包
=============

``` r
library("RMySQL")
```

    ## Loading required package: DBI

本文连接的数据库
================

[一个具体的面向网页的MySQL数据库](http://genome.ucsc.edu/goldenPath/help/mysql.html)。这里告诉我们 连接它数据库的方式为：
mysql --user=genome --host=genome-mysql.soe.ucsc.edu -A

开始使用 R语言进行连接
======================

``` r
ucscdb <- dbConnect(MySQL(),user="genome",host="genome-mysql.soe.ucsc.edu")
result <- dbGetQuery(ucscdb,"SHOW DATABASES;")
dbDisconnect(ucscdb)
```

    ## [1] TRUE

这里，给出一些具体说明：
\* MySQL( )代表的是dbConnect函数连接的数据库类型，可以是oracle，mysql等
\* user 是用户名，host 是数据库的网络位置，如果是本地的，需要的参数是 password
\* dbGetQuery是数据库查询命令，"SHOW DATABASES;"是数据库查询命令，遵循的是Mysql语法和R 语言没有关系。
\* 查询结束之后注意断开连接,会返回一个 TRUE 值
\* result 里包含了这个host下所有的数据库 database

下面我们进入某一个数据库
------------------------

``` r
hg19 <- dbConnect(MySQL(),user="genome",host="genome-mysql.soe.ucsc.edu",db="hg19")
all_tables <- dbListTables(hg19)
length(all_tables)
```

    ## [1] 11048

运行结束之后，我们知道hg19这个数据库里有11048张表。

获取表的信息
------------

我想知道某一个表有多少列？

``` r
dbListFields(hg19,"acemblyPep")
```

    ## [1] "name" "seq"

然后，我又想把知道这个表有多少行？

``` r
dbGetQuery(hg19,"select count(*) from acemblyPep")
```

    ##   count(*)
    ## 1   187692

我想能不能看看这个表具体长啥样？

``` r
table <- dbReadTable(hg19,"acemblyPep")
head(table,n=3)
```

    ##            name
    ## 1 A1BGAS.aAug10
    ## 2 A1BGAS.bAug10
    ## 3 A1BGAS.cAug10
    ##                                                                                                                                                                                                                                               seq
    ## 1                                                                                                                                                              LRRRRAAPAAFTPRTSAPHVTPAETAPVRLLFPPPPAPGTQTPGGLTPQQEKDHEHGHDGRAHSGAVSVWVMDPRTCSRRRR
    ## 2                                                                                                                                                                                                  MAGTQTPGGLTPQQEKDHEHGHDGRAHSGAVSVWVMDPRTCSRRRR
    ## 3 MGDAGAVRRSRGDQELRRLQSDCRAHRRDEDQLGTAAALASAVRDGELWRLPLFGPISILLSTCCMLSVLLRASTWMEAVCSGWTGGECILCRRDNQVLRPEVITRPGALRQGLVARPEEQSSGCAQNSEVRPLNSDRTFQPIGNEAAQAARGLVKSEVCRDGAVILCFLWQSQHQPRCTLLLASLGSPALRVVAASCKYPALRFCNIHFCSLSLAKPAQSVPNLYPLCLKYLVWFLFP

记得查询完之后

``` r
dbDisconnect(hg19)
```

    ## [1] TRUE

[RMySQL文档](https://cran.r-project.org/web/packages/RMySQL/RMySQL.pdf) [SQL查询命令](http://www.pantz.org/software/mysql/mysqlcommands.html) [其他参考资料](https://www.r-bloggers.com/mysql-and-r/)
