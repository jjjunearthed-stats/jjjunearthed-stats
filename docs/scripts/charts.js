var unobtrusiveGoogleCharts = {
    options: {},
    drawChart: {
        "geoMap": function (element, data, options) {
            var chart = new google.visualization.GeoChart(element);
            chart.draw(data, options);
        },
        "bar": function (element, data, options) {
            var chart = new google.charts.Bar(element);
            chart.draw(data, google.charts.Bar.convertOptions(options));
        },
        "pie": function (element, data, options) {
            var chart = new google.visualization.PieChart(element);
            chart.draw(data, options);
        },
        "line": function (element, data, options) {
            var chart = new google.charts.Line(element);
            chart.draw(data, google.charts.Line.convertOptions(options));
        },
        "table": function (element, data, options) {
            var table = new google.visualization.Table(element);
            table.draw(data, options);
        }
    },
    chartPackages: {
        "geoMap": ['geochart'],
        "bar": ['bar'],
        "pie": [],
        "line": ['line'],
        "table": ['table']
    },

    drawChartElement: function (element, data) {
        var dataUrl = data || element.attr("data");
        var chartType = element.attr("chart-type");
        var options = element.data("options") || unobtrusiveGoogleCharts.options[chartType];
        var dataColumns = element.attr("columns");
        var chartElement = element[0];

        $.getJSON(dataUrl, function (json) {
            var data = new google.visualization.DataTable();

            if (chartType === "table") {
                $.each(JSON.parse(dataColumns), function (i, val) {
                    data.addColumn(val[0], val[1]);
                });
                data.addRows(json);
            } else {
                data = google.visualization.arrayToDataTable(json);
            }

            unobtrusiveGoogleCharts.drawChart[chartType](chartElement, data, options);
        });
    },

    bindChartSelectors: function () {
        $('div.chart').each(function () {
            unobtrusiveGoogleCharts.drawChartElement($(this));
        });

        $('.chartSelect').change(function () {
            var data = $(this).val();
            var chartId = $(this).attr("chart-id");
            var chartElement = $("#" + chartId);

            unobtrusiveGoogleCharts.drawChartElement(chartElement, data);
        });
    },

    loadOptions: function() {
        var loadOptions = {
            packages: ['corechart']
        };

        var packages = new Set();
        $('div.chart').each(function () {
            var chartPackages = unobtrusiveGoogleCharts.chartPackages[$(this).attr('chart-type')];
            chartPackages.forEach(function(p) {
                packages.add(p);
            });
        });

        loadOptions.packages = Array.from(packages);
        
        if (unobtrusiveGoogleCharts.options.mapsApiKey) {
            loadOptions.mapsApiKey = unobtrusiveGoogleCharts.options.mapsApiKey
        }

        return loadOptions;
    }
}

$(document).ready(function () {
    google.charts.load('current', unobtrusiveGoogleCharts.loadOptions());
    google.charts.setOnLoadCallback(unobtrusiveGoogleCharts.bindChartSelectors);
});