function addItem() {
  let val = document.getElementById("input").value;
  let output = document.getElementById("result");
  let err = document.getElementById("err");

  if (!val) {
    err.innerText = "Please Write Something To Add";
  } else {
    result.innerHTML += `<option>${val}</option>`;
  }
}
