let x = 0;

function inc()
{
  x++;
  console.log(x);
}
let narutopic = "https://vignette.wikia.nocookie.net/naruto/images/d/dd/Naruto_Uzumaki%21%21.png/revision/latest?cb=20161013233552";
let blackholepic = "https://static01.nyt.com/images/2019/04/10/science/event-horizon-black-hole-images-1554901170942/event-horizon-black-hole-images-1554901170942-articleLarge-v2.jpg"
function changePic()
{
  s = document.getElementById('pic').src;
  if (s == blackholepic)
  {
    document.getElementById('pic').src = narutopic;
  }
  else
  {
    document.getElementById('pic').src = blackholepic;
  }
}
