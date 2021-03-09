from django.shortcuts import render, HttpResponse
from app1.models import Article

def first(request):
    html = "Django Response"
    return HttpResponse(html)

def second(request):
    return render(request, "index.html")  

# 查询
def getArtHeadlines(request): 
    articles = Article.objects.all()  

    # # 终端打印数据 
    # print(articles) 
    # for article in articles: 
    #     print(article.headline) 
    # 第一次测试的返回数据
    # html = str([x.headline for x in articles])
    # return HttpResponse(html)   
    # 写入到 blog 模版中。
    dict  = {}
    dict["articles"] =  articles
    # # Q：why only articles[0]?? 只是测试
    # # Q: why 字典里的current_article 才能传值成功。article就不行。A: article 是个queryset。current——article取出了第一篇文章对象。
    # if len(articles) > 0:
    #     current_article  = articles[0]
    # dict["current_article"] = current_article     
    article_name = request.GET.get('name')
    # 如果name有值，并且数据库存在对应值，当前的文章就显示这篇；  
    if article_name:
        try:
            current_article = Article.objects.get(headline=article_name)
        except: 
            # 如果name有值，但是数据库没有这个对应值，那就默认显示第一篇； 
            current_article  = articles[0]   
       
    # 如果name没有值，那就默认显示第一篇；
    elif len(articles) > 0:
        current_article  = articles[0]
    dict["current_article"] = current_article     
    print(dict["articles"])
    print(article_name)
    print(dict["current_article"])
    # render()函数接收多个值，第一个request，第二个指定的模板【找不到报错】，第三个字典【可选】。
    return render(request, "blog.html", dict)