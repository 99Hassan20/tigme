console.log("ready");  

function send_request()
{
	fetch('http://localhost:5000/sleep')
		.then(res => console.log(res))
		.then(error => console.log(error));
}

// let div = document.querySelectorAll(".shop-item")[1];
// div.remove();
let buttons = document.querySelectorAll(".btn-primary");




for (let i = 0; i < buttons.length; i++)
{
	if (buttons[i].disabled == false)
		buttons[i].addEventListener("click", () => {
			console.log("oooops, clicked\n");
			send_request();
		});
//	buttons[i].remove();
}
