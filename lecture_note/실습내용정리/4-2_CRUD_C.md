
## Create
여태까지 객체를 생성하려면 admin사이트에 들어가서 해야 됬는데, 그런 식으로 구성된 사이트가 있으면 극혐이겠죠?

이제부터 blog 객체를 만들어 줄 create 기능을 구현해봅시다.


##### 1. templates에서 new.html을 만들어줍시다.

##### 2. views.py에서 new.html을 rendering하는 함수를 만들어 줍니다.

```views.py

def new(request):
    return render(request, 'new.html')

```
new.html만 띄우면 되는 함수라 굉장히 간단합니다.

**그리고 이 new.html은 객체를 만들어 줄 form, 새 글을 작성하는 html이 되겠습니다!**

##### 3. 글을 입력 받을 new.html을 만듭니다.

```new.html

<h1>Make New Blog</h1>


<form action="{% url 'create'%}" method="POST" >
    {% csrf_token %}

<h3>제목: <input type="text"name = "title"> </h3>
<p>내용: <textarea name="body" id="" cols="30" rows="10"></textarea></p>

<button type = "submit">작성!</button>
</form>
```
* `form` 태그 안에 action을 통해서 해당 url로 이동하고 아직 만들지 않은 `create` 함수로 생성을 해 줄 것입니다.

*  `button` type을 `submit`으로 했습니다. 누르면 `form` 안에 입력 받은내용 전체가 `create` 함수로 넘어가게 됩니다.

* `input` 태그 랑 `textarea`태그 속성에 name이 있는데요 이 name은 `create` 함수로 넘어 갈때, 중요한 역할을 하니 유심히 보고 넘어갑시다.


그런데 여기서 몇가지 익숙치 않은 코드가 보입니다.

+ form 의 인자에 ***method = "POST"*** <br/>
전 시간 TV 실습에서 request.GET을 통해 html의 정보를 받았는데, 이것을 GET방식이라고 합니다.그러나 이번에는 POST 방식을 사용할 것입니다<br/>
왜냐하면 GET 방식은 넘어가는 정보가 url을 통해 다 보여지기 때문에 보안에 좋지 않습니다. <br/>검색기능 같은 것은 GET을 통해 url에 띄워져도 상관없지만 로그인 form 이라던가 보안을 요구하는 글 작성하는 내용이 url에 그대로 노출되면 아무도 사용하지 않을 것입니다. 

+ {% csrf_token %} <br/>
그리고 POST 방식을 쓰기 위해서는 csrf_token을 보내줘야 하는데 임의에 암호화 된 토큰입니다. 이것으로 [csrf공격](https://swk3169.tistory.com/entry/Web-CSRFCross-Site-Request-Forgery-%EA%B3%B5%EA%B2%A9-%EA%B8%B0%EB%B2%95)을 방지 할 수 있습니다.

#### 4. urls.py 

new.html을 보여주는 url을 추가합시다.

```urls.py
 path('blog/new', blog.views.new, name = "new"),
```
detail 바로 아래 추가하면 됩니다. 뒤에 , 잊지 마시고요

#### 5. 객체를 생성할 create 함수 만들기 

이제 new.html을 통해 들어온 정보로 blog 객체를 만들 create 함수를 만듭시다!

```
from django.shortcuts import render,get_object_or_404,redirect # redirect를 import 합시다.
from django.utils import timezone # pub_date의 내용물을 채우기 위한 timezone을 import 합시다.

def create(request):
    new_blog = Blog() # 1
    new_blog.title = request.POST['title'] #2 
    new_blog.body = request.POST['body'] # 3
    new_blog.pub_date = timezone.datetime.now() #4
    new_blog.save() #5
    return redirect('/blog/' + str(new_blog.id)) #6

```

1. python 에서 객체를 생성해 줄 때 쓰는 문법입니다.
2. 1번에서 객체를 생성했지만 안에 column은 비워져 있습니다.html에 작성한 내용으로 채워 봅시다. POST방식으로 name이 title인 html 태그의 정보를 가져와 새로 만든 객체의 title column에 넣어줍니다.
3. POST방식으로 name이 body인 html 태그의 정보를 가져와 새로 만든 객체의 body column에 넣어줍니다.
4. pub_date column은 만든 날짜,시간 저장해야 하기 때문에 따로 html에서 받지 않고 timezone이라는 모듈에 datetime.now()라는 메소드를 사용해 현재시각을 넣어줍니다.
5. 그리고 만들어주고 각각 column을 넣어준 'new_blog'라는 객체를  save()라는 메소드를 통해 저장합니다
6. 
 * create라는 함수는 새로운 html을 띄어주는 함수가 아닙니다. 단순히 객체를 생성해 주는 함수죠. 그렇기 때문에 return에 html을 띄우는 render를 사용하지 않습니다. 기존에 있던 페이지를 띄워주는 'redirect'를 사용합니다.

 * redirect()에 ()안에는 url주소가 들어갑니다. urls.py에 path에 첫번째 인자입니다.  저 ()안에 경로를 잘 보면 detail 경로와 같다는 걸 알 수있습니다.
 객체를 생성하면 그 객체의 detail페이지로 가게 해둔것 입니다. 그리고 new_blog.id에 왜 str으로 감쌌냐는 의문이 들 수 있는데 id값은 데이터 형이 int지만 경로 ''은 string이기때문에 type에러를 방지하기 위해 str으로 형변환을 한 것입니다.


 #### 6. urls.py 

views.py에서 함수를 만들었으면 실행 시켜 줄 url이 필요합니다.

```urls.py
path('blog/create', blog.views.create, name = "create"),

```


 #### 7. home.html에 글 작성란으로 이동하는 a태그 넣기

```home.html
<h1>LIKELION Blog Project</h1>

<a href="{%url 'new' %}">make your blog</a> # 추가

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

```
<a href="{%url 'new' %}">make your blog</a> 
``
글 작성란으로 가는 a태그 하나를 추가 하시면 됩니다.


 ### CREATE 끝!
