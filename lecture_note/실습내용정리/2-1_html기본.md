# HTML에 대해서
"Hyper Text Mark-up Language" 의 약자. 웹 페이지의 모습을 기술하기 위한 규약. 프로그래밍 언어가 아니라 마크업 언어다. 헷갈리지 않도록 하자. 웹사이트에서 흔히 볼 수 있는 htm이나 html 확장자가 바로 이 언어로 작성된 문서이다.  

웹을 구성하는 요소??? URL , HTTP , HTML  

URL : 정보의 장소를 표시하는 방법  
HTTP : 정보를 주고받는 규칙  
HTML : 정보의 내용을 기술하는 언어  
즉 HTML은 정보의 내용을 웹사이트에 표시하는 언어입니다!  

'URL로 표시한 장소로부터 HTTP라는 방법을 사용해서 HTML로 작성된 정보를 가져온다.' >>웹을 한 문장으로 설명!  

<출처 : 나무위키>

## HTML의 기본구성
HTML의 표준적인 양식? 형식 이다.

``` html
HTML의 기본적인 구성이다.

<!DOCTYPE html>        
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>
```

``` html

<!-- 한 줄씩 설명하겠습니다  -->
<!DOCTYPE html> : DOC 어디서 많이 보셨죠? 마이크로소프트
워드의 파일형식 명입니다.  뭐냐 문서형태로 작성하겠다 이말입니다. 
즉 문서형식으로 작성해서 웹사이트로 띄운다.

<head>~~~~</head> : head는 즉 머리 document title, 외부 파일의 참조, 
메타데이터의 설정등이 들어갑니다. 쉽게 말하면 머리속안의 생각입니다.

<body>~~~~</body> : 바디는 말 그대로 보여지는 것입니다. 머리속의 생각을 기반으로
자신의 생각을 직접 보여주는 느낌으로 받아주셨으면 합니다.

```
## 자료 활용방법
1.처음에 코드를 적용시켜서 보여줍니다.  
ex: <a href="https://www.naver.com/">네이버가기</a>  
이렇게 눈에 보여지는 것을 작성한다.  

2.코드 작성 방법을 보여주겠습니다.

```html
<a href="https://www.naver.com/">네이버가기</a>  
```
이런식으로 자료 진행하겠습니다!






## 예시(블로그 포스팅)
멋사 블로그를 만들었다.
거기에 게시물을 올리는데 들어가는 것은?  
중요한 것들 : 제목 , 글 내용 , 사진 >> HTML로 작성하기!  
서브적인 것들 : 글꼴 글자색상 줄 , 라인  >> CSS로 꾸미기  

HTML은 즉 내용 Real내용? 진짜 작성할것들만 적는 겁니다.
<hr>

## 제목태그 : h태그
태그 폼 : <h?> ~~ </h?>  : 0<?<7 의 정수를 넣어보자  
제목을 작성할때 많이 쓰는 태그이다. 밑에는 1~6의 숫자의 예시

<h1>h1: 안녕!</h1>
<h2>h2: 안녕!</h2>
<h3>h3: 안녕!</h3>
<h4>h4: 안녕!</h4>
<h5>h5: 안녕!</h5>
<h6>h6: 안녕!</h6>
이런식으로 제목을 걸어준다!

``` html
<h1>h1: 안녕!</h1>
<h2>h2: 안녕!</h2>
<h3>h3: 안녕!</h3>
<h4>h4: 안녕!</h4>
<h5>h5: 안녕!</h5>
<h6>h6: 안녕!</h6>
```

## 내용태그 : p , ul , ol ,li 
글을 작성할때 문단을 지정해보자
<br>
P : paragraph 단락
<br>
``` html
<p>~~~</p>  : 단락을 지정해주는 것이다.
그 안에 뭐가 들어갈까?  > 목록 및 내용

<ul></ul> : 문단에 순서 없는 목록

<ol></ol> : 문단에 순서 있는 목록

<li></li> : 문단에 들어가는 내용
```

