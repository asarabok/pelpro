(function (w) {
    w.app = {

        init() {
            this.initializeSelectDays();
            this.fetchMeasurementData();
        },


        initializeSelectDays() {
            var self = this;
            var days = [1, 2, 5, 10, 15, 20, 30];
            var selectEl = document.getElementById("days_delta");
            days.forEach(function(day){
                var option = document.createElement("option");
                option.value = day;
                option.innerHTML = day;
                if (CONFIG.days_delta == day) {
                    option.setAttribute('selected', true)
                }
                selectEl.appendChild(option);
            })

            selectEl.addEventListener("change", e => {
                CONFIG.days_delta = e.target.value;
                self.fetchMeasurementData();
            }, false);

        },

        initializeChart(chart_data){
            var self = this;
            var ctx = document.getElementById('canvas').getContext('2d');
            var chart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: self.getDisctinctValues(chart_data, 'measurement_date'),
                    datasets: self.getChartDatasets(chart_data)
                    //datasets: []
                },
                options: {}
            });
        },

        getDisctinctValues(data_arr, key) {
            var flags = [], output = [], l = data_arr.length, i;
            for( i=0; i<l; i++) {
                if( flags[data_arr[i][key]]) continue;
                flags[data_arr[i][key]] = true;
                output.push(data_arr[i][key]);
            }
            return output;
        },

        getChartDatasets(chart_data) {
            var self = this;
            var datasets = [];
            var all_plants = chart_data.map(x => x.plant);
            var distinct_plants = this.getDisctinctValues(all_plants, 'name');
            distinct_plants.forEach(function(plant){
                datasets.push({
                    label: plant,
                    fill: false,
                    backgroundColor: self.generateColor(plant),
                    borderColor: self.generateColor(plant),
                    data: self.getPlantData(chart_data, plant)
                })
            })

            return datasets

        },

        getPlantData(chart_data, plant) {
            var plant_measurements = chart_data.filter(measurement => measurement.plant.name == plant);
            return plant_measurements.map(x => x.value);
        },

        fetchMeasurementData(url) {
            var self = this;
            fetch(self.getMeasurementRestUrl())
                .then(response => response.json())
                .then(data => self.initializeChart(data));
        },

        getMeasurementRestUrl() {
            return CONFIG.fetch_url_base
                .concat(CONFIG.selected_city_external_id)
                .concat("?days_delta=")
                .concat(CONFIG.days_delta)
        },

        generateColor(str) {
            var hash = 0;
            for (var i = 0; i < str.length; i++) {
              hash = str.charCodeAt(i) + ((hash << 5) - hash);
            }
            var colour = '#';
            for (var i = 0; i < 3; i++) {
              var value = (hash >> (i * 8)) & 0xFF;
              colour += ('00' + value.toString(16)).substr(-2);
            }
            return colour;
        }


    };
    w.app.init();
})(window);
