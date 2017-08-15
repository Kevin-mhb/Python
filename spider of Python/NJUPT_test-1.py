import requests
from bs4 import BeautifulSoup
import re
import bs4


html_doc = """

  <!-- start-listColumn -->
    <div class="listColumn wrapper">
        <div class="listColumnWrapper">
            <table width="100%" border="0" cellpadding="0" cellspacing="0">
                <tbody>
                <tr>
                    <td align="center" valign="top" id="listleft">
                        <table width="100%" border="0" cellspacing="0" cellpadding="0">
                            <tbody>
                            <tr>
                                <td height="33" class="biaoti1">
<span frag="窗口5" portletmode="simpleColumnAnchor"> 
<span class='Column_Anchor'>通知公告</span> 
</span> 
</td>
                            </tr>
                            </tbody>
                        </table>

                        
<div frag="窗口1" portletmode="simpleColumnList"> 
 
 
<table width="100%" border="0" cellpadding="0" cellspacing="0">
  
</table>
  
 
</div> 

                    </td>
                    <td valign="top" id="listright">
                        <table width="100%" height="400" border="0" cellpadding="0" cellspacing="0">
                            <tbody>
                            <tr>
                                <td valign="top">
                                    <table width="100%" height="22" border="0" cellpadding="0" cellspacing="0">
                                        <tbody>
                                        <tr>
                                            <td height="53" class="biaoti5">
<span frag="窗口4" portletmode="simpleColumnName"> 
<span class='Column_Name'>通知公告</span> 
</span> 
</td>
                                            <td height="53" background="/_upload/tpl/00/2c/44/template44/css/images/lmain2_2.gif">
                                                <table width="100%" height="34" border="0" cellpadding="0" cellspacing="0">
                                                    <tbody>
                                                    <tr>
                                                        <td height="20">
                                                            <table width="100%" height="25" border="0" align="center" cellpadding="0" cellspacing="0">
                                                                <tbody>
                                                                <tr>
                                                                    <td align="right">当前位置: 
<span frag="窗口3" portletmode="simpleColumnPosition"> 
<span class='Column_Position'><a href="/main.htm" target="_self">首页</a><span class='possplit'>&nbsp;&nbsp;</span><a href="/72/list.htm" target="_self">通知公告</a></span> 
</span> 
</td>
                                                                </tr>
                                                                </tbody>
                                                            </table>
                                                        </td>
                                                    </tr>
                                                    </tbody>
                                                </table>
                                            </td>
                                        </tr>
                                        </tbody>
                                    </table>
                                    <table width="95%" border="0" cellpadding="0" cellspacing="0">
                                        <tbody>
                                        <tr>
                                            <td>
                                                <div id="newslist">
                                                    
<div frag="窗口2" portletmode="simpleList"> 
 
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
                                                    
  

                                                        <tbody>
                                                        <tr>
                                                            <td height="28"> 
<table width="100%" cellpadding="0" cellspacing="0" border="0"> 
<tr> 
<td align="left"><a href='/2017/0703/c72a109586/page.htm' target='_blank' title='关于学校开具和接收增值税发票相关事项的通知'>关于学校开具和接收增值税发票相关事项的通知</a></td> 
 
<td align="left" width="30px"><div style="white-space:nowrap">2017-07-03</div></td> 
 
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
<td align="left"><a href='/2017/0703/c72a109585/page.htm' target='_blank' title='财务处2017年暑假工作安排'>财务处2017年暑假工作安排</a></td> 
 
<td align="left" width="30px"><div style="white-space:nowrap">2017-07-03</div></td> 
 
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
<td align="left"><a href='/2017/0703/c72a109573/page.htm' target='_blank' title='信息化建设与管理办公室2017年暑假工作安排'>信息化建设与管理办公室2017年暑假工作安排</a></td> 
 
<td align="left" width="30px"><div style="white-space:nowrap">2017-07-03</div></td> 
 
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
<td align="left"><a href='/2017/0703/c72a109530/page.htm' target='_blank' title='关于2017年暑假期间交通车运行时间的通知'>关于2017年暑假期间交通车运行时间的通知</a></td> 
 
<td align="left" width="30px"><div style="white-space:nowrap">2017-07-03</div></td> 
 
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
<td align="left"><a href='/2017/0703/c72a109524/page.htm' target='_blank' title='后勤管理处、后勤服务集团2017年暑假工作安排'>后勤管理处、后勤服务集团2017年暑假工作安排</a></td> 
 
<td align="left" width="30px"><div style="white-space:nowrap">2017-07-03</div></td> 
 
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
<td align="left"><a href='/2017/0622/c72a108725/page.htm' target='_blank' title='关于南京邮电大学第四届“学生安全教育月”活动先进集体、先进工作者和活动积极分子的表彰决定'>关于南京邮电大学第四届“学生安全教育月”活动先进集体、先进工作者和活动积极分子的表彰决定</a></td> 
 
<td align="left" width="30px"><div style="white-space:nowrap">2017-06-22</div></td> 
 
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
<td align="left"><a href='/2017/0622/c72a108711/page.htm' target='_blank' title='南京邮电大学“第九届校园开放日暨通信电子类高校招生咨询会”'><font style='color:#FF0516;'>南京邮电大学“第九届校园开放日暨通信电子类高校招生咨询会”</font></a></td> 
 
<td align="left" width="30px"><div style="white-space:nowrap">2017-06-22</div></td> 
 
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
<td align="left"><a href='/2017/0619/c72a108279/page.htm' target='_blank' title='关于正式启用协同办公系统的通知'>关于正式启用协同办公系统的通知</a></td> 
 
<td align="left" width="30px"><div style="white-space:nowrap">2017-06-19</div></td> 
 
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
<td align="left"><a href='/2017/0619/c72a108225/page.htm' target='_blank' title='关于召开南京邮电大学二级学院（教学单位）“十三五”规划（初稿）答辩评审会的通知'>关于召开南京邮电大学二级学院（教学单位）“十三五”规划（初稿）答辩评审会的通知</a></td> 
 
<td align="left" width="30px"><div style="white-space:nowrap">2017-06-19</div></td> 
 
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
<td align="left"><a href='/2017/0614/c72a107933/page.htm' target='_blank' title='关于开展体检咨询的通知'>关于开展体检咨询的通知</a></td> 
 
<td align="left" width="30px"><div style="white-space:nowrap">2017-06-14</div></td> 
 
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
<td align="left"><a href='/2017/0609/c72a107499/page.htm' target='_blank' title='关于2017年暑假有关事项的通知'>关于2017年暑假有关事项的通知</a></td> 
 
<td align="left" width="30px"><div style="white-space:nowrap">2017-06-09</div></td> 
 
</tr> 
</table> 
</td>
                                                        </tr>
                                                        </tbody>
                                                    
 </table>
 <div id="wp_paging_w2"> 
<ul class="wp_paging clearfix"> 
     <li class="pages_count"> 
         <span class="per_page">每页&nbsp;<em class="per_count">14</em>&nbsp;记录&nbsp;</span> 
         <span class="all_count">总共&nbsp;<em class="all_count">2147</em>&nbsp;记录&nbsp;</span> 
     </li> 
     <li class="page_nav"> 
         <a class="first" href="javascript:void(0);" target="_self"><span>第一页</span></a> 
         <a class="prev" href="javascript:void(0);" target="_self"><span>&lt;&lt;上一页</span></a> 
         <a class="next" href="/72/list2.htm" target="_self"><span>下一页&gt;&gt;</span></a> 
         <a class="last" href="/72/list154.htm" target="_self"><span>尾页</span></a> 
     </li> 
     <li class="page_jump"> 
         <span class="pages">页码&nbsp;<em class="curr_page">1</em>/<em class="all_pages">154</em></span> 
         <span><input class="pageNum" type="text" /><input type="hidden" class="currPageURL" value=""></span></span> 
         <span><a class="pagingJump" href="javascript:void(0);" target="_self">跳转到&nbsp;</a></span> 
     </li> 
</ul> 
</div> 
<script type="text/javascript"> 
     $().ready(function() { 
         $("#wp_paging_w2 .pagingJump").click(function() { 
             var pageNum = $("#wp_paging_w2 .pageNum").val(); 
             if (pageNum === "") { alert('请输入页码！'); return; } 
             if (isNaN(pageNum) || pageNum <= 0 || pageNum > 154) { alert('请输入正确页码！'); return; } 
             var reg = new RegExp("/list", "g"); 
             var url = "/72/list.htm"; 
             window.location.href = url.replace(reg, "/list" + pageNum); 
         }); 
     }); 
</script> 
 
</div> 

                                                </div>
                                            </td>
                                        </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                            </tbody>
                        </table>
                    </td>
                </tr>
                </tbody>
            </table>
        </div>
    </div>
    <!---End-listColumn ---->

"""

soup=BeautifulSoup(html_doc,"html.parser")

print(soup.prettify(),end="\n\n\n")

for a in soup.find_all('a'):
	print(a.string,end="\n\n")

#提取链接
for link in soup.find_all('a'):
	print("http://www.njupt.edu.cn"+link.get('href'),end="\n\n")

'''
ulist=[]
for tbody in soup.find('table').descendants:
	print(tbody.name)
	if isinstance(tbody,bs4.element.Tag):
		tds=tbody('td')
		
		ulist.append([tds[0].string,tds[1].string,tds[3].string]+"\n")

print(ulist)       
'''