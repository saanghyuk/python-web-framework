# Crawling

[내 IP알아보기](###내 IP알아보기. )

[Data Type](##Data Type)

[regex](##Regex)

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

- 

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

