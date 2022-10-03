# | 1 byte (#username) | username | 2 byte (#message) | message

class Packet:
    def __init__(self, username, message):
        self.username = username
        self.message = message

    # CONVERTE OGGETTO IN BYTES
    def to_bytes(self):

        # USERNAME
        username_bytes = self.username.encode()
        buffer = len(username_bytes).to_bytes(1, 'big')
        buffer = buffer + username_bytes

        # MESSAGE
        message_bytes = self.message.encode()
        buffer = len(message_bytes).to_bytes(2, 'big')
        buffer = buffer + message_bytes
        
        return buffer

    @staticmethod
    def from_Bytes(buffer):
        # USERNAME
        username_size = int.from_bytes(buffer[0:1], 'big')
        username = buffer[1:username_size + 1].decode()

        # MESSAGE
        message_size = int.from_bytes(buffer[username_size + 1: username_size + 3], 'big')
        message = buffer[username_size + 3:username_size + 3 + message_size].decode()

        return Packet(username, message)


def main():
    # TEST UNITARI
    ut1 = Packet("Mario", "Hello world")
    pkt = Packet.from_Bytes(ut1.to_bytes())

    assert(ut1.message == pkt.message)
    assert(ut1.username == pkt.username)

if __name__ == "__main__":
    main()