import socket
import subprocess
import concurrent.futures


class NetworkScanner:


    def get_local_ip(self):

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            s.connect(("8.8.8.8", 80))

            ip = s.getsockname()[0]

            s.close()

            return ip

        except:

            return None



    def ping(self, ip):

        try:

            result = subprocess.call(
                [
                    "ping",
                    "-c",
                    "1",
                    "-W",
                    "1",
                    ip
                ],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )


            if result == 0:

                try:

                    name = socket.gethostbyaddr(ip)[0]

                except:

                    name = "Unknown"


                return {

                    "name": name,

                    "ip": ip

                }


        except:

            pass


        return None



    def scan(self):

        local_ip = self.get_local_ip()


        if not local_ip:

            return []



        network = ".".join(
            local_ip.split(".")[:3]
        )


        devices = []



        with concurrent.futures.ThreadPoolExecutor(
            max_workers=40
        ) as executor:


            results = executor.map(
                self.ping,
                [
                    f"{network}.{i}"
                    for i in range(1,255)
                ]
            )


            for item in results:

                if item:

                    devices.append(item)



        return devices