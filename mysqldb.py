import pymysql
import datetime
import re


def datemanager():
    return datetime.datetime.now().strftime("%Y%m%d")


def parser(result, n):
    parsed = re.findall("'(.+?)'", str(result))
    return parsed[n]


def sql_engine(type, name, code):
    conn = pymysql.connect(host="54.180.156.107", user='root', password='aptp2022!', db='database', charset='utf8')
    cur = conn.cursor()

    if type == 1:
        # 해당 code 를 가진 품목의 상태 확인
        # return 값은, 해당 코드가 대여중이라면 대여자와 남은 대여 기간을 반환
        # 해당 코드가 대여중이지 않다면 대여중이지 않다고 반환

        sql = "SELECT status FROM products WHERE code = " + str(code)
        cur.execute(sql)
        conn.commit()
        result = cur.fetchone()
        status = int(str(result)[1])

        if status == 1:  # 대여중
            sql = "SELECT person, date FROM products WHERE code = " + str(code)
            cur.execute(sql)
            conn.commit()
            result = cur.fetchone()
            conn.close()
            return result

        if status == 0:  # 대여중 아님
            conn.close()
            return 0

    if type == 2:
        # 해당 code의 상품에 대여 요청
        # name, code 를 파라미터로 받음
        # 대여자가 없는지는 engine에서 한번 더 확인

        if sql_engine(1, None, code) != 0:
            # 해당 상품에 대여자가 있는 경우
            # 잘못된 요청
            conn.close()
            return -1

        sql = "UPDATE products SET status = 1, person ='" + name + "', date = '" + str(
            datemanager()) + "' WHERE code = " + str(code) + ";"
        print(sql)
        cur.execute(sql)
        conn.commit()
        conn.close()
        return 0

    if type == 3:
        # 해당 code의 상품에 반납 요청
        # name, code 를 파라미터로 받음
        # 대여자가 없는지는 engine에서 한번 더 확인
        if sql_engine(1, None, code) == 0:
            # 해당 상품에 대여자가 없는 경우
            # 잘못된 요청
            conn.close()
            return -1

        if parser(sql_engine(1, None, code), 0) != name:
            # 해당 상품의 대여자가 아닌 경우
            # 잘못된 요청
            conn.close()
            return -2

        sql = "UPDATE products SET status = 0, person = '대여자 없음', date = '대여자 없음' WHERE code = " + str(code) + ";"
        cur.execute(sql)
        conn.commit()
        conn.close()
        return 0
        # 반납

    if type == 4:
        # 전체 물품의 현재시간과 빌린 시간 비교를 통해 기한이 넘지 않았는지 확인
        if sql_engine(1, None, code) == 0:
            # 해당 상품에 대여자가 없는 경우
            # 잘못된 요청
            conn.close()
            return -1

        sql = "SELECT date FROM products WHERE code =" + str(code) + ";"
        cur.execute(sql)
        conn.commit()
        result = cur.fetchone()
        date_product = str(parser(result, 0))

        year_product = int(date_product[:4])
        month_product = int(date_product[4:6])
        day_product = int(date_product[6:8])

        now = datetime.datetime.now()
        prod = datetime.datetime.strptime(date_product, "%Y%m%d")
        date_diff = now - prod

        if date_diff.days > 7:
            # 반납기한 초과
            return -1
        # 반납기한 초과하지 않음
        return 0


# func sql_engine
# param : type, name, code
# type : query type
# name : user name
# code : product code

# 대여 요청
sql_engine(3, "엄준식", 2)

# 반납 요청
sql_engine(2, "이승찬", 1)

# 물품 대여기간 확인
sql_engine(4, None, 2)