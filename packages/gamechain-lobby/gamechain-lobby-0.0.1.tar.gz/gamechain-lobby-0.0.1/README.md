# gamechain-lobby
Sometimes harder than winning a game itself is finding, rounding up, and synchronizing players. Doing it digitally in an open platform is even worse. Let's see if we can't make it better with a flow something like that below.

### Hypothesis
This project is to test my hypothesis that the Bitcoin Cash (BCH) blockchain and mempool with zero-confirmation transaction times can make a good, open, non-proprietary game lobby system for multi-player game participation.

Participants signal their intent to start or join a game (or one of its variants) with a public key-based player identity along with enough information to let participants connect/watch. Challengers can accept, and game moves/summaries/outcomes could published on the blockchain, too (see [GameChain protocol](https://github.com/devalbo/gamechain)).

### What is Game Match-making?
A multiplayer game is a set of shared constraints on possible actions starting from an established set of conditions that a group of participants engages in. For video games, finding other parties who want to accept those constraints has traditionally been a developer-driven set of choices based on their software and servers. With Bitcoin Cash, there is a global, low-cost way for sharing  transactions and messages that isn't bound to a particular server. Just as a variety of cryptocurrency wallets can find each other and transfer units of currency around the Internet, so can a multitude of game clients find other willing parties and transfer intents to play focusing on a shared protocol and not some matchmaking server somewhere.

The point of matchmaking is to make sure that all players interested in a game at a particular point in time can agree on the game itself, how the game will start out, and protocols and semantics to use for making plays and taking turns. These common concerns are handled in this protocol, though each individual game will have to have a protocol and software client for actual use.

## Scope
This protocol focuses on initiating gameplay: selecting a game, finding other participants, and making sure everyone is clear on the rules/variant you are playing.
Once that's done, gameplay can start based on these parameters. For example, if a server is established as part of initiation, different client applications can connect using their gamechain-lobby identities. Note that a companion protocol for on-chain game play is being tested at [GameChain](https://github.com/devalbo/gamechain). Ultimately, how a game ends being played is ultimately up to the participants.

#### There's a lot to do yet...
There are a lot of details to work out and conventions/protocols to support all types of games would be very important, but I am optimistic. One thing to note is that games that use randomness should be possible, but I'm starting as simply as possible. Many games have more than two players, which should also be possible, but I will start with only two players to keep communication simple while testing this hypothesis.

#### Assumptions
This system works by using mempools and 0-conf to notify clients about transaction relevant to protocols used for game discovery and play. We will start with some basic assumptions.
* A Player is denoted by a BCH address. This BCH address is that Player's PlayerId.
* A Player uses their private key to sign/authenticate messages they transmit.
* A Player who wishes to start a game is called the Initiator.
* A Game is defined as: a set of initial conditions, rules that define valid actions players can take, how the game state changes based on those actions, transitions between Player turns, when the game ends, and what the outcome of the game is.
* A Game has a GameLobby identifier BCH address.  
* A Match is an instance of a Game. A concluded Match consists of initial conditions, at least one Player, and a series of Player-induced actions.


##Protocol
####BCH Transaction addressing scheme
 The first occurring P2PKH UTXO in a GameChain Lobby transaction is the address of the message sender. Addresses of intended recipients are the remainig P2PKH UTXO(s). The OP_RETURN code is the GameChain Lobby message.
 
####Message Format
Gamechain Lobby messages are preceded by a version byte and a message code byte. During development, the version byte will be set to 1. Message codes are as follows.

| Message Code<br/>Hex Value | Name    | Description |
|:--------------------------:| --------| ----------- | 
| 0x01                       | **LFG** | Looking for Group. Initiator broadcasts they would like to start a game as detailed in the message. |
| 0x02                       | **WTP** | Willing to Play. Responder indicates interest in participating in a broadcaster's game. |
| 0x03                       | **ACC** | Accepted. Initiator accepts responders and provides information about how to participate in the game. |
| 0x04                       | **REJ** | Rejected. Initiator lets responder know that their WTP will not be fulfilled. |
| 0x05                       | **CAN** | Initiator broadcasts that they will not be listening for WTP responses. |


#### Message: Looking for Game (LFG)
The Initiator broadcasts a signal that they would like to start a game. They send a specially constructed _Looking for Game_ transaction addressed to the GameLobby address of the Game they want to start. The transaction contains the following information in the OP_RETURN:

| Byte Count | Name    | Format/Values | Description |
|:----------:| --------| ----------- | ---- | 
| 1          | Protocol version | Version byte | See protocol description. |
| 1          | **LFG** | 0x01 | Looking for Game message code. See above. |
| 33         | Initiator's public key | <public_key> | Key used by the initiator to sign messages. |
| 1          | Message data size | Size byte| Number of bytes to read for message data  |
| 1          | Signed message data size | Size byte | Number of bytes to read for signed message data |
| <message_data_size> | Accepted parameters for game | Comma-separated UTF-8 encoded values<br/> * game communication channel and protocol<br/> * start parameters (game/protocol-specific)<br/> * initiator game ID | Contains enough information to bootstrap a game. Maximum allowed length is 120 characters. Note that initiator game IDs should NOT be reused once they've been issued!<br/> <br/> Example message: **bch-gc:tic-tac-toe,1X,MyGameId-1** |
| <signed_message_data_size> | Signed message | Byte array used to authenticate message from initiator | Signed version of the message data | 


#### Message: Willing to Play (WTP)
Any client listening to a GameLobby address will see LFG transactions for that Game. To play, they will send a transaction to the Initiator's address. They will use their address as the sender's address. The transaction contains the following information in the OP_RETURN:

| Byte Count | Name    | Format/Values | Description |
|:----------:| --------| ----------- | ---- | 
| 1          | Protocol version | Version byte | See protocol description. |
| 1          | **WTP** | 0x02 | Willing to Play message code. See above. |
| 32         | LFG Tx ID | <transaction_id> | Transaction ID of the LFG message being responded to. |
| 33         | Responder's public key | <public_key> | Public key used by the responder to sign messages. |
| 1          | Message data size | Size byte| Number of bytes to read for message data  |
| 1          | Signed Tx ID data size | Size byte | Number of bytes to read for signed transaction ID data |
| <message_data> | Bootstrap parameters for game | Comma-separated UTF-8 encoded values for counter game start parameters, initiator game ID | Contains enough information to acknowledge a game and propose changes to initial parameters. Maximum allowed length is 120 characters. <br/> <br/> Example message: **2X,MyGameId-1** |
| <signed_tx_id> | Signed LFG Tx ID | Byte array used to authenticate message from responders | Signed version of the transaction ID being responded to. Prevents spoofing of this message.| 


#### Message: Accept/Reject/Cancel Game
Once the Initiator has received responses, it's required to accept and polite to deny the Responder and start/reject the game. This is done by the Initiator sending a message to the Responder's address and using the Initiator's address as the sender's address. 

####_Accept Game_
To accept the challenge, the Initiator is responsible for setting up game  "hosting" and publishing the connection information. For the use of GameChain, hosting will be based on a new, unused _game table address_, which is an address players will send messages to. Regardless of hosting mechanism, the Initiator creates a transaction with the following information in the OP_RETURN:

| Byte Count | Name    | Format/Values | Description |
|:----------:| --------| ----------- | ---- | 
| 1          | Protocol version | Version byte | See protocol description. |
| 1          | **ACC** | 0x03 | Game Accepted. See above. |
| 32         | WTP Tx ID | <transaction_id> | Transaction ID of the WTP message being responded to. |
| 1          | Message data size | Size byte| Number of bytes to read for message data  |
| 1          | Signed Tx ID data size | Size byte | Number of bytes to read for signed transaction ID data |
| <message_data> | Game hosting details | Comma-separated UTF-8 encoded values for game connection information | Contains enough information to let all players join the game constructed by the initiator. Maximum allowed length is 120 characters. <br/> <br/> Example message using BCH gamechain protocol: **bitcoincash-gc:\<txid>** |
| <signed_tx_id> | Signed WTP Tx ID | Byte array used to authenticate message from responders | Signed version of the transaction ID being responded to. Prevents spoofing of this message.| 


####_Reject Game_
To turn down the challenge, the transaction contains the following information in the OP_RETURN:

| Byte Count | Name    | Format/Values | Description |
|:----------:| --------| ----------- | ---- | 
| 1          | Protocol version | Version byte | See protocol description. |
| 1          | **REJ** | 0x04 | Game Rejected. See above. |
| 32         | WTP Tx ID | <transaction_id> | Transaction ID of the WTP message being responded to. |
| 1          | Message data size | Size byte| Number of bytes to read for message data  |
| 1          | Signed Tx ID data size | Size byte | Number of bytes to read for signed transaction ID data |
| <message_data> | Game rejection details | UTF-8 encoded description of game rejection | Information about why the WTP message was rejected. Maximum allowed length is 120 characters. <br/> <br/> Example message: **Sorry. Accepted another game. You can watch here @ bitcoincash-gc:tic-tac-toe:\<txid>** |
| <signed_tx_id> | Signed WTP Tx ID | Byte array used to authenticate message from responders | Signed version of the transaction ID being responded to. Prevents spoofing of this message.| 


####_Cancel Game_
To cancel an offered game, the Initiator sends a transaction with the following information in the OP_RETURN:

| Byte Count | Name    | Format/Values | Description |
|:----------:| --------| ----------- | ---- | 
| 1          | Protocol version | Version byte | See protocol description. |
| 1          | **CAN** | 0x05 | Game Canceled. See above. |
| 32         | LFG Tx ID | <transaction_id> | Transaction ID of the LFG message being responded to. |
| 1          | Message data size | Size byte| Number of bytes to read for message data  |
| 1          | Signed Tx ID data size | Size byte | Number of bytes to read for signed transaction ID data |
| <message_data> | Game cancellation details | UTF-8 encoded description of game rejection | Information about why the LFG message was canceled. Maximum allowed length is 120 characters. <br/> <br/> Example message: **Sorry. Can't play. :( It's bedtime. |
| <signed_tx_id> | Signed LFG Tx ID | Byte array used to authenticate message from responders | Signed version of the transaction ID being responded to. Prevents spoofing of this message.| 
|  |
