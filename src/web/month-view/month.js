let date = new Date();
let month = date.getMonth() + 1;
let month_day = date.getDate();
let year = date.getYear();
let user_events_obj = {};
eel.get_stats()(ret => populate_calendar_data("#week-rows",ret));


function populate_calendar_data(dom_id, calendar_data){
	let days_list = calendar_data.days;
	let user_events = calendar_data.user_events;
	let idx = 0;
	let weeks = $(dom_id).children().toArray(); 
	console.log(user_events)
	for(week of weeks){
		let days = week.children;
		for(day of days){
			day.firstElementChild.textContent = days_list[idx][2]; 
			day.addEventListener("click", display_day_panel);
			day.setAttribute("id",days_list[idx] + "");
			if(days_list[idx][1] < month){
				day.classList.add("prev_month");
			}
			if(days_list[idx][1] > month){
				day.classList.add("next_month");
			}
			if(days_list[idx][0] == month_day && days_list[idx][1] == month){
				day.classList.add("today");
			}
			console.log(days_list[idx]+"");
			console.log(user_events[days_list[idx]+""]);
			//if( l > 0){
			//	let node = document.createElement("DIV");
			//	let text_node = document.createTextNode(l);
			//	node.appendChild(text_node);
			//	day.children[1].appendChild(node);
			//}
			idx = idx+1;
		}
	}
	user_events_obj = user_events; 
}

function display_day_panel(){
	$("#day-side-panel").css("width","600px");
	$("#day-date-info").children()[0].textContent = this.firstElementChild.textContent;
	$("#big-trans-back-button").css("visibility","visible")
	$("#big-trans-back-button").click(hide_day_panel);
	$("#main").css("filter","blur(0.5em)");
}

function hide_day_panel(){
	$("#day-side-panel").css("width","0px");
	$("#big-trans-back-button").off("click", hide_day_panel);
	$("#big-trans-back-button").css("visibility","hidden");
	$("#main").css("filter","none");
}













