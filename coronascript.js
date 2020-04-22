function calculate()
{
    let state = document.querySelector("#state").value;
    let age = document.querySelector("#age").value;
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
}