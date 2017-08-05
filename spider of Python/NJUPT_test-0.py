import requests
from bs4 import BeautifulSoup
import re
import bs4


html_doc = """

<tbody class="hidden_zhpm" style="text-align:center;">
                <tr class="alt"><td>1</td><td><div align="left">清华大学</div></td><td>北京</td><td>111</td></tr>
<tr><td>2</td><td><div align="left">北京大学</div></td><td>北京</td><td>90</td></tr>
<tr class="alt"><td>3</td><td><div align="left">浙江大学</div></td><td>浙江</td><td>88</td></tr>
<tr><td>4</td><td><div align="left">上海交通大学</div></td><td>上海</td><td>79</td></tr>
<tr class="alt"><td>5</td><td><div align="left">复旦大学</div></td><td>上海</td><td>57</td></tr>
<tr><td>6</td><td><div align="left">中山大学</div></td><td>广东</td><td>46</td></tr>
<tr class="alt"><td>7</td><td><div align="left">中国科学技术大学</div></td><td>安徽</td><td>40</td></tr>
<tr><td>8</td><td><div align="left">南京大学</div></td><td>江苏</td><td>34</td></tr>
<tr class="alt"><td>8</td><td><div align="left">华中科技大学</div></td><td>湖北</td><td>34</td></tr>
<tr><td>10</td><td><div align="left">同济大学</div></td><td>上海</td><td>31</td></tr>
<tr class="alt"><td>11</td><td><div align="left">大连理工大学</div></td><td>辽宁</td><td>29</td></tr>
<tr><td>12</td><td><div align="left">哈尔滨工业大学</div></td><td>黑龙江</td><td>23</td></tr>
<tr class="alt"><td>13</td><td><div align="left">东南大学</div></td><td>江苏</td><td>22</td></tr>
<tr><td>14</td><td><div align="left">华南理工大学</div></td><td>广东</td><td>21</td></tr>
<tr class="alt"><td>15</td><td><div align="left">北京协和医学院</div></td><td>北京</td><td>20</td></tr>
<tr><td>16</td><td><div align="left">武汉大学</div></td><td>湖北</td><td>19</td></tr>
<tr class="alt"><td>16</td><td><div align="left">四川大学</div></td><td>四川</td><td>19</td></tr>
<tr><td>16</td><td><div align="left">山东大学</div></td><td>山东</td><td>19</td></tr>
<tr class="alt"><td>19</td><td><div align="left">南开大学</div></td><td>天津</td><td>18</td></tr>
<tr><td>19</td><td><div align="left">吉林大学</div></td><td>吉林</td><td>18</td></tr>
<tr class="alt"><td>21</td><td><div align="left">天津大学</div></td><td>天津</td><td>17</td></tr>
<tr><td>22</td><td><div align="left">中南大学</div></td><td>湖南</td><td>15</td></tr>
<tr class="alt"><td>22</td><td><div align="left">苏州大学</div></td><td>江苏</td><td>15</td></tr>
<tr><td>22</td><td><div align="left">湖南大学</div></td><td>湖南</td><td>15</td></tr>
<tr class="alt"><td>25</td><td><div align="left">西安交通大学</div></td><td>陕西</td><td>14</td></tr>
<tr><td>25</td><td><div align="left">厦门大学</div></td><td>福建</td><td>14</td></tr>
<tr class="alt"><td>27</td><td><div align="left">北京师范大学</div></td><td>北京</td><td>13</td></tr>
<tr><td>27</td><td><div align="left">电子科技大学</div></td><td>四川</td><td>13</td></tr>
<tr class="alt"><td>29</td><td><div align="left">南京航空航天大学</div></td><td>江苏</td><td>12</td></tr>
<tr><td>30</td><td><div align="left">华东理工大学</div></td><td>上海</td><td>11</td></tr>
<tr class="alt"><td>30</td><td><div align="left">中国农业大学</div></td><td>北京</td><td>11</td></tr>
<tr><td>32</td><td><div align="left">北京航空航天大学</div></td><td>北京</td><td>10</td></tr>
<tr class="alt"><td>32</td><td><div align="left">北京理工大学</div></td><td>北京</td><td>10</td></tr>
<tr><td>32</td><td><div align="left">华东师范大学</div></td><td>上海</td><td>10</td></tr>
<tr class="alt"><td>32</td><td><div align="left">东北师范大学</div></td><td>吉林</td><td>10</td></tr>
<tr><td>32</td><td><div align="left">华中农业大学</div></td><td>湖北</td><td>10</td></tr>
<tr class="alt"><td>37</td><td><div align="left">北京化工大学</div></td><td>北京</td><td>9</td></tr>
<tr><td>37</td><td><div align="left">兰州大学</div></td><td>甘肃</td><td>9</td></tr>
<tr class="alt"><td>37</td><td><div align="left">中国地质大学（武汉）</div></td><td>湖北</td><td>9</td></tr>
<tr><td>40</td><td><div align="left">福州大学</div></td><td>福建</td><td>8</td></tr>
<tr class="alt"><td>40</td><td><div align="left">东北大学</div></td><td>辽宁</td><td>8</td></tr>
<tr><td>42</td><td><div align="left">西北工业大学</div></td><td>陕西</td><td>7</td></tr>
<tr class="alt"><td>42</td><td><div align="left">南京理工大学</div></td><td>江苏</td><td>7</td></tr>
<tr><td>42</td><td><div align="left">武汉理工大学</div></td><td>湖北</td><td>7</td></tr>
<tr class="alt"><td>42</td><td><div align="left">上海大学</div></td><td>上海</td><td>7</td></tr>
<tr><td>42</td><td><div align="left">西安电子科技大学</div></td><td>陕西</td><td>7</td></tr>
<tr class="alt"><td>42</td><td><div align="left">南京医科大学</div></td><td>江苏</td><td>7</td></tr>
<tr><td>42</td><td><div align="left">西南大学</div></td><td>重庆</td><td>7</td></tr>
<tr class="alt"><td>42</td><td><div align="left">南京农业大学</div></td><td>江苏</td><td>7</td></tr>
<tr><td>42</td><td><div align="left">南京师范大学</div></td><td>江苏</td><td>7</td></tr>
<tr class="alt"><td>42</td><td><div align="left">西南交通大学</div></td><td>四川</td><td>7</td></tr>
<tr><td>42</td><td><div align="left">南京工业大学</div></td><td>江苏</td><td>7</td></tr>
<tr class="alt"><td>53</td><td><div align="left">北京科技大学</div></td><td>北京</td><td>6</td></tr>
<tr><td>53</td><td><div align="left">东华大学</div></td><td>上海</td><td>6</td></tr>
<tr class="alt"><td>53</td><td><div align="left">沈阳药科大学</div></td><td>辽宁</td><td>6</td></tr>
<tr><td>56</td><td><div align="left">重庆大学</div></td><td>重庆</td><td>5</td></tr>
<tr class="alt"><td>56</td><td><div align="left">北京交通大学</div></td><td>北京</td><td>5</td></tr>
<tr><td>56</td><td><div align="left">江南大学</div></td><td>江苏</td><td>5</td></tr>
<tr class="alt"><td>56</td><td><div align="left">中国药科大学</div></td><td>江苏</td><td>5</td></tr>
<tr><td>56</td><td><div align="left">华南师范大学</div></td><td>广东</td><td>5</td></tr>
<tr class="alt"><td>56</td><td><div align="left">北京林业大学</div></td><td>北京</td><td>5</td></tr>
<tr><td>62</td><td><div align="left">中国人民大学</div></td><td>北京</td><td>4</td></tr>
<tr class="alt"><td>62</td><td><div align="left">首都医科大学</div></td><td>北京</td><td>4</td></tr>
<tr><td>62</td><td><div align="left">华北电力大学</div></td><td>北京</td><td>4</td></tr>
<tr class="alt"><td>62</td><td><div align="left">浙江工业大学</div></td><td>浙江</td><td>4</td></tr>
<tr><td>62</td><td><div align="left">江苏大学</div></td><td>江苏</td><td>4</td></tr>
<tr class="alt"><td>62</td><td><div align="left">汕头大学</div></td><td>广东</td><td>4</td></tr>
<tr><td>62</td><td><div align="left">大连医科大学</div></td><td>辽宁</td><td>4</td></tr>
<tr class="alt"><td>62</td><td><div align="left">宁波大学</div></td><td>浙江</td><td>4</td></tr>
<tr><td>62</td><td><div align="left">云南大学</div></td><td>云南</td><td>4</td></tr>
<tr class="alt"><td>71</td><td><div align="left">北京邮电大学</div></td><td>北京</td><td>3</td></tr>
<tr><td>71</td><td><div align="left">暨南大学</div></td><td>广东</td><td>3</td></tr>
<tr class="alt"><td>71</td><td><div align="left">中国海洋大学</div></td><td>山东</td><td>3</td></tr>
<tr><td>71</td><td><div align="left">中国地质大学（北京）</div></td><td>北京</td><td>3</td></tr>
<tr class="alt"><td>71</td><td><div align="left">南方医科大学</div></td><td>广东</td><td>3</td></tr>
<tr><td>71</td><td><div align="left">哈尔滨工程大学</div></td><td>黑龙江</td><td>3</td></tr>
<tr class="alt"><td>71</td><td><div align="left">北京工业大学</div></td><td>北京</td><td>3</td></tr>
<tr><td>71</td><td><div align="left">中国石油大学（华东）</div></td><td>山东</td><td>3</td></tr>
<tr class="alt"><td>71</td><td><div align="left">深圳大学</div></td><td>广东</td><td>3</td></tr>
<tr><td>71</td><td><div align="left">西北农林科技大学</div></td><td>陕西</td><td>3</td></tr>
<tr class="alt"><td>71</td><td><div align="left">扬州大学</div></td><td>江苏</td><td>3</td></tr>
<tr><td>71</td><td><div align="left">上海师范大学</div></td><td>上海</td><td>3</td></tr>
<tr class="alt"><td>71</td><td><div align="left">南昌大学</div></td><td>江西</td><td>3</td></tr>
<tr><td>71</td><td><div align="left">山西大学</div></td><td>山西</td><td>3</td></tr>
<tr class="alt"><td>71</td><td><div align="left">渤海大学</div></td><td>辽宁</td><td>3</td></tr>
<tr><td>71</td><td><div align="left">黑龙江大学</div></td><td>黑龙江</td><td>3</td></tr>
<tr class="alt"><td>71</td><td><div align="left">青岛大学</div></td><td>山东</td><td>3</td></tr>
<tr><td>71</td><td><div align="left">天津工业大学</div></td><td>天津</td><td>3</td></tr>
<tr class="alt"><td>71</td><td><div align="left">山东科技大学</div></td><td>山东</td><td>3</td></tr>
<tr><td>71</td><td><div align="left">昆明理工大学</div></td><td>云南</td><td>3</td></tr>
<tr class="alt"><td>71</td><td><div align="left">四川师范大学</div></td><td>四川</td><td>3</td></tr>
<tr><td>71</td><td><div align="left">中国科学院大学</div></td><td>北京</td><td>3</td></tr>
<tr class="alt"><td>93</td><td><div align="left">对外经济贸易大学</div></td><td>北京</td><td>2</td></tr>
<tr><td>93</td><td><div align="left">中央财经大学</div></td><td>北京</td><td>2</td></tr>
<tr class="alt"><td>93</td><td><div align="left">华中师范大学</div></td><td>湖北</td><td>2</td></tr>
<tr><td>93</td><td><div align="left">天津医科大学</div></td><td>天津</td><td>2</td></tr>
<tr class="alt"><td>93</td><td><div align="left">中国矿业大学</div></td><td>江苏</td><td>2</td></tr>
<tr><td>93</td><td><div align="left">浙江师范大学</div></td><td>浙江</td><td>2</td></tr>
<tr class="alt"><td>93</td><td><div align="left">陕西师范大学</div></td><td>陕西</td><td>2</td></tr>
<tr><td>93</td><td><div align="left">首都师范大学</div></td><td>北京</td><td>2</td></tr>
<tr class="alt"><td>93</td><td><div align="left">杭州电子科技大学</div></td><td>浙江</td><td>2</td></tr>
<tr><td>93</td><td><div align="left">杭州师范大学</div></td><td>浙江</td><td>2</td></tr>
<tr class="alt"><td>93</td><td><div align="left">湘潭大学</div></td><td>湖南</td><td>2</td></tr>
<tr><td>93</td><td><div align="left">重庆医科大学</div></td><td>重庆</td><td>2</td></tr>
<tr class="alt"><td>93</td><td><div align="left">湖北大学</div></td><td>湖北</td><td>2</td></tr>
<tr><td>93</td><td><div align="left">福建医科大学</div></td><td>福建</td><td>2</td></tr>
<tr class="alt"><td>93</td><td><div align="left">河北大学</div></td><td>河北</td><td>2</td></tr>
<tr><td>93</td><td><div align="left">华南农业大学</div></td><td>广东</td><td>2</td></tr>
<tr class="alt"><td>93</td><td><div align="left">郑州大学</div></td><td>河南</td><td>2</td></tr>
<tr><td>93</td><td><div align="left">天津师范大学</div></td><td>天津</td><td>2</td></tr>
<tr class="alt"><td>93</td><td><div align="left">济南大学</div></td><td>山东</td><td>2</td></tr>
<tr><td>93</td><td><div align="left">沈阳航空航天大学</div></td><td>辽宁</td><td>2</td></tr>
<tr class="alt"><td>93</td><td><div align="left">中南民族大学</div></td><td>湖北</td><td>2</td></tr>
<tr><td>93</td><td><div align="left">山东师范大学</div></td><td>山东</td><td>2</td></tr>
<tr class="alt"><td>93</td><td><div align="left">贵州大学</div></td><td>贵州</td><td>2</td></tr>
<tr><td>93</td><td><div align="left">河南科技大学</div></td><td>河南</td><td>2</td></tr>
<tr class="alt"><td>93</td><td><div align="left">聊城大学</div></td><td>山东</td><td>2</td></tr>
<tr><td>93</td><td><div align="left">南方科技大学</div></td><td>广东</td><td>2</td></tr>
<tr class="alt"><td>93</td><td><div align="left">北京师范大学-香港浸会大学联合国际学院</div></td><td>广东</td><td>2</td></tr>
<tr><td>120</td><td><div align="left">上海财经大学</div></td><td>上海</td><td>1</td></tr>
<tr class="alt"><td>120</td><td><div align="left">西南财经大学</div></td><td>四川</td><td>1</td></tr>
<tr><td>120</td><td><div align="left">合肥工业大学</div></td><td>安徽</td><td>1</td></tr>
<tr class="alt"><td>120</td><td><div align="left">中国医科大学</div></td><td>辽宁</td><td>1</td></tr>
<tr><td>120</td><td><div align="left">中国石油大学（北京）</div></td><td>北京</td><td>1</td></tr>
<tr class="alt"><td>120</td><td><div align="left">东北财经大学</div></td><td>辽宁</td><td>1</td></tr>
<tr><td>120</td><td><div align="left">河海大学</div></td><td>江苏</td><td>1</td></tr>
<tr class="alt"><td>120</td><td><div align="left">北京中医药大学</div></td><td>北京</td><td>1</td></tr>
<tr><td>120</td><td><div align="left">首都经济贸易大学</div></td><td>北京</td><td>1</td></tr>
<tr class="alt"><td>120</td><td><div align="left">浙江理工大学</div></td><td>浙江</td><td>1</td></tr>
<tr><td>120</td><td><div align="left">华侨大学</div></td><td>福建</td><td>1</td></tr>
<tr class="alt"><td>120</td><td><div align="left">上海中医药大学</div></td><td>上海</td><td>1</td></tr>
<tr><td>120</td><td><div align="left">燕山大学</div></td><td>河北</td><td>1</td></tr>
<tr class="alt"><td>120</td><td><div align="left">哈尔滨医科大学</div></td><td>黑龙江</td><td>1</td></tr>
<tr><td>120</td><td><div align="left">南京财经大学</div></td><td>江苏</td><td>1</td></tr>
<tr class="alt"><td>120</td><td><div align="left">温州医科大学</div></td><td>浙江</td><td>1</td></tr>
<tr><td>120</td><td><div align="left">安徽医科大学</div></td><td>安徽</td><td>1</td></tr>
<tr class="alt"><td>120</td><td><div align="left">广东工业大学</div></td><td>广东</td><td>1</td></tr>
<tr><td>120</td><td><div align="left">广州医科大学</div></td><td>广东</td><td>1</td></tr>
<tr class="alt"><td>120</td><td><div align="left">太原理工大学</div></td><td>山西</td><td>1</td></tr>
<tr><td>120</td><td><div align="left">广西大学</div></td><td>广西</td><td>1</td></tr>
<tr class="alt"><td>120</td><td><div align="left">石家庄铁道大学</div></td><td>河北</td><td>1</td></tr>
<tr><td>120</td><td><div align="left">江西财经大学</div></td><td>江西</td><td>1</td></tr>
<tr class="alt"><td>120</td><td><div align="left">长沙理工大学</div></td><td>湖南</td><td>1</td></tr>
<tr><td>120</td><td><div align="left">福建师范大学</div></td><td>福建</td><td>1</td></tr>
<tr class="alt"><td>120</td><td><div align="left">广州大学</div></td><td>广东</td><td>1</td></tr>
<tr><td>120</td><td><div align="left">河北师范大学</div></td><td>河北</td><td>1</td></tr>
<tr class="alt"><td>120</td><td><div align="left">河北科技大学</div></td><td>河北</td><td>1</td></tr>
<tr><td>120</td><td><div align="left">安徽工业大学</div></td><td>安徽</td><td>1</td></tr>
<tr class="alt"><td>120</td><td><div align="left">上海海事大学</div></td><td>上海</td><td>1</td></tr>
<tr><td>120</td><td><div align="left">辽宁工业大学</div></td><td>辽宁</td><td>1</td></tr>
<tr class="alt"><td>120</td><td><div align="left">徐州医科大学</div></td><td>江苏</td><td>1</td></tr>
<tr><td>120</td><td><div align="left">河南大学</div></td><td>河南</td><td>1</td></tr>
<tr class="alt"><td>120</td><td><div align="left">重庆邮电大学</div></td><td>重庆</td><td>1</td></tr>
<tr><td>120</td><td><div align="left">闽南师范大学</div></td><td>福建</td><td>1</td></tr>
<tr class="alt"><td>120</td><td><div align="left">青岛科技大学</div></td><td>山东</td><td>1</td></tr>
<tr><td>120</td><td><div align="left">浙江农林大学</div></td><td>浙江</td><td>1</td></tr>
<tr class="alt"><td>120</td><td><div align="left">江苏师范大学</div></td><td>江苏</td><td>1</td></tr>
<tr><td>120</td><td><div align="left">西安建筑科技大学</div></td><td>陕西</td><td>1</td></tr>
<tr class="alt"><td>120</td><td><div align="left">南通大学</div></td><td>江苏</td><td>1</td></tr>
<tr><td>120</td><td><div align="left">南京中医药大学</div></td><td>江苏</td><td>1</td></tr>
<tr class="alt"><td>120</td><td><div align="left">广西师范大学</div></td><td>广西</td><td>1</td></tr>
<tr><td>120</td><td><div align="left">西南石油大学</div></td><td>四川</td><td>1</td></tr>
<tr class="alt"><td>120</td><td><div align="left">河南师范大学</div></td><td>河南</td><td>1</td></tr>
<tr><td>120</td><td><div align="left">重庆交通大学</div></td><td>重庆</td><td>1</td></tr>
<tr class="alt"><td>120</td><td><div align="left">山西师范大学</div></td><td>山西</td><td>1</td></tr>
<tr><td>120</td><td><div align="left">天津科技大学</div></td><td>天津</td><td>1</td></tr>
<tr class="alt"><td>120</td><td><div align="left">信阳师范学院</div></td><td>河南</td><td>1</td></tr>
<tr><td>120</td><td><div align="left">江苏科技大学</div></td><td>江苏</td><td>1</td></tr>
<tr class="alt"><td>120</td><td><div align="left">山东财经大学</div></td><td>山东</td><td>1</td></tr>
<tr><td>120</td><td><div align="left">西北师范大学</div></td><td>甘肃</td><td>1</td></tr>
<tr class="alt"><td>120</td><td><div align="left">上海电力学院</div></td><td>上海</td><td>1</td></tr>
<tr><td>120</td><td><div align="left">上海第二工业大学</div></td><td>上海</td><td>1</td></tr>
<tr class="alt"><td>120</td><td><div align="left">河南工业大学</div></td><td>河南</td><td>1</td></tr>
<tr><td>120</td><td><div align="left">桂林电子科技大学</div></td><td>广西</td><td>1</td></tr>
<tr class="alt"><td>120</td><td><div align="left">浙江海洋大学</div></td><td>浙江</td><td>1</td></tr>
<tr><td>120</td><td><div align="left">大连大学</div></td><td>辽宁</td><td>1</td></tr>
<tr class="alt"><td>120</td><td><div align="left">西华师范大学</div></td><td>四川</td><td>1</td></tr>
<tr><td>120</td><td><div align="left">东北石油大学</div></td><td>黑龙江</td><td>1</td></tr>
<tr class="alt"><td>120</td><td><div align="left">山东建筑大学</div></td><td>山东</td><td>1</td></tr>
<tr><td>120</td><td><div align="left">东华理工大学</div></td><td>江西</td><td>1</td></tr>
<tr class="alt"><td>120</td><td><div align="left">江西科技师范大学</div></td><td>江西</td><td>1</td></tr>
<tr><td>120</td><td><div align="left">齐鲁工业大学</div></td><td>山东</td><td>1</td></tr>
<tr class="alt"><td>120</td><td><div align="left">新疆大学</div></td><td>新疆</td><td>1</td></tr>
<tr><td>120</td><td><div align="left">成都学院</div></td><td>四川</td><td>1</td></tr>
<tr class="alt"><td>120</td><td><div align="left">嘉应学院</div></td><td>广东</td><td>1</td></tr>
<tr><td>120</td><td><div align="left">上海科技大学</div></td><td>上海</td><td>1</td></tr>
<tr class="alt"><td>120</td><td><div align="left">宁波诺丁汉大学</div></td><td>浙江</td><td>1</td></tr>
<tr><td>120</td><td><div align="left">中国矿业大学（北京）</div></td><td>北京</td><td>1</td></tr>
<tr class="alt"><td>120</td><td><div align="left">湖北工业大学</div></td><td>湖北</td><td>1</td></tr>
<tr><td>120</td><td><div align="left">武汉纺织大学</div></td><td>湖北</td><td>1</td></tr>
<tr class="alt"><td>120</td><td><div align="left">湖北民族学院</div></td><td>湖北</td><td>1</td></tr>

              </tbody>

"""

soup=BeautifulSoup(html_doc,"html.parser")

ulist=[]
for tr in soup.find('tbody').children:
	if isinstance(tr,bs4.element.Tag):
		tds=tr('td')
		
		ulist.append([tds[0].string,tds[1].string,tds[3].string]+"\n")

print(ulist)
	       