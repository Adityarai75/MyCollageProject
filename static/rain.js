function visible(){
    var element = document.getElementsByClassName("output");
    
}
function toggleTextBox() {
      const textBox = document.getElementById('textBox');
      textBox.classList.toggle('show');
    }
function closeit() {
  const textBox = document.getElementById('textBox');
  textBox.classList.add('hide');
  setTimeout(() => {
    textBox.classList.remove('show');
  }, 300);
}



const text = "Rainfall prediction is a critical component in various sectors such as agriculture, water resource management, and disaster preparedness. Traditional methods for forecasting weather, including rainfall, rely heavily on complex physical models that can be computationally intensive and often fail to capture local variability. This project explores the application of machinelearning techniques to improve the accuracy and efficiency of rainfall prediction.Rainfall prediction is a beneficiary one, but it is a challenging task. Machine learning techniques can use computational methods and predict rainfall by retrieving and integrating the hidden knowledge from the linear and non-linearpatterns of past weather data. Existing methods are failing whenever massive datasets are used for rainfall prediction."
let index = 0;
let boxVisible = false;

function toggleBox() {
    const box = document.getElementById("animatedBox");
    const textElement = document.getElementById("text");
    document.getElementById("boxi21").style.backgroundColor = "lightblue";


    if (!boxVisible) {
        box.style.display = "block";
        animateText(textElement, text);
    } else {
        box.style.display = "none";
        textElement.innerHTML = "";
    }
    boxVisible = !boxVisible;
}

function animateText(element, content) {
    element.innerHTML = "";
    index = 0;
    
    function type() {
        if (index < content.length) {
            element.innerHTML += content[index];
            index++;
            setTimeout(type, 100);
        }
    }

    type();
}
