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
    def getEdges(k, s):

        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ WITH order_totals AS (
                    SELECT order_id, SUM(quantity) AS total_quantity
                    FROM bike_store_full.order_items
                    GROUP BY order_id
                )
                SELECT DISTINCT
                    o1.order_id AS o1,
                    o2.order_id AS o2,
                    ot1.total_quantity + ot2.total_quantity AS weight
                FROM
                    bike_store_full.orders o1
                JOIN
                    bike_store_full.orders o2 ON o1.store_id = o2.store_id
                JOIN
                    order_totals ot1 ON o1.order_id = ot1.order_id
                JOIN
                    order_totals ot2 ON o2.order_id = ot2.order_id
                WHERE
                    o1.store_id = %s
                    AND o1.order_id != o2.order_id
                    AND DATEDIFF(o2.order_date, o1.order_date) > 0
                    AND DATEDIFF(o2.order_date, o1.order_date) < %s
                    """

        cursor.execute(query, (s,k,))

        for row in cursor:
            result.append((row['o1'], row['o2'], {'weight': row['weight']}))

        cursor.close()
        conn.close()
        return result
