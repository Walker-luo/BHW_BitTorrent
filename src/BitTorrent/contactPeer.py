import socket
import struct
from connectTracker import *
from decoder import *


def connect_to_peer(peer_ip, peer_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((peer_ip, peer_port))
    return s

def handshake(info_hash, peer_id):
    pstrlen = 19
    pstr = b'BitTorrent protocol'
    reserved = b'\x00' * 8
    return struct.pack('>B19s8s20s20s', pstrlen, pstr, reserved, info_hash, peer_id)


def request_piece(index, begin, length):
    message_id = 6  # 'request' message ID
    return struct.pack('>IBIII', length + 9, message_id, index, begin, length)

def receive_piece(s, index, begin, length):
    s.send(request_piece(index, begin, length))
    response = s.recv(length + 13)  # Length prefix (4) + message ID (1) + index (4) + begin (4)
    piece_data = response[13:]
    return piece_data


def download_file(torrent_path, download_path):
    announce_url, file_name, file_length, piece_length, hash_value, info = BDecoder(file_path = torrent_path)
    info_hash = hashlib.sha1(bencodepy.encode(hash_value)).digest()
    peer_id = generate_peer_id().encode()
    
    tracker_response = get_tracker_peers(announce_url, info_hash, peer_id, port=6881, left=file_length)
    peers = tracker_response[b'peers']
    
    if isinstance(peers, list):  # Single compact response
        for i in range(0, len(peers), 6):
            peer_ip = '.'.join(str(peers[i + j]) for j in range(4))
            peer_port = peers[i + 4] * 256 + peers[i + 5]
            s = connect_to_peer(peer_ip, peer_port)
            s.send(handshake(info_hash, peer_id))
            response = s.recv(68)  # Read handshake response
            print(response)
            # Request and receive a piece
            piece_index = 0
            begin = 0
            length = piece_length
            piece_data = receive_piece(s, piece_index, begin, length)
            print(f"Received piece data: {piece_data[:20]}...")
            # Write the piece data to a file
            with open(download_path, 'wb') as file:
                file.write(piece_data)
            s.close()
            break  # Just download from the first peer for simplicity


peer_ip = '127.0.0.1'  # Replace with actual peer IP from tracker response
peer_port = 6881        # Replace with actual peer port from tracker response



def contact(peer_ip, peer_port, info_hash, peer_id):
    #! peer_id is the id of the BitTorrent client
    s = connect_to_peer(peer_ip, peer_port)
    s.send(handshake(info_hash, peer_id))
    # Read handshake response
    response = s.recv(68)
    print(response)