1. ul태그를 걸었을 경우<br>
    내가 좋아하는 것
    <ul> 
        <li>벤치프레스</li>
        <li>데드리프트</li>
        <li>스쿼트</li>
    </ul>

    ``` html
    내가 좋아하는 것
    <ul> 
        <li>벤치프레스</li>
        <li>데드리프트</li>
        <li>스쿼트</li>
    </ul>
    ```

2. ol태그를 걸었을 경우<br>
    내가 좋아하는 순서
    <ol>
        <li>벤치프레스</li>
        <li>데드리프트</li>
        <li>스쿼트</li>
    </ol>

    ``` html
    내가 좋아하는 순서
    <ol>
        li>벤치프레스</li>
        <li>데드리프트</li>
        <li>스쿼트</li>
    </ol>
    ```

3. ul, ol 태그 둘다 쓴 예제
    차이점을 아시겠죠? 두 예제을 합쳐 보겠습니다.
    <hr>
    <p>
        이관형의 삶<br>
        내가 좋아하는 것 
        <ul>  
            <li>벤치프레스</li>
            <li>데드리프트</li>
            <li>스쿼트</li>
        </ul>
        <hr>
        내가 좋아하는 순서
        <ol>
            <li>벤치프레스</li>
            <li>데드리프트</li>
            <li>스쿼트</li>
        </ol>
    </p>

    ``` html
    <p>
        이관형의 삶<br>
        내가 좋아하는 것
        <ul> 
            <li>벤치프레스</li>
            <li>데드리프트</li>
            <li>스쿼트</li>
        </ul>
        <hr> <!-- 구분선 -->
        내가 좋아하는 순서
        <ol>
            <li>벤치프레스</li>
            <li>데드리프트</li>
            <li>스쿼트</li>
        </ol>
    </p>
    ```
    
    
br : Enter 키 줄바꿈  br태그입니다.  
hr : 저기 보시면 줄이 생겼죠? hr 태그입니다.  
참고로 주석이라는 기능이 있습니다.  
주석은 Ctrl+/ 를 눌러주세요!  
```html
<!-- 주석입니다. 이 안에 쓴 내용은 보이지 않습니다! -->
```
HTML,Python,C 각 언어(html은 언어X) 마다 주석 처리 방법이 다릅니다.


### 글 쓰는 공간 : textarea 태그

<textarea name="" id="" cols="30" rows="10">?????</textarea>  
여기는 뭐하는 걸까요? 여러분이 원하는 텍스트를 작성하는 것입니다.  
사이즈를 조절할 수 있는 장점이 있습니다.

```html
<textarea name="" id="" cols="30" rows="10">?????</textarea>  
여러분 고등학교때 행렬 배우셨죠? 행과 열= cols , rows 입니다.
```


<hr>

## 내용에 id , class 걸어주기  // 미완성
그룹화로 간단히 말씀드리겠습니다.  
id : 이관형  
class : 남자  

id는 즉 구체적인 것 입니다.  
class는 포괄적인 것 입니다.

### 쓰임새
 <a href="https://github.com/LikeLion-at-KMU/Django-tutorial/blob/master/lecture_note/%EC%8B%A4%EC%8A%B5%EB%82%B4%EC%9A%A9%EC%A0%95%EB%A6%AC/2-2_CSS%EA%B8%B0%EB%B3%B8.md#%EC%84%A0%ED%83%9D%EC%9E%90%EC%9D%98-%EC%A2%85%EB%A5%98">예시 링크 </a>  
 해당글을 꾸며줄때도 사용하고 해당글을 찾을떄도 사용합니다

### ID : LKH 
<p id="LKH">안녕 나는 이관형이야</p>  

```html
<p id="LKH">안녕 나는 이관형이야</p>  
```

### Class : Human 
<p class="Human">안녕 나는 사람이야</p>  

```html
<p class="Human">안녕 나는 사람이야</p>  
```



## 링크걸기 : a태그
특정글자를 눌렀을때 구글 홈페이지로   
넘어가듯이 링크를 걸어줄수있습니다.


