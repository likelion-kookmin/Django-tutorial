# CSS 기본
[CSS](https://ko.wikipedia.org/wiki/CSS) 란 Cascading Style Sheets 의 약자로 [HTML](https://ko.wikipedia.org/wiki/HTML)이 문서의 틀을 잡아줬다면 CSS는 거기에 스타일을 입혀주는 역할을 한다. (밥과 반찬, 조미료와 같은 관계를 연상해도 된다)

아래의 실습들을 따라해보고 결과를 확인해보고 싶다면 아래의 과정을 따라하거나 그 아래의 방법을 이용하면 좋을 것 같다.

방법1(권장):
1. vscode에서 *파일 -> 새파일* 을 누르고 hello_css.html 파일을 만들어준다.
1. 같은 방법으로 hello_css.css 파일도 만들어준다.
2. 코드들을 적고 저장한다.
3. 파일을 Chrome으로 열어서 확인한다.

방법2:  
1. [실습폴더주소](https://github.com/LikeLion-at-KMU/Django-tutorial/tree/master/2_HTML%26CSS/CSS%EC%8B%A4%EC%8A%B5)에 들어가 다운을 받는다.
2. 크롬에서 열어서 확인해본다.

## 미리 알고 있어야 하는 내용
+ 기본적인 HTML 태그들
+ HTML 태그의 class, id 같은 속성들

## 기본 문법
CSS의 C, 즉 Cascading을 구글 번역기에 돌려보면 계단식이라는 결과가 나오는데 아마도 CSS 문법이 계단을 연상시키기 때문이 아닐까 생각된다.

``` css
/* 기본 폼 */
선택자 (적용하고 싶은 곳을 가르킨다.) {
    속성이름: 속성값; /* ';' 한 줄 마다 세미콜론을 꼭 찍어줘야 한다! */
}

/* 예시 */
div { 
    width: 100px; /* 해당하는 태그의 너비를 100픽셀로 해라. */
    color : #FFFFFF; /* 해당하는 태그의 글자색을 검정으로 해라. */ 
    background-color: red; /* 해당하는 태그의 배경색을 빨간색으로 하라. */
}
```

### 주석 남기기   /* 메시지 */
위의 예시를 보면 `/* 안에 글씨가 있다. */` 같은 것을 볼 수 있는데 여러 사람이 함께 작업을 하다보면 어디서 쓰는 스타일인지 헷갈릴 때가 있다. 그럴 때를 위해서 `/* */` 사이에 설명을 적어넣으면 *주석* 으로 인식하여 해당 내용을 무시하게 된다.

## HTML에 적용방법
1. HTML 문서에서 바로 사용하기  
   간단하게 바로 사용할 수 있는 방법으로 `<head>` 태그 내부의 `<style>` 태그 사이에 적어준다.
    ``` html
    <html>
    <head> 
        <title>HTML 문서에 CSS 넣기</title>
        
        <style>
            /* 이곳에 넣어주면 된다!! */
            /* 위의 예시를 복사해서 붙여넣었다. */
            div { 
                width: 100px; /* 해당하는 태그의 너비를 100픽셀로 해라. */
                color : #FFFFFF; /* 해당하는 태그의 글자색을 검정으로 해라. */ 
                background-color: red; /* 해당하는 태그의 배경색을 빨간색으로 하라. */
            }
        </style>

    </head>
    <body>
        본문내용
        <p>매우 간단하다. 위의 예시를 복사하여 
        <head>태그 안의 style 태그 사이에 넣어주면 끝!</p>
        
        <div>모든 div 태그들이 선택되었으니 여기에도 스타일이 적용된다.</div>
    </body>
    </html>
    ```
2. HTML 태그에 바로 적용하기  
   만약 여러 곳에서 사용할 스타일(ex. 박스모양, 글씨체 등)이 아니라 딱 한 군데에서만 쓰일 스타일이라면 HTML 태그 하나에 바로 넣어줄 수 있다.

   이때는 HTML 선택자가 필요없게 된다.
    ``` html
    <div style="width: 100px;
                color : #FFFFFF;
                background-color: red;">빨간바탕에 흰색글씨!</div>
    ```
3. CSS 파일로 따로 저장하기
   mycss.css 파일을 만들고 그 안에 CSS 문법에 맞춰 속성을 지정해준다. 이번에는 파란색 배경을 주어봤다.

   `./hello_css.css`
   ``` css
    div { 
        width: 100px; /* 해당하는 태그의 너비를 100픽셀로 해라. */
        color : #FFFFFF; /* 해당하는 태그의 글자색을 검정으로 해라. */ 
        background-color: blue; /* 해당하는 태그의 배경색을 파란색으로 하라. */
    }
   ```

   `./hello_css.html`
   ``` html
    <html>
    <head> 
        <title>HTML 문서에 CSS 넣기</title>
        <!-- ./hello_css.css 뜻 : './' 현재폴더 안의 'hello_css.css'라는 뜻이다. -->
        <link href="./hello_css.css" rel="stylesheet">

    </head>
    <body>
        <div>이제 이곳이 파란색으로 보인다.</div>
    </body>
    </html>
   ```

## 선택자의 종류
1. HTML tag selector - 태그이름   
    태그이름 : h1, h2 ~ h6, p, span, img, input 등 HTML 태그들 전부에 스타일을 주고 싶을 때 사용
    ``` css
    h1 {
        text-align: center; /* left center right 정렬*/
    }
    ```
2. ID selector - #아이디
   `<div id="human"></div>` human 아이디를 가진 태그에만 스타일을 주고 싶을 때 사용

    ``` css
    #human {
        font-family: Georgia, "Times New Roman", serif; /* 폰트 바꾸기 */
        font-size: 5rem; /* 폰트 크기 1rem은 기본 글자 크기 */
    }
    ```
3. Class selector - .클래스이름  
    `<div class="image-wrapper"></div>` 와 같은 클래스들 전부에 스타일을 주고 싶을 때 사용  

    ``` css
    .image-wrapper {
        width: 500px;
        height: 300px;
    }
    ```


## 선택자 응용
+ div 안의 .black 선택 (띄어쓰기로 분리)
    ``` css
    div .black {
        width:100%;
        background-color: black;
        color: white;
    }
    ```
+ link 클래스를 가진 a 태그 선택 (붙여서 사용)
    ``` css
    a.link {
        color: red;
        font-size: 3rem;
    }
    ```
+ div랑, h1이랑, span이랑 p 태그 전부 선택 (쉼표로 분리)
    ``` css
    div.cyan,
    h1,
    span,
    p {
        background-color: blueviolet;
        border-radius: 10px; /* 해당 태그의 모서리 부분을 둥글게 만든다. */
    }
    ```
+ 마우스를 올렸을 때 모양이나 색을 바꾸고 싶을 때
    ``` css
    div:hover {
        color: brown;
        background-color: aqua;
    }
    ```

## 기본적인 속성들
TODO  
위에서 사용한 내용들 정리.

TODO
CSS로 애니메이션도 만들 수 있다.  
관련 예시 추가

## 그밖의 다양한 속성들
CSS는 정말 많은 속성들이 존재하고, 어떻게 이용하느냐에 따라 천차만별이다. 그렇기 때문에 모든 것을 한번에 다 외우는 것은 거의 불가능하고, 그때그때 필요한 내용들을 공부하는 것이 가장 적합한 공부법일 것이다. 아래 몇가지 상황 예시를 참고해보자.

#### 아래의의 두 가지 예시 상황의 예제들도 [여기](https://github.com/LikeLion-at-KMU/Django-tutorial/tree/master/2_HTML%26CSS/CSS%EC%8B%A4%EC%8A%B5)에 코드로 정리를 해놓았으니 먼저 직접 해보고, 확인, 참고용으로 사용하면 좋을 것 같습니다.

### 프로필 카드를 만들어야 할 때
일단 정직하게 인터넷에 검색해보면 `"CSS 카드 디자인"`을 검색해보면 W3School이라는 사이트나 Stackoverflow 라는 사이트가 반겨줄 가능성이 높다. W3School 같은 경우에는 바로바로 테스트도 해볼 수 있도록 준비도 되어 있으니 가서 이것저것 바꿔보거나 예시들을 사용해보면 CSS를 공부하는데 많은 도움이 될 것이다. [W3School 카드 디자인 예시](https://www.w3schools.com/howto/howto_css_cards.asp) 한글로 되어 있는 블로그들도 많이 있으니 잘 찾아보면 이쁜 카드를 건져낼 수도 있다. 

### 인터넷에서 이쁜 폰트를 찾아서 쓰고 싶을 때
[눈누(noonnu)](https://noonnu.cc/)(국민대 멋사 작품..ㅎ) 홈페이지를 들어가 보면 다양한 한글 폰트들이 많이 있는데 어떻게 사용을 할까? 구글에 `"CSS 웹폰트"` 를 검색해서 확인해보면 [생활코딩 웹폰트](https://www.opentutorials.org/course/2418/13372) 같은 주옥같은 글들을 찾아볼 수 있다.


## 참고하면 좋은 사이트들
[W3School (CSS교과서)](https://www.w3schools.com/css/)  
[ofcourse CSS 입문](https://ofcourse.kr/css-course/CSS-%EC%9E%85%EB%AC%B8)  
[생활코딩 CSS 수업](https://www.opentutorials.org/course/2418)
