<template>
  <div>
    <div class="sandbox container">
      <div class="tile is-ancestor">
        <div class="tile is-parent is-shady">
          <article class="tile is-child notification is-white">
            <p class="title">Updates</p>
            <div class="content">
              <!--<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin ornare magna eros, eu pellentesque tortor vestibulum ut. Maecenas non massa sem. Etiam finibus odio quis feugiat facilisis.</p>-->
              <section class="accordions">
                <article class="accordion is-active">
                  <div class="accordion-header toggle">
                    <p>Hello World</p>
                  </div>
                  <div class="accordion-body">
                    <div class="accordion-content">
                      Lorem ipsum dolor sit amet, consectetur adipiscing elit. <strong>Pellentesque risus mi</strong>, tempus quis placerat ut, porta nec nulla. Vestibulum rhoncus ac ex sit amet fringilla. Nullam gravida purus diam, et dictum <a>felis venenatis</a> efficitur. Aenean ac <em>eleifend lacus</em>, in mollis lectus. Donec sodales, arcu et sollicitudin porttitor, tortor urna tempor ligula, id porttitor mi magna a neque. Donec dui urna, vehicula et sem eget, facilisis sodales sem.
                    </div>
                  </div>
                </article>
                <article class="accordion">
                  <div class="accordion-header">
                    <p>Hello World</p>
                    <button class="toggle" aria-label="toggle"></button>
                  </div>
                  <div class="accordion-body">
                    <div class="accordion-content">
                      Lorem ipsum dolor sit amet, consectetur adipiscing elit. <strong>Pellentesque risus mi</strong>, tempus quis placerat ut, porta nec nulla. Vestibulum rhoncus ac ex sit amet fringilla. Nullam gravida purus diam, et dictum <a>felis venenatis</a> efficitur. Aenean ac <em>eleifend lacus</em>, in mollis lectus. Donec sodales, arcu et sollicitudin porttitor, tortor urna tempor ligula, id porttitor mi magna a neque. Donec dui urna, vehicula et sem eget, facilisis sodales sem.
                    </div>
                  </div>
                </article>
                <article class="accordion">
                  <div class="accordion-header">
                    <p>Hello World</p>
                    <button class="toggle" aria-label="toggle"></button>
                  </div>
                  <div class="accordion-body">
                    <div class="accordion-content">
                      Lorem ipsum dolor sit amet, consectetur adipiscing elit. <strong>Pellentesque risus mi</strong>, tempus quis placerat ut, porta nec nulla. Vestibulum rhoncus ac ex sit amet fringilla. Nullam gravida purus diam, et dictum <a>felis venenatis</a> efficitur. Aenean ac <em>eleifend lacus</em>, in mollis lectus. Donec sodales, arcu et sollicitudin porttitor, tortor urna tempor ligula, id porttitor mi magna a neque. Donec dui urna, vehicula et sem eget, facilisis sodales sem.
                    </div>
                  </div>
                </article>
              </section>
            </div>
          </article>
        </div>
        <div class="tile is-parent is-shady">
          <article class="tile is-child notification is-white">
            <p class="title">Timeline</p>
            <div class="timeline is-centered">
              <header class="timeline-header">
                <span class="tag is-medium is-primary">Start</span>
              </header>
              <div class="timeline-item is-primary">
                <div class="timeline-marker is-primary"></div>
                <div class="timeline-content">
                  <p class="heading">January 2016</p>
                  <p>Timeline content - Can include any HTML element</p>
                </div>
              </div>
              <div class="timeline-item is-warning">
                <div class="timeline-marker is-warning is-image is-32x32">
                  <img src="http://bulma.io/images/placeholders/32x32.png">
                </div>
                <div class="timeline-content">
                  <p class="heading">February 2016</p>
                  <p>Timeline content - Can include any HTML element</p>
                </div>
              </div>
              <header class="timeline-header">
                <span class="tag is-primary">2017</span>
              </header>
              <div class="timeline-item is-danger">
                <div class="timeline-marker is-danger is-icon">
                  <i class="fa fa-flag"></i>
                </div>
                <div class="timeline-content">
                  <p class="heading">March 2017</p>
                  <p>Timeline content - Can include any HTML element</p>
                </div>
              </div>
              <header class="timeline-header">
                <span class="tag is-medium is-primary">End</span>
              </header>
            </div>
          </article>
        </div>
      </div>
    </div>
