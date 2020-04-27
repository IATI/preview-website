/*======================================
	Show messages
*/

export default function setupMessages() {

	function setCookie (key, value) {
		document.cookie = key + '=' + value + ';expires=0;path=/';
	}

	function getCookie (key) {
		var keyValue = document.cookie.match('(^|;) ?' + key + '=([^;]*)(;|$)');
		return keyValue ? keyValue[2] : null;
	}

	// Check cookie
	var alert_cookie = getCookie('alert_cookie');
	// alert(getCookie('alert_cookie'));
	if(alert_cookie != 1){
		// $('#message__wrapper').slideDown(300);
		$('#message__wrapper').css('display', 'block');
	}

	$('#message__close').on('click', function(e) {
		e.preventDefault();
		$('#message__wrapper').slideUp(300, function(){
			$(this).remove();
		});
		setCookie('alert_cookie',1);
	});
};