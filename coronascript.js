function calculate()
{
	
	convertStringsToNums();
	let county_num = document.querySelector("#county").value;
	
	let gender = document.querySelector("#gender").value;
	
	//gender population
	let female_pop = astatic_data[county_num][1] * astatic_data[county_num][0];
	let male_pop = astatic_data[county_num][0] - female_pop;
	
	let calculated_pops = [male_pop, female_pop, astatic_data[county_num][0]];
	let calculated_infected = [updated_data[county_num][1] * 0.638, updated_data[county_num][1] * 0.362, updated_data[county_num][1]];

	let prob_i = calculated_infected[gender] / calculated_pops[gender]

	//let prob_i = updated_data[county_num][1] / astatic_data[county_num][0]; 	
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






/**let age = document.querySelector("#age").value;
    let health = document.querySelector("#health").value;

    console.log(state,age,health);

    if ((state === 'ME') && (age == 2) && (health == 1))
    {
        document.querySelector('#p_infected').innerHTML = '100%';
        document.querySelector('#p_dying').innerHTML = '100%';
    }
    else
    {
        document.querySelector('#p_infected').innerHTML = 'NA';
        document.querySelector('#p_dying').innerHTML = 'NA';
    }
**/
}

function convertStringsToNums()
{
	for(let i = 0; i < updated_data.length; i++)
	{
		updated_data[i][1] = parseInt(updated_data[i][1]);
		updated_data[i][2] = parseInt(updated_data[i][2]);
	}

}
