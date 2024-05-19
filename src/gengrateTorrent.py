import os
import hashlib
import bencodepy

def generate_torrent(file_path, announce_url, piece_length=256*1024):
    # Read file contents
    with open(file_path, 'rb') as f:
        file_data = f.read()

    # Calculate SHA1 hash of file
    file_hash = hashlib.sha1(file_data).digest()

    # Calculate total file size
    file_size = os.path.getsize(file_path)

    # Calculate total number of pieces
    num_pieces = (file_size + piece_length - 1) // piece_length

    # Calculate piece hashes
    piece_hashes = [hashlib.sha1(file_data[i*piece_length:(i+1)*piece_length]).digest()
                    for i in range(num_pieces)]

    # Construct torrent dictionary
    torrent_data = {
        'announce': announce_url,
        'info': {
            'length': file_size,
            'name': os.path.basename(file_path),
            'piece length': piece_length,
            'pieces': b''.join(piece_hashes),
            'sha1': file_hash
        }
    }

    # Encode torrent data using bencode
    torrent_file = bencodepy.encode(torrent_data)

    return torrent_file

if __name__ == "__main__":
    # Example usage
    file_path = './test.txt'
    announce_url = 'http://tracker.example.com:8080/announce'
    torrent_data = generate_torrent(file_path, announce_url)

    # Write torrent data to file
    with open('test.torrent', 'wb') as f:
        f.write(torrent_data)