### a태그
a태그의 형식

href: 클릭시 이동 할 링크  
target: 링크를 여는 방법  
_self: 현재 페이지 (기본값) : <a href="http://google.co.kr" target="_self">Google_현재 </a>  
_blank: 새 탭 : <a href="http://google.co.kr" target="_blank">Google_새로운탭</a>  
프레임이름: 직접 프레임이름을 명시해서 사용할 수도 있습니다.  
1. 인터넷 링크
``` html
<a href="">글 내용</a>

""여기에다가 이동하고 싶은것을 쓰세요!
<br>
1.주소  : <a href="https://www.naver.com/">네이버</a>
2.응용 : target <a href="http://google.co.kr" target="_blank">Go Google (new window)</a>
```
   
2. id :  여러분이 걸은 아이디로 가고 싶다!  
제가 아까 이관형을 걸었던 것 기억나시나요?  
거기로 가보겠습니다.  
<a href="#LKH">이관형으로 가기</a>

``` html
<a href="#LKH">이관형으로 가기</a>
```



## 목적에 따라서 묶기 : div , span
- 컨텐츠를 목적에 따라서 묶는 기능입니다.  
    태그를 소개합니다.  
    div : 줄바꿈 기능 O  
    span : 줄바꿈 기능 X

컨텐츠를 묶는다? 무슨 말이냐  
1. 맛집을 소개하는 큰 글
2. 그안에 컨텐츠를 보여주는데?
3. 중식 / 양식이 있다
4. 중식끼리 묶고 양식끼리 묶자!

예시 입니다.  
<div style="background-color: red;">안녕 나는 div</div>

<span style="background-color: salmon;">안녕 나는 span1</span>
<span style="background-color: salmon;">안녕 나는 span2</span>
<span style="background-color: salmon;">안녕 나는 span3</span>
<span style="background-color: salmon;">안녕 나는 span4</span>

```html
<div style="background-color: red;">안녕 나는 div</div>
<span style="background-color: salmon;">안녕 나는 span1</span>
<span style="background-color: salmon;">안녕 나는 span2</span>
<span style="background-color: salmon;">안녕 나는 span3</span>
<span style="background-color: salmon;">안녕 나는 span4</span>
```
근데 style이 뭐지? back...??? 뭐지?? CSS에서 알려줍니다.



## 이미지
블로그에 사진이 빠지면 섭하죠?  
사진을 넣어 봅시다!  
형식 : 

``` html
<img src="" alt="">
```
src=" " : 여기안에 이미지를 넣어줍니다.  
이미지를 넣는 형식은 두가지!
- 이미지 주소 복사 : 크롬에서 이미지 주소복사하고 넣으세요!
- 파일명 작성 : 파일명을 넣을때 >> 폴더/폴더/이미지.jpg  
  
alt="" : alt 속성은 Alternate(대체하다)의 줄임 말입니다.  
이미지가 정상적으로 뜨지 않았을때 대체해서 표시해주는 것!


