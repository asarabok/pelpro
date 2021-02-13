(function () {
    function startApp() {
        initializeSelectDaysSelect();
    }

    function initializeSelectDaysSelect() {
        var days = [1, 2, 5, 10, 15, 20, 30];
        var selectEl = document.getElementById("days_delta");
        days.forEach(function(day){
            var option = document.createElement("option");
            option.value = day;
            option.innerHTML = day;
            if (CONFIG.default_days_delta == day) {
                option.setAttribute('selected', true)
            }
            selectEl.appendChild(option);
        })
    }

    function measurementDataLoaded(data) {
        console.log(data);
    }

    fetch('/api/measurements/city/'+CONFIG.selected_city_external_id+'?days_delta='+CONFIG.default_days_delta)
        .then(response => response.json())
        .then(data => measurementDataLoaded(data));


    var ctx = document.getElementById('canvas').getContext('2d');
    var chart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'line',

        // The data for our dataset
        data: {
            labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
            datasets: [{
                label: 'My First dataset',
                backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 132)',
                data: [0, 10, 5, 2, 20, 30, 45]
            }]
        },

        // Configuration options go here
        options: {}
    });

    startApp();
})();
