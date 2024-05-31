import pymysql
import csv

# 데이터베이스 연결 설정
connection = pymysql.connect(host='127.0.0.1',
                             port=13306,
                             user='jeff',
                             password='123123..',
                             db='index_test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


def shoot(q):
    cursor.execute(q)
    row = cursor.fetchone()
    print(q)
    print(row)
    print()


try:
    with connection.cursor() as cursor:
        # 프로파일링 활성화

        # _q = "EXPLAIN ANALYZE SELECT * FROM employees_nonindexed WHERE hire_date between  '2014-01-01' and '2015-01-01';"
        # shoot(_q)
        # _q = "EXPLAIN ANALYZE SELECT * FROM employees_indexed WHERE hire_date between  '2014-01-01' and '2015-01-01';"
        # shoot(_q)
        # _q = "EXPLAIN ANALYZE SELECT * FROM employees_indexed_with_composite WHERE hire_date between  '2014-01-01' and '2015-01-01';"
        # shoot(_q)


        _q = "EXPLAIN ANALYZE SELECT * FROM employees_nonindexed WHERE department='개발' and hire_date BETWEEN '2010-01-01' AND '2015-01-01';"
        shoot(_q)
        _q = "EXPLAIN ANALYZE SELECT * FROM employees_indexed WHERE department='개발' and hire_date BETWEEN '2010-01-01' AND '2015-01-01';"
        shoot(_q)
        _q = "EXPLAIN ANALYZE SELECT * FROM employees_indexed_with_composite WHERE department='개발' and hire_date BETWEEN '2010-01-01' AND '2015-01-01';"
        shoot(_q)

        # _q = "ANALYZE TABLE employees_nonindexed;"
        # shoot(_q)
        # _q = "ANALYZE TABLE employees_indexed;"
        # shoot(_q)
        # _q = "ANALYZE TABLE employees_indexed_with_composite;"
        # shoot(_q)

        # _q = "EXPLAIN ANALYZE SELECT * FROM employees_indexed_with_composite WHERE hire_date BETWEEN '2014-01-01' AND '2014-01-10';" # 10일치
        # shoot(_q)
        # _q = "EXPLAIN ANALYZE SELECT * FROM employees_indexed_with_composite WHERE hire_date BETWEEN '2014-01-01' AND '2014-01-20';" # 20일치
        # shoot(_q)


finally:
    connection.close()

print("테스트 완료")
