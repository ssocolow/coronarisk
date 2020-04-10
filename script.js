let x = 0;

function inc()
{
  x++;
  console.log(x);
}

function changePic()
{
  s = document.getElementById('pic').src;
  if (s == "file:///C:/Users/Simon%20Socolow/Desktop/website/blackhole.jpg")
  {
    document.getElementById('pic').src = "file:///C:/Users/Simon%20Socolow/Desktop/website/naruto.jpg";
  }
  else
  {
    document.getElementById('pic').src = "file:///C:/Users/Simon%20Socolow/Desktop/website/blackhole.jpg";
  }
}
