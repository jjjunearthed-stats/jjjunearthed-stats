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
        "barChart": function (element, data, options) {
            var chart = new google.visualization.BarChart(element);
            chart.draw(data, options);
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
    }
}

unobtrusiveGoogleCharts.init = {
    packagesForChart: {
        "geoMap": ['geochart'],
        "bar": ['bar'],
        "barChart": ['bar'],
        "pie": [],
        "line": ['line'],
        "table": ['table']
    },

    loadOptions: function() {
        var chartTypes = $.map($('div.chart'), function(e) {
            return $(e).attr('chart-type');
        });

        return {
            packages: unobtrusiveGoogleCharts.init.chartPackages(chartTypes),
            mapsApiKey: unobtrusiveGoogleCharts.options.mapsApiKey
        };
    },

    chartPackages: function(chartTypes) {
        var packages = new Set(['corechart']);

        chartTypes.forEach(function (chartType) {
            var chartPackages = unobtrusiveGoogleCharts.init.packagesForChart[chartType];
            chartPackages.forEach(function(package) {
                packages.add(package);
            });
        });

        return Array.from(packages);
    }
}

$(document).ready(function () {
    google.charts.load('current', unobtrusiveGoogleCharts.init.loadOptions());
    google.charts.setOnLoadCallback(unobtrusiveGoogleCharts.bindChartSelectors);
});

$(window).resize(function() {
    if(this.resizeTO) clearTimeout(this.resizeTO);
    this.resizeTO = setTimeout(function() {
        $(this).trigger('resizeEnd');
    }, 500);
});

$(window).on('resizeEnd', function() {
    unobtrusiveGoogleCharts.bindChartSelectors();
});
