from qsnark_python_sdk.http.request import Request


class Block(Request):
    __API_QUERY_SINGLE_BLOCK = '/dev/block/query'
    __API_QUERY_BLOCKS_BY_PAGE = '/dev/blocks/page'
    __API_QUERY_BLOCKS_BY_RANGE = '/dev/blocks/range'

    def __init__(self):
        pass

    def query_block_by_number(self, number):
        query = '?type=number&value=' + str(number)
        url = self.__API_QUERY_SINGLE_BLOCK + query
        return self.get(url)

    def query_block_by_hash(self, hash_address):
        query = '?type=hash&value=' + str(hash_address)
        url = self.__API_QUERY_SINGLE_BLOCK + query
        return self.get(url)

    def query_blocks_by_page(self, page=1, page_size=10):
        query = '?index=' + str(page) + '&pageSize=' + str(page_size)
        url = self.__API_QUERY_BLOCKS_BY_PAGE + query
        return self.get(url)

    def query_blocks_by_range(self, from_num, to_num):
        query = '?from=' + str(from_num) + '&to=' + str(to_num)
        url = self.__API_QUERY_BLOCKS_BY_RANGE + query
        return self.get(url)
