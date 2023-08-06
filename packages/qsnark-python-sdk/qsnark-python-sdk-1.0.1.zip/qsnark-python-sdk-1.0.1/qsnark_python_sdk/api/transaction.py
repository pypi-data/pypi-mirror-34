from qsnark_python_sdk.http.request import Request


class Transaction(Request):
    __API_COUNT_TRANSACTION = '/dev/transaction/count'
    __API_QUERY_TRANSACTION_BY_HASH = '/dev/transaction/query'
    __API_QUERY_TXRECEIPT_BY_HASH = '/dev/transaction/txreceipt'
    __API_QUERY_ALL_ILLEGAL_TRANSACTIONS = '/dev/transactions/discard'

    def __init__(self):
        pass

    def count_transaction(self):
        return self.get(self.__API_COUNT_TRANSACTION)

    def query_transaction_by_hash(self, hash_address):
        query = '?hash=' + str(hash_address)
        url = self.__API_QUERY_TRANSACTION_BY_HASH + query
        return self.get(url)

    def query_txreceipt_by_hash(self, hash_address):
        query = '?txhash=' + str(hash_address)
        url = self.__API_QUERY_TXRECEIPT_BY_HASH + query
        return self.get(url)

    def query_all_illegal_transactions(self, start_time, end_time):
        query = '?start=' + str(start_time) + '&end=' + str(end_time)
        url = self.__API_QUERY_ALL_ILLEGAL_TRANSACTIONS + query
        return self.get(url)
