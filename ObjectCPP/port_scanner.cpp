class PortScanner
{
public:
	PortScanner(const std::string& target) : target(target) {};

	void scanTCP(int start, int end)
	{
		for (int port = start; port <= end; port++)
		{
			if (isTCPPortOpen(port))
			{
				std::cout << "Port " << port << " is open" << std::endl;
			}
		}
	}

private: 
	std::string target;
	bool isTCPPortOpen(int port)
	{
		struct sockaddr_in address;
		int sock = 0;
		struct timeval timeout;
		timeout.tv_sec = 1;
		timeout.tv_usec = 0;
		address.sin_family = AF_INET;
		address.sin_port = htons(port);
		inet_pton(AF_INET, target.c_str(), &address.sin_addr);
		sock = socket(AF_INET, SOCK_STREAM, 0);
		if (sock < 0)
		{
			std::cerr << "Socket creation error" << std::endl;
			return false;
		}
		setsockopt(sock, SOL_SOCKET, SO_RCVTIMEO, (char*)&timeout, sizeof(timeout));
		if (connect(sock, (struct sockaddr*)&address, sizeof(address)) < 0)
		{
			close(sock);
			return false;
		}
		close(sock);
		return true;
	}	
}