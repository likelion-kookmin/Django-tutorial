## 4주차 - CRUD
웹 페이지 기본 형식인 [CRUD](https://ko.wikipedia.org/wiki/CRUD)방법으로 블로그를 만들어 봅시다!


### CRUD란?
1.  **C** 객체 생성(create)
2.  **R** 객체 읽기(Read)
3.  **U** 객체 수정(update)
4.  **D** 객체 삭제(delete)

### 환경 설정
BlogProject라는 project와 blog앱을 만들어 주세요! 
저번 시간에 했던거니까 따로 코드는 안올리겠습니다.



### Models.py 이용

저번 실습 때는 모델을 이용하지 않고 TV(templates, views) 만을 이용하여 웹페이지를 만들었습니다. 이러면 HTML에 써놓았던 정보들이 사이트를 꺼버리면 다 날아가버리게 됩니다.
이제부터 blog에 글을 저장하기 위해 [DataBase](https://ko.wikipedia.org/wiki/%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4)를 사용해야 합니다.
`database`라는 표를 짜기 위해 우리는 'models.py'에 `class`를 만들어줘야 합니다.

+ class가 사용되는 이유
파이썬 공부 하셨을 때, 배우셨겠지만 class 는 객체를 만들어주는 틀입니다.
이와 마찬가지로 db에 어떤 정보를 저장할때, 일정한 규격에 맞게 저장하기 위해 class로 우리가 만들어 줘야 할 객체의 틀을 만들어 줍니다.


### models.py 
```models.py
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
```

blog글을 만들 것이기 때문에 **제목(title)**, **날짜(pub_date)**, **본문(body)** 이라는 field를 만들어 줍시다.<br/>
얘네는 엑셀로 따지면 가로줄 입니다. 그래서 column이라고도 부릅니다.

코드를 계속 보다보면 **models.**Model, **models.**CharField 처럼 models라는 것이 많이 등장합니다.
models라는 모듈안에서 Model ,CharField를 사용한다는 뜻입니다.  
그래서 맨 위에 
```
from django.db import models
```
django.db라는 곳에서 models를 import 해왔습니다.<br/>
저 모듈을 통해서 django에 맞는 db구조를 class로 짜는 것입니다.

`models.Model` django.db에 models라는 모듈안에 Model class를 상속 받아 class를 만든다.<br/>
`models.CharField` models 안에 CharField라는 char형 정보를 저장해주는 field입니다. ()안에 `max_length`는 최대 몇 byte 저장 할것인지 설정하는겁니다. 필수로 지정해야 것이니 꼭 써 놓읍시다.~~(안그러면 에러납니다)~~<br/>
`models.DateTimeField` 얘는 date와 time을 저장하는 field입니다. <br/>
`models.TextField` 긴 문자열을 저장하는 field입니다. CharField 와는 달리 `max_length`가 필요 없습니다.<br/>

class로 db의 model을 짰으면 얘를 db에 알려줘야 합니다. <br/>

manage.py 가 있는 경로에서 터미널에  두가지 명령어를 쳐줍니다.<br/>

```
python manage.py makemigrations
```
+ migration 파일 만들기

```
python manage.py migrate
```
+ migration 파일을 db에 적용하기.

model에 변경사항 알려주고 적용시키는 명령어라고 생각하시면 됩니다. <br/>
**models.py를 수정할때, 반드시 이 명령어를 실행해야 됩니다.**


* 그리고 이제 이 모델이 어떤 식으로 만들어졌는지 보기 위해 admin 사이트로 가겠습니다.

### admin 만들기
admin.py에 아래 코드를 적습니다.

```
from django.contrib import admin
from .models import Blog # 현재 경로의 models에서 Blog 클래스를 가져오기 위해 import 해줍니다


admin.site.register(Blog)
```

admin에 Blog라는 모델이 만들어졌다고 알려주는 코드 입니다.<br/>

이제 어드민 페이지에 접근 할 수 있는  **SuperUser**를 만들어줍니다.

manage.py 가 있는 경로에서 터미널에서 쳐 줍시다.

```
python manage.py createsuperuser

```
만들라는 것, 다 만들면 superuser가 생성됩니다.


```
python manage.py runserver
```

서버를 돌리고 url에 기존 url에 '/admin'을 더해서 admin 사이트로 이동합니다.<br/>

그리고 객체를 만들어보면 Object어쩌구저쩌구 객체가 이상한 이름으로 생성이 됩니다. ㅠ<br/>

title로 이 객체를 볼 수있게  models.py에 Blog 클래스에 메소드를 하나 추가해 줍시다.<br/>

```models.py
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    
    def __str__(self): 
        return self.title

```
제목을 반환하는 메소드입니다. 그러면 admin page에서 제목으로 객체가 나오는 것을 보실 수 있습니다.<br/>
메소드만 만든거라 migrate를 할 필요는 없습니다.


***이제 모델을 만들었으니 본격적으로 이 만들어 준 모델을 이용하여 crud를 구현해서 블로그 사이트를 만들어 봅시다.***<br/>

## Read 

### home만들기

Blog 객체를 만들었으니 객체를 html에 띄어 봅시다.

#### 1. templates안에 home.html 생성

#### 2. views.py에서 함수 작성

```views.py

from django.shortcuts import render 
from .models import Blog # 1

def home(request):
    blogs = Blog.objects.all() # 2
    return render(request, 'home.html',{'blogs':blogs}) # 3

```
1. models.py 에서 만든 Blog 클래스로 만들어진 데이터를 사용할 것이므로 import 합니다.
2. Blog 의 objects 들을 all() 메소드를 사용해서 전부 가져와서 queryset 형태로 blogs에 넣는다. 그래서 `blogs = Blog.objects.all()`
   * all() 말고도 filter , get 등등 다양한 메소드가 존재합니다.
   * queryset은 query들의 집이고, query는 하나의 객체라고 생각하시면 됩니다.
3. {'blogs':blogs}는 위에 queryset을 저장한 blogs을  dic형태로 'blogs'라는 key값에 저장합니다. <br/>
    이 dictionary와 함께 home.html 을 request 한 것을 rendering 합니다.

#### 3. url 연결하기 

``` urls.py
from django.contrib import admin
from django.urls import path
import blog.views  #blog 앱에 있는 views.py를 import합니다.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name = "home" ), # 추가 된 url
]

```
이제 url path를 views.py에서 함수 하나 만들때 마다 path 하나씩 만들게 됩니다. path에는 3가지 인자가 들어가는데,<br/>

`path('해당 url', views함수 , namespace)`<br/>

+ 첫번째 인자는 views.py에 만든 함수를 실행시킬 url 경로 입니다.(사이트 첫화면에 home을 띄울 것이기 때문에 ''으로 만듭니다.)

+ 두번째 인자는 views.py에 함수 입니다.

+ 세번째 인자는 namespace입니다.  html파일 같은 곳에서 이 path를 호출할때 사용됩니다.

#### 4. home.html 작성

home.html에 그냥 `{{blogs}}`로 받으면 이상한 queryset 어쩌구 저쩌구 뜹니다.<br/>

이 queryset을 for문으로 통해 하나씩 객체로 보여줍니다.<br/>

```home.html

<h1>LIKELION Blog Project</h1>

<div>
   {% for blog in blogs%}
      <hr>
      <h2>{{blog}}</h2>
   {% endfor %}
</div>

```

이렇게 보내주면 object 어쩌구라고 뜨고 안에 내용물을 볼 수가 없습니다.<br/>
다시 수정해 줍시다.<br/>

```home.html

<h1>LIKELION Blog Project</h1>

<div>
   {% for blog in blogs%}
      <hr>
      <h2>{{blog.title}}</h2>
      <p>{{blog.pub_date}}</p>
      <p>{{blog.body}}</p>
   {% endfor %}
</div>

```
우리가 class에서 만들었던 'title','pub_date','body'를  '객체.필드(혹은 메소드)'라는 문법 꺼내 보여 줄 수 있습니다.<br/>

그런데 하나 문제가 있습니다. body가 엄청 긴 객체가 오면 home이 굉장히 더러워 진다는 점입니다. 그래서 model에 메소드 하나를 짜도록 하겠습니다.<br/>

##### 5. summary

그래서 models.py에서 메소드를 하나 추가할 것입니다.<br/>


```models.py
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]
```


summary라는 메소드를 추가했습니다. 이 함수를 호출하면 body를 100자만 보여줍니다. <br/>
이 역시 메소드만 만든 것이니 migrate를 할 필요는 없습니다.


```home.html

<h1>LIKELION Blog Project</h1>

<div>
   {% for blog in blogs%}
      <hr>
      <h2>{{blog.title}}</h2>
      <p>{{blog.pub_date}}</p>
      <p>{{blog.summary}}</p>
   {% endfor %}
</div>

```

위에 body 대신에 summary로 고쳐줍니다. 

### detail만들기

home에서 글 list가 보여질때, 글 하나를 선택해서 세부내용(detail) 화면이 보여 질 수 있도록 detail 기능을 만들어 보겠습니다<br/>
home을 만들때는 Blog 객체 뭉텅이로, queryset으로 보내면 되는데 detail은 한 글에 대한 세부내용이기 때문에 특정 객체 1개만 보내야 합니다.<br/>

그래서 객체의 [pk](https://ko.wikipedia.org/wiki/%EA%B8%B0%EB%B3%B8_%ED%82%A4) 개념을 알아야 되는데
pk는 만들어진 db테이블에객체 하나에 부여되는 고유한 값입니다. id라고 할 수도 있습니다. 그 객체에 대해서 접근을 할 때 주로 쓰입니다. 

#### 1. views.py에서 detail 함수 만들기

```views.py
from django.shortcuts import render,get_object_or_404 # get_object_or_404라는 메소드를 하나 추가로 import 받습니다.
from django.utils import timezone
from .models import Blog
# Create your views here.

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html',{'blogs':blogs})

def detail(request,blog_id): # 매개변수에 blog_id가 추가됬고 이 매개변수로 객체의 id값을 받습니다. 
    blog = get_object_or_404(Blog,pk = blog_id) #1
    return render(request, 'detail.html',{'blog':blog}) #2
```

home 함수 아래 detail 함수를 만들었습니다. `get_object_or_404`라는 메소드를 사용할 것입니다.

`get_object_or_404(model이름, pk = id값) `

이 메소드의 첫번째 인자는 가져올 객체의 모델이름, 그리고 두번째 인자는 그 객체의 id값입니다.<br/>

1. 메소드의 기능은 모델의 몇번 id값의 객체를 가져와라 아니면 [404에러](https://ko.wikipedia.org/wiki/HTTP_404)를 띄워라 라는 기능을 하는 메소드입니다.<br/> 이로써 queryset이 아닌 우리가 특정 할 수있는 하나의 객체를 가져올 수 있게 됩니다.

2. 그리고 이 id값의 객체를 blog에 담아서 'blog'라는 key 값으로 detail.html과 함께 rendering 합니다

#### 2. urls.py

``` urls.py
from django.contrib import admin
from django.urls import path
import blog.views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name = "home" ),
    path('blog/<int:blog_id>', blog.views.detail, name = "detail"), # 이 줄을 추가해 줍시다.

]

```
객체에 따라서 보여 줘야 할 url이 다 다릅니다. 이것을 path-converter를 통해서 다르게 보여 줍니다.

(example)<br/>
+ 1번 객체의 대한 detail url  http://127.0.0.1:8000/blog/1
+ 2번 객체의 대한 detail url  http://127.0.0.1:8000/blog/2

##### path-converter 란
위에 `<int:blog_id>`같은 것들을 path-converter라고 합니다.
장고에서 여러 객체들을 다루는 계층적 url이 필요할 경우에 사용하며, `<type:name>`와 같은 모양입니다.
'지정한 converter type의 name변수를 view 함수로 넘겨라' 하고 정리할 수 있습니다.<br/>
converter의 다양한 타입에 대해 궁금하시면 구글에 검색해보시는 걸 추천드립니다!

#### 3. detail.html

templates 폴더 안에 detail.html을 만들어 줍시다.

```detail.html
<h1>Blog Project Detail</h1>
<br>
<br>
<h2>{{blog.title}}</h2>
<hr>
<p>{{blog.pub_date}}</p>
<hr>
<p>{{blog.body}}</p>

```
위와 같이 detail.html을 만들어 줍니다.

이제 id값을 넘겨주고 url을 연결 시켜줄 a태그를 home.html에 만들면 됩니다.

#### 4. home.html 

```home.html
<h1>LIKELION Blog Project</h1>

<a href="{%url 'new' %}">make your blog</a> # 추가된 a태그

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
```

* `<a href="{% url 'detail' blog.id %}"><a>` 이 a태그가 추가 되었습니다. a태그를 어디다가 씌울지는 상관은 없지만 for문 안에 있어야 됩니다.

* urls.py 에서 path의 세번째 인자인 namespace를 여기서 사용합니다 `name = "detail"`했던 부분, 그것을 사용해서 url을 호출합니다. 그래서  `'detail'` 을 넣고 뒤에 보내줘야 할 blog의 id인 **blog.id**를 써 줍니다  


### 이로써 read의 역할을 하는 home과 detail이 완성이 됬습니다. 
