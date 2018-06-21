<template>
  <div id="app">
    <div>
      <section class="hero is-info is-medium is-bold">
        <div class="hero-head">
          <nav class="navbar">
            <div class="container">
              <div class="navbar-brand">
                <a class="navbar-item" href="../">
                  <!--<img src="http://bulma.io/images/bulma-type-white.png" alt="Logo">-->
                  <h1 style="font-family: 'Nunito',  sans-serif;"><span id="logo">The Spiny Lumpsuckers</span></h1>
                </a>
                <span class="navbar-burger burger" data-target="navbarMenu">
                <span></span>
                <span></span>
                <span></span>
              </span>
              </div>
              <div id="navbarMenu" class="navbar-menu">
                <div class="navbar-end">
                    <router-link :to="navlink1.toLowerCase()" class="navbar-item">
                          {{ navlink1 }}
                    </router-link>
                    <router-link :to="navlink2.toLowerCase()" class="navbar-item">
                          {{ navlink2 }}
                    </router-link>
                    <router-link :to="navlink3.toLowerCase()" class="navbar-item">
                          {{ navlink3 }}
                    </router-link>
                  <span class="navbar-item">
                  <a class="button is-white is-outlined is-small" href="https://github.com/dodekoekjes/IDP">
                    <span class="icon">
                      <i class="fa fa-github"></i>
                    </span>
                    <span>View Source</span>
                  </a>
                </span>
                </div>
              </div>
            </div>
          </nav>
        </div>

      </section>
    </div>
    <router-view/>
  </div>
</template>

<script>
import 'bulma/css/bulma.css'
import 'bulma-timeline/dist/bulma-timeline.min.css'
import 'bulma-accordion/dist/bulma-accordion.min.css'
import 'bulma-accordion/dist/bulma-accordion.min.js'
import './css/style.css'

export default {
  name: 'App',
  data () {
    return {
      navlink1: 'Home',
      navlink2: 'Progress',
      navlink3: 'About'
    }
  }
}

</script>

<style>
#app {
  font-family: 'Avenair', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
