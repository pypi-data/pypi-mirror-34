from qsnark_python_sdk.http.request import Request


class Contract(Request):
    __API_COMPILE_CONTRACT = '/dev/contract/compile'
    __API_DEPLOY_CONTRACT_ASYNC = '/dev/contract/deploy'
    __API_DEPLOY_CONTRACT_SYNC = '/dev/contract/deploysync'
    __API_GET_PAYLOAD = '/dev/payload'
    __API_INVOKE_CONTRACT_ASYNC = '/dev/contract/invoke'
    __API_INVOKE_CONTRACT_SYNC = '/dev/contract/invokesync'
    __API_MAINTAIN_CONTRACT = '/dev/contract/maintain'
    __API_QUERY_CONTRACT_STATUS = '/dev/contract/status'

    def __init__(self):
        pass

    def compile_contract(self, data):
        return self.post_json(self.__API_COMPILE_CONTRACT, data)

    def deploy_contract_async(self, data):
        return self.post_json(self.__API_DEPLOY_CONTRACT_ASYNC, data)

    def deploy_contract_sync(self, data):
        return self.post_json(self.__API_DEPLOY_CONTRACT_SYNC, data)

    def get_payload(self, data):
        return self.post_json(self.__API_GET_PAYLOAD, data)

    def invoke_contract_async(self, data):
        return self.post_json(self.__API_INVOKE_CONTRACT_ASYNC, data)

    def invoke_contract_sync(self, data):
        return self.post_json(self.__API_INVOKE_CONTRACT_SYNC, data)

    def maintain_contract(self, data):
        return self.post_json(self.__API_MAINTAIN_CONTRACT, data)

    def query_contract_status(self, hash_address):
        query = '?address=' + str(hash_address)
        url = self.__API_QUERY_CONTRACT_STATUS + query
        return self.get(url)
