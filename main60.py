from coinbase_advanced_trader.enhanced_rest_client import EnhancedRESTClient

api_key = "organizations/1073f4e6-52f3-49e4-b7e4-e2bd34261c51/apiKeys/98d72869-c4dd-40cd-8a66-b6974022dae5"
api_secret = "-----BEGIN EC PRIVATE KEY-----\nMHcCAQEEILuQ+nBhRlUvcYABLUqzEprYTLkALB6ingIrAteSqMoHoAoGCCqGSM49\nAwEHoUQDQgAEYPYQKEooGDLbvPP47stcsiDCj/NG9vWMTu+c1ckwx2BdhQIYQSBB\nJ/LaS1v96ena8OXynGo/XOPSQjw1kmnLDA==\n-----END EC PRIVATE KEY-----\n"

client = EnhancedRESTClient(api_key=api_key, api_secret=api_secret)

balance = client.get_crypto_balance("GIGA")
print(balance)