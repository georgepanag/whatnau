let days_list = eel.get_month_days()(ret => populate_calendar_nums("#week-rows",ret));

function populate_calendar_nums(dom_id, days_obj){
	let month = days_obj.month;
	let today = days_obj.day;
	let days_list = days_obj.days_list;
	let idx = 0;
	let weeks = $(dom_id).children().toArray(); 
	for(week of weeks){
		let days = week.children;
		for(day of days){
			day.firstElementChild.textContent = days_list[idx][0]; 
			if(days_list[idx][1] != month){
				day.style.backgroundColor = "#b9c9c8";
				day.style.color = "white";
			}
			if(days_list[idx][0] == today && days_list[idx][1] == month){
				day.firstElementChild.style.color = "#0088ff";
			}
			idx = idx+1;
		}
	}
}
