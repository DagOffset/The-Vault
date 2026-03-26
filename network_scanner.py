import os

def ping_sweep(base_ip):
    print(f"[*] Starting reconnaissance on: {base_ip}.x")
    for i in range(1, 255):
        ip = f"{base_ip}.{i}"
        # Comando silenzioso per testare la presenza di un dispositivo
        response = os.system(f"ping -n 1 -w 100 {ip} > nul" if os.name == 'nt' else f"ping -c 1 -w 1 {ip} > /dev/null")
        
        if response == 0:
            print(f"[+] Device detected at: {ip}")

if __name__ == "__main__":
    # Cambia questo con la tua sottorete locale (es. 192.168.1)
    target = "192.168.1" 
    ping_sweep(target)
