let date = new Date();
let c_month = date.getMonth() + 1;
let c_month_day = date.getDate();
let c_year = date.getFullYear();
let user_events_obj = {};
let months = ["January","February","March","April","May","June","July",
            "August","September","October","November","December"];

//put hour tags 
for(let i=0;i<24;i++){
	let time = i.toString().padStart(2,'0')+":"+"00";
	$("#day-gantt").append("<div class=\"time-slot\" id="+time+"><h>"+time+"</h></div>");
}

eel.get_stats(c_year, c_month)(ret => populate_calendar_data("#week-rows",ret));

//-=-=+__++__+=-_++__++__++__++_-==-_++_-==-_++_

function populate_calendar_data(dom_id, calendar_data){
	let days_list = calendar_data.days;
	let user_events = calendar_data.user_events;
	let idx = 0;
	let weeks = $(dom_id).children().toArray(); 
	for(week of weeks){
		let days = week.children;
		for(day of days){
			day.firstElementChild.textContent = days_list[idx][2];
			day.addEventListener("click", display_day_panel);
			day.setAttribute("id",days_list[idx] + "");
			day.addEventListener("click", function(){this_day = this.id.split(",")[2];eel.package_events_array_for_js(c_year,c_month,parseInt(this_day))(ret => draw_gannt(ret,this_day))})
			if(days_list[idx][1] < c_month){
				day.classList.add("prev_month");
			}
			if(days_list[idx][1] > c_month){
				day.classList.add("next_month");
			}
			if(days_list[idx][0] == c_year && days_list[idx][1] == c_month && days_list[idx][2]==c_month_day){
				day.classList.add("today");
			}
			let l = user_events[days_list[idx]+""]
			if( l > 0){
				let node = document.createElement("DIV");
				let text_node = document.createTextNode(l);
				node.appendChild(text_node);
				day.children[1].appendChild(node);
			}
			idx = idx+1;
		}
	}
	user_events_obj = user_events; 
}

function display_day_panel(){
	$("#day-side-panel").css("width","500px");
	$("#big-trans-back-button").css("visibility","visible")
	$("#big-trans-back-button").click(hide_day_panel);
	$("#main").css("filter","blur(0.5em)");
	update_date_info(this.id);
}

function hide_day_panel(){
	$("#day-side-panel").css("width","0px");
	$("#big-trans-back-button").off("click", hide_day_panel);
	$("#big-trans-back-button").css("visibility","hidden");
	$("#main").css("filter","none");
}

function update_date_info(date){
	x = date.split(",");
	$("#day-date-info").children()[0].textContent = x[2];
	$("#day-date-info").children()[1].firstElementChild.textContent = months[x[1]-1];
	$("#day-date-info").children()[1].lastElementChild.textContent = x[0];
}

function draw_gannt(array, day_iq){
	x_offset = 80;
	slot_offset = 40;
	svg = $("#day-svg");
	svg.html("");
	for(slot of array){
		for(evnt of slot){
			x = x_offset;
			y1 = evnt[4][2] < day_iq ?0    :evnt[4][3] * 60 + evnt[4][4]
			y2 = evnt[5][2] > day_iq ?60*24:evnt[5][3] * 60 + evnt[5][4]
			svg.append("<line onmouseover=\"mouseIN_event(this)\" class=\"event_id_"+ evnt[0] + "\" x1="+x+" y1="+y1+" x2="+x+" y2="+y2+" stroke-linecap=\"round\" style=\"stroke:#b50b05;stroke-width:7;\"/>");
			svg.append("<circle class=\"event_id_"+ evnt[0] +"\" cx="+x+" cy="+y1+" r=\"8\"fill=\"#b50b05\" on/>");
		}
		x_offset = x_offset + slot_offset;
	}
	svg.html(svg.html());

}

function mouseIN_event(svg){
	//find all elements of this class
	let evnt_class = svg.className.baseVal;
	let elems = document.getElementsByClassName(evnt_class);
	console.log(evnt_class)
	for(elem of elems){
		elem.style.stroke = "white";
	}
}

function display_event_panel(){
	
}








