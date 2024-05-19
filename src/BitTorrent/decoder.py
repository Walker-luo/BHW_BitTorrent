import bencodepy


#! This module is uesd to change bencode in .torrent file to python dict

def BDecoder(file_path):
    # Read and decode the .torrent file
    with open(file_path, "rb") as file:
        encoded_data = file.read()
        torrent = bencodepy.decode(encoded_data)

    # Print the decoded torrent file content
    print("Decoded .torrent file content:")
    print(torrent)

    # Access specific elements (if needed)
    announce_url= torrent[b'announce'].decode()
    info = torrent[b'info']
    file_length = info[b'length']
    file_name = info[b'name'].decode()
    piece_length = info[b'piece length']
    hash_value = info[b'pieces']
    
    return announce_url, file_name, file_length, piece_length, hash_value, info #! info need?

if __name__ == "__main__":
    # Define the path to the .torrent file
    file_path = '../test.torrent'
    torrent = BDecoder(file_path)

    print("\nTorrent Details:")
    print(f"Announce URL: {torrent[0]}")
    print(f"File Name: {torrent[1]}")
    print(f"File Length: {torrent[2]} bytes")
    print(f"Piece Length: {torrent[3]} bytes")
    print(f"hash value: {torrent[4]}")




