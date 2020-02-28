## 1주차 - 1.기본환경 셋팅 + HelloWorld 띄우기

### 미리 준비해와야 하는것 !! 중요! 꼭 설치해오기
1. `git bash` 설치하기
2. `vscode` 설치하기
3. `python` 설치하기
+오늘 하는 모든 것을 이해하지않아도 된다! 라는 마음으로 따라 칠것

### 1. 바탕화면에 폴더를 만들고 vscode로 연다.

### 2. 터미널을 연다. (터미널 -> 새 터미널)

### 3. 터미널 상태를 git bash로 맞춰준다

### 4. 파이썬 버젼을 확인한다.

```
python --version 
```
`python`이 설치가 잘되었는지 확인하는 의미

### 5. 가상환경을 설치한다.

```
python -m venv (내 가상환경 이름)

ex)
python -m vevn myvenv 
```
예시에선 `myvenv`가 내 가상환경 이름이다

### 6. 가상환경을 실행한다.

```
source myvenv/Scripts/activate
```
`Scripts`에 S는 대문자이다!!!!!

### 7. 장고를 설치한다.

```
pip install django
```

자 여기까지 해줬으면 장고 프로젝트를 시작하기 위한 가장 기본적인 설정은 끝난것이다!!


### 이제 화면에 Hello World 를 띄워보자!!

### 1.장고 프로젝트 만들기 
```
django-admin startproject (프로젝트이름)

ex)
django-admin startproject myproject
```
예시에서 `myproject`가 본인 프로젝트 이름이다.<br/>
`myproject`를 보면 `manage.py` 라는 파일이 있는데 그 파일이 서버를 돌리는 역할을 해준다.

### 2.장고프로젝트 폴더 안에서 앱 만들기
```
cd myproject
```
터미널 상에서 `myproject`라는 폴더안으로 이동하는 명령어이다.<br/>
 이렇게 해야지 `manage.py` 가 있는 폴더로 이동한다.

```
python manage.py startapp (앱이름)

ex)
python manage.py startapp HelloWorld
```
`HelloWorld`가 앱이름이다. <br/>
앱은 프로젝트를 이루는 작은 단위이다.<br/>
우리가만든 `HelloWorld`앱은 화면에 `HelloWorld`를 출력하는 역할을 하는 앱이다.<br/>
각자의 기능과 역할에 맞게 앱을 만들어주면된다.<br/>
예를 들면 네이버 메인화면을 봤을 때 검색창을 띄워주는 부분이 있고 로그인하는 부분이 있고 기사를 띄워주는 부분이있는데 <br/>
검색창을 띄워주는 부분 따로 앱을 만들고 로그인 하는 부분을 따로 <br/>
앱을 만들어주고 기사띄워주는 부분을 앱을 따로만들고 요런식으로 기능에 맞게 앱을 분할하면 된다.

### 3.settings.py 에 앱 등록하기
 앱을 만들었다고 해서 프로젝트가 바로 알수 있는게 아니다. <br/>
 그래서 프로젝트(myproject)안의 `settings.py` 에다가 앱을 인식시켜줘야한다.<br/>

 `myproject`<br/>
├─ `__pycache__` 폴더<br/>
├─ `__init__.py`<br/>
├─ `wsig.py`<br/>
├─ `setting.py`<br/>
└─ `url.py`<br/>
안에서 아래와 같은 부분에
 ```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'HelloWorld',
]
 ```
`HelloWorld`를 적어주면된다.<br/>
뒤에 쉼표 잊지말것! 이것 때문에 오류많이남!<br/>

### 4. HelloWorld 앱에 새폴더 만들기
새폴더 이름은 templates <br/>
우리가 만들 템플릿이 들어갈 공간이다!

`HelloWorld`<br/>
├─ `migration` 폴더<br/>
├─ `templates` 폴더<br/>
├─ `__init.py`<br/>
├─ `admin.py`<br/>
├─ `apps.py`<br/>
├─ `models.py`<br/>
├─ `test.py`<br/>
└─ `views.py`<br/>

### 5. tempates 폴더안에 템플릿 만들고 내용작성
템플릿 파일이름은 `home.html`<br/>
이 파일안에 우리가 화면에 출력할 Hello World라는 내용이들어감

```
<h1>Hello World !!!!!!!!!</h1>
```
이렇게 작성 ㄱㄱ

### 6. 앱의 views.py에 함수작성
```
def home(request):
    return render(request,'home.html')

```

### 7. 프로젝트의 urls.py에 경로 설정
```
from django.contrib import admin
from django.urls import path
import HelloWorld.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HelloWorld.views.home, name= "home"),
]

```
`import HelloWorld.views` 이 코드를 적어넣는 것을 까먹지말자!!!

### 8.터미널에서 실행시켜보자
```
python manage.py runserver
```
실행시키고 뜨는 127.0.0.1.8000을 누르고 Hello World가 잘 뜨는지 확인하자<br/>
만약 `manage.py` 를 찾을 수가 없다는 에러가 뜨면 터미널에다가

```
ls
```
를 입력해서 현재 폴더에 `manage.py`가 있는지 확인하고 있는 위치로 `cd`를 통해 이동하자<br/>
`cd ..`는 상위 폴더로 이동<br/>
`cd myproject`는 하위에 있는 `myproject`폴더 안으로 이동<br/>

### 9. 잘 따라오셧나여???
맞춤법이나 오타있으면 피드백점




