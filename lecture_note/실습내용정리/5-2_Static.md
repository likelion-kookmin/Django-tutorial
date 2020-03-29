# Static 이란?
이미지나 css.js 파일처럼 내용이 고정되어 있어, 응답을 할때 별도의 처리없이 파일 그대로 보여주면 되는 정적파일

#### 즉! 사용자가 직접 업로드하는 파일말고  개발자가 웹페이지에 이미지를 넣고 싶을 때 사용
<br>

## 1. Static 파일 생성
#### 앱 안에 static 파일 생성후 넣고 싶은 사진 static 폴더에 넣어주기
 `App`<br>
    └─ `static`<br> 
<br>

## 2. Static 경로 설정
#### django에 static폴더 만든거 알려주기
#### settings.py 맨밑에 코드 작성   
```
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'blog', 'static')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```
+ STATICFILES_DIR : static파일 있는 경로 작성 ('blog'안에 'static'폴더 있음)
+  STATIC_ROOT : static 파일을 한곳에 모을때, 모아줄 위치
+ 기존에 있던 STATIC_URL = '/static/' : static 파일을 불러올때의 URL

<br>

## 3. 파일 모으기 `python manage.py collectstatic` 
###### 우리는 지금 하나의 앱에만 static 파일을 만들어줬지만, 프로젝트가 더 커지면 각각 다른 앱들의 static 폴더가 많아지게 된다.

###### 이때 정적파일들이 마구 흩어져있어 모든 파일들을 하나의 경로로 모아주는 작업이 필요하다.
 collectstatic 파일은 프로젝트에서 사용하는 css, javascript,font등 모든 정적파일들 하나의 경로로 모아준다. 
 (settings.py 의 STATIC_ROOT 변수에 저장해준곳)

#### 터미널에 입력
```
python manage.py collectstatic
```
#### 모두 다 진행하면 프로젝트 밑에 하위폴더로 static이 생긴다.
 `Project`<br>
    └─ `static`<br> 

<br>

## 4. 이미지 띄우기
이미지를 띄우고 싶은 html에 들어간다. 이때, static 파일 불러오기위해 해야할것이 있다.

#### 상단에 template에 static 파일을 불러오겠다는 템플릿태그 작성
```
{% load static %}
```

#### 그다음, 원하는 곳에 img 태그를 이용해 이미지를 띄우면 된다.
```
<img src="{% static 'logo.png' %}" alt="">
```
+ {% static 'STATIC_URL이후의 경로' % } ->  쉽게는 이미지명.확장자 쓰면 됨!

<br>

## 5. 서버 돌려서 확인하기
`python manage.py runserver` 돌려서 확인해보기!