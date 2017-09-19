# Gender Distribution

The goal of this is to examine the gender distribution of artists listed on JJJ Unearthed. Please note that this is only a rough guide to the gender make-up of JJJ artists and not an exhaustive, 100% accurate study of it.

While it is impractical to survey the gender of each band member in 60000+ bands, a rough estimate can be achieved by guessing the gender based on names. Unisex names (eg: Sam, Alex) were disregarded for the purpose of this study. 

<div
    class="chart"
    data="data/gendersStacked.json"
    chart-type="barChart"
    data-options='{
          "isStacked": "percent",
          "height": 300,
          "title": "Male/Female representation per genre",
          "legend": {"position": "right", "maxLines": 3}
        }'>
</div>

Pop is the most popular genre for females at 18.9% while metal bands seem to have the fewest females in them at 5.04%. As you can see playing in a band is still an overwhelmingly male pastime.

## Plays on JJJ
By only counting artists that have been played on JJJ, we can see the gender distribution of artists played on JJJ:

<div
    class="chart"
    data="data/gendersPlayedOnJJJ.json"
    chart-type="barChart"   
    data-options='{
          "isStacked": "percent",
          "height": 300,
          "title": "Male/Female representation per genre",
          "legend": {"position": "right", "maxLines": 3}
        }'>
</div>


## Female vocalists
We can see how many artists per genre have female vocalists:

<div
    class="chart"
    data="data/artistsWithFemaleVocalist.json"
    chart-type="barChart"
    data-options='{
          "isStacked": "percent",
          "height": 300,
          "title": "Artists with female vocalists per genre",
          "legend": {"position": "right", "maxLines": 3}
        }'>
</div>

## Female Bassists
We can see how popular playing bass is for females per genre:

<div
    class="chart"
    data="data/artistsWithFemaleBassist.json"
    chart-type="barChart"
    data-options='{
          "isStacked": "percent",
          "height": 300,
          "title": "Artists with female bassist per genre",
          "legend": {"position": "right", "maxLines": 3}
        }'>
</div>

