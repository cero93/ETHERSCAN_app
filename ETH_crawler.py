from web3 import Web3
from web3.auto import w3
import time, ccxt


INFURA_URL="https://mainnet.infura.io/v3/b985331c93914c45b58bd46456044039"
w3 = Web3(Web3.HTTPProvider(INFURA_URL))
print("-----------------------------------------------------------------------------------")

userInputAddress = input("GIVEN ADDRESS:")
_1_ETH_Address = "{}".format(userInputAddress)
ETH_address=Web3.toChecksumAddress(_1_ETH_Address)

#INFO NR. BLOCK, TIME UTC
_block_nr=input("GIVEN BLOCK NUMBER:")
block_nr=int(_block_nr)
_timestamp=w3.eth.get_block(block_nr)
timestamp=_timestamp['timestamp']
readable_time=time.strftime('%A, %Y-%m-%d %H:%M:%S', time.localtime(timestamp))

#PRICE ETH CURRENT
binance = ccxt.binance()
eth_ticker = binance.fetch_ticker('ETH/USDT')
eth_last = eth_ticker['last']

#GET TRANSACTIONS IN GIVEN BLOCK
block = w3.eth.get_block(block_nr)
block_specific_hashes_or_tansactions=block['transactions']

print("\nstart calculating")

#HASHES
clean_hash=[]
for cl_hash in block_specific_hashes_or_tansactions:
    clean_hash.append(cl_hash.hex())

#from SPECIFIC OUTSIDE ADDRESS TO our ADDRESS
clean_hash_to=[]    
for i in clean_hash:
    print("calculating....",i)
    clean_hash_to.append(w3.eth.get_transaction(i)['to'])

#from our ADDRESS TO SPECIFIC outside ADDRESS
clean_hash_from=[]    
for j in clean_hash:
    print("calculating....",j)
    clean_hash_from.append(w3.eth.get_transaction(j)['from'])

print("\n\n-----------------------------------------------------------------------------------")
print("CURRENT ETH PRICE: ",eth_last, "USD")
print("CURRENT BLOCK NUMBER: ",w3.eth.block_number)
print("-----------------------------------------------------------------------------------")
print("GIVEN ETH ADDRESS: ",userInputAddress)
print("GIVEN BLOCK NUMBER: ",_block_nr)
print("GIVEN BLOCK TIME: ",readable_time)

#DEPOSITS ADDRESS INFO 
for addr_to in clean_hash_to:
    if addr_to == ETH_address:
        transaction_to_place_to=clean_hash_to.index(ETH_address)
        belonging_hash_to=clean_hash[transaction_to_place_to]
        _transaction_info= w3.eth.get_transaction(belonging_hash_to)
        transaction_to=_transaction_info['to']
        transaction_from=_transaction_info['from']
        _transaction_value_wei=_transaction_info['value']
        gas_price = w3.eth.getTransaction(belonging_hash_to).gasPrice
        gas_used = w3.eth.getTransactionReceipt(belonging_hash_to).gasUsed
        transaction_value_eth= w3.fromWei(_transaction_value_wei, 'ether')
        total_gas_price=gas_used*gas_price
        gas_price_ETH=w3.fromWei(total_gas_price, 'ether')
        print("\n-----------------------------DEPOSITS-------------------------------------------")
        print("transaction IS ON:",transaction_to_place_to, "PLACE in BLOCK")
        print ("RECIPIENT: ", transaction_to,"\nSENDER: ",transaction_from,"\ntransaction value: ",transaction_value_eth," ETH","\ntransaction costs: ",gas_price_ETH," ETH")
        print("----------------------------------------------------------------------------------")
    else:
        continue

#WITHDRAWALS ADDRESS INFO
for addr_from in clean_hash_from:
    if addr_from == ETH_address:
        transaction_to_place_from=clean_hash_from.index(ETH_address)
        belonging_hash_from=clean_hash[transaction_to_place_from]
        _2_transaction_info= w3.eth.get_transaction(belonging_hash_from)
        _2_transaction_to=_2_transaction_info['to']
        _2_transaction_from=_2_transaction_info['from']
        _2_transaction_value_wei=_2_transaction_info['value']
        _2_gas_price = w3.eth.getTransaction(belonging_hash_from).gasPrice
        _2_gas_used = w3.eth.getTransactionReceipt(belonging_hash_from).gasUsed
        _2_transaction_value_eth= w3.fromWei(_2_transaction_value_wei, 'ether')
        total_gas_price=_2_gas_price*_2_gas_used
        _2_gas_price_ETH=w3.fromWei(total_gas_price, 'ether')
        print("\n---------------------------WITHDRAWALS------------------------------------------")
        print("transaction IS ON:",transaction_to_place_from, "PLACE in BLOCK")
        print ("RECIPIENT: ", _2_transaction_to,"\nSENDER: ",_2_transaction_from,"\ntransaction value: ",_2_transaction_value_eth," ETH","\ntransaction costs: ",_2_gas_price_ETH," ETH")
        print("----------------------------------------------------------------------------------")
    else:
        continue

print("\ncalculation finished")



