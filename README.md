
# T2taNic
```angular2html
Predictive Model Serving Inspired by 
Titanic ML Model + A/B Test Pipeline + Fun Service
```

![T2taNic](https://images.chosun.com/resizer/gE-go0I5-2QsuwlgUUavoU3SfiI=/616x0/smart/cloudfront-ap-northeast-1.images.arcpublishing.com/chosun/TPUMVAPDGDTDD2ST4RDJB56LVU.jpg)

# DEV
### bigbang
- pipenv --python 3.9.17 

### step #1
- pipenv shell


### install pip
- pipenv install streamlit

### run
- streamlit run app.py

---
# DEPLOY
- fly deploy

----
# TIP
### use docker
``` bash
$ docker build -t t2tanic:0.2.0 .
$ docker images t2tanic          
REPOSITORY   TAG       IMAGE ID       CREATED              SIZE
t2tanic      0.2.0     299578446bd6   About a minute ago   1.04GB

$ docker run --name t2tanic -d -p 8888:8080 t2tanic:0.2.2
$ docker ps
CONTAINER ID   IMAGE           COMMAND                  CREATED          STATUS          PORTS                    NAMES
92d1841c87e6   t2tanic:0.2.2   "streamlit run app.p…"   3 seconds ago    Up 2 seconds    0.0.0.0:8888->8080/tcp   t2tanic
```

### use jupyter
```
python -m jupyter notebook --no-browser --notebook-dir=/Users/m2/code/t2tanic --NotebookApp.token=abcd --NotebookApp.port=7942
```

----
# Referenced
- 캐글 타이타닉 생존자 분석하기, https://speedanddirection.tistory.com/66
