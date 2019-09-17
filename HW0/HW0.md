1.热身练习：
对于练习3中的“Pi计算”和练习4中的“单词计数”示例：
（1）提供截图以证明您已完成练习。 （10％）
（2）列出每个练习中涉及的Spark转换和操作。确定触发程序执行的RDD操作。 （20％）
2.纽约自行车专家（30％）
在此处下载NYC Citi自行车数据，将csv文件上传到云存储桶，然后将数据加载到BigQuery中（查看文档）。您可以在创建表时选择“自动检测”架构。回答以下问题并提供您的查询的屏幕截图：
（1）数据集中有多少个唯一的station_id？
（2）电台的最大容量是多少？列出所有的station_id容量最大的车站？
（3）region_id 70中可用的自行车总数是多少？
3.了解威廉·莎士比亚（40％）
编写Spark程序，找到从莎士比亚作品中提取的shakes.txt文件中最常用的5个单词。提供您的结果（单词及其频率）并截取您的代码/ jupyter笔记本的屏幕截图：
（1）找到前5个常用词而不进行任何文本预处理。
（2）通过先滤除由提供的停用词，找出前5个常用词NLTK包。 Natural Language Toolkit，或者更常见的是NLTK，是一套用Python进行自然语言处理的库和程序。

## Homework 0 (E6893)

####                                                                                                                       Jing Qian (jq2282)

#### 1. Warm-up exercises

**1)**![Screen Shot 2019-09-15 at 11.35.30 PM](/Users/mac/Desktop/BigData/HW0/Screen Shot 2019-09-15 at 11.35.30 PM.png)

![Screen Shot 2019-09-15 at 11.36.59 PM](/Users/mac/Desktop/BigData/HW0/Screen Shot 2019-09-15 at 11.36.59 PM.png)

![Screen Shot 2019-09-15 at 11.37.59 PM](/Users/mac/Desktop/BigData/HW0/Screen Shot 2019-09-15 at 11.37.59 PM.png)

![Screen Shot 2019-09-15 at 11.55.35 PM](/Users/mac/Desktop/BigData/HW0/Screen Shot 2019-09-15 at 11.55.35 PM.png)

**2)**





#### 2. NYC Bike expert

**1)** 843.



**2)** The largest capacity for a station is 79. The *station_id* of stations that have the largest capacity are: 445, 422, 501.



**3)** The total number of bikes available in region_id 70 is 394.



####3. Understanding William Shakespeare

**1)** The top 5 frequent words without any text preprocessing are: [('the', 604), ('and', 409), ('of', 389), ('to', 359), ('I', 263)].



**2)** 