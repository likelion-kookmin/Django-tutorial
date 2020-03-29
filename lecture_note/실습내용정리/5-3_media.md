# Media 란?
#### 사용자가 사이트에서 업로드하는 파일, 사이트 관리자가 admin 페이지에서 데이터를 추가할때 올리는 이미지 파일
ex) imagefield나 filefield를 통해 업로드되는 이미지나 파일

-  static : 개발자를 위한 폴더
- media: 사용자를 위한 폴더

<br>

## 1. Media 경로 설정
```
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```
###### static 이랑 비슷한거 눈치채셨나요? 나중에는 STATIC_URL,STATIC_ROOT 복붙하고 media로만 바꿔서 작성하면 끝!

+ media 파일 요청 받을 URL 주소 MEDIA_URL 변수에 설정
+ 실제 media 파일 저장할 폴더 MEDIA_ROOT 변수에 설정

#### 이때, media파일은 분산되어 있지 않아 따로 모아줄 필요없이 MEDIA_ROOT에 모이게 됨.

## 2.URL 설정
#### url 맨뒤에 추가
#### 방법 1
```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name="home"),
    path('new/', blog.views.new, name='new'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
#### 방법2 
```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name="home"),
    path('new/', blog.views.new, name='new'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
<br>

## 3. 이미지 받아올 model 만들기

우리 이전에 했던 model을 만들고 form을 받아서 정보를 받아오는 방법으로 해봅시다!

#### 먼저, model에 imagefield 추가
```
image = models.ImageField( upload_to="blog/", null=True, blank=True)
```
+ upload_to:업로드 된 이미지들을  media/blog/ 경로로 넣기

#### migrations + migrate 해주기
modeld을 수정했으니 `python manage.py makemigrations` 와 `python manage.py migrate` 해주기
<br>

#### 주의사항! makemigrations 오류 해결
file을 다루기 위해서는 파이썬패키지인 pillow 필요!
```
pip install Pillow
```
설치하기!

## 4. form에 알려주기
model에 만들어 줬으니 form 에도 알려주기
 #### forms.py에 가서 fields 에 'image' 추가
 ```
 class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body', 'image']
```

#### view.py 수정
##### 이미지를 받아올때는 file을 다루는거기 때문에 `request.FILES`추가 해줘야함
```
def new(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            content = form.save(commit=False)
            content.pub_date = timezone.now()
            content.save()
            return redirect('home')        
    else:
        form = BlogForm()
        return render(request, 'new.html', {'form':form})
```

## 5. 서버 돌려서 확인하기
`python manage.py runserver` 돌려서 확인해보기!

<br>

## 번외) Model에만 추가하고 Form 사용하지 않을때 이미지 띄우기
#### 3번 과정까지 한뒤, html에 가서 image 불러오면 됨
```
<img src="{{ blog.image.url }}">
<img src="{{ blog.image.path }}">
```
#### 이때 뒤에 `~.url` 이나 `~.path` 꼭 붙여줘야함! <br>
* DB에는 파일의 경로가 문자열로 저장되어 있기때문에 이미지가 들어있는 경로를 불러오지 않으면 이미지 볼러 올 수 없다.
