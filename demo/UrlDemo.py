#conding=utf-8
import  urllib.request
import  re
from  bs4 import  BeautifulSoup


# urllib.request.urlopen('http://www.baidu.com')
souphtml="""
<!DOCTYPE html>
<html lang="zh-cn">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>指针怒草内存栈 - 博客园</title>
<link type="text/css" rel="stylesheet" href="/bundles/blog-common.css?v=m_FXmwz3wxZoecUwNEK23PAzc-j9vbX_C6MblJ5ouMc1"/>
<link type="text/css" rel="stylesheet" href="/blog/customcss/289497.css?v=vnT%2bg4L0O9AQRJYsxKkdAT60gR8%3d"/>
<link id="mobile-style" media="only screen and (max-width: 768px)" type="text/css" rel="stylesheet" href="/skins/ThinkInside/bundle-ThinkInside-mobile.css?v=XiHqzbpMg2U13FTnOc9wLUlANuknD0GvNM80XwtTSvY1"/>
<link title="RSS" type="application/rss+xml" rel="alternate" href="http://www.cnblogs.com/java-synchronized/rss"/>
<link title="RSD" type="application/rsd+xml" rel="EditURI" href="http://www.cnblogs.com/java-synchronized/rsd.xml"/>
<link type="application/wlwmanifest+xml" rel="wlwmanifest" href="http://www.cnblogs.com/java-synchronized/wlwmanifest.xml"/>
<script src="//common.cnblogs.com/script/jquery.js" type="text/javascript"></script>
<script type="text/javascript">var currentBlogApp = 'java-synchronized', cb_enable_mathjax=false;var isLogined=true;</script>
<script src="/bundles/blog-common.js?v=CPv0EEqm9L2aCgolHxaZfVYM6J-Sn5az_FJXbjzgr-o1" type="text/javascript"></script>
</head>
<body>
<a name="top"></a>

<!--done-->
<div id="home">
<div id="header">
	<div id="blogTitle">
	<a id="lnkBlogLogo" href="http://www.cnblogs.com/java-synchronized/"><img id="blogLogo" src="/Skins/custom/images/logo.gif" alt="返回主页" /></a>

<!--done-->
<h1><a id="Header1_HeaderTitle" class="headermaintitle" href="http://www.cnblogs.com/java-synchronized/">指针怒草内存栈</a></h1>
<h2>人一定要有梦想，万一实现了呢！</h2>




	</div><!--end: blogTitle 博客的标题和副标题 -->
	<div id="navigator">

<ul id="navList">
<li><a id="blog_nav_sitehome" class="menu" href="http://www.cnblogs.com/">博客园</a></li>
<li><a id="blog_nav_myhome" class="menu" href="http://www.cnblogs.com/java-synchronized/">首页</a></li>
<li><a id="blog_nav_newpost" class="menu" rel="nofollow" href="https://i.cnblogs.com/EditPosts.aspx?opt=1">新随笔</a></li>
<li><a id="blog_nav_contact" class="menu" rel="nofollow" href="https://msg.cnblogs.com/send/%E6%8C%87%E9%92%88%E6%80%92%E8%8D%89%E5%86%85%E5%AD%98%E6%A0%88">联系</a></li>
<li><a id="blog_nav_rss" class="menu" href="http://www.cnblogs.com/java-synchronized/rss">订阅</a>
<!--<a id="blog_nav_rss_image" class="aHeaderXML" href="http://www.cnblogs.com/java-synchronized/rss"><img src="//www.cnblogs.com/images/xml.gif" alt="订阅" /></a>--></li>
<li><a id="blog_nav_admin" class="menu" rel="nofollow" href="https://i.cnblogs.com/">管理</a></li>
</ul>
		<div class="blogStats">
	 """


soup=BeautifulSoup(souphtml)

print(soup.title.string)


