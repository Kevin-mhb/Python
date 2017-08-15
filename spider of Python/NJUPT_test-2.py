import requests
from bs4 import BeautifulSoup
import re
import bs4


html_doc="""

 <head>
    <meta charset="utf-8" />
    <meta name="renderer" content="webkit" />
    <meta http-equiv="X-UA-Compatible" content="IE=Edge" />

    <title>关于参保学生报销意外伤害、校外门诊医疗费以及特困生医疗补助的通知</title>
    <meta name="description" content="各位参保同学：根据《关于南京邮电大学参加南京市城镇居民基本医疗保险大学生的医疗待遇的通知》（校发〔2011〕10号）文件的要求，将于近期对参加2016-2017年度南京市城镇居民基本医疗保险的学生，在这一学年中发生的符合文件规定范围内的医疗费用给予报销。报销范围：1、在校园内及在校外实习期间发生的意外伤害（需提供有辅导员签字和所在学院盖章的证明）所产生的门、急诊医疗费；2、急诊或因校门诊部条件限制由校门诊部转诊到校外定点医院就诊的门诊医疗费在一个学年内累计达1000元以上的；3、各学院认定的经济困难的学生（需提供有所在学院领导签字和盖章的证明）在一个学年内发生的校外门急诊和住院医疗费。医疗费发票（收据）时效：2016年9月1日至2017年8月31日（2017届毕业生限离校前发票）。报销时请务必携带智慧校园卡（或学生证）、身份证、中信银行卡、就诊时所用病历、医疗费发票或收据，2017届毕业生优先办理。具体安排如下：仙林校区正常工作日10：00—15：00（中午不休）门诊部二楼医保办公室（208室）电话：85866876三牌楼校区正常工作日8：20—11：30，14：00—16：00行政北" />

<link type="text/css" href="/_css/_system/system.css" rel="stylesheet"/>
<link type="text/css" href="/_upload/site/1/style/1/1.css" rel="stylesheet"/>
<link type="text/css" href="/_upload/site/00/05/5/style/163/163.css" rel="stylesheet"/>
<link type="text/css" href="/_js/_portletPlugs/simpleNews/css/simplenews.css" rel="stylesheet" />
<link type="text/css" href="/_js/_portletPlugs/datepicker/css/datepicker.css" rel="stylesheet" />

<script language="javascript" src="/_js/jquery.min.js" sudy-wp-context="" sudy-wp-siteId="5"></script>
<script language="javascript" src="/_js/jquery.sudy.wp.visitcount.js"></script>
<script type="text/javascript" src="/_js/_portletPlugs/datepicker/js/jquery.datepicker.js"></script>
<script type="text/javascript" src="/_js/_portletPlugs/datepicker/js/datepicker_lang_HK.js"></script>
<link rel="icon" href="/_upload/tpl/00/2c/44/template44/images/njupt-favicon.ico" type="image/x-icon">
    <!-- My css -->
    <link href="/_upload/tpl/00/2c/44/template44/css/base.css" rel="stylesheet">
    <link href="/_upload/tpl/00/2c/44/template44/css/ui.css" rel="stylesheet">
    <link href="/_upload/tpl/00/2c/44/template44/css/style.css" rel="stylesheet">
</head>

 
""" 

soup=BeautifulSoup(html_doc,"html.parser")
print(soup.prettify(),end="\n\n\n\n\n")

for a in soup.find_all('meta')
	print(a)