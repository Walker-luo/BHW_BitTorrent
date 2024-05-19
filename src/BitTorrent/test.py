import bencodepy
import hashlib
from utilities import *

# Define the path to the .torrent file
file_path = './torrentFiles/example.torrent'

# Read and decode the .torrent file
with open(file_path, "rb") as file:
    encoded_data = file.read()
    torrent = bencodepy.decode(encoded_data)

# Print the decoded torrent file content
# print("Decoded .torrent file content:")
# print(torrent)

# Access specific elements (if needed)
announce = torrent[b'announce'].decode()
info = torrent[b'info']
file_length = info[b'length']
file_name = info[b'name'].decode()
piece_length = info[b'piece length']
pieces = info[b'pieces']

# print("\nTorrent Details:")
# print(f"Announce URL: {announce}")
# print(f"File Name: {file_name}")
# print(f"File Length: {file_length} bytes")
# print(f"Piece Length: {piece_length} bytes")
# print(f"Pieces: {pieces}")

# info_hash = hashlib.sha1(pieces)
# print(info_hash)

# for i in range(10):
#     print(generate_peer_id())
info_hash = hashlib.sha1(bencodepy.encode(pieces)).digest()
print(f'info_hash = {info_hash.hex()}')
peer_id = generate_peer_id().encode()
port = 6881  # Default BitTorrent port

tracker_response =getPeersFromTracker(announce, info_hash, peer_id, port, left=file_length)
print(tracker_response)

