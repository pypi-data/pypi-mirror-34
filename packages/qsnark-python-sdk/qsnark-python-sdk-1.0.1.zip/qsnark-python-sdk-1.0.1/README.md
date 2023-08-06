## Qsnark-Python-SDK

趣链开发者平台 SDK for Python

## 安装

* 使用 pip 安装

```bash
pip install qsnark-python-sdk
```

## 使用方法

```py
# 导入模块
from qsnark_python_sdk import QsnarkSDK

# 初始化实例
qsnark = QsnarkSDK({
    'phone': '17816656663',
    'password': "123456",
    'client_id': "0b6fca20-d7bb-414a-be12-d573db72dfcb",
    'client_secret': "7z99lk58450s27FJdHW2Q9zIkh4P4RFR"
})

# 调用相关接口
response = qsnark.create_account()

# 使用响应数据
print(response)
```

## API

### 规范

* 当前 SDK 使用趣链开发者平台 v1 版本的 API
* 所有接口返回的数据的格式都是 dict（获取 payload 接口例外，后期会统一进行规范）
* 初始化 Qsnark 实例时，sdk 会自动获取 `access token`，并且也会在 token 过期后，自动根据 `refresh token` 获取新的 `access token` （细节参见 `Request.php` 的 `handle_request()` 方法）

### 初始化 SDK 实例

```py
# 导入模块
from qsnark_python_sdk import QsnarkSDK

# 初始化实例
qsnark = QsnarkSDK({
    'phone': '17816656663',
    'password': "123456",
    'client_id': "0b6fca20-d7bb-414a-be12-d573db72dfcb",
    'client_secret': "7z99lk58450s27FJdHW2Q9zIkh4P4RFR"
})
```

### 授权码

* **获取授权码**
  * get_access_token()

```py
response = qsnark.get_access_token()
```

* **获取最新的授权码**
  * refresh_access_token()

```py
response = qsnark.refresh_access_token()
```

### 账号

* **新建账号**
  * create_account()

```py
response = qsnark.create_account()
```

### 区块

* **根据区块编号查询单个区块**
  * query_block_by_number(int number)

```py
number = 10223

response = qsnark.query_block_by_number(number)
```

* **根据区块hash查询单个区块**
  * query_block_by_hash(string hash_address)

```py
hash_address = "0x502ca40015f8f64f2b98987c10201b4e5fd58c2f33a79cf0dc2847d03cc35152";

response = qsnark.query_block_by_hash(hash_address)
```

* **以分页的方式查询多个区块信息**
  * query_blocks_by_page(int page, int page_size)

```py
page = 1
page_size = 10

response = qsnark.query_blocks_by_page(page, page_size)
```

* **根据区块号范围查询多个区块信息**
  * query_blocks_by_range(int from_num, int to_num)

```py
from_num = 1024
to_num = 1030

response = qsnark.query_blocks_by_range(from_num, to_num)
```

### 智能合约

* **编译合约**
  * compile_contract(dict data)

```py
data = {
    'CTCode': 'pragma solidity ^0.4.0;\n\ncontract HelloWorld{\n    string str = \"hello world\";\n    \n    function update(bytes32[] amount) returns (address, bytes32[], string){\n        return (msg.sender, amount, str);\n    }\n}'
}

response = q.compile_contract(data)
```

* **异步部署合约：** 直接返回交易的hash值，但不能保证合约一定能部署成功，一般会通过查询交易hash是否有数据来判断是否部署成功
  * deploy_contract_async(dict data)

* **同步部署合约：** 只有合约部署成功或失败后，才会返回数据
  * deploy_contract_sync(dict data)

