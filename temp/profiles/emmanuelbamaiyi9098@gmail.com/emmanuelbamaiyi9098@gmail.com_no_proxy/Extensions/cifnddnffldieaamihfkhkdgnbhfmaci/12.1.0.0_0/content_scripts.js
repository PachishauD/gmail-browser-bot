let port;
function connect() {
	port = chrome.runtime.connect({name: 'foxitconnect'});
	port.onDisconnect.addListener(connect);
}
connect();

// document.onmousemove = function(evt){
               // chrome.tabs.sendMessage(-1, {cmd: "ToggleSwitch"},function(response) {});
            // };   
//chrome.extension.sendMessage({cmd: "InitPage"},function(response) {});

//设置或获取对象指定的文件名或路径。
//alert(window.location.pathname)

 
//设置或获取整个 URL 为字符串。
//alert(window.location.href);

//设置或获取与 URL 关联的端口号码。
//alert(window.location.port)

 
//设置或获取 URL 的协议部分。
//alert(window.location.protocol)

 
//设置或获取 href 属性中在井号“#”后面的分段。
//alert(window.location.hash)

 
//设置或获取 location 或 URL 的 hostname 和 port 号码。
//alert(window.location.host)

 
//设置或获取 href 属性中跟在问号后面的部分。
//alert(window.location.search)
