import datetime

import pymysql
import csv

exec_dt = datetime.datetime.now().strftime('%y%m%d_%H%M%S')
# 데이터베이스 연결 설정
connection = pymysql.connect(host='127.0.0.1',
                             port=13306,
                             user='jeff',
                             password='123123..',
                             db='index_test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # 프로파일링 활성화
        cursor.execute("SET profiling = 1;")

        loop_cnt = 1000
        cases = {
            "start_dt": "2014-01-01",
            "table_nms": [
                {"tbl_nm": "employees_nonindexed", "loop": 100},
                {"tbl_nm": "employees_indexed_with_composite", "loop": 100},
                {"tbl_nm": "employees_indexed", "loop": 100},
            ],
            "end_dts": ["2015-01-01", "2016-01-01", "2017-01-01"],
            "loop_cnt": 100
        }

        for case in cases["table_nms"]:

            table_nm = case["tbl_nm"]
            loop_cnt = case["loop"]
            start_dt = cases["start_dt"]
            for end_dt in cases["end_dts"]:
                q = f"""
                                SELECT * FROM {table_nm}
                                WHERE department = '개발' AND hire_date BETWEEN '{start_dt}' AND '{end_dt}';
                            """
                print(q, end_dt)

                # 쿼리 수행 시간을 저장할 리스트
                execution_times = []

                for _ in range(loop_cnt):
                    # 쿼리 실행 -> 숫자 및 테이블 바꿔가면서 진행
                    cursor.execute(q)
                    # 프로파일 정보 가져오기
                    cursor.execute("SHOW PROFILES;")
                    profiles = cursor.fetchall()

                    # 가장 최근 쿼리 번호 찾기 (employees_indexed 쿼리)
                    query_number = profiles[-1]['Query_ID']  # 마지막 실행된 쿼리 ID

                    # 해당 쿼리 ID의 프로파일 세부 정보 가져오기
                    cursor.execute(f"SHOW PROFILE FOR QUERY {query_number};")
                    profile_details = cursor.fetchall()
                    print(_)
                    # 'executing' 단계의 시간을 찾아 리스트에 추가
                    for detail in profile_details:
                        if detail['Status'] == 'executing':
                            execution_times.append(detail['Duration'])
                            break
                # CSV 파일로 결과 저장
                with open(f'{f"{exec_dt}"}_{table_nm}_{cases["start_dt"]}_{end_dt}_loop_{loop_cnt}.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(['Execution Time'])
                    for time in execution_times:
                        writer.writerow([time])

finally:
    connection.close()

print("테스트 완료")
