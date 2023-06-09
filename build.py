from aptos_sdk.account import Account
from aptos_sdk.client import FaucetClient, RestClient
import time
from datetime import datetime
import sys

NODE_URL = 'https://fullnode.mainnet.aptoslabs.com/v1'

rest_client = RestClient(NODE_URL)
print(f'Connect to chain ID = {rest_client.chain_id}')

# Run multiple
if len(sys.argv) > 1:
  listPrivate = sys.argv[1]

account = Account.load_key(str(listPrivate))
address = account.address()
publicKey = account.public_key()
privateKey = account.private_key

payload = {
  "function": "0xd37c243d20e3ee25957397711c4703442468db38c7571120e0af7a6c4fa11e5f::factory::mint_with_quantity",
  "type_arguments": [],
  "arguments": [
    "2"
  ],
  "type": "entry_function_payload"
}

def timestamp():
    timeNow = datetime.now()
    return timeNow

try:
  while True:
    timeNow = time.time()
    startTime = 1666368000
    countdown = (int(timeNow)-startTime)
    if countdown > 0:
      txh = rest_client.submit_transaction(account, payload)
      print(txh)
      print(rest_client.wait_for_transaction(txh))
      break
    else:
      print(f'{timestamp()} | Loading... {countdown} seconds')
except Exception as exc:
  print(exc)

input('pause')