<!--  table -->
    <div class="container">
      <table class="table is-fullwidth is-hoverable">
        <thead>
        <tr>
          <th><abbr title="Position">Pos</abbr></th>
          <th>Team</th>
          <th><abbr title="Played">Pld</abbr></th>
          <th><abbr title="Won">W</abbr></th>
          <th><abbr title="Drawn">D</abbr></th>
          <th><abbr title="Lost">L</abbr></th>
          <th><abbr title="Goals for">GF</abbr></th>
          <th><abbr title="Goals against">GA</abbr></th>
          <th><abbr title="Goal difference">GD</abbr></th>
          <th><abbr title="Points">Pts</abbr></th>
          <th>Qualification or relegation</th>
        </tr>
        </thead>
        <tfoot>
        <tr>
          <th><abbr title="Position">Pos</abbr></th>
          <th>Team</th>
          <th><abbr title="Played">Pld</abbr></th>
          <th><abbr title="Won">W</abbr></th>
          <th><abbr title="Drawn">D</abbr></th>
          <th><abbr title="Lost">L</abbr></th>
          <th><abbr title="Goals for">GF</abbr></th>
          <th><abbr title="Goals against">GA</abbr></th>
          <th><abbr title="Goal difference">GD</abbr></th>
          <th><abbr title="Points">Pts</abbr></th>
          <th>Qualification or relegation</th>
        </tr>
        </tfoot>
        <tbody>
        <tr>
          <th>1</th>
          <td><a href="https://en.wikipedia.org/wiki/Leicester_City_F.C." title="Leicester City F.C.">Leicester City</a> <strong>(C)</strong>
          </td>
          <td>38</td>
          <td>23</td>
          <td>12</td>
          <td>3</td>
          <td>68</td>
          <td>36</td>
          <td>+32</td>
          <td>81</td>
          <td>Qualification for the <a href="https://en.wikipedia.org/wiki/2016%E2%80%9317_UEFA_Champions_League#Group_stage" title="2016–17 UEFA Champions League">Champions League group stage</a></td>
        </tr>
        <tr>
          <th>2</th>
          <td><a href="https://en.wikipedia.org/wiki/Arsenal_F.C." title="Arsenal F.C.">Arsenal</a></td>
          <td>38</td>
          <td>20</td>
          <td>11</td>
          <td>7</td>
          <td>65</td>
          <td>36</td>
          <td>+29</td>
          <td>71</td>
          <td>Qualification for the <a href="https://en.wikipedia.org/wiki/2016%E2%80%9317_UEFA_Champions_League#Group_stage" title="2016–17 UEFA Champions League">Champions League group stage</a></td>
        </tr>
        <tr>
          <th>3</th>
          <td><a href="https://en.wikipedia.org/wiki/Tottenham_Hotspur_F.C." title="Tottenham Hotspur F.C.">Tottenham Hotspur</a></td>
          <td>38</td>
          <td>19</td>
          <td>13</td>
          <td>6</td>
          <td>69</td>
          <td>35</td>
          <td>+34</td>
          <td>70</td>
          <td>Qualification for the <a href="https://en.wikipedia.org/wiki/2016%E2%80%9317_UEFA_Champions_League#Group_stage" title="2016–17 UEFA Champions League">Champions League group stage</a></td>
        </tr>
        <tr class="is-selected">
          <th>4</th>
          <td><a href="https://en.wikipedia.org/wiki/Manchester_City_F.C." title="Manchester City F.C.">Manchester City</a></td>
          <td>38</td>
          <td>19</td>
          <td>9</td>
          <td>10</td>
          <td>71</td>
          <td>41</td>
          <td>+30</td>
          <td>66</td>
          <td>Qualification for the <a href="https://en.wikipedia.org/wiki/2016%E2%80%9317_UEFA_Champions_League#Play-off_round" title="2016–17 UEFA Champions League">Champions League play-off round</a></td>
        </tr>
        <tr>
          <th>5</th>
          <td><a href="https://en.wikipedia.org/wiki/Manchester_United_F.C." title="Manchester United F.C.">Manchester United</a></td>
          <td>38</td>
          <td>19</td>
          <td>9</td>
          <td>10</td>
          <td>49</td>
          <td>35</td>
          <td>+14</td>
          <td>66</td>
          <td>Qualification for the <a href="https://en.wikipedia.org/wiki/2016%E2%80%9317_UEFA_Europa_League#Group_stage" title="2016–17 UEFA Europa League">Europa League group stage</a></td>
        </tr>
        <tr>
          <th>6</th>
          <td><a href="https://en.wikipedia.org/wiki/Southampton_F.C." title="Southampton F.C.">Southampton</a></td>
          <td>38</td>
          <td>18</td>
          <td>9</td>
          <td>11</td>
          <td>59</td>
          <td>41</td>
          <td>+18</td>
          <td>63</td>
          <td>Qualification for the <a href="https://en.wikipedia.org/wiki/2016%E2%80%9317_UEFA_Europa_League#Group_stage" title="2016–17 UEFA Europa League">Europa League group stage</a></td>
        </tr>
        <tr>
          <th>7</th>
          <td><a href="https://en.wikipedia.org/wiki/West_Ham_United_F.C." title="West Ham United F.C.">West Ham United</a></td>
          <td>38</td>
          <td>16</td>
          <td>14</td>
          <td>8</td>
          <td>65</td>
          <td>51</td>
          <td>+14</td>
          <td>62</td>
          <td>Qualification for the <a href="https://en.wikipedia.org/wiki/2016%E2%80%9317_UEFA_Europa_League#Third_qualifying_round" title="2016–17 UEFA Europa League">Europa League third qualifying round</a></td>
        </tr>
        <tr>
          <th>8</th>
          <td><a href="https://en.wikipedia.org/wiki/Liverpool_F.C." title="Liverpool F.C.">Liverpool</a></td>
          <td>38</td>
          <td>16</td>
          <td>12</td>
          <td>10</td>
          <td>63</td>
          <td>50</td>
          <td>+13</td>
          <td>60</td>
          <td></td>
        </tr>
        <tr>
          <th>9</th>
          <td><a href="https://en.wikipedia.org/wiki/Stoke_City_F.C." title="Stoke City F.C.">Stoke City</a></td>
          <td>38</td>
          <td>14</td>
          <td>9</td>
          <td>15</td>
          <td>41</td>
          <td>55</td>
          <td>−14</td>
          <td>51</td>
          <td></td>
        </tr>
        <tr>
          <th>10</th>
          <td><a href="https://en.wikipedia.org/wiki/Chelsea_F.C." title="Chelsea F.C.">Chelsea</a></td>
          <td>38</td>
          <td>12</td>
          <td>14</td>
          <td>12</td>
          <td>59</td>
          <td>53</td>
          <td>+6</td>
          <td>50</td>
          <td></td>
        </tr>
        <tr>
          <th>11</th>
          <td><a href="https://en.wikipedia.org/wiki/Everton_F.C." title="Everton F.C.">Everton</a></td>
          <td>38</td>
          <td>11</td>
          <td>14</td>
          <td>13</td>
          <td>59</td>
          <td>55</td>
          <td>+4</td>
          <td>47</td>
          <td></td>
        </tr>
        <tr>
          <th>12</th>
          <td><a href="https://en.wikipedia.org/wiki/Swansea_City_A.F.C." title="Swansea City A.F.C.">Swansea City</a></td>
          <td>38</td>
          <td>12</td>
          <td>11</td>
          <td>15</td>
          <td>42</td>
          <td>52</td>
          <td>−10</td>
          <td>47</td>
          <td></td>
        </tr>
        <tr>
          <th>13</th>
          <td><a href="https://en.wikipedia.org/wiki/Watford_F.C." title="Watford F.C.">Watford</a></td>
          <td>38</td>
          <td>12</td>
          <td>9</td>
          <td>17</td>
          <td>40</td>
          <td>50</td>
          <td>−10</td>
          <td>45</td>
          <td></td>
        </tr>
        <tr>
          <th>14</th>
          <td><a href="https://en.wikipedia.org/wiki/West_Bromwich_Albion_F.C." title="West Bromwich Albion F.C.">West Bromwich Albion</a></td>
          <td>38</td>
          <td>10</td>
          <td>13</td>
          <td>15</td>
          <td>34</td>
          <td>48</td>
          <td>−14</td>
          <td>43</td>
          <td></td>
        </tr>
        <tr>
          <th>15</th>
          <td><a href="https://en.wikipedia.org/wiki/Crystal_Palace_F.C." title="Crystal Palace F.C.">Crystal Palace</a></td>
          <td>38</td>
          <td>11</td>
          <td>9</td>
          <td>18</td>
          <td>39</td>
          <td>51</td>
          <td>−12</td>
          <td>42</td>
          <td></td>
        </tr>
        <tr>
          <th>16</th>
          <td><a href="https://en.wikipedia.org/wiki/A.F.C._Bournemouth" title="A.F.C. Bournemouth">AFC Bournemouth</a></td>
          <td>38</td>
          <td>11</td>
          <td>9</td>
          <td>18</td>
          <td>45</td>
          <td>67</td>
          <td>−22</td>
          <td>42</td>
          <td></td>
        </tr>
        <tr>
          <th>17</th>
          <td><a href="https://en.wikipedia.org/wiki/Sunderland_A.F.C." title="Sunderland A.F.C.">Sunderland</a></td>
          <td>38</td>
          <td>9</td>
          <td>12</td>
          <td>17</td>
          <td>48</td>
          <td>62</td>
          <td>−14</td>
          <td>39</td>
          <td></td>
        </tr>
        <tr>
          <th>18</th>
          <td><a href="https://en.wikipedia.org/wiki/Newcastle_United_F.C." title="Newcastle United F.C.">Newcastle United</a> <strong>(R)</strong>
          </td>
          <td>38</td>
          <td>9</td>
          <td>10</td>
          <td>19</td>
          <td>44</td>
          <td>65</td>
          <td>−21</td>
          <td>37</td>
          <td>Relegation to the <a href="https://en.wikipedia.org/wiki/2016%E2%80%9317_Football_League_Championship" title="2016–17 Football League Championship">Football League Championship</a></td>
        </tr>
        <tr>
          <th>19</th>
          <td><a href="https://en.wikipedia.org/wiki/Norwich_City_F.C." title="Norwich City F.C.">Norwich City</a> <strong>(R)</strong>
          </td>
          <td>38</td>
          <td>9</td>
          <td>7</td>
          <td>22</td>
          <td>39</td>
          <td>67</td>
          <td>−28</td>
          <td>34</td>
          <td>Relegation to the <a href="https://en.wikipedia.org/wiki/2016%E2%80%9317_Football_League_Championship" title="2016–17 Football League Championship">Football League Championship</a></td>    </tr>
        <tr>
          <th>20</th>
          <td><a href="https://en.wikipedia.org/wiki/Aston_Villa_F.C." title="Aston Villa F.C.">Aston Villa</a> <strong>(R)</strong>
          </td>
          <td>38</td>
          <td>3</td>
          <td>8</td>
          <td>27</td>
          <td>27</td>
          <td>76</td>
          <td>−49</td>
          <td>17</td>
          <td>Relegation to the <a href="https://en.wikipedia.org/wiki/2016%E2%80%9317_Football_League_Championship" title="2016–17 Football League Championship">Football League Championship</a></td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Progress'
}
</script>

<style scoped>

</style>
