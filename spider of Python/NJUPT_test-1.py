import requests
from bs4 import BeautifulSoup
import re
import bs4


html_doc = """

<table align="left" width="100%" border="0" cellpadding="0" cellspacing="0"> 

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
                                                        </table>


"""

soup=BeautifulSoup(html_doc,"html.parser")

print(soup.prettify(),end="\n\n\n")
ulist=[]
for tr in soup.find('table').children:
	#for tr in tbody.find('td').children:
		if isinstance(tr,bs4.element.Tag):
			tds=tr('td')
			ulist.append([tds[0].string,tds[1].string])

print(ulist)
	       