# Location

<div class="flex-container">
    <div class="flex-2">
        <h2>Artists by Location</h2>
        <div 
            class="chart" 
            data="data/artistsByLocation.json"
            chart-type="geoMap">
        </div>
    </div>
    <div class="flex-2">
        <h2>Artists Per Capita</h2>
        <div 
            class="chart" 
            data="data/artistsPerCapita.json"
            chart-type="geoMap">
        </div>
    </div>
</div>

<div 
    class="chart" 
    data="data/artistsLocationTable.json" 
    columns='[["string", "Location"],["number", "Artists"],["number", "Artists per 100 000 people"]]'
    data-options='{
        "showRowNumber": false,
        "width": "100%",
        "height": "100%",
        "sortColumn": 2,
        "sortAscending": false
    }'
    chart-type="table">
</div>

## Locations played on JJJ per Year
The number of artists from a location played on JJJ per year:
<div 
    class="chart" 
    data="data/locationsPlayedOnJJJPerYear.json"
    chart-type="line"
    style="width: 900px; height: 500px;">
</div>

## Locations played on Unearthed per Year
The number of artists from a location played on Unearthed per year:
<div 
    class="chart" 
    data="data/locationsPlayedOnUnearthedPerYear.json" 
    style="width: 900px; height: 500px;"
    chart-type="line">
</div>
