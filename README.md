# FastCampus Data Engineering Extension SCHOOL 2 
### ( Project Team2 )

# 가상화폐 가격정보 수집, 분석, 예측, 시각화
- 가상화폐 가격정보를 수집
- 수집데이터를 전처리 하여 추가 지표 생성
- 전처리 데이터를 이용 분석하여 가격을 예측
- 예측 값이 특정 기준에 부합하며 slack 를 통해 alert 해줌
- 시계열적으로 시각화 해서 보여주고

## Schema

- 빗썸

![빗썸](https://github.com/zeuslabs/dees2projectteam2/blob/master/img/2.JPG)

- 코인원

![코인원](https://github.com/zeuslabs/dees2projectteam2/blob/master/img/3.JPG)

- 코빗

![코빗](https://github.com/zeuslabs/dees2projectteam2/blob/master/img/4.JPG)

## Repository

![repository](https://github.com/zeuslabs/dees2projectteam2/blob/master/img/1.JPG)


## Collect schedule
- AirFlow
    ![AirFlow](https://github.com/zeuslabs/dees2projectteam2/blob/master/img/airflow.JPG)
    - DAG - [collect]
    - ![DAG](https://github.com/zeuslabs/dees2projectteam2/blob/master/img/dag.JPG)    
    ```
        1분마다 실행
    ```
    - Task
    - ![TASK](https://github.com/zeuslabs/dees2projectteam2/blob/master/img/task.JPG)    
        - [print_date]
        ```
        - 날짜 print
        ```
        - [collect_task]        
        ```
        - ./bin/collect.sh shell 을 실행
        - Repository 에 년/월/일 경로에 json 파일 저장
        - 저장된 파일을 git push 
        ```

