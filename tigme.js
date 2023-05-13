console.log("ready");  
let div = document.querySelectorAll(".shop-item")[1];
div.remove();
let buttons = document.querySelectorAll(".btn-primary");
for (let i = 0; i < buttons.length; i++)
{
	if (buttons[i].disabled == false)
		buttons[i].disabled = true;
	buttons[i].remove();
}
