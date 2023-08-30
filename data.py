import subprocess

class Data:
    def __init__(self, list_interfaces: list[str]):
        self.ip_dict: dict = {}
        self.list_interfaces: list[str] = list_interfaces
        self._update()

    def _get_ip(self, interface):
        try:
            ip_result = subprocess.check_output(["ip", "addr", "show", "dev", interface])
            ip_result = ip_result.decode("utf-8")
            ip_lines = ip_result.split("\n")
            for line in ip_lines:
                if "inet " in line:
                    ip = line.split("inet ")[1].split("/")[0]
                    return ip
            return "N/A"
        except subprocess.CalledProcessError:
            return "N/A"

    def get_all(self):
        return self.ip_dict

    def _discover_docker_containers(self):
        try:
            docker_info = subprocess.check_output(["docker", "ps", "--format", "{{.Names}};{{.Networks}}"])
            docker_info = docker_info.decode("utf-8")
            docker_lines = docker_info.split("\n")
            for line in docker_lines:
                if line:
                    name, network_info = line.split(";")
                    network_info = json.loads(network_info)
                    for network_name, network_data in network_info.items():
                        if "IPAddress" in network_data:
                            ip = network_data["IPAddress"]
                            self.interfaces.append(name)
                            self.ip_dict[name] = ip
        except subprocess.CalledProcessError:
            pass

    def _update(self):
        for interface in self.list_interfaces:
            ip = self._get_ip(interface)
            self.ip_dict[interface] = ip

