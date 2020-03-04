## 4주차 - CRUD


## Update
글을 만드는 것은 좋은데 실수로 오타가 들어가거나 내용을 잘못 적어서 글을 수정하고 싶을 때가 있을겁니다.
이번에는 글을 수정하는 기능을 만들어 봅시다. 기본적인 원리는 앞에 create 부분과 비슷합니다.


### 1. templates에서 edit.html을 만들어줍시다.

create에서 new.html 과 똑같은 역할을 합니다. 글을 수정할 수 있는 수정 form 입니다.


### 2. views.py에서 edit.html로 rendering하는 함수를 만들어 줍니다.

'''
def edit(request,blog_id): # blog 객체의 id값을 받는 매개변수를 받는다.
    blog = get_object_or_404(Blog,pk = blog_id) # id값을 통해 객체를 불러온다.
    return render(request, 'edit.html',{'blog':blog})

'''

여기서 new.html 과 다른 점이 있는데요 바로 객체를 가져와야 한다는 점입니다. 글의 원래 내용을 바탕으로 수정을 해야하기 때문에
매개변수 받는 부분이 추가 되었고 수정 form에다가 수정을 할 blog객체를 보내줘야 합니다.


### 3. 글을 수정할 edit.html을 만듭니다.

'''
<h1>Edit Your Blog</h1>

<div>
<form action="{% url 'update' blog.id%}" method="POST" >
    {%csrf_token%}

<h3>제목: <input type="text" name = "title" value = "{{blog.title}}"> </h3>
<p>내용: <textarea name="body" id="" cols="30" rows="10">
   {{blog.body}} 
</textarea></p>

<button type = "submit">작성!</button>
</form>

</div>

'''

new.html 의 form과 비슷하게 생겼습니다. 다른점은 input 태그 안에 value값과 textarea에 {{blog.body}} edit함수에서 보내준 blog객체의 정보입니다.
그밖에는 new.html과 똑같습니다.


### 4. urls.py 

edit.html을 보여주는 url을 추가합시다.

'''urls.py
  path('blog/edit/<int:blog_id>',blog.views.edit, name = "edit"),
'''

수정해야 할 blog의 id값을 edit함수에서 매개변수로 받기 때문에 path-converter가 사용되었습니다.


### 4. 객체를 수정하는 update 함수 만들기 

'''views.py

def update(request,blog_id): # 수정할 객체의 id값을 매개변수로 받는다.
    edit_blog = get_object_or_404(Blog,pk= blog_id) #매개변수로 받은 id값으로 blog객체를 가져온다
    edit_blog.title = request.POST['title']
    edit_blog.body = request.POST['body']
    edit_blog.pub_date = timezone.datetime.now()
    edit_blog.save()
    return redirect('/blog/' + str(edit_blog.id))

'''

id값을 매개변수로 받고 그 id값으로 객체를 불러와서 그 객체의 column에 html의 수정한 정보를 덧씌웁니다.
**create는 객체를 생성했는데 update는 id값으로 객체를 가져오는게 큰 차이점입니다.**


### 4. urls.py 

views.py에서 함수를 만들었으면 얘를 연결 시킬 url이 필요합니다.

'''urls.py
path('blog/update/<int:blog_id>',blog.views.update, name = "update"),

'''
update도 매개변수를 받기 때문에 path-coverter가 필요합니다.


### 5. detail.html에 수정하기 연결

'''
<h1>Blog Project Detail</h1>
<br>
<br>
<h2>{{blog.title}}</h2>
<hr>
<p>{{blog.pub_date}}</p>
<hr>
<p>{{blog.body}}</p>

<a href="{%url 'edit' blog.id%}">수정하기</a>

'''
new.html로 가는 버튼은 home.html에 있었지만 edit.html은 detail.html에 있습니다.
이유는 설명 안해도 아시죠?

'''
<a href="{%url 'edit' blog.id%}">수정하기</a>
'''
이 a태그 하나 추가합시다 namespace 뒤에 blog.id를 넘겨줘야 한다는 점 잊지맙시다.


## UPDATE 끝!

## Delete 

수정도 만들어 줬는데 삭제도 만들어 줘야죠 바로 시작합시다.

### 1. views.py

얘는 html파일 만들 필요가 없습니다. 바로 함수 만들어 줍시다.

'''views.py

def delete(request,blog_id): # 매개변수로 id값을 받는다.
    delete_blog =get_object_or_404(Blog,pk = blog_id) # 그 id값으로 객체를 불러온다.
    delete_blog.delete() # 삭제한다
    return redirect('home') # home.html로 이동한다

'''
delete함수는 id값을 받아서 그 객체를 불러온 다음 그 객체를 delete()라는 메소드를 사용해서 삭제합니다.
그리고 namespace가 home인 home.html로 이동합니다. 

### 2. urls.py


''' urls.py

path('blog/delete/<int:blog_id>',blog.views.delete, name = "delete"),

'''

url 연결해줍니다. id를 넘겨줘야하기 때문에 path-converter를 넣어줍니다.