```py
data = {
    'From': '0xdc252d441c53cb9aecf3e888a0e9dc7cbfbe2164',
    'Bin': '0x606060405260408051908101604052600b81527f68656c6c6f20776f726c640000000000000000000000000000000000000000006020820152600090805161004b92916020019061005c565b50341561005757600080fd5b6100fc565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061009d57805160ff19168380011785556100ca565b828001600101855582156100ca579182015b828111156100ca5782518255916020019190600101906100af565b5b506100d79291506100db565b5090565b6100f991905b808211156100d757600081556001016100e1565b5090565b90565b6102788061010b6000396000f300606060405263ffffffff7c01000000000000000000000000000000000000000000000000000000006000350416630fdb3f31811461003d575b600080fd5b341561004857600080fd5b61008c600460248135818101908301358060208181020160405190810160405280939291908181526020018383602002808284375094965061016895505050505050565b60405173ffffffffffffffffffffffffffffffffffffffff84168152606060208201818152906040830190830185818151815260200191508051906020019060200280838360005b838110156100ed5780820151818401525b6020016100d4565b50505050905001838103825284818151815260200191508051906020019080838360005b8381101561012a5780820151818401525b602001610111565b50505050905090810190601f1680156101575780820380516001836020036101000a031916815260200191505b509550505050505060405180910390f35b6000610172610228565b61017a610228565b33846000808054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156102135780601f106101e857610100808354040283529160200191610213565b820191906000526020600020905b8154815290600101906020018083116101f657829003601f168201915b505050505090509250925092505b9193909250565b60206040519081016040526000815290565b602060405190810160405260008152905600a165627a7a72305820f8030ada26e96e0d8cc19cd6816aef3ea4c5622cb4a1b76d48b6c10eb7261f620029'
}

# 异步部署
response = q.deploy_contract_async(data)

# 同步部署
response = q.deploy_contract_sync(data)
```

* **获取 Payload**
  * get_payload(dict data)

```py
data = {
    'Abi': '[{\"constant\":false,\"inputs\":[{\"name\":\"amount\",\"type\":\"bytes32[]\"}],\"name\":\"update\",\"outputs\":[{\"name\":\"\",\"type\":\"address\"},{\"name\":\"\",\"type\":\"bytes32[]\"},{\"name\":\"\",\"type\":\"string\"}],\"payable\":false,\"type\":\"function\"}]',
    'Args': [['1', '345']],
    'Func': 'update'
}

response = q.get_payload(data)
```

* **异步调用合约：** 直接返回交易的hash值，但不能保证合约一定能调用成功，一般会通过查询交易hash是否有数据来判断是否调用成功
  * invoke_contract_async(dict data)

* **同步调用合约：** 只有合约调用成功或失败后，才会返回数据
  * invoke_contract_sync(dict data)

```py
data = {
    'From': '0xdc252d441c53cb9aecf3e888a0e9dc7cbfbe2164',
    'Const': False,
    'Payload': '0x0fdb3f310000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000231000000000000000000000000000000000000000000000000000000000000003334350000000000000000000000000000000000000000000000000000000000',
    'To': '0x1831dc6be6d803f7407588a312d6e27377b1aa79',
}

# 异步调用合约
response = q.invoke_contract_async(data)

# 同步调用合约
response = q.invoke_contract_sync(data)
```

* **维护智能合约：** 可对部署后的合约进行升级/冻结/解冻
  * maintain_contract(dict data)

```py
# Operationt: 升级合约填 1,冻结合约填 2,解冻合约填 3
data = {
    'From': '0xdc252d441c53cb9aecf3e888a0e9dc7cbfbe2164',
    'Operation': 1,
    'Payload': '0x0fdb3f310000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000231000000000000000000000000000000000000000000000000000000000000003334350000000000000000000000000000000000000000000000000000000000',
    'To': '0x1831dc6be6d803f7407588a312d6e27377b1aa79'
}

response = q.maintain_contract(data)
```

* **查询智能合约状态**
  * query_contract_status(string hash_address)

```py
hash_address = '0x51180905345b1d1def37f2fde487e73c769dc2e0'

response = q.query_contract_status(hash_address)
```

### 交易

* **查询区块链交易总数**
  * count_transaction()

```py
response = qsnark.count_transaction()
```

* **通过交易哈希值查询单条交易信息**
  * query_transaction_by_hash(string hash_address)

```py
hash_address = '0x0d3ad8ac53087a858a86ddc5fb2cf8bf205f1ddbbdc19140c7f77b8a88d6dbf4'

response = qsnark.query_transaction_by_hash(hash_address)
```

* **通过交易哈希值查询交易回执信息**
  * query_txreceipt_by_hash(string hash_address)

```py
hash_address = '0x0d3ad8ac53087a858a86ddc5fb2cf8bf205f1ddbbdc19140c7f77b8a88d6dbf4'

response = qsnark.query_txreceipt_by_hash(hash_address)
```

* **根据时间戳范围查询非法交易**
  * query_all_illegal_transactions(int start_time, int end_time)

```py
start_time = 1483228800000
end_time = 1514764800000

response = q.query_all_illegal_transactions(start_time, end_time)
```
