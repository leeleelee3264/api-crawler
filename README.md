# musical-twitterbot-without-selenium

<br>

## 프로젝트 계기
1년 전에 [[Selenium을 사용하는 뮤지컬 봇]](https://github.com/leeleelee3264?tab=repositories)을 만들었다. Selenium을 사용하지 않는 프로젝트를 시작하는 계기는 2가지 이다. 

- Selenium 사용시 지나친 리소스 점유율
- 동적 웹페이지 크롤링에서 오는 불안정함


#### Selenium 사용시 지나친 리소스 점유율
2023년 03월에 해당 프로젝트 환경을 `Docker`로 이전하는 테스크를 진행했다. 진행하다 보니 Selenium이 돌아가는 Docker 이미지를 만들어보니 이미지의 사이즈가 1GB를 넘겼다. 또한 Selenium에서 `Google Chrome`을 사용하기 때문에 메모리 점유율이 높았다. 사용하지 않는 노트북을 서버로 쓰고 있는데 RAM이 4GB라서 Selenium의 메모리 점유율이 조금 부담스러웠다. 점유율 자체보다는 Selenium 이미지를 구동하기 위해 필수적으로 `shm_size`를 2GB 까지 할당하는 것이 부담스러웠다. 

<br>

<img alt="스크린샷 2023-03-21 오후 9 05 55" src="https://user-images.githubusercontent.com/35620531/226633018-15d029a3-edba-44b6-82db-4289ac51e4b1.png">

<img alt="스크린샷 2023-03-21 오후 9 05 24" src="https://user-images.githubusercontent.com/35620531/226631474-9345aa30-4139-4d8c-b1ee-2c00a566bf9b.png">


#### 동적 웹페이지 크롤링에서 오는 불안정함
여러 deepth의 페이지들을 왔다 갔다 동적으로 크롤링을 해야 해서 리소스가 뜨는 대기시간을 위해 곳곳에 Sleep을 걸어두는 둥 코드 자체에 불안정한 부분이 더러 있었다. 하지만 알고보니 웹크롤링 말고도 API를 이용해서 정보를 얻어올 수 있어, Selenium 없는 프로젝트를 시작하게 되었다.

<br>

## Project TODO List 
- [ ] Jenkinsf로 CI/CD 구성
- [ ] 1st Implement
- [ ] 2nd Refactoring  
- [ ] Jenkins 설정 문서화
- [ ] 프로젝트 진행, 결과 문서화
