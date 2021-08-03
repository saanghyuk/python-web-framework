# Deploy

### python anywhere

1. Settings.py

   ```python
   DEBUG = False
   
   # python anywhere에 가입한 사용자 아이디
   # 다른 주소로 올리면 막히게 함. 
   # '*'로 해도 되긴 하는데, 이러면 모든 호스트를 다 받음. 
   ALLOWED_HOSTS = [
       'saanghyuk.pythonanywhere.com'
   ]
   
   
   # 우리는 이 static file들을 한 곳으로 다 모아주는 기능(배포서비스)을 활용한 후 
   # 배포 서비스 안에서 경로 지정하고 이용할 것. 
   # 고로, dirs를 주석처리
   STATIC_URL = '/static/'
   # STATICFILES_DIRS = [
   #     os.path.join(BASE_DIR, 'static')
   # ]
   STATIC_ROOT = os.path.join(BASE_DIR, 'static')
   
   ```

   

2. 그 다음 pythonanywhere로

   zip file 업로드

   ![1_3](./materials/1_3.png)

   그 다음 사진에서 바로 보이는, `Open Bash Console Here` 클릭

   bash 콘솔에서

   - `unzip community.zip` 압축 풀기

   - 가상환경 설정(python anywhere에는 기본으로 virtualenv 사용 가능)

     ```python
     # 가상환경 생성
     virtualenv --python=python3.7 community_env
     
     # 가상환경 활성화
     source community_env/bin/activate
     
     # django 설치
     pip install django
     ```

     

   - 프로젝트 내부로 들어가서, 필요한 명령어 실행. 

     ```python
     python manage.py collectstatic
     ```

   - DB Migration

     이때 Zip파일에 migrate(sqlite3 파일)파일까지 넣어 놨으면, makemigrations도 해야 함 

     ```python
     python manage.py makemigrations
     python manage.py migrate
     ```

   - Python Anywhere 설정

     파일에서 설정할 부분은 끝났음. 

     `exit`로 나가면 됨. 

     *web -> Add new app*

     ![1_4](./materials/1_4.png)

     *manual configuration* -> *python3.7*

     ![1_4](./materials/1_5.png)

     소스코드 경로 써주기. 

     아까 bash 콘솔에서 있던, 프로젝트의 경로 써주면 됨. 

     `/home/saanghyuk/community

     ![1_4](./materials/1_6.png)

​			

​		그 다음 WSGI configuration file 클릭

  ​		![1_4](./materials/1_7.png)
  ​		현재는 Hello world보여주게 설정이 되어 있음.  하단 부분 주석처리

  		![1_4](./materials/1_8.png)			하단에 내리다 보면, 장고 설정이 있음. 거기서, 주석 풀고 source code path랑 settings path를 내 파일명으로 변경

![1_4](./materials/1_9.png)

​		아까 만들었던 virtualenv 경로 써주기

​		![1_4](./materials/1_10.png)

​	![1_4](./materials/1_11.png)

​			이렇게만 해놓고, 들어가면, 아래처럼만 나옴. 

​			![1_4](./materials/1_12.png)

​		static을 수집 해놨는데, 그걸 연결 아직 안한거지. 

​		![1_4](./materials/1_13.png)

​		이렇게 한다음에, 상단에서 reload를 하면 돼. 
