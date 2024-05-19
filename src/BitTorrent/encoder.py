import bencodepy

#! This module is uesd to change python dict to bencode and save in .torrent file


# Define the torrent file structure
torrent = {
    'announce': 'http://example-tracker.com/announce',
    'info': {
        'length': 1024,
        'name': 'example.txt',
        'piece length': 256,
        'pieces': b'0123456789abcdef0123456789abcdef'
    }
}

# Encode the dictionary to Bencoded format
encoded_torrent = bencodepy.encode(torrent)
print(encoded_torrent)

# Write the encoded data to a .torrent file
with open('./torrentFiles/example.torrent', 'wb') as file:
    file.write(encoded_torrent)

print("example.torrent file created successfully.")
