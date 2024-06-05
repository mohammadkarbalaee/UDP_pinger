import time
import socket

server_address = ('localhost', 12000)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(1)  

rtt_list = []
packet_loss_count = 0

for i in range(10):
    send_time = time.time()
    message = f'ping {i+1}'
    
    try:
        client_socket.sendto(message.encode(), server_address)
        
        response, server = client_socket.recvfrom(1024)
        receive_time = time.time()
        
        rtt = receive_time - send_time
        rtt_list.append(rtt)
        
        print(f'Ping {i+1} response: {response.decode()}')
        print(f'RTT: {rtt:.4f} seconds')
    except socket.timeout:
        print(f'Ping {i+1} request timed out')
        packet_loss_count += 1

if rtt_list:
    min_rtt = min(rtt_list)
    max_rtt = max(rtt_list)
    avg_rtt = sum(rtt_list) / len(rtt_list)
    print(f'\nMinimum RTT: {min_rtt:.4f} seconds')
    print(f'Maximum RTT: {max_rtt:.4f} seconds')
    print(f'Average RTT: {avg_rtt:.4f} seconds')
else:
    print('\nNo successful pings to calculate RTTs.')

packet_loss_rate = (packet_loss_count / 10) * 100
print(f'Packet loss rate: {packet_loss_rate:.2f}%')

client_socket.close()