1. 이미지 주소로 넣기  (구글 크롬에서 이미지 주소복사)  
    ![국민대이미지]("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAATYAAACjCAMAAAA3vsLfAAABvFBMVEX////+zE73lUgGsH2Mx1H8/Pz5+fn29vbs7OzR0tTw8PDLzM3l5ebi4uPX19jz8/N7fH/c3N2+v8CpqqyhoqQAUKeCg4bExcaysrTT1NW6u7ymp6mBgoWwsLKPkJOYmZuG1vgAVqpvcHPJ2euBrNSKi44TZrGduNmUlJcAWaxrlsiuyuSHxUj3kD7O7vyf3vnp7fXB6fvL7fyb3fnw+v5BfbwAX6/1+u+93p2K0rej0nYPoI0ArHbV6sLs9eP+8+qTyVnKomD807b838ysyH3i9P1LhL/D1ulvnswrcrbk8dYjc7e125BqnMtiiMBMjsaMstfJ5LGJyGXK6tyn387n6MfR0cVLwIDn4qkASaXn1KZqx4D/02GB0LPw04ey3rn9zl7dx1Lt05jJzHKy5NSQzIx0wmZCwZKj0Gvb9O1XwJuu1NwTrYwcgLDj0GqWv2zR3pnPzmG1zmTBx58Tg6Gkqm/4rXRqvX+Lwn2xqGt6q4WXxVIAbaVCr3unrHr3nVdTkpqbgofqqlvTtmi8s0zMx36Tuq9/qnD81bpRcab6vZCrkYEroqBgu674p2qUn4nGknWKip5odZnSl26jNCMRAAAS6klEQVR4nO1d+2PTVpa+iXOlq/fTlixbEnaQ45A3cRJIA2UoCYTSDlC2LV3aHaa0AbaPbZeFbqcdZrqzOx2m252d+YfnnnslRw6mpKQljKzvh9iWZdn6ch7fuU+ESpQoUaJEiRIlSpQoUaJEiRIlSpQoUaJEiRIlSpQoUaLEYQILItHt0O1GCUUUN0LPIqKAD/t3vcggluJEplmLYtfx/SDwfceNo5ppRo5iyYf9615MEK+RtGuuXdeIkTMubBCtbru1duR45PB+3YsJQYmbZteTwRsFVbJ9x3HCkP7xbUkVwHeJ3TWbsVJ6ax+iFlIzUyhhRFOCMFC0nEPK6SFCyVOo0YWaeHi/9AWCUHepnRGEdcVTJE0Yeo4m0Td1TD25a7r1oeeMFvS4HVsiIoGvEyM9homFkUiZsnInGqruBwSJFv2Afhi/9MUBViMzVpFghXZKmVj3wBsl+jRUBGpfyIjsvnkZdkjNUY3NSB3hIEd807WQIdks0lMbo3+tiAY2RaPP/Do/K0JKo/8RrNiSgajF+SObVuu1miIgxbbSIC+58Ne3keBBTggDHaghMRITeENTJDhRtGyFZt5aUj+kn324MJy2YyDNscADiQpHIjA6EhPDgxMcRQejUwJUh9ckkFV2nPq0o6UfHzlYTWouxOZEGD4nihmQ58gKPDZ4Qgj9wIdHtSEiA+QvcGvbBEm1pjXkwkUG9swGof6ppq8FHyynzmKYGHtgZcjVgCYUiSpzXtGV2IPPHlTqqaRhjpb8xWE7wILPMqTCTEsCQ8MJS5kWC2Wi27BtqtRMaoWMKakLf9WYUy3UfQEHbX+EeBMiU0dayHOhniRU+Ys2hHuXUYi03LlEoVqtS+BYBKSGcIoO3klCDdXN7shoX9JNNCSBUmNxypc91/V8kLCePbxyki3Dl4nLPiuCVPEgqRp2HWlJd0SUCIlqBHkQlawQhIbm0eLJc8Ez5Se7nKpL4J0Nbo/IdQiIOA+R5mjwJtYigmyWMzEVFxRMuQo5ynBvc36JYX6zlx3G8MSK+AvJNQIIeFSa0P/CCBT3ctKVcUA9UoSgFIDxaMHuffc2jy8tLR/JYwHI4++KARcsJJGphcIzPUBylBRewBlujeCARnTiQFjHVLhS1ZbmALy5tLB8fLO3Cca2AFhezqjb5Kcwh0y1CNIp81aASc0tOm+OqSIbor9gu2Busp8pWISXFo4cOZ7aFXXUFJvHF4C45YXj/YvYIfdcB2xPt5Fqhs/3Lp43fNNCXtrs4zsIwlvaJNlbWl5e2HzCx+YZc0eWOKdKmgSEmIkP3UOWGfycv/qwobe9VN5SCC41FsPjhtObn9/8IeU6z7x1eR6IwyqPhSo1OmhFp1f02gVuglNrDrLs/ksxdjxvvx1Sm2mQyxmkpMhKCJezLeTU1Cd+9B8coltDJMipekFT96/xN9PssJQZpei6iizABYSAoJpbVBlimxq2QaU+28d7S6nBsQiHZXfXbomNNdN+4if/oUHojSk0BNWf1Z1wmhmWwVGxl8+eukL/KcWsFtxIID5THtrTTx6O3iYXI/MIpXI3g0+EyD3wT3wB4Zkqdtgz7HsHiEObUEQsPXbYwarpPftVX1TIUQMpWWus5R2kXbZ3fPnI/N6DloIaUfHGiXgmkW2WNw1L8aPagdqzNx/nTbBlUjxzM2g+8DQayOMkcn2JHHDoVe/IkUzAYSVgRqZ5NCsUrTYNEmJAT4oaKk89dz+YP3KE6RADqQHiRuYbJClYjSU0A+QzoxAk+6cQCr0Fpt+EOqZlB7+g7KOgWawmchrZSGYJaugRDC3bB7rFeZ5Odb3RFyIBKVh0EyMHBQbKeGJ9dkQ6EG14gYc3AlqG9U4jI0BOVKQSS6fG5mFUD7g7QeDG9YPRhmiptcDziqH4EhtE4hHVLFBLCPYT6k0Ia0G3P+JFlfSD0UaTKVMhxHakVK/R70gK1HEqNxXsMW0gepGryQIMyJIO2tIzv3xkuQdjfvv0GzZWasWRvHWQutkLJWLdLpJ14KS3ubSQiV6RD00FyVucgUiui5XdqsCg9iDq9Z8idvdYY69gKVLMLqcp2C1OQd/2kDN4hBzYRXMIdNFLRbSDvPZPd+HDhWVqBvVR3fHqKpFZt5UuDYnck8dWp6dXLqOZlVZnZYY+rLZeTd/qHat2ts5f2J6e7hxbhDM7q1uT2ecEJIepx9uGZj5zs9QLhiDBHhiX3Q1CpwEllizpQxPeheo0JQVNdWbgVe/11up5/sb51dYF/jCVnrmVD42KDlmUQlVwYQqs2EVcFmg2FmTIqDQhDD3zaHWVRqvzHW5I+Gi1dYw/u1BltE12WjP8zKljKW0XEfQq2J5FmHTzkRv/jLfyHGHUPGxz4xJ5XYqkH6Lt/HbqfgJ1Ss7g4qvbjMAhtF1CYGNiarz0i7xaMZpBLJNofPABMvQY+DKkJzgppU2c3EqZQb3XZjrVo3Dia5cvVF9HQ2lbvzhwBUkjZjGGpiptVKdhWtbtRiO0IWCrkjQsJQBtncnto9mrxV8u/rLaocFucXvxaHWrN4y2tdtX4EH1A4Ud0Oqo/dM0TR02giaickPwaq5m8Hu1KG1DxTylbbu6vZi+WtxanLxevUwPv4YuV1c2h9F28QzzUkczVJ4TJNQsRE7ATowUVonqYWDBOAQqP54Q3ChtU61WJx0+Q2lDW61pMDZ0uQUR73Harsyur6WDUlkgIAqKnSKUpWLs98fHEA/aQAygbeh8MxrbhKOt6jHOG9A206pOzdBsMDU9lLa1S7NnaHDTQN+wpjZZwWFchMYjOfJEpc8RDAaUJcCwNl7IpFTZTnNxNvl6Dy2utLa3qHibme6cZ7Rluu0yezh9ZuLqG5Q2C4YMwgFBEb1CdGCRmi73gzQGcUAYbdYQV2ICZHOltcpsilnU1DQzvplVOLa4UuVCTniVW92J2YkPr0FXc///osh6rQjd86qp0oCDuQXI4En/9CbQVh8iry4wuTu52loFuXYMKFrcZhzOrDL3nKp2ZihDvcsrLG+cnpiYeOvawCUUQr/wZ72h5wPNJEAbK69Qg9LWe/vN4V66OLVavX6MsjNz/frq1Pmjrc4Fyt6FlR7CUyvVKiiT3tTq9OtHj25t8Wx7aXZionISpq9Zel1h36AQUoiqVDNlShtSAwNhVpD23n6H0abt9VJhkYG68mIGanuLUJZm78DLy0enJnnOuEKN7Z83KG1y4Hm2zkKBQuQi0YaEQHVY1O69feOJwe1HAVi7WgHaiIZklSuQotBmMdqwpdVjR7NoyutdGWNeesC+hLUTE2BslY13MRJUbAgiC5ZAWxGqK25tOGiETsOJA0bbewen7dT6LDM2Zm05FMXaUtqyufA0cv3LzV+9OSy2/RicANImzuwUmDZCBovrkzfHfv0EvbtfXOGsvVWhtO0VIMXIpFy3AYjF7+fazTEwtwPQRosD8FBgrVIppm7LqgQc1mLXBa6uvT829l59eBvI/sBc9MMdxlrlVjqNjaMoVUJWk/ow44etuXDrg7GxsXcOYG1r67NXP+SmRkFrUrUO849ksUA1adoCQni7uEb99M4Ope3Gm8+eEk7f3iWtsnMH5kk6IVW8CmsB8QvRApK2t2k8rkFjYu/ujTFw02cWIBc/qOziLkZYNYhqeWGAi9PelrbuEq5B2TI8d89R2sZ+/cwJ718/2mVt492BtwrTupv1JUgajM7iOeGtMcbb4lM/OxSTH+dpuzXwXnH6EtKeK9FznJh1XKE7G59w3l5+pguufJWnjVb1THBwzyxOz1XWT4qJnrUmVj5ltI29d/oZrne+uv3SLm079IhFkNBNYDIRtoWi9JPu9spTk5NZljv54Cbn7ea/nV77sZc71uq8NOijYoA8la3AUqBeeRREaSOl6LmhDTnhTuX9sRSfXbpy6tTFH2F1i9t52iqs5U2CNQuwV6wxIOmIIySEsSrLFuVNuPvWWB+fTZw5c3v9yn6tbqYzvUsbtBohmNKRhHYsw7jA4ow4ysa3WVxQQVX1xq65UeX7+cTE7Ozslf3JranW9Fd92r7OzBTzedBFGt/GRlNSG6jzUdwWU7wbNwZ5o8yd2A9vwoVWa1eA/DvLMWKWO4s1mjIdu6vyu4M4hK5lyZTzdpvxdmUf11rcarXuZaz9xyswBhXZ2forxRq7m44UZwMpkdVl97hT+SzH280Jhn3Et8XObkb44324ni6EKo9nhoeVZhHqeI50XgKyJM0KE5XJ0zc2HuTclOYFMLf1x3lbO02Rez1Trd7bSG1tHORy4CaKyOvbgs1LQHqbzYJBmhfAwuA+2Nu7lS/ybsrC28SlQd7WTp1Yv3379vqJU/3jK9WPU1v7z/FHcACrTuiH8J/AHiFFmgWTzblCaQnkwk3e2amcy/H2CXfT9bxlnVqHDAuYWD/FD12+fo/ng51fzH3PazPRECymcQs354rN8OtP6MBsEUV0q5JXISlvs7MnTq9BJbZ2+soZStfEmQ8ffHnu89/8ZmL94hrqTaXl6Ne/HZ97CPmAaLyUghYCu2gz/HLzSREsL4lkeH5y4+s8b5+d4cRNrJ+goIYGrz79Xaf6+/G58W/+6w9/+O93/oclg6//+Ntv5sbnvqWXqAdOf6XsAs4nzWYvC6DfpEB02ZpYdze+/mRvWuAmNzvLn1z9qtX608Nxirm58Yfj3/wC8M3DOfoaAptAjcty0x6XAs5ezubKQ1KwYz/iK1rQ8Dbop2cm9uCr1nTrz0DS+MOz9+cYfeMMc/chsIm+QAtdzlUh58rnVmYgoZu5652djYG88KvPB4ib/d309HTrITW0+2dfuZ8SlmONXtW1bTEAyy3mygz9dUCwF+/OZGS8fZHXbzfzxF39uNqqrs49OvsKfuX7YawhbCkEsbXMCroOSH/VGWWg8fVOZaPyIO+oYzc++/xqamxfvvrVve/+92XKyqPxPDLpkaIOtBV01Rm+xhGEIS7jMzF/5y7NjQ/ymSFlj+LBBsUt9PLZubkB2h493pgeFHWNI7aiVrbAIiJ+9qx3EmqlTx8nbuwcNKjtnD77/SBpc2ezpmK975S6V9gVteiNqThbBMRux/0Fda9VgLgH79/YY2+VjY3Kd/+3l7SH32bXk8xs+4kir982sFqgEfIQF0PnDHNUYO7cJ7vU3Xjw0Xcfr/5pD2vcQTnjerYAarFXC2RrU+qDcduK2Gpu13ayJrS3PvjiHMUXX96rUnT+MsjafWZqeqpgMqKKvTYltIQouyuh8uWd5bAGB+6crGzkRihsfEeF7nSr8+cB2fH9WaZxQ7PdyF+16CuhDq67C4uyJwR8zQGzWXs3JY5mz48+7gBr2zlbo8mUkYasJNGcdq4Nl6276z/3W3mu6K/yTEHreduk2ld0TT5q/Nbdj1566aXv7k1XW63Wauf/H2as0drq0Sv8Mw6sTCzUkn7aZKs8O0O+qkgw4oSvKU4hNSVUb9NKXGvybTkQnpw6tt26Xq22Xv3r7//Ga9C5uYf3H32bKjUriTVY10hvp+tjj8ia4rsr2EPvZs0JzFrNa0BksgMW1IXFyZnL7l/+9j3lixrZfVpZvZxyJquoDm0AYreBnDSY6QGWo6SARdVeGLv7JSDitmPRarYd8Duzmdi7myZghvS5iAQsd7krGjoK2oqcNCNqs3V7RPZLyO/OQeElvmg0XNCunuHFbWo8j5GAGwmt/+WEbTGBw7YqxqYV0wTMdueojcbuHPm9YCisONYE6p5+2+ACxfUFbLF5usQSdYKw5Dfb7bZE/ZIPY212sWWajopEWxqhvWD27DykMBFmxO2GhRo1VWz7iFqTadYMO7FqtGIy213ZoqampOHMbocNU8Js5yHdjArWDP5DSPe5gulDJDGzZfyTJmXQpoyKXdaYEdTYPggERFrYpmemTRym2RCyfa7CAnWLPh27u6qpEV8jRLGRqAd1FEUG0AZsBKbLaDNdVYdeApfFfhzCJ0ZyVzWU28OPhzjql+yRKddB2rBiNiNP0EOTje/AMGLJG809/NCeHSNpecSFvt2G1QK6sSGKgp+km5VgWWo0E0dq8xIKj/COkRQS7E+K+f6kWkxpIUhwwehEtxZRNDPagqTLWjVr0FmQ7U9aK87Qoh+J/G64ohV0Eydosn11VItCa2S0WenGr5KEy91wUW7vZQdUnED8Wjs3hDTNpDkYdmiVey8D6rmdvsV0+68UQZKnzSDlTt855PaVV5R6fk8dTTLSJSzLfeWHQNTCdg22JhWIpgRhoGi5FGmkh2AFcsWttUNtJAr3/UFQ4ia1ORm2URBUyfYdxwlD+se3JTBALBC7azbjkZO3TwXxnIganV3XiJEjBxtEq9vUzCLHG+Hk+UMgluJEtIiPYtfx/SDwfceNo5ppRo5ijUBT5LMDCyLR7dDtRglF1HVD2yLiAbdAKVGiRIkSJUqUKFGiRIkSJUqUKFGiRIkSJUqUKFGiRIkSB8XfAVLLF6hkMY+nAAAAAElFTkSuQmCC") 
    ```html
    <!-- 이미지 주소가 너무 길어서 좀 잘랐습니다;; -->
    <img src="data:image/png;base64,iVBORw0KGgoAAAA" alt="">
    ```
