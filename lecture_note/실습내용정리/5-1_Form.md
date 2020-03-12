# Form
사용자부터 정보를 받아와 서버에 제출하는것(텍스트box, 체크박스, 날짜 등등)

`django`에서는 모델로부터 form 형태를 자동으로 만들어 주는 기능 있다.

### Form을 이용하면 얻는 장점
우리는 기존에 정보를 받는 칸을 만들때 model 객체를 이용해서 html에 하나하나 직접 만들어 줬다!

물론 이 방법도 전혀 문제는 안되지만,
만약 model의 입력받는 수가 많아지고 수정/삭제가 빈번하게 일어날때 기존의 방법으로는 비효율적이다.

따라서! 우리는
#### model을 기반한 form을 만들고, model로부터 field를 읽어들여 formfield를 세팅하는 더 간단한 방법으로 해본다!(말만 어려워요ㅎ.ㅎ)

## 1. forms.py 만들기
#### 상속받을 `model`이 있는 위치에 `forms.py` 파일 생성
 `App`<br>
    ├─ `models.py` <br>
    └─ `forms.py` 



 #### `forms.py` 생성후 import 해야할것 기입
  + forms 클래스
 + 상속 받을 모델
```
from django import forms
from .models import Blog 
```




#### 클래스 만들기
```
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body']
```
+ `django`에서는 `Meta class`가 내부클래스로 활용, 기본 필드값을 재정의함
+ `Meta class`안에 어떤 `model`기반으로 `form` 생성 할것인지 적기
+ `model`의 속성중 입력받길 원하는 값들 작성

##### 어? pub_date는 그럼 어떻게 받지? 
우리는 현재 model안에 title, pub_date, body가 있지만 날짜는 따로 기입안해도 서버가 저절로 넣어서 처리하게끔 할 것 이다!
->  `views.py`에서 처리하자!

## 2. `views.py` 수정

#### 폼 불러오기
```
from .forms import BlogForm
```

#### 함수 작성
form으로 만들어 지는 페이지는 2가지 처리를 해주어야한다.<br>
1. 데이터가 입력된 후 제출 버튼을 눌렀을 때 DB에 입력
2. form이 빈칸상태로 보여지는 것(입력전 상태)


#### 1. 인 경우 request를 받은 method가 `POST`상태일때를 말한다
```
def new(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            content = form.save(commit=False)
            content.pub_date = timezone.now()
            content.save()
            return redirect('home')    
```
+ `if request.method == 'POST':`<br> 
   `form = BlogForm(request.POST)`<br>
   POST방식으로 요청이 들어오면 form에 BlogForm 객체를 만들고 넣어준다.
+ `is_valid`함수는 받아온 값들이 유효한지 판단해주는 함수이다. 유효하면 form에 입력된 데이터들을 가져온다. `content = form.save(commit=False)`
+ 원래는 `form.save()`로 바로 저장할 수 있지만, pub_date를 처리하기 위해 일단 데이터를 불러오고 pub_date까지 넣은 뒤 저장해 준다.
+ pub_date는 `django utility`를 이용해 넣어준다.`pub_date = timezone.now()`
  - `from django.utils import timezone`도 잊지 않고 맨위에 써준다.(매우 중요!)
+ 마지막으로 `save()`메소드로 DB에 넣어주고 메인페이지로 돌아가게 하기 `return redirect('home') `

#### 2. 인 경우 url을 타고 딱 들어왔을때니깐 method가 `GET`상태일때를 말한다
```
    else:
        form = BlogForm()
        return render(request, 'new.html', {'form':form})
```
+ if문이 `POST`이니깐 `GET`인 경우는 else 로 처리
+ BlogForm의 객체를 만들어 변수에 넣어준다. `form = BlogForm()`
+ html에 띄우기 위해 3번째 인자 즉, 딕셔너리 자료형으로 넣어 전달한다. `return render(request, 'new.html', {'form':form})`

#### 완전한 함수는 이렇게 된다.
```
def new(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            content = form.save(commit=False)
            content.pub_date = timezone.now()
            content.save()
            return redirect('home')        
    else:
        form = BlogForm()
        return render(request, 'new.html', {'form':form})
```

## 3.  `urls.py` 설정
127.0.0.1:8000/new 로 접속하면 new 함수 실행하도록 path추가<br>
` path('new/', blog.views.new, name='new'), `

## 4. `form` 띄울 `html`만들기
#### new.html 만들기
 `templates`<br/>
    ├─ `home.html` <br>
    └─ `new.html` 

#### html 채우기
```
<div calss='container'>
    <form method='POST' action='' enctype="multipart/form-data">
        {% csrf_token %}
        <table>
            {{form.as_table}}
        </table>
        <br>
        <input class="btn btn-dark" type="submit" value="제출하기">
    </form>

</div>
```
+ `{% csrf_token %}` 웹 해킹 기법 중 하나인 csrf 기법을 방지하기 위한 기능
+ `{{form.as_table}}` form을 table 형식으로 출력
  - form 객체의 템플릿 변수<br>
  폼의 각 모델을 모두 각각의 특정 태그로 씌워서 나타내주는 변수 ex) `form.as_p` (p태그로 나타냄) , `form.as_ul` 등


## 5. 서버 돌려서 확인
`python manage.py runserver` 입력한 뒤 만든 form을 확인하고 그전과 달라진게 있나 확인해보자!


