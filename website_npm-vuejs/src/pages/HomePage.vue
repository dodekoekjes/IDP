<template>
  <div>
    <div class="hero-body">
      <div class="container has-text-centered">
        <h1 class="title">
          IDP GROEP 12
        </h1>
        <h2 class="subtitle">
          <b>[tell about what the project is]</b>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        </h2>
      </div>
    </div>
    <div>
      <div class="box cta">
        <p class="has-text-centered">
          <span class="tag is-primary">Update</span> [place here the latest update].
        </p>
      </div>
    </div>
<!--  Card containers -->
    <section class="container">
      <div class="columns features">
        <div class="column is-4">
          <div class="card is-shady">
            <div class="card-image has-text-centered">
              <i class="fa fa-laptop"></i>
            </div>
            <div class="card-content">
              <div class="content">
<!--  Card 1  -->
                <h4>{{ title1 }}</h4>
                <p>{{ msg1 }}</p>
                <p><router-link :to="title1.toLowerCase()" class="tag is-dark is-large">Learn more</router-link></p>
              </div>
            </div>
          </div>
        </div>
        <div class="column is-4">
          <div class="card is-shady">
            <div class="card-image has-text-centered">
              <i class="fa fa-plug"></i>
            </div>
            <div class="card-content">
              <div class="content">
<!--  Card 2  -->
                <h4>{{ title2 }}</h4>
                <p>Ut venenatis tellus in metus vulputate. Amet consectetur adipiscing elit pellentesque. Sed arcu non odio euismod lacinia at quis risus. Faucibus turpis in eu mi bibendum neque egestas cmonsu songue. Phasellus vestibulum lorem sed risus.</p>
                <p><router-link :to="title2.toLowerCase()" class="tag is-success is-large">Learn more</router-link></p>
              </div>
            </div>
          </div>
        </div>
        <div class="column is-4">
          <div class="card is-shady">
            <div class="card-image has-text-centered">
              <i class="fa fa-cogs is-info"></i>
            </div>
            <div class="card-content">
              <div class="content">
<!--  Card 3  -->
                <h4>{{ title3 }}</h4>
                <p>Imperdiet dui accumsan sit amet nulla facilisi morbi. Fusce ut placerat orci nulla pellentesque dignissim enim. Libero id faucibus nisl tincidunt eget nullam. Commodo viverra maecenas accumsan lacus vel facilisis.</p>
                <p><router-link :to="title3.toLowerCase()" class="tag is-warning is-large">Learn more</router-link></p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="intro column is-8 is-offset-2">
        <h2 class="title">Perfect for developers or designers!</h2><br>
        <p class="subtitle">Vel fringilla est ullamcorper eget nulla facilisi. Nulla facilisi nullam vehicula ipsum a. Neque egestas congue quisque egestas diam in arcu cursus.</p>
      </div>
    </section>
    <footer class="footer">
      <div class="container">
        <div class="content has-text-centered">
          <p>
            <strong>Bulma Templates</strong> by <a href="https://github.com/dansup">Daniel Supernault</a>. The source code is licensed
            <a href="http://opensource.org/licenses/mit-license.php">MIT</a>.
          </p>
          <p>
            <a class="icon" href="https://github.com/dansup/bulma-templates">
              <i class="fa fa-github"></i>
            </a>
          </p>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      title1: 'Informatica',
      msg1: 'De informatica student, ook wel bekend als de codeklopper' +
            ' is te vinden achter de computer zijn natuurlijke habitat.' +
            ' Het doel van de informatica student is om het brein te maken' +
            ' van de robot. Dit doen ze door middel van python code te laten' +
            ' draaien op de raspberry pi.',
      title2: 'Elektrotechniek',
      msg2: '',
      title3: 'Werktuigbouwkunde',
      msg3: ''
    }
  }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h1, h2 {
    font-weight: normal;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    display: inline-block;
    margin: 0 10px;
  }
  a {
    color: #42b983;
  }
</style>
