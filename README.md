# ETHERSCAN_app
Program is written in Python language version 3.10. 
For program to run, those features must be installed:
py -3 -m pip install web3
py -3 -m pip install infura
py -3 -m pip install ccxt

I utilized API service through Infura, made here an account for access to Ethereum network. My Infura URL is still open so you don’t have to modify it. For Ethereum node library I choose web3.py. I do not run node on my computer, so that was one of the choices how to speak with Ethereum blockchain. 
After all of this is installed (I hope I didn’t forget something-if so, do not hesitate to contact me) you can run the program.
You can start the program in console and run the file ETH_crawler.py

In console:
The program asks you to input Ethereum address (GIVEN ADDRESS:) which you want to observe (press enter after pasted it).
The program asks you to input Block number (GIVEN BLOCK NUMBER:) which you want to observe (press enter after pasted it).
When calculation starts, console shows: start calculating
When calculation is in progress, console shows: calculating…<transaction hash>
The program is running and calculating-try to find in the blockchain if there was an interaction with this address in the given block. Program is looking for each transaction hash in the given block and try to find if there was withdrawal to or deposit from given address. 
If program finds there was interaction with given address, it then looks at the transaction hash on which place it was and collect information about. Program finds if the address was recipient or sender. At the end of calculation there are information about:
-	Current ETH price in USD
-	Current block number
-	Given ETH address 
-	Given block number
-	Given block time

In as much as readable way it shows if the transaction was made to given address or from it. It is shown as WITHDRAWALS or DEPOSITS.
Printout collects information about: 
- on which place in block was transaction observed (transaction hash)
- who was SENDER and who RECIPIENT (depending if it was withdrawal or deposit)
- transaction value in ETH
- transaction costs in ETH (total gas)

When calculation is finish it shows: calculation finished

If there is no WITHDRAWALS or DEPOSITS there is nothing at the end. If there was transaction made for any other token than ETH in ERC20 network the transaction value would be: 0. Any other information will be visible. 
