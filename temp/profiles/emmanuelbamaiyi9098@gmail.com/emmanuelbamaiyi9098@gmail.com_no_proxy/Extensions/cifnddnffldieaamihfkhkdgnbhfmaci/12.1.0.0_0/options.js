
var bgPage = chrome.extension.getBackgroundPage();
var g_bUninstallSuccess = false;
function Uninstall() {
	if (confirm(chrome.i18n.getMessage("UninstallSureTip")))
	{
		var method = new Object();
		if (g_bUninstallSuccess)
		{
			method.methodname = g_Method_Install;
		}
		else
		{
			method.methodname = g_Method_Uninstall;
		}
		bgPage.invoke(method);
		
		chrome.extension.onRequest.addListener(
		function(request, sender, sendResponse) {
			//alert(JSON.stringify(request));
			if (request.message == "UninstallSuccess")
			{
				//alert(request.message);
				//alert(request.Parameters.bUninstallSuccess);
				var bUninstallSuccess = request.Parameters.bUninstallSuccess;
				if (bUninstallSuccess)
				{
					g_bUninstallSuccess = true;
					document.getElementById("Uninstall").style.visibility="hidden";
					document.getElementById("Uninstall").innerText = chrome.i18n.getMessage("Reinstall");
					document.getElementById("Tip").innerText = chrome.i18n.getMessage("UninstallSuccessTip");
				}
			}
			else if (request.message == "InstallSuccess")
			{
				var bInstallSuccess = request.Parameters.bInstallSuccess;
				if (bInstallSuccess)
				{
					g_bUninstallSuccess = false;
					//document.getElementById("Uninstall").style.visibility="visible";
					document.getElementById("Uninstall").innerText = chrome.i18n.getMessage("Uninstall");
					document.getElementById("Tip").innerText = chrome.i18n.getMessage("UninstallTip");
				}
			}
			
			sendResponse('');
		});
	}
}

document.getElementById("Uninstall").addEventListener('click', Uninstall);

document.getElementById("Uninstall").innerText = chrome.i18n.getMessage("Uninstall");
document.getElementById("Tip").innerText = chrome.i18n.getMessage("UninstallTip");
document.title = chrome.i18n.getMessage("OptionsTitle");