2.파일로 넣었을때
    ```html
    <img src="폴더/폴더/파일명.확장자명" alt="">
    ```  

## 입력 양식 : Form 태그 
웹페이지에서 입력 양식 입니다!  
ex: 로그인 , 회원가입 등 다양한 것들이 있습니다.

<hr>

### form과 같이 사용 되는 속성들
- name : form의 이름
- action : 폼 데이터가 전송되는 백엔드 url
- method : 폼 전송 방식 (GET / POST)  

그냥 이런게 있구나~~~ 라고 우선 알아두세요!


### form의 형식 :
폼의 전송 방식에 따라서 method에 따라서 분류 해봤습니다.

```html
<form action=""></form>
<form action="" method="get"></form>
<form action="" method="post"></form>
```

근데? form 태그는 약간 위에서 말했듯이 단락 같은 느낌입니다.  
form태그는 입력 양식입니다. 근데 무엇을 입력할지 정해줘야겠죠?

### 입력할 공간 : input 태그

회원가입,로그인의 기본 아이디랑 비밀번호겠죠?  
그정보를 받는 다양한 타입이 있습니다.

- text : 일반문자
- password : 비밀번호
- button : 버튼
- submit : 양식 제출용 버튼
- reset : 양식 초기화용 버튼
- radio : 한개만 선택할 수 있는 것
- checkbox : 다수를 선택할 수 있는 것
- file : 파일업로드

