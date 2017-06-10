# Tags
The most popular tags for artists per genre:

<select class="chartSelect" chart-id="mostpopulartags">
    <option value="data/mostPopularTags.json">All</option>
    <option value="data/mostPopularTagsDance.json">Dance</option>
    <option value="data/mostPopularTagsElectronic.json">Electronic</option>
    <option value="data/mostPopularTagsHipHop.json">Hip Hop</option>
    <option value="data/mostPopularTagsIndie.json">Indie</option>
    <option value="data/mostPopularTagsMetal.json">Metal</option>
    <option value="data/mostPopularTagsPop.json">Pop</option>
    <option value="data/mostPopularTagsPunk.json">Punk</option>
    <option value="data/mostPopularTagsRock.json">Rock</option>
    <option value="data/mostPopularTagsRoots.json">Roots</option>
</select>
<div 
    id="mostpopulartags" 
    class="chart" 
    chart-type="bar"
    data="data/mostPopularTags.json" 
    style="width: 900px; height: 900px;"></div>