function getWeather() {
    const city = document.getElementById("cityInput").value;
    const apiKey = "3e5658e401884ab781b132457251704";
    const url = `http://api.weatherapi.com/v1/current.json?key=3e5658e401884ab781b132457251704&q=London&aqi=no=${city}&appid=${apiKey}&units=metric`;
    
    fetch(url)
      .then(response => response.json())
      .then(data => {
        const weatherDiv = document.getElementById("weather");
        if (data.cod === 200) {
          weatherDiv.innerHTML = `
            <h2>${data.name}, ${data.sys.country}</h2>
            <p>Temperature: ${data.main.temp} °C</p>
            <p>Weather: ${data.weather[0].description}</p>
            <p>Humidity: ${data.main.humidity}%</p>
          `;
        } else {
          weatherDiv.innerHTML = `<p>City not found</p>`;
        }
      })
      .catch(error => {
        document.getElementById("weather").innerHTML = `<p>Error fetching data</p>`;
      });
  }