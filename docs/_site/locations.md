# Artists by Location
<div 
    class="chart" 
    data="data/artistsByLocation.json"
    chart-type="geoMap">
</div>

# Artists Per Capita
<div 
    class="chart" 
    data="data/artistsPerCapita.json"
    chart-type="geoMap">
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

# Locations played on JJJ per Year
<div 
    class="chart" 
    data="data/locationsPlayedOnJJJPerYear.json"
    chart-type="line"
    style="width: 900px; height: 500px;">
    </div>

# Locations played on Unearthed per Year
<div 
    class="chart" 
    data="data/locationsPlayedOnUnearthedPerYear.json" 
    style="width: 900px; height: 500px;"
    chart-type="line"
    ></div>
