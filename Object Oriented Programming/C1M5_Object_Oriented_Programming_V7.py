import random

class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections = {}

    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        connection_load = random.random()*10+1
        self.connections[connection_id] = connection_load

    def close_connection(self, connection_id):
        """Closes a connection on this server."""
        if connection_id in self.connections.keys():
            self.connections.pop(connection_id)

    def load(self):
        """Calculates the current load for all connections."""
        total = 0
        for connection in self.connections.values():
            total += connection
        return total

    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())
    
server = Server()
server.add_connection("192.168.1.1")

print(server.load())
server.close_connection("192.168.1.1")
print(server.load())

class LoadBalancing:
    def __init__(self):
        """Initialize the load balancing system with one server"""
        self.connections = {}
        self.servers = [Server()]

    def add_connection(self, connection_id):
        """Randomly selects a server and adds a connection to it."""
        server = random.choice(self.servers)
        self.connections[connection_id] = server
        server.add_connection(connection_id)
        self.ensure_availability()

    def close_connection(self, connection_id):
        """Closes the connection on the the server corresponding to connection_id."""
        
        for connection in self.connections.keys():
            if connection == connection_id:
                server_ = self.connections[connection]
        server_.close_connection(connection_id)
        del self.connections[connection_id]       

    def avg_load(self):
        """Calculates the average load of all servers"""
        result = 0
        count = 0
        
        for server in self.servers:
            result += server.load()
            count += 1
        return result/count

    def ensure_availability(self):
        """If the average load is higher than 50, spin up a new server"""
        if self.avg_load() >= 50:
            self.servers.append(Server())

    def __str__(self):
        """Returns a string with the load for each server."""
        loads = [str(server) for server in self.servers]
        return "[{}]".format(",".join(loads))

l = LoadBalancing()
l.add_connection("fdca:83d2::f20d")
print(l.avg_load())

l.servers.append(Server())
print(l.avg_load())

l.close_connection("fdca:83d2::f20d")
print(l.avg_load())

for connection in range(20):
    l.add_connection(connection)
print(l)

print(l.avg_load())