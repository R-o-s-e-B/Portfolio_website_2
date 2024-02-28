
const root = document.documentElement;

document.addEventListener('mousemove', evt => {
    let x = evt.clientX + 'px';
    let y = evt.clientY + 'px';

    root.style.setProperty('--x', x);
    root.style.setProperty('--y', y);
});

      function myFunction() {
  var x = document.getElementById("skill");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
  }

        function myFunctionN() {
  var y = document.getElementById("skill_two");
  if (y.style.display === "none") {
    y.style.display = "block";
  } else {
    y.style.display = "none";
  }
  }

  let four = document.getElementById('four');
  let one = document.getElementById('one');
  let two = document.getElementById('two');
  let three = document.getElementById('three');

  window.addEventListener('scroll', () => {
  let valOne = two.style.top;
  let valueTwo = window.scrollY;


  two.style.left = valueTwo + 50 + 'px';
  three.style.right = valueTwo + 50 + 'px';
  four.style.right = valueTwo + 50 + 'px';
  one.style.left = 50 + valueTwo + 'px';

  });

  function showSuccess() {
  alert("Email sent successfully")
  }