import socket

url_host    = 'httpbin.org'
url_image   = '/image/png'

url_request = f'GET {url_image} HTTP/1.1\r\nHOST: {url_host}\r\n\r\n' 
host_port   = 80
buffer_size = 10240

sock_img = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_img.connect((url_host, host_port))
sock_img.sendall(url_request.encode())

print('\nBaixando a imagem...')
# Montado a variável que armazenará os dados de retorno
data_ret = ''.encode()
while True:
    data = sock_img.recv(buffer_size)
    if not data: break
    data_ret += data

# Obtendo o tamanho da imagem
img_size = -1
tmp = data_ret.split('\r\n'.encode())
for line in tmp:
   if 'Content-Length:'.encode() in line:
      img_size = int(line.split()[1])
      break
print(f'\nTamanho da Imagem: {img_size} bytes')

# Separando o Cabeçalho dos Dados
delimiter = '\r\n\r\n'.encode()
position  = data_ret.find(delimiter)
headers   = data_ret[:position]
image     = data_ret[position+4:]

# Salvando a imagem
file_output = open('image.png', 'wb')
file_output.write(image)
file_output.close()
