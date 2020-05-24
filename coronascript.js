function calculate()
{
	//convert the strings of numbers to integer numbers
	convertStringsToNums();
	
	//get an array with probabilities for each gender in the county pop
	let gender_probs = getGenderProbs();

	//get county, age, and gender data
	let county_num = document.querySelector("#county").value;
	let gender = document.querySelector("#gender").value;
	let age = document.querySelector("#age").value;

	//have array of gender probabilities according to corona study
	//goes male, female, total
	gender_probs_i = [0.638, 0.362, 1];

	//get total population of county
	let tcpop = astatic_data[county_num][0];

	//get the number of infected that belong to the selected demographic
	let dpop_i = updated_data[county_num][1] * gender_probs_i[gender] * corona_age_data[age];

	//get the number of people in the county that belong to the selected demographic
	let dpop = tcpop * gender_probs[county_num][gender] * county_age_data[age];

	//the probability of being infected is the infected selected demographic pop over total demographic pop
	let prob_i = dpop_i / dpop;

	document.querySelector('#p_infected').innerHTML = prob_i*100 + "%";
	
	let prob_d = prob_i * (updated_data[county_num][2]/updated_data[county_num][1]);
	if (prob_d == 0)
	{
		document.querySelector('#p_dying').innerHTML = prob_d*100 + "%" + " (no deaths currently recorded in selected county)";
	}
	else
	{
		document.querySelector('#p_dying').innerHTML = prob_d*100 + "%";
	}
}


//function that returns array of probabilities of gender for each county
function getGenderProbs()
{
	let p_arr = [];
	for(let i = 0; i < 16; i++)
	{
		p_arr.push([]);
		p_arr[i][0] = 1 - astatic_data[i][1];
		p_arr[i][1] = astatic_data[i][1];
		p_arr[i][2] = 1;
	}
	
	return p_arr;
}

function convertStringsToNums()
{
	for(let i = 0; i < updated_data.length; i++)
	{
		updated_data[i][1] = parseInt(updated_data[i][1]);
		updated_data[i][2] = parseInt(updated_data[i][2]);
	}

}

function updateDate()
{
	let updated_date = date;
	document.getElementById("date").innerHTML = "Data updated as of:  " + "<b>" + updated_date + "</b>";
}
