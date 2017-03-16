# Artists by Location
<div class="geoMap" data-url="data/artistsByLocation.json"></div>

# Artists Per Capita
<div class="geoMap" data-url="data/artistsPerCapita.json"></div>

<div class="table_div" data-url="data/artistsLocation.json"></div>
<table>
<thead>
<tr><th>Location</th><th>Number of artists</th></tr>
</thead>
<tbody>
{% for location in site.data.artistsByLocation %}
  <tr>
    <td>{{ location[0] }}</td>
    <td>{{ location[1] }}</td>
  </tr>
{% endfor %}
</tbody>
</table>
# Hierarchial likes
<iframe src="artistHierarchialGraph.html" width="960" height="960" scrolling="no"></iframe>
