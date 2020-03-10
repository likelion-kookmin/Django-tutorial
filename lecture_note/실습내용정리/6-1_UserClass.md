# User class 확장하기

여러분들은 지금까지 블로그를 잘 만들었습니다! 글을 쓰기도 하고 수정도 하면서 어느정도 기능을 갖춘 것 같습니다. 그런데 무엇인가 허전하지 않나요??

무엇이 빠졌을까요..?

맞습니다. 대부분의 웹사이트들이 가지고 있는 회원가입과 로그인이 없습니다. 그렇다면 회원이 기능이 없는 블로그는 어딘가 이상해 보입니다.

작성자가 누구인지 알 수 없으니말이죠. 과연 그렇다면 이 회원가입과 로그인, 로그아웃은 도대체 어떻게 구현하는 것일까요?



## 시작하기

먼저 해야할 일은 app을 추가해 주는 것 입니다.
```
python manage.py startapp user
```

그리고는..? 아마 아무것도 떠오르지 않을 것입니다. 하지만 생각을 조금만 해봅시다. 우리가 글을 쓰기 위해서 했던 일이 무엇인지 말이죠!

우선은 먼저 글을 쓰기 위해 글의 구성요소를 짰을것 입니다. 

제목이 필요하고~ 내용도 필요하고~ 또 날짜랑 사진도 넣으면 좋겠다고 생각했죠.

그렇다면 우리 유저를 만들기 위해서는 어떤 구성요소를 넣어야 할까요?

우선 먼저 떠오르는 건 아이디랑 비밀번호, 뭐 성별, 자기소개, 좋아하는 것들, 기타 등등 여러가지 것들이 생각나네요.

그렇다면 이것들을 구현하기 위해서 저희가 건들인 게 무엇이죠?

혹시 기억이 나시나요? 바로 models.py에서 틀을 만드는 일입니다! 혹시 기억이 나지 않는다면 몰래 전에 만들었던 models.py를 훔쳐보고 오세요!



## 모델 생성하기

자 그렇다면 모델을 한번 수정해 볼까요?
```
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    gender = models.CharField(max_length=10, blank=True)
```

#### 엥? 선생님 이게 뭐죠? 가장 중요한 아이디랑 패스워드 어디갔나요?!

이런 생각이 드는 게 당연합니다. blog 모델을 만들 때에도 다 일일이 넣어주었거든요. 하지만 User는 다르답니다.

거의 모든 웹사이트에 유저가 있기 때문에 장고에서 특별히 username(우리가 흔히 아는 id), password, 스탭인지 아닌지 등을 자동으로 제공해 주고 있습니다.

심지어 사용자가 로그인상태인지 아닌지도 알 수 있는 간편한 라이브러리들을 제공해 준답니다.

저희는 그것을 써먹기만 하면 되는 거에요! 그렇담 어떻게 써먹을 수 있을까요?

```
from django.contrib.auth.models import AbstractUser
```

이 첫번째 코드가 바로 해석하면 '우리는 장고에서 만들어 놓은 User모델을 쓰겠다'라고 선언한 거에요.

이후, 

```
class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    gender = models.CharField(max_length=10, blank=True)
```
이런식으로 사용해주면 된답니다. 근데 무엇인가 이상하죠? Blog랑 다르게 User의 괄호안에 무엇이 들어가 있나요?

우리가 방금 사용하겠다고 선언한 AbstractUser가 들어가 있네요! 저희는 그것을 고대로 가져다 사용하겠다는 것입니다.

이게 바로 상속이라는 것입니다. 우리는 장고가 미리 만들어 놓은 User를 그대로 사용하고, 내가 추가적으로 gender과 bio를 만들겠다라는 의미에요.

코드를 만약 설명해 준다면 이런 모양 일 것 입니다.

```
class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    
    ...(기타 요소들)
    
    bio = models.TextField(max_length=500, blank=True)
    gender = models.CharField(max_length=10, blank=True)
```

이제 좀 감이 오시나요? 후후 우리는 벌써 유저를 만들 준비가 끝났습니다. 이제 model에 선언해 준 것처럼 생성해주기만 하면 됩니다!


## 회원가입, 로그인 폼 생성하기

좋습니다 지금까지 모델이 새로 생겼기 떄문에 makemigrations 와 .


