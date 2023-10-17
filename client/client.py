import socket, time, sys
while True:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('talkto',2000))
	msg = 'Hello, world\n'
	s.send(msg.encode())
	data = s.recv(1024)
	print('Received:', data)
	sys.stdout.flush()
	s.close()
	time.sleep(5)
