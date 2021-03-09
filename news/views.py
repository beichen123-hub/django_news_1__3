from django.shortcuts import render, HttpResponse, redirect

from news.models import NewsType, NewsInfo, Login


def show(request):
    return render(request, 'Index.html', {"info": NewsInfo.objects.all()})


def add(request):
    n1 = NewsType.objects.create(tName='新闻')
    n2 = NewsType.objects.create(tName='财经')
    n3 = NewsType.objects.create(tName='娱乐')
    n4 = NewsType.objects.create(tName='体育')

    NewsInfo.objects.create(tid_id=n1.tid, nTitle='彭于晏', nAuthor='张一', nContent='彭于晏哈哈哈哈', NStatus=False)
    NewsInfo.objects.create(tid_id=n2.tid, nTitle='彭于晏', nAuthor='张二', nContent='彭于晏哈哈哈哈', NStatus=True)
    NewsInfo.objects.create(tid_id=n3.tid, nTitle='彭于晏', nAuthor='张三', nContent='彭于晏哈哈哈哈', NStatus=False)
    NewsInfo.objects.create(tid_id=n4.tid, nTitle='彭于晏', nAuthor='张四', nContent='彭于晏哈哈哈哈', NStatus=True)
    NewsInfo.objects.create(tid_id=n4.tid, nTitle='彭于晏', nAuthor='张五', nContent='彭于晏哈哈哈哈', NStatus=True)
    NewsInfo.objects.create(tid_id=n4.tid, nTitle='彭于晏', nAuthor='张六', nContent='彭于晏哈哈哈哈', NStatus=False)
    return HttpResponse('success')


def insert(request):
    if request.method == 'POST':
        nTitle = request.POST.get('nTitle')
        nAuthor = request.POST.get('nAuthor')
        tName = request.POST.get('tName')
        NStatus = request.POST.get('NStatus')
        nContent = request.POST.get('nContent')
        t = NewsType.objects.filter(tName=tName).first()
        print(t.tid)
        if t:
            NewsInfo.objects.create(tid_id=t.tid, nTitle=str(nTitle), nAuthor=str(nAuthor), nContent=str(nContent),
                                    NStatus=str(NStatus))
        else:
            pass
        return redirect('show')
    return render(request, 'InsertNewsInfo.html')




def delete(request, id):
    print(id)
    NewsInfo.objects.get(nid=id).delete()
    return redirect('show')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if Login.objects.filter(email=email, password=password).first():
            return redirect('show')
        else:
            return HttpResponse('密码输入错误')
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        Login.objects.create(email=email, password=password)
        return redirect('login')
    return render(request, 'register.html')
