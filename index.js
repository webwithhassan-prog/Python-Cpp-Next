function convert() {
  let f = document.getElementById("input").value;
  let result = document.getElementById("result");

  let c = (f - 32) / (9 / 5);

  console.log(c);
  result.value = c.toFixed(2);
}
