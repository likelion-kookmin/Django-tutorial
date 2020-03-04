## 4주차 - CRUD


### 환경 설정
전 시간 환경 설정까지 세팅해주세요. 
project 이름은 BlogProject
app 이름은 blog
setting에 blog 있다고 알려주고
templates 만들어 주고
저번 시간에 다 했죠?

### Start Blog Project

이제부터 웹사이트의 기본 중 기본인 crud를 실습하고 blog 웹 페이지를 만들어 봅시다!

### Models.py 이용

저번 실습 때는 모델을 이용하지 않고 TV(templates, views) 만을 이용하여 웹페이지를 만들었습니다.
이제부터 blog에 글을 저장하기 위해 [DataBase](https://ko.wikipedia.org/wiki/%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4)를 사용해야 합니다. 'database'가 어렵다면 그냥 excel 표처럼 어딘가 저장된다라고 생각하면 되시고요 
중요한건, 이 'database'라는 표를 짜기 위해 우리는 'models.py'에 'class'를 만들어줘야 합니다.

### 왜 class가 사용되나요?
파이썬 공부 하셨을 때, 배우셨겠지만 class 는 객체를 만들어주는 틀 같은 놈입니다.
이와 마찬가지로 db에 어떤 정보를 저장할때, 일정한 틀이 있어야겠죠? 그래서 class로 우리가 만들어 줘야 할 객체의 틀을 만들어 줍니다.


### models.py 
'''models.py
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()

'''

일단 이렇게만 만들어 봅니다. 
blog글을 만들 것이기 때문에 **제목(title)**, **날짜(pub_date)**, **본문(body)** 이라는 field를 만들어 줍시다.
field는 그냥 직관적으로 생각하는데로 아시면 됩니다. 영역?,공간? 흠..  
얘네는 엑셀로 따지면 가로줄 입니다. 그래서 column이라고도 부릅니다.

코드를 계속 보다보면뭔가 겹치는게 보이시지 않습니까? 바로 models 입니다.
이 친구 덕분에 우리는 django에 맞는 db를 저장 시킬 수 있는 class를 만들 수 있게 됩니다.
그래서 맨 위에 
'''
from django.db import models
'''
import를 해 주었고요(import는 python 시간에서 배웠을거라 믿습니다.)
models라는 친구를 이용해서 만들어 주는 것이 있죠

**models.Model** django.db에 models 라는 거를 상속 받아 class를 만든다(상속이라는 개념은 따로 공부하시고 오면 더 좋습니다.)
**models.CharField** models 라는 친구의 CharField라는 char형 정보를 저장해주는 field입니다. ()안에 max_length는 최대 몇 byte 저장 할꺼냐? 설정하는겁니다. 필수로 지정해야 것이니 꼭 써 놓읍시다.~~(안그러면 에러나요)~~
**models.DateTimeField** 얘는 date와 time을 저장하는 field입니다. 날짜 저장한다고 심플하게 생각하시면 될 것 같습니다. 
**models.TextField** 얘는 긴 문자열을 저장하는 녀석입니다. 위에 charfield는 max_length가 반드시 필요하잖아요? 그렇기 때문에 몇 글자를 적을지 알 수없는 본문에는 맞지 않습니다. 그러므로 TextField()를 사용합니다.

그러면 우리는 우리가 만들고 싶은 데이터 형식의 틀을 만든 것입니다.

그리고 이 모델을 만들었다. 이런 형식으로 데이터를 저장할꺼다! 라고 db에 알려줘야 됩니다.

manage.py 가 있는 경로에서 터미널에  두가지 명령어를 쳐줍니다.

'''
python manage.py makemigrations
'''
migration 파일 만들기

'''
python manage.py migrate
'''
migration 파일을 db에 적용하기.

model에 변경사항 알려주고 적용시키는 명령어라고 생각하시면 됩니다. 
**models.py를 수정할때, 반드시 이 명령어를 실행해야 됩니다.**


그리고 얘가 어떻게 저장되는지 보고 싶을 수 있는데요? 그러기 위해 admin 페이지를 이용합시다

### admin 만들기
admin.py에 아래 코드를 적습니다.

'''
from django.contrib import admin
from .models import Blog # 현재 경로의 models에서 Blog 클래스를 가져오기 위해 import 해줍니다


admin.site.register(Blog)
'''
admin에 Blog라는 모델이 만들어졌다. 라고 알려주는 코드 입니다.

어드민 페이지를 아무나 들어갈 순 없겠죠?
그러니 **SuperUser**를 만들어줍니다.

manage.py 가 있는 경로에서 터미널에서 쳐 줍시다.

'''
python manage.py createsuperuser
'''
만들라는 것, 다 만들면 superuser가 생성됩니다.


'''
python manage.py runserver
'''
를 하고 위에 url에 기존 url에 '/admin'을 더해서 admin 사이트로 이동합니다. 
그리고 객체를 만들어보면 Object어쩌구저쩌구 이쁘지 않게 객체가 생성됩니다. ㅠ

title이 뜰 수 있도록 models.py에 Blog 클래스에 메소드를 하나 추가해 줍시다.

'''models.py
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    
    def __str__(self):
        return self.title

'''
제목을 반환하는 메소드입니다. 그러면 admin page에서 제목으로 객체가 나오는 것을 보실 수 있습니다.
메소드만 만든거라 migrate를 할 필요는 없습니다.



## CRUD
이제 모델을 만들었으니 본격적으로 blog를 만들어 봅시다.

### CRUD란?
1.  **C** 객체 생성(create)
2.  **R** 객체 읽기(Read)
3.  **U** 객체 수정(update)
4.  **D** 객체 삭제(delete)

## Read 

### home만들기

Blog 객체를 만들었으니 얘를 html에 띄어 봅시다.

1. templates안에 home.html 만들기

2. views.py에서 함수 작성

'''views.py

from django.shortcuts import render 
from .models import Blog # 현 경로에 있는 models.py에 Blog 를 import 합니다.

def home(request):
    blogs = Blog.objects.all() # Blog 의 객체를 전부다 가져와서 blogs에 저장합니다
    return render(request, 'home.html',{'blogs':blogs}) # home.html에 blogs라는 객체집합을 'blogs'라는 key값으로 전달해서 rendering 합니다.

'''
3. url 연결하기 

''' urls.py
from django.contrib import admin
from django.urls import path
import blog.views  #blog 앱에 있는 views.py를 import합니다.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name = "home" ),
]

'''
path라고 제공되는 메소드의 들어가야할 내용은 다음과 같습니다.

path('해당 url', views함수 , namespace)

우리는 home.html을 사이트를 키면 첫 페이지에 띄울 것이기 때문에 '' 빈칸으로 두고

이 url로 갔을 때, blog 안에 views.py home함수를 실행시킵니다. views.py에서 만든 그 함수입니다.

namespace는 html파일 같은 곳에서 이 path를 호출할때 사용됩니다.

4. home.html 작성

home.html에 그냥 blogs로 받으면 이상한 queryset 어쩌구 저쩌구 뜹니다.
queryset은 query들의 집합으로 query는 하나의 객체라고 생각하시면 됩니다.

이 queryset을 for문으로 통해 하나씩 보여줍시다.

'''home.html

<h1>LIKELION Blog Project</h1>

<div>
   {% for blog in blogs%}
      <hr>
      <h2>{{blog}}</h2>
   {% endfor %}
</div>

'''

{%%} 와 {{}}에서 배웠던 template 문법입니다. 

이렇게 보내주면 object 어쩌구라고 뜹니다. 그러면 안에 내용물을 볼 수가 없죠 
다시 수정해 줍시다.

'''home.html

<h1>LIKELION Blog Project</h1>

<div>
   {% for blog in blogs%}
      <hr>
      <h2>{{blog.title}}</h2>
      <p>{{blog.pub_date}}</p>
      <p>{{blog.body}}</p>
   {% endfor %}
</div>

'''
우리가 class에서 만들었던 'title','pub_date','body'를  **객체.필드(혹은 메소드)**라는 문법 꺼내 보여 줄 수 있습니다.

그런데 하나 생각을 해 봅시다. body가 너무 길어 버리면 너무 더럽지 않을까요?

5. summary

그래서 models.py에서 메소드를 하나 추가할 것입니다.


'''models.py
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]

'''

summary라는 메소드를 추가했습니다. 이 함수를 호출하면 body를 100자만 보여줍니다. 
이 역시 메소드만 만든 것이니 migrate를 할 필요는 없습니다.


'''home.html

<h1>LIKELION Blog Project</h1>

<div>
   {% for blog in blogs%}
      <hr>
      <h2>{{blog.title}}</h2>
      <p>{{blog.pub_date}}</p>
      <p>{{blog.summary}}</p>
   {% endfor %}
</div>

'''

위에 body 대신에 summary로 고쳐줍니다.

### detail만들기

home에 객체 list가 보여질때, 객체 하나를 선택해서 이 객체의 body를 포함한 하나의 정보만 보게 만들겠습니다.

detail을 들어가기 전에 **pk** 와 **path-converter** 라는 개념을 알아야 합니다.

pk 또는 id라고도 하는데 객체 하나에 부여되는 고유한 값입니다. 그냥 python에서도 변수에 .id 를 하면 어려운 숫자의 id값을 확인 할 수 있는데요.
이처럼 객체 하나에 대해서도 id값이 부여됩니다. 이를 장고가 1번 2번... 필드처럼 제공을 합니다. 우리가 따로 column을 만들지 않아도 자동적으로 만들어집니다.

path-converter 는 url 에서 설명드리겠습니다.

1. views.py에서 detail 함수 만들기

'''views.py
from django.shortcuts import render,get_object_or_404 # get_object_or_404라는 메소드를 하나 추가로 import 받습니다.
from django.utils import timezone
from .models import Blog
# Create your views here.

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html',{'blogs':blogs})

def detail(request,blog_id): # 매개변수에 request 말고도 blog_id가 추가 되는데요 여길 통해서 객체의 id값을 받을 것입니다.
    blog = get_object_or_404(Blog,pk = blog_id)
    return render(request, 'detail.html',{'blog':blog})
'''

home 함수 아래 detail 함수를 만들었습니다. **get_object_or_404** 라는 메소드를 사용할 것입니다.

이 메소드의 파라미터, 즉 ()안에 내용물은 get_object_or_404(model이름, pk = id값) 입니다. 

메소드의 역할은 '저 모델의 몇번 id값의 객체를 가져와라 아니면 [404에러](https://ko.wikipedia.org/wiki/HTTP_404)를 띄워라' 라는 기능을 하는 메소드입니다. 
이로써 queryset이 아닌 우리가 특정 할 수있는 하나의 객체를 가져올 수 있게 됩니다.

그리고 얘를 blog에 담아서 'blog'라는 key 값으로 detail.html과 함께 rendering 합니다

2. urls.py

''' urls.py
from django.contrib import admin
from django.urls import path
import blog.views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name = "home" ),
    path('blog/<int:blog_id>', blog.views.detail, name = "detail"), # 이 줄을 추가해 줍시다.

]

'''
**path-converter 란**
위에 `<int:blog_id>`같은 것들을 path-converter라고 합니다.
장고에서 여러 객체들을 다루는 계층적 url이 필요할 경우에 사용하며, `<type:name>`와 같은 모양입니다.
'지정한 converter type의 name변수를 view 함수로 넘겨라' 하고 정리할 수 있겠네요.
converter의 다양한 타입에 대해 궁금하시면 구글에 검색해보시는 걸 추천드립니다!

저 path-converter를 통해 detail 함수로 id값을 넘겨 올 수 있습니다.

3. detail.html

templates 폴더 안에 detail.html을 만들어 줍시다.

'''detail.html
<h1>Blog Project Detail</h1>
<br>
<br>
<h2>{{blog.title}}</h2>
<hr>
<p>{{blog.pub_date}}</p>
<hr>
<p>{{blog.body}}</p>

'''
위와 같이 detail.html을 만들어 줍니다.

여기서 끝일 것 같지만 하지만 한가지 의문이 듭니다. id값은 어디서 오는거지?

4. home.html 

우리가 detail을 보기 위해서는 home.html에서 접근을 해야하는데요. a태그 하나 만들어주면 됩니다.

'''home.html
<h1>LIKELION Blog Project</h1>

<a href="{%url 'new' %}">make your blog</a>

<div>

   {% for blog in blogs%}
      <hr>
      <a href="{% url 'detail' blog.id %}">
      <h2>{{blog.title}}</h2>
      <p>{{blog.pub_date}}</p>
      <p>{{blog.summary}}</p>
     </a>
   {% endfor %}
</div>
'''
위에 기존 home에서 추가 된 것이 있는데

'''
<a href="{% url 'detail' blog.id %}"><a>
'''
이 a태그 입니다 a태그를 어디다가 씌울지는 상관은 없지만 for 안에 있어야 됩니다.

path의 세번째 인자인 namespace를 여기서 사용합니다 **name = "이름"** 했던 부분에 그 **"이름"** 을 넣고 뒤에 path-converter를 거쳐서 detail함수의 매개변수로 받을 blog의 id인 **blog.id**를 써 줍니다  


### 이로써 read의 역할을 하는 home과 detail이 완성이 됬습니다. 
