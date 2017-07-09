# Influences
The most popular influences for artists per genre:

<select class="chartSelect" chart-id="mostpopularinfluences">
    <option value="data/mostPopularInfluences.json">All</option>
    <option value="data/mostPopularInfluencesDance.json">Dance</option>
    <option value="data/mostPopularInfluencesElectronic.json">Electronic</option>
    <option value="data/mostPopularInfluencesHipHop.json">Hip Hop</option>
    <option value="data/mostPopularInfluencesIndie.json">Indie</option>
    <option value="data/mostPopularInfluencesMetal.json">Metal</option>
    <option value="data/mostPopularInfluencesPop.json">Pop</option>
    <option value="data/mostPopularInfluencesPunk.json">Punk</option>
    <option value="data/mostPopularInfluencesRock.json">Rock</option>
    <option value="data/mostPopularInfluencesRoots.json">Roots</option>
</select>
<div 
    id="mostpopularinfluences" 
    class="chart" 
    chart-type="bar"
    data="data/mostPopularInfluences.json" 
    style="height: 700px;"></div>