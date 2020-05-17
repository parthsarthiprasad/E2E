import socket
import cv2
import struct
import pickle

class Pred:
    def __init__(self,HOST="127.0.0.1",PORT=6666):
        self.HOST = HOST
        self.PORT = PORT
        self.out_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.out_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.out_sock.connect((HOST,PORT))
        self.encode_params = [int(cv2.IMWRITE_JPEG_QUALITY),90]
        
    def send_frame(self,frame):
        result, image_encode = cv2.imencode(".jpg",frame,self.encode_params)
        data = pickle.dumps(image_encode,0)
        self.out_sock.sendall(struct.pack("L", len(data))+data)
        return True
        
    def recv_frame(self):
        self.in_sock.bind(('',self.PORT))
        self.in_sock.listen(10)
        print('Socket now listening')
        self.conn, self.addr=self.in_sock.accept()
        data = b""
        payload_size = struct.calcsize("L")
        print("payload_size: {}".format(payload_size))
        while len(data) < payload_size:
            data += self.conn.recv(4096)
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("L", packed_msg_size)[0]
        while len(data) < msg_size:
            data += self.conn.recv(4096)

        frame_data = data[:msg_size]
        data = data[msg_size:]
        new_frame = pickle.loads(frame_data, fix_imports=True, encoding="bytes")
        new_frame = cv2.imdecode(new_frame, cv2.IMREAD_COLOR)
        new_frame = cv2.cvtColor(new_frame, cv2.COLOR_BGR2RGB)
        return new_frame
        
    def get_pred(self,frame):
        chk = False
        while not(chk):
            self.send_frame(frame)
        new_frame = self.recv_frame()
        return new_frame