<hr>

1. input의 형식 : type="text"

    <form action="">
    <p>아이디</p>
    <input type="text" name="id" value="여기가 value">
    </form>


    ```html
   <form action="">
    <p>아이디</p>
    <input type="text" name="id" value="여기가 value">
    </form>
    ```  
<hr>

2. 비밀번호 :  type="password"
    <form action="">
        <p>비밀번호</p>
    <input type="password" name="password">
    </form>

    ```html
    <form action="">
        <p>비밀번호</p>
    <input type="password" name="password">
    </form>
    ```
<hr>


3. 버튼 :  type="button"
    <form action="">
        <p>버튼</p>
    <input type="button" name="button123" value="버튼이다">
    </form>

    ```html
    <form action="">
        <p>버튼</p>
    <input type="button" name="button123" value="버튼이다">
    </form>
    ```
<hr>

4. 제출 :  type="submit"
    <form action="">
        <p>제출</p>
    <input type="submit" name="submit123" value="제출이다">
    </form>

    ```html
    <form action="">
        <p>제출</p>
    <input type="submit" name="submit123" value="제출이다">
    </form>
    ```
<hr>

5. radio :  type="radio"
    <form action="">
        <p>radio</p>
    <input type="radio" name="gender" value="radio">남자
    <input type="radio" name="gender" value="radio">여자
    </form>

    ```html
   <form action="">
        <p>radio</p>
    <input type="radio" name="gender" value="radio">남자
    <input type="radio" name="gender" value="radio">여자
    </form>
    ```
<hr>

6. checkbox  :  type="checkbox"
    <form action="">
        <p>checkbox</p>
    <input type="checkbox" name="gender1" value="radio">남자
    <input type="checkbox" name="gender1" value="radio">여자
    </form>

    ```html
     <form action="">
        <p>checkbox</p>
    <input type="checkbox" name="gender1" value="radio">남자
    <input type="checkbox" name="gender1" value="radio">여자
    </form>
    ```
<hr>


7. file   :  type="file"
    <form action="">
        <p>file</p>
    <input type="file" name="file12" >
    </form>

    ```html
     <form action="">
        <p>file</p>
    <input type="file" name="file12">
    </form>
    ```
<hr>

