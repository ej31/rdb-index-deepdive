import pymysql
import csv

# 데이터베이스 연결 설정
connection = pymysql.connect(host='127.0.0.1',
                             port=3306,
                             user='jeff',
                             password='123123',
                             db='index_test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # 프로파일링 활성화
        cursor.execute("SET profiling = 1;")

        # 쿼리 수행 시간을 저장할 리스트
        execution_times = []

        # 쿼리 1000번 실행
        for _ in range(10):
            # 쿼리 실행 -> 숫자 및 테이블 바꿔가면서 진행
            cursor.execute("""
                SELECT * FROM employees_nonindexed
                WHERE department = '개발' AND hire_date BETWEEN '2014-01-01' AND '2014-01-20';
            """)

            # 프로파일 정보 가져오기
            cursor.execute("SHOW PROFILES;")
            profiles = cursor.fetchall()

            # 가장 최근 쿼리 번호 찾기 (employees_indexed 쿼리)
            query_number = profiles[-1]['Query_ID']  # 마지막 실행된 쿼리 ID

            # 해당 쿼리 ID의 프로파일 세부 정보 가져오기
            cursor.execute(f"SHOW PROFILE FOR QUERY {query_number};")
            profile_details = cursor.fetchall()

            # 'executing' 단계의 시간을 찾아 리스트에 추가
            for detail in profile_details:
                if detail['Status'] == 'executing':
                    execution_times.append(detail['Duration'])
                    break
            print(_)
        # CSV 파일로 결과 저장
        with open('query_execution_times.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Execution Time'])
            for time in execution_times:
                writer.writerow([time])

finally:
    connection.close()

print("테스트 완료")
