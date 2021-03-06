# Crawling

[내 IP알아보기](###내 IP알아보기. )

[Data Type](##Data Type)

[regex](##Regex)

[BeautifulSoup](##BeautifulSoup)

[고급한정자](#####고급 한정자)

[POST](# POST)

[Error Case](#ERROR CASE)

[동적크롤링](#동적 크롤링)

- #### Basic 

  웹 크롤러(web crawler)는 조직적, 자동화된 방법으로 월드 와이드 웹을 탐색하는 컴퓨터 프로그램이다.

  **Crawling**은 검색엔진에서 쓰는 것. World Wide Web을 쫙다 탐색하면서, 인덱싱하고 검색을 준비해주는것. 

  **Parsing**은, 특정 정보만 가지고 오는 것. 우리가 검색엔진을 만드는게 아니면, 사실 우리가 하는건 다 파싱이야. 

  

  - 미국 사이트 들어간다? 와이파이 공유기를 통해서 지역별 라우터, 타고 라우터 라우터 타고 해저케이블 타고 그 서버 있는 곳으로 간다.  

    네이버에 들어가려고 시도해도, 라우터 타고 타고 타고 해서 네이버까지 가는 것. 이 라우터끼리 서로 막 할당해주고 한다. 

  - **http와 소켓**

    https는 통신 규격. 

    이 규격이 전부이다. 

    ```
    Request Line
    Request-Line = Method SP Request-URI SP HTTP-Version CRLF
    0개 이상의 헤더 빈 라인
    바디
    ```

    메타데이터(우리가 보낸 데이터에 대한 데이터)![1_1](./materials/1_1.png)

    CRLF는 그냥 *Enter*. SP는 *Space Bar*

    - HTTP Methods -> `http.cat/400`이런식으로 검색하면 어떤 에러인지 알 수 있다.

      ```
      GET : 오직 데이터 요청
      HEAD : Header만 가져올때 자주 쓰임. 
      POST : 데이터를 내가 준다. 
      PUT : 수정
      DELETE : 삭제
      OPTIONS 
      ```

    - HTTP Example Login

      ```
      100-199 정보전달용 
      200-299 성공
      300-399 리다이렉트 
      400-499 클라이언트 에러(request가 뭔가 잘못줬다는 거야) 
      500-599 서버 에러(서버에 문제가 있다는 거야)
      ```

      - *GET /money HTTP/1.1* -> `HTTP/1.1 400 Unauthorized`

      - ![1_1](./materials/1_2.png)

        **Set-Cookie?** 한번 아이디 비번 보내서 로그인 했으면, 그 뒤로는 이 쿠키값만 보내면 된다.  임시신분증

        ![1_1](./materials/1_3.png)

        근데, 이 HTTP에서 아이디 비번 누가 가로채면 어떻게? 그거때문에 나온게 HTTPS. 많은 라이브러리들이 기능 지원한다. 

      - web-stoket

        HTTP에서 request-response는 **무조건** 짝을 이뤄서 핑퐁을 하게 된다. 

        허나 web-socket은 자유롭다. 계속 request만, 계속 response만 이렇게 가능하다. 한번 request했더니, 여러번 response오고 이런 것이 가능하다. 

    - 웹앱과 API

      그냥 html을 긁어오는 것이 아니라, API요청을 해서 데이터 자체를 가져와야 한다. 

      ![1_1](./materials/1_4.png)

    - 주의사항(네티켓)

      [대법원 "웹사이트 무단 크롤링은 불법"](http://news.bizwatch.co.kr/article/mobile/2017/09/27/0023)

      [여기어때 vs. 야놀자](http://www.zdnet.co.kr/view/? no=20200211153634)

      공식 페이지 https://www.robotstxt.org/robotstxt.html robots.txt : 크롤링 관련된 규칙 설명

      [robot.txt 설명](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=http-log&logNo=221104827805)

      *User-agent*: * -> 어떠한, user-agent(사용자 정체)에 대해서도 
      *Disallow*: / -> 메인 페이지 포함 모든 페이지 Disallow하겠다. 
      *Allow* : /$  -> 끝이 /로 끝나는 것은 허용하겠다(정규표현식 $).

       사실 robot.txt는 크롤링 봇들 보라고 만든 것. 그래도 사람이 파싱 하면 봐야지. 

      > User-agent : 다음 규칙이 적용되는 로봇의 이름
      > Disallow : 차단할 URL 경로
      > Allow : 차단 된 상위 디렉토리의 하위 디렉토리에있는 URL 경로이며 차단 해제 할 디렉토리

      ```
      # robots.txt for http://www.danawa.com/
      
      User-agent: HMSE_Robot
      Disallow: /
      
      User-agent: bingbot
      Crawl-delay: 3600
      
      User-agent: *
      Disallow: /user_report/
      
      Sitemap: http://www.danawa.com/WWW_main.xml
      ```

      HMSE에 대해서 싹다 불허. 그리고, 나머지 User-agent는 /user_report/ 빼고 싹다 허용. 

      `crawl-delay`: bingbot은 한번 크롤링을 하면, 3600초 이내에는 다시 수집하지 마라. 





- ### 내 IP알아보기. 

  ```
  # Find My IP
  # http://api.ipify.org/
  res = req.get("http://api.ipify.org/")
  print(res.text)
  
  ```

  res.text 했는데, html이 안오네. 

  이유 2가지 가능

  1. 예를 들어 요청하는 사람이, 닌텐도면 html을 못읽으니깐 그것에 맞게 주는 거야. 

     실제로, 서버는 요청한 것에 따라서 다르게 준다. 브라우져는 http request를 보낼때, 정보가 여러가지가 있음. 그런데, 이렇게 요청할때는, 아무 정보도 없는 그냥 브라우져 인것. 

  2. 실제로, 서버에서 저런 html자체를 브라우져에 보낸 적이 없는 것. 서버에서는, 49.245.49.178 그냥 이것만 보냈는데, 브라우져에서 그거만 보여주기 좀 그래서 채운거야. 그게 확인이 가능한게, 페이지 소스 보기해 보면. 아래 처럼만 나온다. 페이지 소스 보기가 실제 응답값과 유사하게 보여준다. 그렇다고 완전 100% 동일한 것은 아님. 

     ![1_5](./materials/1_5.png)

     

- ## Data Type

  - #### XML

    이 문서에는 note라는 노드 1개 밖에 없음. note 노드 안에, to/from/heading/body가 있음.  **? metadata ?** 부분은 메타데이터

    ```XML
    <?xml version="1.0" encoding="UTF-8" ?>
    <note>
      <to>Tove</to>
      <from>Jani</from>
      <heading>Reminder</heading>
      <body>Don't forget me this weekend!</body>
    </note>
    ```

    

##Regex

- ```python
url = "https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"
  res = req.get(url)
body = res.text
  
  r = re.compile(r"h_lst.*?blind\">(.*?)</span>.*?value\">(.*?)</", re.DOTALL)
  captures = r.findall(body)
  

  ```

  

- ![1_5](./materials/1_6.png)

  ​	

  - ```
    # * -> * 바로 앞 글자가 0개 이상일 수 있다. 
    # 그런데, \n 를 포함하지 않는다. \n가 나오면 끝나버린다. 
    print(re.match(r'hi1*', s))
    ```
    
    `r = re.compile(r"미국 USD.*value\">(.*)</", re.DOTALL)` 
    
    **엔터도 포함해서 준비하라는 것.** 
    
    그리고, 그냥 .*하면 끝까지 다 가져와 버린다. 가장 좁은 범위를 가져오라고 하고 싶으면, 
    
    ```
    .*?
    ```
    
    
    
  -  `+` -> 1개 이상 
  
  - ? -> 없을수도 있다.
  
    진짜 물음표쓰고 싶으면 \, 
  
    ```python
    print(re.match(r'colou?r', s))
    
    print(re.match(r'how are you\?', s))
    ```
  
  - [] -> 이 중 아무거나. 괄호 내부는 모두 가능성 있는 글자가되는 것.
  
    ```python
    print(re.match(r'이 영화는 [ABCDE]등급 입니다\.', s))
    ```
  
  - () -> 캡쳐
  
    ```python
    s = "이 영화는 F등급 입니다."
    print(re.findall(r'이 영화는 (.)등급 입니다\.', s))
    print(re.findall(r'이 (.*)는 (.)등급 입니다\.', s))
    ```
  
    **['F']**





## 쿼리스트링 query string

- **웹 요청시에 보내는 추가 인자 값**

  `https://finance.naver.com/marketindex/exchangeDetail.nhn?marketindexCd=FX_USDKRW`

  `?` 뒤가 쿼리 스트링

  *url?querystring1&querystring2*

  **key=value**

  **?adults=2&children=3**

  ```
  - arr[] = 1
    arr[] = 2
    arr[] = 3
    arr[1, 2, 3]
  ```

- 만약 값으로 ***?***나 ***&***이 쓰인다면? 또한 한글은 querystring으로 넘어갈 수가 없다. 

  urlencode로 보내주게 된다. request는 url encode를 알아서 해준다. 

  ![1_5](./materials/1_7.png)

  ```python
  res = req.get(
      "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EA%B0%90%EC%9E%90")
  print(res.text)
  ```

  알아서 보내주고 받는다. 

  **requests말고 다른 라이브러리 쓰면, 우리가 urlencode를 해줘야 한다.**









##BeautifulSoup 

- **requests : http통신을 편하게** 

  **beautifulsoup : html통신을 편하게**. html을 알아서 가져오고 인식해준다. 

  *bs4는 http 통신을 해주는 애가 아니다. requests로 http 통신을 해서 가져온 html을 사용하기 편하게 해주는 친구이다.* 

- 특징

  - parents, children, contents, descendants, sibling : html구조의 파싱을 편하게 해준다. tree구조. 
  - String, strings, stripped_strings, get_text() : 태그 내부를 알아서 편하게 가져와줌. 
  - prettify : *tab, enter*
  - html attribute : 

- 네이버 금융 파싱하는데, iframe이 들어있다. 다른 html문서를 감쪽같이 가져온다. 

  ![1_5](./materials/1_8.png)

  - 그럼 소스를 바꿔야 한다. iframe으로

  ```python
  
  for td in tds:
      if len(td.find_all("a")) == 0:
          continue
      print(td.get_text(strip=True))
      print(td.string)
      for s in td.strings:
        
          print(s)
      for s in td.stripped_strings:
          print(s)
  
  ```

  - `strings`, `stripped_strings`

    `<div> 총 가격은 <b>19,000</b>원 입니다.`

    b내부를 잘라내고 싶을 수 있잖아. 그런 경우에 쓰는게, **strings**, **stripeed_strings**

    ```python
    from bs4 import BeautifulSoup as bs
    import requests as req
    
    url = "https://finance.naver.com//marketindex/exchangeList.nhn"
    res = req.get(url)
    
    soup = bs(res.text, "html.parser")
    # print(soup.title)
    # print(soup.title.string)
    
    tds = soup.find_all("td")
    
    
    names = []
    for td in tds:
        if len(td.find_all("a")) == 0:
            continue
        # print(td.get_text(strip=True))
        names.append(td.get_text(strip=True))
    
    prices = []
    for td in tds:
        if "class" in td.attrs:
            if "sale" in td.attrs["class"]:
                prices.append(td.get_text(strip=True))
    
    print(names)
    print(prices)
    
    ```

    



- #### CSS Selector

  - ##### CSS

    - 크롬 개발자 도구. 

      - `document.querySelector("div#container")` : 처음 만나는 놈만 리턴
      -  `document.querySelectorAll("div#container")` : 모두 리턴

    - html attribute로 select

      [all atributes references](https://www.w3schools.com/tags/ref_attributes.asp)

      attribute = html의 속성. 

      `<img height="90" width="130">` 이런 height/width 이런 것들도 모두 활용이 가능하다. 

    - *=: 포함

      ^=: ~으로 시작

      $=: ~으로 끝남

      ![1_5](./materials/1_9.png)

    - #####고급 한정자

      ![1_5](./materials/1_10.png)

      ```python
      select("*")
      
      select("div, p") : p와 div를 둘다 가져온다. 서로 다른 별개의 셀렉터를 만든 것이라고 보면 된다. 하나의 배열로 같이 온다. 
      
      select("div > p") : div의 바로 자식 p. 바로 자식만 된다. 손자가 안돼. 
        
      select("div p") : 이건 자식이든 자식의 자식이든, div 안에 있는 게 다된다. 
        
      select("div ~ p") : 바로 형제. 동급에서 바로 앞을 의미. 
      
      select("div + p") : 이것도 바로 형제 의미. 동급에서 바로 뒤
      ```
      
      `document.querySelectAll("td.sale + td + td")` 이렇게 계속 가능 하다. 
      
    - 진짜 우아하게. **가장 중요하다 이게**

      ![1_5](./materials/1_11.png)

        - `:enabled` : html이 비활성화되면 회색으로 보이거나, input인데 못치는 상태거나 그런 상태들을 의미한다. 

          `document.querySelector("input:disabled")`

        - `:checked` : input type="checkbox" 같은 것에서 체크된 상태 의미한다. 

        - `:disabled`

        - `:empty` : string같은거로 값 가져오는데, 값이 비어있는지를 의미.

          `<p></p>` 이렇게 빈거 가져오라는 것. 빈 테그를 가져오라는 것. Input 같은거는 대부분 값이 없지. 

      - `:first-child` / `:last-child` : 자식 중에 첫번째 혹은 마지막 자식. 

      - `first-of-type`/`last-of-type` : 나오는 해당 테그나 뭐 그런것 중에서 제일 첫번째나 마지막을 의미. 

        부모 기준에서 내가 처음이면 다 나온다. 

      - `:hover` : 마우스 올라가있으면, hover상태

      - `:not`: 위 모든 것에 융합될 수 있다. 

        <pre>
        div.sale:checked
        위는 체크가 된것을 찾는 것인데
        여기서 체크가 안된것을 보고 싶다면?

        div.sale:not(:checked)

        **:not(:selector)** 이 형식을 기억하자 자주쓴다.  

        **div:not(:first-child)** : 이런식으로 한다. 첫번째 자식 빼고. 

      - `:nth-child` : n번째 자식, 버튼 5개 있으면, 그 중에 3번째 가져오고 싶을 때. 

        `div:nth-child(3)` (css는 인덱싱이 또 1번부터 시작한다)

        **지금 여기서 중요한게, div:nth-child같은애들 다 보면, div중에서 3번째를 찾는 것. 이게 div 자식 중에서 3번째가 아니야**

      - `:nth-of-type` : 

        `div:nth-of-type(3)` : 3번째 div를 가져온다. 

      - ```python
        
        # enabled
        arr = soup.select("input:enabled")
        
        # checked
        arr = soup.select("input:checked")
        
        # disabled
        arr = soup.select("input:disabled")
        
        # empty
        # label 옆, input:empty
        arr = soup.select("label+input:empty")
        
        # first_child
        arr = soup.select("b:first-child")
        
        # last_child
        arr = soup.select("table tbody tr:last-child")
        
        # first-of-type
        # 자신이 부모의 첫번째 인 놈들이 다 나온다.
        arr = soup.select("table tbody td:first-of-type")
        
        # last-of-type
        # 자신이 부모의 첫번째 인 놈들이 다 나온다.
        arr = soup.select("table tbody td:last-of-type")
        
        # not
        arr = soup.select("b:not(:first-of-type)")
        
        # nth-child
        arr = soup.select("table tobody tr:nth-child(2)")
        
        # nth-of-type
        arr = soup.select("table tobody tr:nth-of-type(2)")
        
        ```

        

    - **:first-child 와 :first-of-type 의 차이점**

      HTML

      ```html
      <div>
          <div>text1</div>
          <p>text2</p>
          <p>text3</p>
      </div>
      ```

      위와 같은 마크업이 있다고 가정하고 text2의 글자 색상을 빨간색으로 지정하려고 합니다.

      CSS

      ```css
      /* Case1 */ 
      div p:first-child { color: #ff0000; }
      
      /* Case2 */ 
      div p:first-of-type { color: #ff0000; }
      ```

      위와 같이 CSS를 정의한다고 했을 경우에 결과물은 매우 다르게 나타납니다.

      Case1 의 경우는 text2 글자 색상에 변화가 없고, Case2 인 경우에만 원하는 결과물을 얻을 수 있습니다.

      그 이유는 `:first-child` 의 경우 **div 하위 엘리멘트중에 p 엘리먼트가 가장 첫번째에 위치해야  :first-child 가상클래스를 통해 선택**할 수 있기 때문입니다.

      위 마크업은 div 하위 요소중에 가장 첫번째는 div 엘리먼트이기 때문에 선택할 수 없었던 것입니다. 

      

      반면에, `:firt-of-type` 은 실제 p 엘리먼트만을 기준으로 카운트를 하기 때문에 선택할 수 있는 것입니다.

      다시 말해 가상클래스 명칭에서도 알 수 있듯이 **타입만을 체크**하는 것입니다.(예제는 p타입 중에 첫번째를 선택한다는 의미)

      

      이 점이 두 가상클래스 선택자의 중요한 차이점입니다.

      

- XPATH

  






# POST

- #### Send Test request to [webhook.site](webhook.site). 

  ```python
  # webhook.site
  import requests as req
  
  
  res = req.get(
      "https://webhook.site/abcc1b45-1ef5-494d-a032-9b7590452971?name=hi", headers={
          "User-Agent": "sanghyuk/B1"
      })
  print(res.text)
  
  ```

  ```python
  # webhook.site
  import requests as req
  
  url = "https://webhook.site/abcc1b45-1ef5-494d-a032-9b7590452971"
  res = req.post(url, data={"type": "SS"}
                 )
  print(res)
  
  ```

  

- #### 이미지를 HTTP로 보내는 방법?

  - 이미지란 실제로 문자열이다. 

    



# ERROR CASE

1. 브라우저로 접속할 때는 되는데 requests 로는 접속이 안되는 경우. 

   - header를 확인한다. 왼쪽은 브라우져에서 보내는 header, 오른쪽은 그냥 우리가 Request. 

     ![1_12](./materials/1_12.png)

   - 주요 header
     - **User-Agent** : 사용자 식별. 원래 용도는 device같은 것 따지기 위함. 
     -  Cookie : 여기에 user의 상태가 담기기 때문에, 서버에서 확인하는 경우가 있다. 
     - Accept : aceept에 따라서 데이터 다르게 주는 경우 많다. 데이터 타입 등을 여기에 명시하는 경우가 있다.  
     - Referer : 어디서 온 요청인지에 대한 부분. 어디서 부터 타고 왔는지. 

   - 그 외의 경우
     - SPA : Single Page App들.  
     - CSRF : 보안
     - Captcha : 인증번호 입력 등. 
     - IP Ban : ban까지 들어오면, 크롤링 하면 문제 될 수 있다. 

2. 쿠키는 어디서 보는것?

   - 웹서버가 처음에 딱 유저를 보고, 쿠키가 없으면 쿠키를 준다. 유저한테 주면서, *set-cookie:650* . 이후부터, 유저가 다음 요청 보낼때부터는 cookie를 같이 보낸다. 서버입장에서는 session. 유저입장에서는 cookie. 완전히 같은건 아니긴 함. 어쨋든 유저입장에서는 내 식별자다. 

     ![1_12](./materials/1_13.png)

   - 브라우저는 쿠키를 어떻게 관리할까요?

     - Name

     - Value

     - Domain : 처음에 쿠키 받을때, 이 도메인일 경우에 이 쿠키 적용하라는 정보가 들어가있다, 줄때도 거기로 다시 주는 것. 네이버에서 받은 쿠키를 페이스북에 주면 안되잖아. 

     - Path : domain+**/mypage** 경로까지 주지. 이렇게 경로

     - Expires : 서버가 쿠키를 덮어씌우는 건 되는데 지우는건 안됨. 그래서 expires들이 보통 들어 있음. 

     - **서버에서 실제 쿠키를 주는 모습.**

       ![1_12](./materials/1_14.png)

     - **서버에게 쿠키를 주는 모습**

       ![1_12](./materials/1_15.png)

     - 로그인 한 다음에, **Network -> All 혹은 Doc -> 메인 페이지로 보낸 리퀘스트 확인하면 request헤더에 쿠키값 같이 있다.**  그것을 그대로 사용하면 된다. 

3. 매 요청때마다 값이 자꾸 바뀌어서 코드를 짤 수가 없어요

   - 아래 사진 보면, id&password부분 보자. **&csrf** 가 있음. **csrf가 바뀐다.** 그러면, 우리가 request할때, 뭘 보내야돼? 

   - ![1_12](./materials/1_16.png)

   - **CSRF는 직접 파싱해서 써야 한다.**

     - CSRF란? Cross-site Request Forgery

     - CSRF 란? 어떤 사이트를 함부로 실행시키는 것. 

       *예 : 이메일을 열었는데 갑자기 결제가 되어버린다.*

       *원인 : 이메일 본문에 결제하는 링크가 iframe, img 등으로 연결되어 있는 것*

       **방지 : CSRF 토큰을 넣는다, referer 를 체크한다 등**

     - CSRF 토큰?

       - cookie
       - header
       - STP (Synchronizer Token Pattern)

     - CSRF는 결국은 보내는 쪽이랑 받는 쪽에서 랜덤한 값을 가지고 확인하는 것. 리퀘스트 보낼때, 랜덤으로 생성된 그 값을 같이 보내라는 것. 그럼 서버에서 진짜인지 확인한다. 
     - 우리가 해볼수 있는 방법은, 해당 페이지에 먼저 들어가서 csrf토큰을 먼저 받아와서 헤더나 쿠키 등 알맞게 보낸다. 

     

4. 소스보기를 클릭 했는데 원하는 값이 없어요. 

   - 서버가 데이터를 즉각 주지 않는 상황

     즉, HTML (빈껍데기) 만 주고 실제 내용물은 따로 패키징해서 주는 형태, 페이지 바뀔 때 새로고침 안되고 무한스크롤 되는 형태 등이 이런 구조(Reajct, View 등 SPA Framework들). 

   - 크롬 개발자 도구를 통해 추가 패키지 요청(XHR) 을 분석한다!

     네이버 같은데 들어가도, 우리가 모르는 사이에 2번째 3번째 요청이 일어나고 있는 것. GFA광고 텝 등. 

     **이 XHR에서 추가 요청 찾아서, 우리가 요청을 그 주소로 보내면 된다.** 

     ![1_12](./materials/1_17.png)

   - 다 해도 안되면? **정적 크롤링 (requests) 의 한계일 수 있습니다.**

   - Captcha

   - Client-Side Javascript Dependecy



# 동적 크롤링

- 브라우져 

  - 랜더링 : html문서를 화면에 그려주는 것. 

  - 브라우져의 역할 예시 

      1. 네이버 접속 (HTTP 통신, 렌더링)
      2. 블로그 버튼 클릭 (인터렉션, HTTP 통신) 
      3. 블로그 페이지 접속 (HTTP 통신, 렌더링) 
      4. 블로그 검색 (인터렉션, HTTP 통신)
      5. 블로그 글 검색 (HTTP 통신, 렌더링)
      1. 블로그 글쓰기 클릭
      2. 글 입력(제목, 본문, 태그, 사진 등) 3. 작성완료 버튼
  
- #### Seleium

  - 브라우저 테스팅 툴, 브라우저 원격 조종 툴. 
  - 셀레니움은 디버깅 모드의 브라우저와 TCP통신. 리모콘. 

  - 동적 웹사이트의 특징 

    - 사이트가 깜빡이지 않는다.

    - 화면이 한번에 다 로딩되지 않는다. (DOM 생성)

    - javascript 가 필수이다. 정적 웹사이트는 다 준비된 html/css를 로딩. 동적 웹사이트는 js를 통해서 서버랑 통신하면서 html을 만들어간다. 동적으로 html/css를 생성해간다. 

      

  - 설치 

    - 셀리니움 필요한 것.

      - *chrome*

      - *chrome driver* : 셀레늄은 크롬 뿐만 아니라, safari/firefox/opera 등도 조절이 가능하다. chrome만을 위해 만들어 진 것이 아니다. 셀레늄과 해당 브라우져가 통신하기 위해서 해당 브라우져의 드라이버가 필요하다. 

        버전도 다양하다. 내가 쓰는 크롬의 버전과 일치시켜야 한다. 

        [chrome driver 93](https://chromedriver.storage.googleapis.com/index.html?path=93.0.4577.15/)

      - *selenium python library*

      - 테스트 코드 

        

    - 도커

      - 도커란 ? 가상의 컴퓨터를 실험실처럼 만들어 사용하는 것

        [docker](https://www.docker.com/get-started)

      - [docker hub](https://hub.docker.com/)에 들어가서 selenium을 검색한다. 

        `selenium/standalone-chrome` 이 이미지 이름을 복사. 

      - terminal에서 4444:4444는 셀레늄이 쓰는 포트

        `docker run -p 4444:4444 selenium/standalone-chrome`

      - 실행 후 테스트

        ```python
        # docker
        from selenium import webdriver
        from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
        browser = webdriver.Remote(
            "http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME)
        browser.get("http://naver.com")
        print(browser.title)
        browser.close()
        ```

    - 로컬

      - pip3 install selenium

      - test code

        ```python
        
        from selenium import webdriver
        import time
        browser = webdriver.Chrome("../../chromedriver")
        browser.get("http://naver.com")
        time.sleep(10)
        browser.close()
        
        ```

        

