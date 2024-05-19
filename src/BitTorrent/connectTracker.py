import requests
import hashlib
import random
import bencodepy


def get_tracker_peers(announce_url, info_hash, peer_id, port, uploaded=0, downloaded=0, left=0):
    params = {
        'info_hash': info_hash,
        'peer_id': peer_id,
        'port': port,
        'uploaded': uploaded, #alreay上传的总字节数
        'downloaded': downloaded, #already下载的总字节数
        'left': left, # 客户端要下载的剩余字节数
        'compact': 1, #客户端是否接受一个压缩的对等点列表
 
    }
    response = requests.get(announce_url, params=params)
    tracker_response = bencodepy.decode(response.content)
    return tracker_response

def generate_peer_id():
    #! -PC0001- + 12 random numbers
    return '-PC0001-' + ''.join([str(random.randint(0, 9)) for _ in range(12)])

def connectTracker(announce_url, total_length, hash_value, port = 6881):

    # port = 6881  Default BitTorrent port
    info_hash = hashlib.sha1(bencodepy.encode(hash_value)).digest()
    peer_id = generate_peer_id().encode()
    tracker_response = get_tracker_peers(announce_url, info_hash, peer_id, port, left=total_length) # total_length = file_length when downloaded = 0
    print(tracker_response)
