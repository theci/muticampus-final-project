- 🎮 Six-Sigma
# 프로젝트명 : 음식 추천 웹서비스
표정기반 맛집추천 서비스 - The Born

## 💡 서비스 및 프로젝트 소개
1. 사용자 업로드 이미지 수집에 대한 사전 동의.(비동의 시 서비스 이용 불가)
2. 사용자 얼굴 이미지를 업로드 받아 사용자의 현재 감정 파악(기쁨/슬픔/분노/중립)
3. 실시간 날씨 데이터 크롤러를 통한 날씨 데이터 수집(비/눈/이외)
4. 현재 계절 정보 수집(봄/여름/가을/겨울)
5. 감정, 날씨, 계절 데이터를 활용한 메뉴 추천(상황에 따라 메뉴별로 가중치가 다르게 부여됨. 계산 후 상위 5개 메뉴 추천)
6. 제공된 5개의 메뉴 중 사용자가 메뉴를 선택 시 해당 메뉴를 판매 매장 위치 및 매장 정보 제공.
7. 사용자가 선택한 메뉴는 로그데이터로 DB에 축적(추후 추천 알고리즘 성능 향상에 활용 가능) 

## 팀원 소개
- Data Engineering
  - 이원근(DE파트장)
  - 최인태 
  - 박창훈 

- Data Science
  - 박은지(DS파트장)
  - 주경배 
  - 정찬영 

## 폴더
- DL_Model
  - 웹서비스에 사용된 감정파악 딥러닝 모델
- DataSet
  - 각 소스코드 파일에 필요한 데이터셋 / 수집 및 정리된 데이터셋 
- Django/web_study
  - 웹 서비스 구현(**Django 활용**)
  - 웹서비스 제공을 위한 Front-end 및 Back-end 소스코드
  - DataBase(**MYSQL 활용**)
- MachineLearning
  - 데이터 사이언스 팀의 각종 자료 및 소스코드
- WebScraping
  - 해당 프로젝트를 위한 웹 스크래핑 소스코드
  - 더본코리아 매장 데이터/ 브랜드별 메뉴 데이터/ 실시간 날씨 데이터 수집 크롤러 제작(**BeautifulSoup,Selenium 활용**)
- visualization
  - 웹 스크래핑으로 수집한 더본코리아 매장 위치 데이터 시각화(**folium라이브러리 활용**)
 


## 🔧 사용 기술 스택
Python 1.8
scikitLearn
MySQL 8.0
Django
Pandas
Matlib

🤖 프로젝트 아키텍처
system_architecture

system_architecture

💾 ER Diagram
erd


