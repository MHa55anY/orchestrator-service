# orchestrator-service
An RPC Orchestration Service is created such that:
Request Sequence: Client --> PORT9000 --> PORT9001--> PORT10000
Response Sequence: Client <-- PORT9000 <-- PORT9001 <-- PORT10000

Directions for executing the service:
1. Copy the directory to your computer as is
2. Start the servers one by one in your terminal windows, starting with server_9000.py
3. Start server_9001.py
4. Start dummy-server.py located in /datamock/ (this will serve and return the User objected generated from user's name)
5. Finally start client.py and answer the query which pops up

There will be a distinguishable message on each terminal indicating how the message is propogated/orchestrated

