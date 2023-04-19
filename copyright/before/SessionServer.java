package org.tain.async;

import java.net.InetSocketAddress;
import java.net.ServerSocket;
import java.net.Socket;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Component;
import org.tain.infos.SessionInfo;
import org.tain.utils.PropertiesUtil;

import lombok.extern.slf4j.Slf4j;

@Component
@Slf4j
public class SessionServer {

	@Autowired
	private AsyncCloser asyncCloser;
	
	@Autowired
	private AsyncReceiver asyncReceiver;
	
	@Autowired
	private AsyncSender asyncSender;
	
	@Async(value = "async_SessionServer.starter")
	public void starter() throws Exception {
		System.out.println(">>>>> SessionServer.starter....");
		
		@SuppressWarnings("resource")
		ServerSocket serverSocket = new ServerSocket();
		
		String host = PropertiesUtil.get(this.getClass().getName(), "host.ip");
		int port = Integer.parseInt(PropertiesUtil.get(this.getClass().getName(), "host.port"));
		serverSocket.bind(new InetSocketAddress(host, port));
		
		int idx = 1;
		while (Boolean.TRUE) {
			log.info("SERVER : Connect Ready: " + host + ", " + port);
			System.out.println(">>>>> SERVER : Connect Ready: " + host + ", " + port);
			Socket socket = serverSocket.accept();  // blocking
			
			SessionInfo sessionInfo = new SessionInfo(String.format("SESSION-%03d", idx++));
			sessionInfo.setHostIp(host);
			sessionInfo.setHostPort(port);
			sessionInfo.setSocket(socket);
//			sessionInfo.setTransactionQueue(new TransactionQueue());
			
			asyncCloser.processing(sessionInfo);
			asyncReceiver.processing(sessionInfo);
			asyncSender.processing(sessionInfo);
		}
	}
}