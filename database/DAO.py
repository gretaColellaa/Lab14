from database.DB_connect import DBConnect
from model.orders import Order
from model.stores import Store


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getStores():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select s.*
                    from bike_store_full.stores s 
                    order by s.store_name 
                """

        cursor.execute(query,)

        for row in cursor:
            result.append(Store(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getOrders(store_id):

        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select o.*
                    from bike_store_full.orders o 
                    where o.store_id = %s
                """

        cursor.execute(query, (store_id,))

        for row in cursor:
            result.append(Order(**row))

        cursor.close()
        conn.close()
        return result



    @staticmethod
    def getNodes(k):

        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT
                    distinct
                    o1.order_id, o2.order_id
                    FROM
                    bike_store_full.orders
                    o1, bike_store_full.orders
                    o2
                    WHERE
                    DATEDIFF(o1.order_date, o2.order_date) < 3
                    AND
                    o1.order_id != o2.order_id;
                    """

        cursor.execute(query, (k,))

        for row in cursor:
            result.append(Order(**row))

        cursor.close()
        conn.close()
        return result
