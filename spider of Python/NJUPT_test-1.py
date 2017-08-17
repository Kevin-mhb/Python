import requests
from bs4 import BeautifulSoup
import re
import bs4


html_doc = """

   <tbody>
                                                        <tr>
                                                            <td height="28"> 
<table width="100%" cellpadding="0" cellspacing="0" border="0"> 
<tr> 
<td align="left"><a href='/2017/0804/c72a111266/page.htm' target='_blank' title='关于仙林校区教三多媒体教室设备开启方式变动的通知'>关于仙林校区教三多媒体教室设备开启方式变动的通知</a></td> 
 
<td align="left" width="30px"><div style="white-space:nowrap">2017-08-04</div></td> 
 
</tr> 
</table> 
</td>
                                                        </tr>
                                                        </tbody>
<tbody>
                                                        <tr>
                                                            <td height="28"> 
<table width="100%" cellpadding="0" cellspacing="0" border="0"> 
<tr> 
<td align="left"><a href='/2017/0717/c72a110757/page.htm' target='_blank' title='关于认真组织收看电视专题片《将改革进行到底》的通知'><font style='color:#FF3912;'>关于认真组织收看电视专题片《将改革进行到底》的通知</font></a></td> 
 
<td align="left" width="30px"><div style="white-space:nowrap">2017-07-17</div></td> 
 
</tr> 
</table> 
</td>
                                                        </tr>
                                                        </tbody>
                                                    
  

                                                        <tbody>
                                                        <tr>
                                                            <td height="28"> 
<table width="100%" cellpadding="0" cellspacing="0" border="0"> 
<tr> 
<td align="left"><a href='/2017/0705/c72a109686/page.htm' target='_blank' title='关于2017年暑假期间安全保卫工作相关事项的通知'>关于2017年暑假期间安全保卫工作相关事项的通知</a></td> 
 
<td align="left" width="30px"><div style="white-space:nowrap">2017-07-05</div></td> 
 
</tr> 
</table> 
</td>
                                                        </tr>
                                                        </tbody>


"""

soup=BeautifulSoup(html_doc,"html.parser")

#print(soup.prettify(),end="\n\n\n"
for a in soup.find_all('a'):
    tds1=a.string
    tds2=("http://www.njupt.edu.cn"+a.get('href'))
    print({tds1:tds2},end="\n\n")

