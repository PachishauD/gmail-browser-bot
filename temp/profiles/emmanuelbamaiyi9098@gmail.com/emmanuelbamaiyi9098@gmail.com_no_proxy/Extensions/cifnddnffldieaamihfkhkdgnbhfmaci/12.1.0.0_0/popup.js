
// var message = chrome.i18n.getMessage("@@ui_locale");//en_US
// alert(message);
// message = chrome.i18n.getMessage("@@extension_id");//id
// alert(message);
// message = chrome.i18n.getMessage("@@bidi_dir");//ltr
// alert(message);
// message = chrome.i18n.getMessage("@@bidi_start_edge");//left
// alert(message);
// message = window.navigator.language;//en-US
// alert(message);
// function getAcceptLanguages() {
  // chrome.i18n.getAcceptLanguages(function(languageList) {
    // var languages = languageList.join(",");
    // alert(languages);
  // })
// }
// getAcceptLanguages();

const channel = new BroadcastChannel('PopuBackGroundChannel');

channel.onmessage = (msg) => {
	if(msg.data.name == 'GetStatus')
	{
		if(msg.data.value == 1)
		{
			window.close();
		}
	}
	else if (msg.data.name = 'GetVivewResult')
	{
		document.getElementById("ViewPDFResultsCheckbox").checked = (msg.data.value == 1);
		document.getElementById("ViewResults").value = msg.data.value;
	}
}
channel.postMessage({name:'GetStatus'});
channel.postMessage({name:'GetVivewResult'});

function ConvertToPDFPopupMenu() {
	channel.postMessage({name:'ConvertToPDFPopupMenu'});
	window.close();	
}

function AppendToExistingPDFPopupMenu() {
	channel.postMessage({name:'AppendToExistingPDFPopupMenu'});
	window.close();
}

function CreateAndEmailPopupMenu() {
	channel.postMessage({name:'CreateAndEmailPopupMenu'});
	window.close();
}

function ToggleViewResultCheckbox() {
	var bViewPDF = document.getElementById("ViewResults").value;
	//alert((bViewPDF == 1) ? "0" : "1");
	channel.postMessage({name:'ToggleViewResultCheckbox', value:!(bViewPDF == 1)});
	window.close();
}

function GetViewResultCheckbox() {
	return document.getElementById("ViewResults").value;
}


function ShowPreferencesDialog() {
	channel.postMessage({name:'ShowPreferencesDialog'});
	window.close();
}

document.getElementById("ConvertToFoxitPDF").addEventListener('click', ConvertToPDFPopupMenu);
document.getElementById("AppendToExistingPDF").addEventListener('click', AppendToExistingPDFPopupMenu);
document.getElementById("CreateAndEmail").addEventListener('click', CreateAndEmailPopupMenu);
document.getElementById("ViewPDFResults").addEventListener('click', ToggleViewResultCheckbox);
document.getElementById("Preferences").addEventListener('click', ShowPreferencesDialog);

document.getElementById("ConvertToFoxitPDFText").innerText = chrome.i18n.getMessage("ConvertToFoxitPDF");
document.getElementById("AppendToExistingPDFText").innerText = chrome.i18n.getMessage("AppendToExistingPDF");
document.getElementById("CreateAndEmailText").innerText = chrome.i18n.getMessage("CreateAndEmail");
document.getElementById("ViewPDFResultsText").innerText = chrome.i18n.getMessage("ViewPDFResults");
document.getElementById("PreferencesText").innerText = chrome.i18n.getMessage("Preferences");


